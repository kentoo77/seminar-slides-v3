#!/usr/bin/env python3
"""
rdlp.jp LP Archive Collector
個別LPページ (/archives/otherdesign/lp/{id}) から情報抽出

URL構造: https://rdlp.jp/archives/otherdesign/lp/{id}
抽出情報:
  - タイトル (<title>SHISEIDO オイデルミン エッセンスローションのLPデザイン</title>)
  - 企業名 (description の「xxx様」)
  - LP実体URL (body内の最初の外部リンク)
  - プラットフォーム (description の「〇〇に掲載されている」)
  - OG画像URL
  - 企業所在地

Usage:
  python3 rdlp_collect.py crawl <start_id> <end_id> [workers=4]
  python3 rdlp_collect.py merge
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
from concurrent.futures import ThreadPoolExecutor, as_completed

CORPUS_DIR = Path("/Users/oidekento/lp-corpus")
RDLP_DIR = CORPUS_DIR / "rdlp"
RDLP_DIR.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def fetch(url: str, timeout: int = 10) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return None


def parse_lp_detail(html: str, lp_id: int) -> dict | None:
    """Parse rdlp.jp individual LP page."""
    if not html:
        return None

    # タイトル: 「XXXのLPデザイン」形式
    title_match = re.search(r"<title[^>]*>([^<]+?)のLPデザイン</title>", html)
    title = title_match.group(1).strip() if title_match else None

    # descriptionから企業名・所在地・プラットフォーム抽出
    # 例: 「東京都中央区の資生堂ジャパン株式会社 様の楽天に掲載されている...」
    desc_match = re.search(r'name="description"\s+content="([^"]+)"', html)
    description = desc_match.group(1) if desc_match else ""

    location = None
    company = None
    platform = None

    # 所在地 + 企業名: 「[所在地]の[企業名] 様の[platform]に掲載されている」
    addr_co = re.search(
        r"([^の]+[都道府県][^の]+)の([^様]+?)\s*様の([^に]+)に掲載", description
    )
    if addr_co:
        location = addr_co.group(1).strip()
        company = addr_co.group(2).strip()
        platform = addr_co.group(3).strip()
    else:
        # 所在地なしパターン
        co_only = re.search(r"([^の\s]+?)\s*様の([^に]+)に掲載", description)
        if co_only:
            company = co_only.group(1).strip()
            platform = co_only.group(2).strip()

    # 外部LPのURL（body内の最初の外部リンク）
    body_match = re.search(r"<body[^>]*>(.*)</body>", html, re.DOTALL)
    ext_url = None
    if body_match:
        ext_links = re.findall(r'href="(https?://[^"]+)"', body_match.group(1))
        for link in ext_links:
            if (
                "rdlp.jp" not in link
                and "gmpg.org" not in link
                and "doubleclick" not in link
                and "google" not in link
                and "facebook" not in link
                and "twitter" not in link
                and "amazon-adsystem" not in link
            ):
                ext_url = link
                break

    # OG画像
    og_match = re.search(r'property="og:image"\s+content="([^"]+)"', html)
    og_image = og_match.group(1) if og_match else None

    # keywords からカテゴリ推測
    kw_match = re.search(r'name="keywords"\s+content="([^"]+)"', html)
    keywords = kw_match.group(1) if kw_match else ""

    return {
        "id": lp_id,
        "title": title,
        "company": company,
        "location": location,
        "platform": platform,
        "lp_url": ext_url,
        "og_image": og_image,
        "keywords": keywords,
        "description": description[:200],
        "crawled_at": datetime.now().isoformat(),
    }


def crawl_one(lp_id: int) -> dict | None:
    url = f"https://rdlp.jp/archives/otherdesign/lp/{lp_id}"
    html = fetch(url)
    return parse_lp_detail(html, lp_id)


def crawl_range(start_id: int, end_id: int, workers: int = 4):
    """Crawl a range of LP IDs in parallel."""
    batch_file = RDLP_DIR / f"batch_{start_id}_{end_id}.jsonl"
    existing = set()
    if batch_file.exists():
        with open(batch_file) as f:
            for line in f:
                try:
                    existing.add(json.loads(line)["id"])
                except Exception:
                    pass
        print(f"Resume: {len(existing)} existing entries in {batch_file.name}")

    todo = [i for i in range(start_id, end_id + 1) if i not in existing]
    print(f"Crawling {len(todo)} IDs ({start_id}-{end_id}) with {workers} workers")

    count = 0
    valid = 0
    with open(batch_file, "a") as out, ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(crawl_one, i): i for i in todo}
        for fut in as_completed(futures):
            lp_id = futures[fut]
            try:
                result = fut.result()
                if result and result.get("lp_url"):
                    out.write(json.dumps(result, ensure_ascii=False) + "\n")
                    out.flush()
                    valid += 1
            except Exception as e:
                print(f"  [{lp_id}] error: {e}", file=sys.stderr)
            count += 1
            if count % 50 == 0:
                print(f"  Progress: {count}/{len(todo)} ({valid} valid)")

    print(f"Batch done: {count} crawled, {valid} valid entries saved")


def merge_all():
    """Merge all batch files into one master JSON."""
    master_file = RDLP_DIR / "master.jsonl"
    master = []
    for batch in RDLP_DIR.glob("batch_*.jsonl"):
        with open(batch) as f:
            for line in f:
                try:
                    master.append(json.loads(line))
                except Exception:
                    pass
    master.sort(key=lambda x: x["id"])

    with open(master_file, "w") as f:
        for item in master:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Master file: {len(master)} entries -> {master_file}")

    # 統計
    platforms = {}
    for m in master:
        p = m.get("platform") or "unknown"
        platforms[p] = platforms.get(p, 0) + 1

    print("\nPlatform distribution:")
    for p, c in sorted(platforms.items(), key=lambda x: -x[1])[:15]:
        print(f"  {p}: {c}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "crawl":
        start = int(sys.argv[2])
        end = int(sys.argv[3])
        workers = int(sys.argv[4]) if len(sys.argv) > 4 else 4
        crawl_range(start, end, workers)
    elif cmd == "merge":
        merge_all()
    elif cmd == "test":
        # Single ID test
        lp_id = int(sys.argv[2]) if len(sys.argv) > 2 else 227598
        result = crawl_one(lp_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
