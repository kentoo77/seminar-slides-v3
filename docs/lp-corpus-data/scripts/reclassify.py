#!/usr/bin/env python3
"""
既存DB内のLPエントリをジャンル再分類。
分類ロジック改善版: title + company を主に、keywordsは補助的にのみ使用。
"""
import sqlite3
import re
from pathlib import Path

DB_FILE = Path("/Users/oidekento/lp-corpus/db/lp_corpus.db")

# より精密なジャンル判定ルール
# (genre, [正規表現パターン])
RULES = [
    # 士業・法律事務所
    (
        "professional",
        [
            r"法律事務所",
            r"弁護士",
            r"税理士事務所",
            r"司法書士",
            r"行政書士",
            r"社労士",
            r"社会保険労務士",
            r"弁理士",
            r"会計事務所",
            r"特許事務所",
            r"債務整理",
            r"過払い金",
            r"自己破産",
            r"個人再生",
            r"任意整理",
            r"相続.*相談",
            r"法テラス",
        ],
    ),
    # 美容医療クリニック
    (
        "medical-clinic",
        [
            r"美容クリニック",
            r"美容外科",
            r"美容皮膚科",
            r"湘南美容",
            r"TCB",
            r"品川美容",
            r"ゴリラクリニック",
            r"脱毛クリニック",
            r"医療脱毛",
            r"歯科",
            r"インプラント",
            r"矯正歯科",
            r"美容整形",
            r"二重整形",
            r"鼻整形",
            r"脂肪吸引",
            r"整形外科",
            r"形成外科",
            r"眼科",
            r"皮膚科",
            r"病院",
            r"診療所",
            r"訪問看護",
            r"介護",
        ],
    ),
    # 金融・保険
    (
        "finance-insurance",
        [
            r"銀行",
            r"保険.*相談",
            r"生命保険",
            r"医療保険",
            r"自動車保険",
            r"火災保険",
            r"クレジットカード",
            r"ローン",
            r"カードローン",
            r"住宅ローン",
            r"FX",
            r"投資信託",
            r"NISA",
            r"iDeCo",
            r"仮想通貨",
            r"ファクタリング",
            r"ネオバンク",
            r"証券",
            r"ファンド",
            r"ベンチャーキャピタル",
            r"資産運用",
        ],
    ),
    # 転職・求人・採用
    (
        "recruit-job",
        [
            r"採用",
            r"求人",
            r"転職",
            r"人材派遣",
            r"人材紹介",
            r"キャリア",
            r"リクルート",
            r"エントリー",
            r"新卒",
            r"中途",
            r"ハローワーク",
            r"バイト",
            r"アルバイト",
            r"しごと",
            r"UIターン",
            r"IJUターン",
            r"移住",
        ],
    ),
    # 不動産・建築
    (
        "real-estate",
        [
            r"不動産",
            r"マンション",
            r"注文住宅",
            r"戸建",
            r"分譲",
            r"リフォーム",
            r"リノベーション",
            r"工務店",
            r"建築設計",
            r"住宅展示場",
            r"モデルハウス",
            r"外壁塗装",
            r"賃貸",
            r"ハウスメーカー",
            r"ゼネコン",
            r"建設",
        ],
    ),
    # 車・バイク
    (
        "car-vehicle",
        [
            r"自動車",
            r"軽自動車",
            r"新車",
            r"中古車",
            r"ディーラー",
            r"試乗",
            r"レクサス",
            r"トヨタ",
            r"ホンダ",
            r"日産",
            r"スズキ",
            r"ダイハツ",
            r"マツダ",
            r"スバル",
            r"アウディ",
            r"BMW",
            r"メルセデス",
            r"バイク",
            r"原付",
            r"カーコーティング",
            r"車検",
        ],
    ),
    # インフラ・産業
    (
        "life-infra",
        [
            r"電力",
            r"ガス",
            r"でんき",
            r"オール電化",
            r"再生可能エネルギー",
            r"太陽光",
            r"蓄電池",
            r"エネルギー",
            r"水道",
            r"インフラ",
            r"工事",
            r"鉄鋼",
            r"製造",
            r"プラント",
        ],
    ),
    # 美容医療系と区別する純美容クリニック/エステ
    (
        "beauty-clinic",
        [
            r"エステ",
            r"脱毛サロン",
            r"痩身",
            r"ブライダルエステ",
            r"フェイシャル",
        ],
    ),
    # 健康・ウェルネス
    (
        "wellness-health",
        [
            r"健康食品",
            r"青汁",
            r"酵素",
            r"サプリメント",
            r"プロテイン",
            r"ダイエット食品",
            r"栄養補助",
            r"機能性表示食品",
            r"漢方",
            r"鍼灸",
            r"整体",
            r"マッサージ",
            r"接骨院",
            r"カイロプラクティック",
            r"フィットネス",
            r"パーソナルジム",
            r"ヨガ",
            r"ピラティス",
            r"メンタル",
            r"カウンセリング",
            r"医療ダイエット",
        ],
    ),
    # 化粧品・コスメ (beauty-cosmeticsとbeauty-clinicを区別)
    (
        "beauty-cosmetics",
        [
            r"化粧品",
            r"コスメ",
            r"スキンケア",
            r"美容液",
            r"化粧水",
            r"乳液",
            r"クレンジング",
            r"ファンデーション",
            r"リップ",
            r"アイシャドウ",
            r"マスカラ",
            r"アイライナー",
            r"香水",
            r"シャンプー",
            r"トリートメント",
            r"ヘアオイル",
            r"育毛",
            r"アルファース",
            r"ALFACE",
            r"フェイスパック",
            r"パック",
        ],
    ),
    # 学校・教育・スクール
    (
        "school-education",
        [
            r"英会話",
            r"英語.*スクール",
            r"英語.*学習",
            r"英語学校",
            r"語学スクール",
            r"プログラミングスクール",
            r"オンラインスクール",
            r"通信講座",
            r"予備校",
            r"進学塾",
            r"学習塾",
            r"家庭教師",
            r"大学",
            r"専門学校",
            r"幼稚園",
            r"保育園",
            r"通信教育",
            r"資格.*講座",
            r"TOEIC",
            r"TOEFL",
            r"IELTS",
            r"英検",
        ],
    ),
    # SaaS・ITサービス
    (
        "saas-service",
        [
            r"SaaS",
            r"クラウド",
            r"システム",
            r"ソフトウェア",
            r"アプリ.*開発",
            r"API",
            r"ツール",
            r"プラットフォーム",
            r"ダッシュボード",
            r"CRM",
            r"SFA",
            r"MA",
            r"会計ソフト",
            r"勤怠",
            r"経費精算",
            r"請求書",
            r"電子契約",
            r"名刺管理",
            r"データ分析",
            r"AIソリューション",
        ],
    ),
    # 旅行・観光・ホテル
    (
        "travel-hotel",
        [
            r"旅行",
            r"ホテル",
            r"旅館",
            r"温泉",
            r"ツアー",
            r"観光",
            r"リゾート",
            r"民宿",
            r"ゲストハウス",
            r"航空券",
            r"レンタカー",
            r"体験.*予約",
            r"テーマパーク",
            r"遊園地",
            r"水族館",
            r"動物園",
            r"神社",
            r"寺",
        ],
    ),
    # キャンペーン・特設
    (
        "campaign-special",
        [
            r"キャンペーン",
            r"プレゼント企画",
            r"抽選",
            r"懸賞",
            r"フェア",
            r"セール",
            r"大決算",
            r"初売り",
            r"50周年",
            r"100周年",
            r"\d+周年",
            r"特集",
            r"限定",
            r"コラボ",
        ],
    ),
    # 食品・飲食
    (
        "food-beverage",
        [
            r"お菓子",
            r"スイーツ",
            r"ケーキ",
            r"チョコレート",
            r"クッキー",
            r"お取り寄せ",
            r"ギフト",
            r"お中元",
            r"お歳暮",
            r"ふるさと納税",
            r"食品",
            r"グルメ",
            r"飲料",
            r"ジュース",
            r"お茶",
            r"コーヒー",
            r"ビール",
            r"日本酒",
            r"ワイン",
            r"焼酎",
            r"ウィスキー",
            r"チューハイ",
            r"ハイボール",
            r"レストラン",
            r"居酒屋",
            r"カフェ",
            r"食材",
            r"野菜",
            r"果物",
            r"肉",
            r"魚",
            r"米",
            r"パン",
            r"ベーカリー",
            r"アサヒ.*(ビール|レモン|チューハイ|ハイボール)",
            r"サントリー",
            r"キリン",
            r"サッポロ",
            r"コカ・?コーラ",
            r"ぎょうざ",
            r"餃子",
        ],
    ),
    # ファッション
    (
        "fashion",
        [
            r"ファッション",
            r"アパレル",
            r"ブランド服",
            r"コート",
            r"ジャケット",
            r"ワンピース",
            r"スーツ",
            r"ジーンズ",
            r"スニーカー",
            r"ブーツ",
            r"バッグ",
            r"財布",
            r"ジュエリー",
            r"アクセサリー",
            r"時計",
            r"下着",
            r"ランジェリー",
            r"水着",
            r"メガネ",
            r"サングラス",
            r"帽子",
        ],
    ),
    # ECショップ（楽天掲載は自社じゃない）
    (
        "ec-shop",
        [
            r"オンラインショップ",
            r"ECサイト",
            r"通販サイト",
            r"楽天市場",
            r"購入.*サイト",
            r"カート",
        ],
    ),
    # 出版
    (
        "publication",
        [
            r"書籍",
            r"新刊",
            r"発売.*書籍",
            r"小説",
            r"漫画",
            r"コミック",
            r"雑誌",
            r"写真集",
            r"電子書籍",
            r"出版社",
            r"書店",
        ],
    ),
    # 生活用品・家具・家電
    (
        "life-goods",
        [
            r"家具",
            r"家電",
            r"白物家電",
            r"冷蔵庫",
            r"洗濯機",
            r"エアコン",
            r"掃除機",
            r"オーブン",
            r"レンジ",
            r"ドライヤー",
            r"文具",
            r"ステーショナリー",
            r"インテリア",
            r"ベッド",
            r"ソファ",
            r"テーブル",
            r"チェア",
            r"収納",
            r"食器",
            r"キッチン用品",
            r"調理器具",
            r"洗剤",
            r"シャンプー.*ボトル",
        ],
    ),
    # 体験・インタラクティブ
    (
        "experience",
        [
            r"体験型",
            r"VR",
            r"AR",
            r"インタラクティブ",
            r"ワークショップ",
            r"教室.*体験",
        ],
    ),
]

