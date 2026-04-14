#!/usr/bin/env python3
"""
LP Corpus Database Builder
SANKOU! + rdlp.jp のデータを統合してSQLiteに投入
タグ付け + 全文検索 + ジャンル別引き込みのためのDB
"""
import sys
import json
import sqlite3
import re
from pathlib import Path
from datetime import datetime

CORPUS_DIR = Path("/Users/oidekento/lp-corpus")
RAW_DIR = CORPUS_DIR / "raw"
RDLP_DIR = CORPUS_DIR / "rdlp"
DB_DIR = CORPUS_DIR / "db"
DB_DIR.mkdir(exist_ok=True)
DB_FILE = DB_DIR / "lp_corpus.db"


SCHEMA = """
CREATE TABLE IF NOT EXISTS lps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,                -- 'sankou' or 'rdlp'
    source_id TEXT,                      -- rdlp LP id or sankou slug
    genre TEXT NOT NULL,                 -- 21 ジャンル
    subgenre TEXT,                       -- サブジャンル（分析で発見したもの）
    title TEXT,
    company TEXT,
    location TEXT,
    platform TEXT,                       -- 楽天 / 自社 / Shopify 等
    lp_url TEXT NOT NULL,
    og_image TEXT,
    keywords TEXT,                       -- カンマ区切り
    tags TEXT,                           -- カンマ区切り（色・スタイル・ムード等）
    html_path TEXT,                      -- ローカル保存パス（nullable）
    html_size INTEGER,
    has_html BOOLEAN DEFAULT 0,
    metadata_json TEXT,                  -- その他メタデータ
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(source, lp_url)
);

CREATE INDEX IF NOT EXISTS idx_lps_genre ON lps(genre);
CREATE INDEX IF NOT EXISTS idx_lps_source ON lps(source);
CREATE INDEX IF NOT EXISTS idx_lps_company ON lps(company);
CREATE INDEX IF NOT EXISTS idx_lps_has_html ON lps(has_html);

CREATE VIRTUAL TABLE IF NOT EXISTS lps_fts USING fts5(
    title, company, keywords, tags, platform,
    content='lps', content_rowid='id',
    tokenize='unicode61'
);

CREATE TRIGGER IF NOT EXISTS lps_ai AFTER INSERT ON lps BEGIN
    INSERT INTO lps_fts(rowid, title, company, keywords, tags, platform)
    VALUES (new.id, new.title, new.company, new.keywords, new.tags, new.platform);
END;

CREATE TRIGGER IF NOT EXISTS lps_ad AFTER DELETE ON lps BEGIN
    DELETE FROM lps_fts WHERE rowid=old.id;
END;

CREATE TABLE IF NOT EXISTS genre_insights (
    genre TEXT PRIMARY KEY,
    analysis_file TEXT,                  -- analysis/*.md へのパス
    subcategories TEXT,                  -- JSON配列
    common_patterns TEXT,                -- 要点サマリ
    color_palettes TEXT,                 -- 頻出カラーJSON
    fonts TEXT,                          -- 頻出フォントJSON
    libraries TEXT,                      -- 頻出ライブラリJSON
    section_order TEXT,                  -- 標準セクション順序JSON
    cta_patterns TEXT,                   -- CTAパターンJSON
    decorations TEXT,                    -- 装飾要素JSON
    dos TEXT,                            -- やるべきこと
    donts TEXT,                          -- 避けるべきこと
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS genre_mapping (
    sankou_category TEXT PRIMARY KEY,
    our_genre TEXT NOT NULL,
    notes TEXT
);
"""


def slug_from_url(url: str) -> str:
    s = re.sub(r"https?://", "", url)
    s = re.sub(r"[^a-zA-Z0-9\-_.]", "_", s)
    return s[:80]


def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.executescript(SCHEMA)
    conn.commit()
    return conn


