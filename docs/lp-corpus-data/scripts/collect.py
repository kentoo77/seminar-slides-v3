#!/usr/bin/env python3
"""
LP Corpus Collector
- SANKOU!の指定カテゴリから外部LP URLを大量取得
- 各LPのHTMLとメタデータを保存
- ジャンル別にディレクトリ分け

Usage:
  python3 collect.py <genre_slug> <sankou_category> [max_pages]
  例: python3 collect.py beauty-clinic beauty-cosmetics-caregoods 5
"""
import sys
import re
import os
import json
import time
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

CORPUS_DIR = Path("/Users/oidekento/lp-corpus/raw")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def fetch(url: str, timeout: int = 15) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, Exception) as e:
        print(f"  [fetch error] {url}: {e}", file=sys.stderr)
        return None


def extract_articles_and_externals(html: str) -> tuple[list[dict], list[str]]:
    """Extract SANKOU article permalinks and external LP URLs."""
    # SANKOU記事ページへの内部リンク
    articles = re.findall(r'href="(https://sankoudesign\.com/[^"/]+/[^/"]+/)"', html)
    articles = list(
        {a for a in articles if "/category/" not in a and "/tag/" not in a and "/page/" not in a}
    )

    # 外部リンク (SANKOU以外)
    all_links = re.findall(r'href="(https?://[^"]+)"', html)
    excluded = [
        "sankoudesign.com",
        "gravatar",
        "gstatic",
        "fbcdn",
        "googleapis",
        "googletagmanager",
        "google-analytics",
        "facebook.com",
        "twitter.com",
        "x.com/intent",
        "line.me",
        "hatena.ne",
        "pocket.com",
        "googleadservices",
        "doubleclick",
        "youtube.com/embed",
        "youtu.be",
    ]
    externals = [
        u for u in all_links if not any(e in u for e in excluded) and not u.startswith("#")
    ]
    externals = list(set(externals))

    return [{"permalink": a} for a in articles], externals


def collect_category(genre: str, sankou_cat: str, max_pages: int = 5, delay: float = 1.5):
    """Collect external LP URLs from a SANKOU category."""
    genre_dir = CORPUS_DIR / genre
    genre_dir.mkdir(parents=True, exist_ok=True)

    urls_file = genre_dir / "urls.json"
    collected: dict[str, dict] = {}
    if urls_file.exists():
        collected = json.loads(urls_file.read_text())
        print(f"[{genre}] Existing: {len(collected)} URLs")

    base_url = f"https://sankoudesign.com/category/{sankou_cat}/"
    for page in range(1, max_pages + 1):
        url = base_url if page == 1 else f"{base_url}page/{page}/"
        print(f"[{genre}] Fetching page {page}: {url}")
        html = fetch(url)
        if not html:
            print(f"[{genre}] Page {page}: fetch failed, stopping")
            break

        _, externals = extract_articles_and_externals(html)
        new_count = 0
        for ext_url in externals:
            if ext_url not in collected:
                collected[ext_url] = {
                    "genre": genre,
                    "sankou_category": sankou_cat,
                    "source_page": page,
                    "discovered_at": datetime.now().isoformat(),
                }
                new_count += 1
        print(f"[{genre}] Page {page}: +{new_count} new URLs (total: {len(collected)})")

        if new_count == 0 and page > 1:
            print(f"[{genre}] No new URLs, stopping pagination")
            break

        time.sleep(delay)

    # Save
    urls_file.write_text(json.dumps(collected, ensure_ascii=False, indent=2))
    print(f"[{genre}] Saved {len(collected)} URLs to {urls_file}")
    return collected


def fetch_lp_html(url: str, save_dir: Path, slug: str, delay: float = 1.0) -> dict | None:
    """Fetch a single LP's HTML and save."""
    html = fetch(url, timeout=20)
    if not html:
        return None

    html_file = save_dir / f"{slug}.html"
    html_file.write_text(html)

    meta = {
        "url": url,
        "slug": slug,
        "size_bytes": len(html),
        "fetched_at": datetime.now().isoformat(),
        "title": re.search(r"<title[^>]*>([^<]+)</title>", html, re.I),
    }
    if meta["title"]:
        meta["title"] = meta["title"].group(1).strip()

    meta_file = save_dir / f"{slug}.meta.json"
    meta_file.write_text(json.dumps(meta, ensure_ascii=False, indent=2))

    time.sleep(delay)
    return meta


def slug_from_url(url: str) -> str:
    """Generate a safe filename from URL."""
    s = re.sub(r"https?://", "", url)
    s = re.sub(r"[^a-zA-Z0-9\-_.]", "_", s)
    return s[:80]


def fetch_all_for_genre(genre: str, limit: int = 50):
    """Fetch HTML for all collected URLs in a genre."""
    genre_dir = CORPUS_DIR / genre
    urls_file = genre_dir / "urls.json"
    if not urls_file.exists():
        print(f"[{genre}] No urls.json. Run collect first.")
        return

    collected = json.loads(urls_file.read_text())
    html_dir = genre_dir / "html"
    html_dir.mkdir(exist_ok=True)

    fetched_count = 0
    for url, meta in collected.items():
        if fetched_count >= limit:
            break
        slug = slug_from_url(url)
        if (html_dir / f"{slug}.html").exists():
            continue
        print(f"[{genre}] Fetching ({fetched_count + 1}/{limit}): {url[:70]}")
        result = fetch_lp_html(url, html_dir, slug)
        if result:
            fetched_count += 1

    print(f"[{genre}] HTML fetch complete. {fetched_count} new LPs saved.")


def main():
    if len(sys.argv) < 3:
        print("Usage: collect.py <command> <genre> [sankou_cat] [max_pages|limit]")
        print("Commands:")
        print("  urls <genre> <sankou_cat> [max_pages=5]     # Collect URL list")
        print("  fetch <genre> [limit=50]                     # Fetch HTMLs")
        sys.exit(1)

    cmd = sys.argv[1]
    genre = sys.argv[2]

    if cmd == "urls":
        sankou_cat = sys.argv[3]
        max_pages = int(sys.argv[4]) if len(sys.argv) > 4 else 5
        collect_category(genre, sankou_cat, max_pages)
    elif cmd == "fetch":
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 50
        fetch_all_for_genre(genre, limit)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