# デフォルト分類（いずれにもマッチしない場合）
DEFAULT_GENRE = "brand-corporate"


def classify(title: str | None, company: str | None, description: str | None) -> str:
    """改善された分類ロジック。keywordsは使わない（全エントリ同じため）。"""
    text = " ".join(filter(None, [title or "", company or "", description or ""]))
    if not text.strip():
        return DEFAULT_GENRE

    for genre, patterns in RULES:
        for pat in patterns:
            if re.search(pat, text):
                return genre
    return DEFAULT_GENRE


def main():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row

    # rdlp エントリだけ再分類
    cursor = conn.execute(
        "SELECT id, title, company, metadata_json FROM lps WHERE source='rdlp'"
    )
    entries = cursor.fetchall()
    print(f"Reclassifying {len(entries)} rdlp entries...")

    updated = 0
    genre_counts = {}
    for row in entries:
        import json

        desc = None
        if row["metadata_json"]:
            try:
                meta = json.loads(row["metadata_json"])
                desc = meta.get("description", "")
            except Exception:
                pass
        new_genre = classify(row["title"], row["company"], desc)
        genre_counts[new_genre] = genre_counts.get(new_genre, 0) + 1
        conn.execute("UPDATE lps SET genre=? WHERE id=?", (new_genre, row["id"]))
        updated += 1

    conn.commit()
    print(f"Updated {updated} entries")
    print("\nNew distribution (rdlp only):")
    for g, c in sorted(genre_counts.items(), key=lambda x: -x[1]):
        print(f"  {g}: {c}")

    print("\n=== Full DB stats (after reclassify) ===")
    for row in conn.execute(
        "SELECT genre, COUNT(*) FROM lps GROUP BY genre ORDER BY COUNT(*) DESC"
    ):
        print(f"  {row[0]}: {row[1]}")

    conn.close()


if __name__ == "__main__":
    main()