def insert_sankou_data(conn):
    """Insert data from SANKOU! URL lists + HTML files."""
    count = 0
    for genre_dir in sorted(RAW_DIR.iterdir()):
        if not genre_dir.is_dir():
            continue
        genre = genre_dir.name
        urls_file = genre_dir / "urls.json"
        if not urls_file.exists():
            continue

        urls = json.loads(urls_file.read_text())
        html_dir = genre_dir / "html"

        for url, meta in urls.items():
            slug = slug_from_url(url)
            html_file = html_dir / f"{slug}.html"
            meta_file = html_dir / f"{slug}.meta.json"

            has_html = html_file.exists()
            html_path = str(html_file) if has_html else None
            html_size = html_file.stat().st_size if has_html else None

            title = None
            if meta_file.exists():
                try:
                    local_meta = json.loads(meta_file.read_text())
                    title = local_meta.get("title")
                except Exception:
                    pass

            try:
                conn.execute(
                    """
                    INSERT OR IGNORE INTO lps (source, source_id, genre, title, lp_url,
                        html_path, html_size, has_html, metadata_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        "sankou",
                        slug,
                        genre,
                        title,
                        url,
                        html_path,
                        html_size,
                        has_html,
                        json.dumps(meta, ensure_ascii=False),
                    ),
                )
                count += 1
            except Exception as e:
                print(f"  insert error: {e}")

    conn.commit()
    return count


def classify_rdlp_genre(entry: dict) -> str:
    """rdlp.jpエントリから既存ジャンルを推定。"""
    text = " ".join(
        filter(
            None,
            [entry.get("title", ""), entry.get("keywords", ""), entry.get("description", "")],
        )
    ).lower()

    # ジャンル判定ルール（既存21ジャンルにマッピング）
    rules = [
        ("beauty-cosmetics", ["化粧品", "コスメ", "スキンケア", "美容液", "リップ", "ファンデ"]),
        ("medical-clinic", ["クリニック", "病院", "医療", "歯科", "皮膚科", "整形"]),
        ("wellness-health", ["健康", "サプリ", "ダイエット", "フィットネス", "整体"]),
        ("food-beverage", ["食品", "飲料", "カフェ", "レストラン", "お取り寄せ", "グルメ", "料理"]),
        ("fashion", ["ファッション", "アパレル", "ジュエリー", "時計", "バッグ", "靴"]),
        ("school-education", ["スクール", "教室", "学校", "大学", "英会話", "資格", "講座"]),
        ("real-estate", ["不動産", "マンション", "住宅", "リフォーム", "建築", "工務店"]),
        ("finance-insurance", ["銀行", "保険", "投資", "クレジット", "ローン", "FX", "金融"]),
        ("recruit-job", ["採用", "求人", "転職", "キャリア", "エントリー"]),
        ("saas-service", ["saas", "クラウド", "システム", "ソフトウェア", "アプリ", "ツール"]),
        ("ec-shop", ["楽天", "amazon", "online", "ショップ", "通販"]),
        ("travel-hotel", ["旅行", "ホテル", "旅館", "温泉", "ツアー", "観光"]),
        ("car-vehicle", ["自動車", "バイク", "車", "ディーラー", "試乗"]),
        ("portfolio-agency", ["制作", "デザイン", "エージェンシー", "クリエイティブ"]),
        ("publication", ["書籍", "本", "出版", "雑誌"]),
        ("campaign-special", ["キャンペーン", "プレゼント", "抽選", "特集"]),
        ("brand-corporate", ["ブランド", "企業", "コーポレート", "会社案内"]),
        ("life-goods", ["家具", "家電", "文具", "日用品", "インテリア"]),
        ("life-infra", ["インフラ", "産業", "エネルギー", "電気", "ガス"]),
        ("experience", ["体験", "アクティビティ", "テーマパーク", "遊園地"]),
    ]

    for genre, keywords in rules:
        for kw in keywords:
            if kw in text:
                return genre
    return "uncategorized"


def insert_rdlp_data(conn):
    """Insert data from rdlp.jp master or batch files."""
    count = 0
    for batch_file in sorted(RDLP_DIR.glob("*.jsonl")):
        with open(batch_file) as f:
            for line in f:
                try:
                    entry = json.loads(line)
                except Exception:
                    continue
                if not entry.get("lp_url"):
                    continue
                genre = classify_rdlp_genre(entry)
                try:
                    conn.execute(
                        """
                        INSERT OR IGNORE INTO lps (source, source_id, genre, title, company,
                            location, platform, lp_url, og_image, keywords, has_html, metadata_json)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            "rdlp",
                            str(entry["id"]),
                            genre,
                            entry.get("title"),
                            entry.get("company"),
                            entry.get("location"),
                            entry.get("platform"),
                            entry["lp_url"],
                            entry.get("og_image"),
                            entry.get("keywords"),
                            0,
                            json.dumps(
                                {"description": entry.get("description")}, ensure_ascii=False
                            ),
                        ),
                    )
                    count += 1
                except Exception as e:
                    print(f"  rdlp insert error: {e}")
    conn.commit()
    return count


def import_genre_insights(conn):
    """Import analysis/*.md files into genre_insights table."""
    analysis_dir = CORPUS_DIR / "analysis"
    if not analysis_dir.exists():
        print("No analysis directory found")
        return 0

    count = 0
    for md_file in sorted(analysis_dir.glob("*.md")):
        genre = md_file.stem
        content = md_file.read_text()

        # シンプルな抽出（後でLLMで詳細パースする）
        conn.execute(
            """
            INSERT OR REPLACE INTO genre_insights
            (genre, analysis_file, common_patterns)
            VALUES (?, ?, ?)
            """,
            (genre, str(md_file), content[:5000]),
        )
        count += 1

    conn.commit()
    return count


def stats(conn):
    print("\n=== DB Statistics ===")

    # Total
    total = conn.execute("SELECT COUNT(*) FROM lps").fetchone()[0]
    print(f"Total LPs: {total}")

    # By source
    print("\nBy source:")
    for row in conn.execute("SELECT source, COUNT(*) FROM lps GROUP BY source"):
        print(f"  {row[0]}: {row[1]}")

    # By genre
    print("\nBy genre:")
    for row in conn.execute(
        "SELECT genre, COUNT(*) FROM lps GROUP BY genre ORDER BY COUNT(*) DESC"
    ):
        print(f"  {row[0]}: {row[1]}")

    # Has HTML
    with_html = conn.execute("SELECT COUNT(*) FROM lps WHERE has_html=1").fetchone()[0]
    print(f"\nWith HTML: {with_html}")

    # Genre insights
    insights = conn.execute("SELECT COUNT(*) FROM genre_insights").fetchone()[0]
    print(f"Genre insights: {insights}")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    conn = init_db()

    if cmd in ("all", "sankou"):
        n = insert_sankou_data(conn)
        print(f"Inserted {n} SANKOU entries")
    if cmd in ("all", "rdlp"):
        n = insert_rdlp_data(conn)
        print(f"Inserted {n} rdlp entries")
    if cmd in ("all", "insights"):
        n = import_genre_insights(conn)
        print(f"Imported {n} genre insights")
    if cmd in ("all", "stats"):
        stats(conn)

    conn.close()


if __name__ == "__main__":
    main()
