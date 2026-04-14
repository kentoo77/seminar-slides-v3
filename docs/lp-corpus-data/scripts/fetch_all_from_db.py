#!/usr/bin/env python3
"""
DB内の全LPのHTMLを並列取得
- has_html=0 のLPのみ対象
- ThreadPoolExecutor で並列実行
- HTML保存 + DB更新
"""
import sys
import os
import re
import json
import sqlite3
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

CORPUS_DIR = Path("/Users/oidekento/lp-corpus")
DB_FILE = CORPUS_DIR / "db" / "lp_corpus.db"
HTML_ROOT = CORPUS_DIR / "raw_all"  # 全件保存用新ディレクトリ
HTML_ROOT.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def fetch(url: str, timeout: int = 15) -> tuple[str | None, int]:
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "ja,en;q=0.9",
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read()
            if len(content) > 10 * 1024 * 1024:  # 10MB超はスキップ
                return None, 413
            return content.decode("utf-8", errors="ignore"), 200
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception as e:
        return None, 0


def safe_filename(url: str, lp_id: int) -> str:
    """Generate a safe, unique filename from URL."""
    s = re.sub(r"https?://", "", url)
    s = re.sub(r"[^a-zA-Z0-9\-_.]", "_", s)
    return f"{lp_id}_{s[:60]}.html"


def fetch_one(lp_id: int, url: str, genre: str) -> dict:
    genre_dir = HTML_ROOT / genre
    genre_dir.mkdir(exist_ok=True)
    filename = safe_filename(url, lp_id)
    filepath = genre_dir / filename

    if filepath.exists() and filepath.stat().st_size > 500:
        return {"id": lp_id, "status": "skip", "path": str(filepath), "size": filepath.stat().st_size}

    html, status = fetch(url)
    if html and len(html) > 500:
        filepath.write_text(html)
        return {
            "id": lp_id,
            "status": "ok",
            "path": str(filepath),
            "size": len(html),
            "http_status": status,
        }
    else:
        return {"id": lp_id, "status": "fail", "path": None, "http_status": status}


def run(workers: int = 15, batch_size: int = 500):
    """Fetch all HTML from DB for entries with has_html=0."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row

    cursor = conn.execute(
        """
        SELECT id, lp_url, genre FROM lps
        WHERE has_html = 0
          AND lp_url IS NOT NULL AND lp_url != ''
        ORDER BY id
        """
    )
    entries = cursor.fetchall()
    total = len(entries)
    print(f"Fetching {total} LPs with {workers} workers...")

    fetched_count = 0
    failed_count = 0
    skip_count = 0
    processed = 0

    update_stmt = "UPDATE lps SET has_html=?, html_path=?, html_size=? WHERE id=?"

    # バッチごとに処理してコミット
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for batch_start in range(0, total, batch_size):
            batch = entries[batch_start : batch_start + batch_size]
            futures = {
                ex.submit(fetch_one, row["id"], row["lp_url"], row["genre"] or "uncategorized"): row
                for row in batch
            }
            for fut in as_completed(futures):
                row = futures[fut]
                try:
                    result = fut.result()
                    if result["status"] == "ok":
                        conn.execute(
                            update_stmt, (1, result["path"], result["size"], result["id"])
                        )
                        fetched_count += 1
                    elif result["status"] == "skip":
                        conn.execute(
                            update_stmt, (1, result["path"], result["size"], result["id"])
                        )
                        skip_count += 1
                    else:
                        failed_count += 1
                except Exception as e:
                    failed_count += 1
                    print(f"  error: {e}", file=sys.stderr)
                processed += 1
                if processed % 100 == 0:
                    print(
                        f"  [{processed}/{total}] ok={fetched_count} skip={skip_count} fail={failed_count}"
                    )
            conn.commit()

    conn.close()
    print(
        f"\nDone: ok={fetched_count} skip={skip_count} fail={failed_count} total={processed}"
    )


if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    run(workers=workers)
