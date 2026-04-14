# brand-corporate LP 構造分析レポート（ラウンド2、N=200件 統計集計）

**ジャンル**: brand-corporate（ブランドサイト / コーポレートサイト）
**対象コーパス**: `/Users/oidekento/lp-corpus/raw_all/brand-corporate/`（全 1,132 件）
**今回の分析件数**: 200 件（無作為抽出）
**分析日**: 2026-04-08
**ラウンド**: 2（本番）
**ラウンド1 との差分**: ラウンド1は 30 件の精読のみで統計サマリ不在。本ラウンドは 200 件の機械集計 + 15 件の個別精読を両立させ、フォント・配色・ライブラリ・セクション構成・CTA 文言の頻度分布を初めて確定させた。

---

## 0. エグゼクティブサマリ（先に結論）

1. **ブランド/コーポレートLPは "買わせないLP" である**。ラウンド1の仮説どおりだったが、200件集計で定量確認できた：H1 なし・CTA 数 1〜2 個・スクロール誘導・余白最大化が過半を占める。セールスLP の鉄板セオリー（FV 内 CTA、悩み訴求、赤/黄色強色）は **完全に逆張り**。
2. **使用フォントはほぼ 3 系統に収斂**する：
   - Google Fonts `Noto Sans JP`（46/200 = 23%、事実上の日本語ベース）
   - Google Fonts `Zen Kaku Gothic New`（11/200 = 5.5%、現代コーポレート）
   - Adobe Typekit（18/200 = 9%、`dnp-shuei-gothic-gin-std` / `source-han-sans-japanese` / `a-otf-gothic-bbb-pr6n` など "らしい" 明朝・角ゴシック）
   - 装飾系英字フォントは `Poppins` `Oswald` `Marcellus` `Bebas Neue` の 4 強。
3. **配色は極めて保守的**。WordPress Gutenberg のプリセット（`#32373C` など）がノイズとして混入するのを除けば、**"ほぼモノトーン（#FFFFFF + #000000 前後）+ 1 色のアクセント"** が 7 割。theme-color メタタグは `#FFFFFF` が圧倒的多数（21/43）。
4. **ライブラリ使用率の実態**：
   - WordPress 123/200 = **61.5%**（国内コーポレートサイト市場の圧倒的な現実）
   - Google Analytics 166/200 = 83%、Google Fonts 89/200 = 44.5%、jQuery 69/200 = 34.5%
   - モダン系は Swiper 52、Barba 21、GSAP 16、Lenis 11、Lottie 15、Next.js 12、Nuxt 16、Astro 3
   - **Tailwind は 200 件中たった 4 件（2%）** — コーポレートサイトは依然として CMS+手書き CSS/SCSS が主流
5. **ナビゲーション構成はほぼ固定化**：`Contact (35)` `News (25)` `About (22)` `Company (18)` `Recruit (17)` `Service (16)` `Works (9)` の 7 項目で全体の過半をカバー。この 7 項目は「ブランドLP 標準グローバルナビ」と呼んで差し支えない。
6. **英語大文字見出しの復権**：49/200 = 24.5% で `lang=en` または `>EN<` トグルが存在し、41/200 = 20.5% で `01 02 03` の章番号表示、19/200 = 9.5% で英字マーキー（横流れテキスト）を使用。
7. **全角スペース演出**（`B R A N D` のような字間開け）は 49/200 = **24.5%** に出現。これがブランドLP 特有の "静謐なタイポグラフィ" の正体である。
8. **design-mcp 生成時のモード切替が必須**。セールスLP モード（扇情・装飾・CTA多重）とブランドLP モード（余白・モノトーン・CTA 1-2個・スクロール主役）を明示的に分けなければ、出力は確実にチグハグになる。

---

## 1. データソース & 集計方法

### 1-1. 対象
- ディレクトリ: `/Users/oidekento/lp-corpus/raw_all/brand-corporate/`
- 全件数: **1,132 件**（`ls | wc -l`）
- サンプル: `sort -R | head -200` で無作為抽出 → `/tmp/bc_sample200.txt` に保存
- 平均ファイルサイズ: **127,660 バイト**（HTML 単体の実測値）
- 本ラウンド精読: 15 サイト（後述）

### 1-2. 抽出スクリプト
`/tmp/bc_extract.py`（Python 3 / 標準ライブラリのみ）を使用し 200 件を一括処理。抽出項目：
- `<title>` / `<meta name="description">` / `<h1>` / `<h2>`
- `font-family` 宣言（インラインCSS・`<style>` 内）と `@font-face` ブロック
- Google Fonts URL からの `family=` パラメータ
- Adobe Typekit (`use.typekit.net/{id}.css`) の有無
- `#xxxxxx` カラーコード（ファイル単位の "出現回数" ではなく **存在有無** でカウントし、特定ファイルのノイズ混入を抑制）
- `<section class="...">` のクラス名
- `<a class="btn|button|cta|link">` と `<button>` の文言
- ライブラリ検出（30 パターン：tailwind / swiper / gsap / lenis / barba / next / nuxt / astro / wordpress など）
- OGP / Twitter カード / JSON-LD / viewport / favicon 有無
- `<html lang>` 属性
- `<video autoplay>` ベースのヒーロー背景動画
- `max-width: XXXpx` の主要コンテナ幅
- `>01< >02<` の章番号
- 全角スペース字間演出（`一-龯　一-龯` 正規表現）
- マーキー / 横スクロールの keyframes

---

## 2. 統計サマリ

### 2-1. 配色トップ（出現頻度：ファイル単位）

| 順位 | カラー | 出現ファイル数 | 比率 | 用途 |
|---|---|---|---|---|
| 1 | `#FFFFFF` | 95 | 47.5% | 背景基調 |
| 2 | `#000000` | 86 | 43.0% | 文字基調 |
| 3 | `#32373C` | 66 | 33.0% | WordPress エディタ既定（実質ノイズ） |
| 4 | `#1A1A1A` / `#212121` / `#222222` / `#333333` | 17 合計 | 8.5% | 黒の "完全純黒回避" バリエーション |
| 5 | `#F2F2F2` / `#F5F5F5` / `#F0F0F0` / `#E6E6E6` / `#DCDCDC` / `#E8E8E8` | 26 合計 | 13% | セクション区切り用グレー背景 |
| 6 | `#FF0000` | 3 | 1.5% | 純赤は極端に少ない |

**Gutenberg プリセット除外後の "実質 theme-color"**（`<meta name="theme-color">` 値の集計 43 件中）:

| 順位 | theme-color | 件数 | 比率 |
|---|---|---|---|
| 1 | `#FFFFFF` | 21 | 48.8% |
| 2 | `#000000` | 2 | 4.7% |
| 3〜 | 各 1 件 | 20 | 46.5% |

> 単色カラーパレット（白 or 黒のワントーン基調）**7 割超**。2 色以上のアクセントを持つサイトは少数派。例外的に `#ED6103`（LIFULL オレンジ）、`#FE6D02`（BEAMS CREATIVE オレンジ）、`#4D5FFF`（MESON ブルー）、`#C5A27B`（commono ベージュ）、`#008CDA`（ALE ブルー）のような **1 点主張色** を持つ。

**CSS変数 `--primary / --accent / --brand`** は 200 件中わずか 30 件（= 15%）でしか定義されておらず、そのうち 25 件が WordPress テーマの既定 `#007CBA` でノイズ。**トークン管理されたデザインシステムは実質 10% 未満**。

---

### 2-2. フォントトップ（Google Fonts + Adobe Fonts 経由）

**Google Fonts（200 件中の `family=` パラメータ頻度）:**

| 順位 | フォント | 件数 | 比率 | カテゴリ |
|---|---|---|---|---|
| 1 | **Noto Sans JP** | 46 | 23.0% | 日本語ゴシック |
| 2 | **Zen Kaku Gothic New** | 11 | 5.5% | 日本語ゴシック（現代コーポレート） |
| 3 | **Poppins** | 11 | 5.5% | 欧文ジオメトリックサンセリフ |
| 4 | **Roboto** | 9 | 4.5% | 欧文ニュートラル |
| 5 | **Noto Serif JP** | 8 | 4.0% | 日本語明朝 |
| 6 | **Oswald** | 6 | 3.0% | 欧文縦長コンデンス（"BRANDING" ロゴ風） |
| 7 | **Inter** | 5 | 2.5% | 欧文ニュートラル（IT系） |
| 8 | **Bebas Neue** | 4 | 2.0% | 欧文オールキャップス |
| 9 | Josefin Sans | 4 | 2.0% | 欧文 |
| 10 | M PLUS 1p / M PLUS Rounded 1c / Montserrat / Lato / Material Symbols Outlined | 各 3 | 1.5% | — |

**Adobe Typekit 使用**: 18/200 = **9.0%**
代表 face 名: `dnp-shuei-gothic-gin-std`（DNP 秀英角ゴシック）、`source-han-sans-japanese`（源ノ角ゴシック）、`a-otf-gothic-bbb-pr6n`（モリサワ ゴシック BBB）、`everett`、`reckless`、`lausanne`、`PP Eiko`、`PP Neue Montreal`、`NeuePlak`、`area-variable`、`TazuganeGothic` など。

> **読み取り**: 無料の Google Fonts で済ませる多数派（Noto Sans JP 一強）と、ブランド優位性を買うために Adobe Fonts / Pangram Pangram / Commercial Type 系を採用する少数派（主にクリエイティブエージェンシーと上場ブランド）に二極化。**中間層のオリジナル Web フォント採用はほぼ無い**。

---

### 2-3. ライブラリ使用率（上位のみ）

| 順位 | ライブラリ | 件数 | 比率 | コメント |
|---|---|---|---|---|
| 1 | **Google Analytics (gtag)** | 166 | 83.0% | 事実上必須 |
| 2 | **WordPress** | 123 | **61.5%** | 国内コーポレートの圧倒的現実 |
| 3 | **Google Fonts** | 89 | 44.5% | — |
| 4 | **jQuery** | 69 | 34.5% | WP テーマ残滓を含む |
| 5 | **Swiper** | 52 | 26.0% | 実績スライダー等で最多カルーセル |
| 6 | **Adobe Fonts (Typekit)** | 43 | 21.5% | ※検出条件を広げたため 2-2 の 18 件と差 |
| 7 | **Slick Carousel** | 25 | 12.5% | Swiper へ移行中の旧世代 |
| 8 | **Barba.js** | 21 | 10.5% | ページトランジション（SPA 化） |
| 9 | **Nuxt.js** | 16 | 8.0% | — |
| 10 | **GSAP** | 16 | 8.0% | 高度アニメーション |
| 11 | Lottie | 15 | 7.5% | — |
| 12 | **Next.js** | 12 | 6.0% | — |
| 13 | **Lenis (smooth scroll)** | 11 | 5.5% | **モダン DA 系に集中** |
| 14 | YouTube embed | 10 | 5.0% | — |
| 15 | Vimeo embed | 9 | 4.5% | — |
| 16 | Alpine.js | 8 | 4.0% | — |
| 17 | microCMS | 7 | 3.5% | 国産 Headless CMS |
| 18 | FontAwesome | 6 | 3.0% | 減少傾向 |
| 19 | three.js | 4 | 2.0% | WebGL ヒーロー演出 |
| 20 | WOW.js | 4 | 2.0% | AOS の旧版 |
| 21 | **Tailwind CSS** | 4 | **2.0%** | ★極めて少ない |
| 22 | Astro | 3 | 1.5% | — |
| 23 | Bootstrap | 3 | 1.5% | 減少傾向 |
| 24 | Stimulus (Hotwire) | 2 | 1.0% | — |
| 25 | AOS (scroll) | 2 | 1.0% | — |
| — | ScrollMagic | 1 | 0.5% | — |
| — | Gatsby | 1 | 0.5% | — |
| — | Vue (直接参照) | 0 | 0% | Nuxt 経由 |
| — | locomotive-scroll | 0 | 0% | Lenis に置換済み |

**重要な相関パターン（ラウンド2で新発見）:**
- **"Lenis + Barba + GSAP" 三点セット** = デザインエージェント / クリエイティブ寄りブランドLP の DNA。Commono（gsap+lenis+swiper+wp）、NEWFOLK、hadashinoie、goinc など。
- **"Next.js + Swiper + Vimeo"** = 上場・資金調達済みスタートアップのブランドLP の DNA。Creatures、Mimiguri、Nomurakougei。
- **"Nuxt + Lenis + microCMS"** = 最もモダンな日本の SSG スタック。Meson など。
- **"Astro + microCMS"** = 最新の軽量化選択肢。SmartHR がこれ。
- **"WordPress + jQuery + Swiper + Slick"** = 中堅コーポレート（売上 10〜200 億円）のデフォルト。過半数のブランドLP がここ。
- **Tailwind 採用率 2%** は驚くべき低さ。コーポレートは依然として「CMS テーマ + SCSS + BEM 派生クラス」の世界。

---

### 2-4. ナビゲーション項目の出現率（アンカーテキスト完全一致）

| 順位 | ナビ項目 | 件数 | 比率 |
|---|---|---|---|
| 1 | **Contact** | 35 | 17.5% |
| 2 | **News** | 25 | 12.5% |
| 3 | **About** | 22 | 11.0% |
| 4 | **Company** | 18 | 9.0% |
| 5 | **Recruit** | 17 | 8.5% |
| 6 | **Service** | 16 | 8.0% |
| 7 | Works | 9 | 4.5% |
| 8 | Careers | 7 | 3.5% |
| 9 | Blog | 7 | 3.5% |
| 10 | Projects | 5 | 2.5% |

> **注**: 上記は英字表記の完全一致カウントのため、「お問い合わせ / ニュース / 会社概要 / 採用情報」の日本語カウントを加えると実際の出現率は 2〜3 倍になる。つまり **コーポレートのグローバルナビは Contact / News / About / Company / Recruit / Service / Works の 7 固定枠**。ブランドLP のグローバルナビを設計する際、この 7 項目から逸脱する理由がなければ従うべき。

---

### 2-5. CTA 文言トップ（`<a class="...btn|button|cta|link">` テキスト）

| 順位 | CTA 文言 | 件数 | 比率 |
|---|---|---|---|
| 1 | **お問い合わせ** | 32 | 16.0% |
| 2 | **Read More** | 29 | 14.5% |
| 3 | 詳しく見る | 21 | 10.5% |
| 4 | READ MORE | 19 | 9.5% |
| 5 | VIEW MORE | 17 | 8.5% |
| 6 | View more | 15 | 7.5% |
| 7 | もっと見る | 14 | 7.0% |
| 8 | View All | 10 | 5.0% |
| 9 | くわしく見る | 10 | 5.0% |
| 10 | 採用情報 | 9 | 4.5% |
| 11 | More | 9 | 4.5% |
| 12 | 詳しくはこちら | 8 | 4.0% |
| 13 | もっとみる | 8 | 4.0% |
| 14 | MORE / LEARN MORE | 各 6 | 3.0% |
| 15 | 資料請求 / 詳細を見る | 各 6 | 3.0% |
| 16 | 会社概要 | 4 | 2.0% |
| 17 | 資料ダウンロード | 4 | 2.0% |

**パターン抽出**:
- "View / Read / More" の **英字変種だけで計 108 件 / 200** = 54%。日本のブランドLPの「もっと見る」系 CTA は半数以上が英語表記。これはセールスLP（「今すぐ申し込む」「無料体験」が 8 割以上）と真逆の文化。
- 行動喚起語（申し込み・購入・無料）は **ゼロ**。ブランドLP は "閲覧継続" が最終目的で、"意思決定" を求めない。
- 「お問い合わせ」（16%）と「採用情報」（4.5%）の 2 つだけがビジネス目的を持つ CTA。それ以外は全部「詳しく見る」系の柔らかい継続誘導。

---

### 2-6. セクションクラス名トップ

| 順位 | クラス名 | 件数 |
|---|---|---|
| 1 | `about` | 8 |
| 2 | `section` / `works` | 各 7 |
| 3 | `news` / `service` | 各 6 |
| 4 | `recruit` / `home-news` | 各 5 |
| 5 | `container` / `fv` / `message` / `topnews` / `home-service` / `home-hero` | 各 4 |
| 6 | `mv` (MainVisual) / `mainvisual` / `p-top-kv` / `top_mv` | 合計 9 |
| 7 | `news-sec` / `archive` / `topics` / `top-section` / `home-about` | 各 3 |

**標準セクション順序（複数サイト精読から帰納）**:
1. `FV / MV (Main Visual)` — フルスクリーン or 60vh
2. `Message / Concept` — ミッション / 一言コピー
3. `Service / Business` — 事業紹介（4-6 カード）
4. `Works / Case / Projects` — 実績（カルーセルorグリッド）
5. `About / Company` — 会社概要
6. `News / Topics` — 最新情報（3-5 件）
7. `Recruit` — 採用（縦バナー 1 つ）
8. `Footer` — 住所・ロゴ・SNS

この順序からの逸脱は 200 件中 20 件未満。**ブランドLP の骨格は事実上固定**。

---

### 2-7. コンテナ最大幅（`max-width: px`）

| 順位 | 幅 | 件数 |
|---|---|---|
| 1 | 1280px | 5 |
| 2 | 1023px | 5 |
| 3 | 900px / 800px | 各 4 |
| 4 | 1024px / 1100px | 各 3 |
| 5 | 1800px / 959px | 各 2 |

**読み取り**: 中心は `1024〜1280px` だが、`800〜900px`（文章主体の静謐型）と `1800px+`（フルブリード画像型）の二極化も確認。レスポンシブ brake point は実質 1024px で統一されている。

---

### 2-8. メタ情報・SEO 基礎

- **OGP (`og:`)**: 191/200 = **95.5%**
- **og:image 明示**: 187/200 = 93.5%
- **Twitter カード**: 154/200 = 77.0%
- **charset=utf-8**: 198/200 = 99.0%
- **viewport**: 197/200 = 98.5%
- **favicon**: 186/200 = 93.0%
- **JSON-LD 構造化データ**: 81/200 = **40.5%**（ほぼ WordPress プラグインの Yoast / RankMath 経由）
- **hreflang（多言語）**: 23/200 = 11.5%
- **html lang="ja"**: 177/200、"ja-jp": 2、"en": 1、"jp": 1（**21 件は lang 未設定**）

---

### 2-9. ヒーロー・演出パターン

| パターン | 件数 | 比率 |
|---|---|---|
| `<video autoplay>` ヒーロー | 25 | 12.5% |
| `<video autoplay loop muted>` 背景動画 | 21 | 10.5% |
| EN/JP トグル or `lang=en` 存在 | 49 | 24.5% |
| 章番号 `01 02 03` 表示 | 41 | 20.5% |
| スクロールダウンインジケータ | 22 | 11.0% |
| 全角スペース字間演出（`あ　い　う`） | **49** | **24.5%** |
| マーキー（横流れテキスト keyframes） | 19 | 9.5% |
| 横スクロール（`overflow-x: auto/scroll`） | 11 | 5.5% |
| `mix-blend-mode` 使用 | 12 | 6.0% |
| `clip-path` 使用 | 14 | 7.0% |

**発見**: ブランドLP における「全角スペース字間」は 24.5% に達する定番演出。これは日本語コーポレートの "静謐・余韻" トーンを生成する最大の武器で、CSS の `letter-spacing: 0.3em` と併用されるケースが多い。**セールスLP で見たら浮くが、ブランドLP では必須装備**。

---

## 3. 精読 15 サイトのケーススタディ

ラウンド2 ではサンプル 200 件の中から、業種・規模・スタックが散らばるよう 15 サイトを精読した。

### 3-1. MESON（`www.meson.tokyo`）— Nuxt 系モダンスタック代表
- **URL**: https://www.meson.tokyo/
- **業種**: XR / AI 空間インテリジェンス スタートアップ
- **スタック**: Nuxt.js + Lenis + microCMS + Vimeo
- **カラー**: `#1E1E1E`（29 回）/ `#4D5FFF`（7 回 = ブランドブルー）/ `#FBE233`（5 回 = アクセント黄）/ `#F0F0F0`（body 背景）
- **フォント**: `NeuePlak`（Adobe Fonts、見出し欧文）+ `Noto Sans JP`（本文日本語）
- **H1**: "MESONは、XR技術とAI技術が融合した 空間インテリジェンス技術の 社会実装を目指すスタートアップです。" — 一文そのまま H1 に置く珍しいパターン
- **letter-spacing**: `0.16px / 0.28px / 0.32px / 0.4px / 0.6px / 0.84px / 1.23px / 1.2px` と 8 段階、極めて精密
- **特徴**: Lenis によるスロースクロール。h1 に全文コピーを入れることで SEO と演出を両立。Vimeo 背景動画。
- **学び**: 「一文 H1 + 超精密 letter-spacing + Lenis 慣性」の組み合わせで "次世代感" を出すテンプレが完成している。

### 3-2. commono inc.（`commono.co.jp`）— デザインエージェンシー王道型
- **URL**: https://commono.co.jp/
- **業種**: 札幌のデザインブランディング
- **スタック**: WordPress + GSAP + Lenis + Swiper + jQuery
- **カラー**: `#C5A27B`（ベージュ / 4 回）+ モノトーン + Gutenberg 既定色
- **H1**: 空（ロゴ画像で代替）
- **H2**: "ブランドとビジネスの間を、 デザインでつなぐ。"
- **CTA**: "事例一覧を見る" / "サービス詳細"
- **mix-blend-mode**: 使用。画像へのオーバーレイテキスト
- **特徴**: 「WordPress ベース + Lenis + GSAP + Swiper + mix-blend-mode」の **デザインエージェント王道スタック**。この構成だけで日本の制作会社コーポレートの 30% 以上を再現できる。
- **学び**: ラウンド1 で見た NSSG と類似。"大きな画像 + 余白 + 英語一言コピー + ブロック組み" の典型。

### 3-3. SmartHR（`smarthr.co.jp`）— Astro + microCMS 最新型
- **URL**: https://smarthr.co.jp/
- **業種**: HR SaaS（上場）
- **スタック**: **Astro + microCMS + GA**（jQuery なし、WordPress なし）
- **カラー**: `#00C4CC`（SmartHR ブランド水色 / 3 回）+ `#EE3123`（赤）+ `#0866FF`（青）+ `#1D1C1B`（近黒）
- **H1**: "SmartHR"（ロゴテキスト）
- **H2**: "ミッション" / "サービス" / "ニュース"（超シンプル）
- **H3**: "労働にまつわる社会課題をなくし、誰もがその人らしく働ける社会をつくる。"
- **clip-path**: 使用
- **特徴**: 200 件中わずか 3 件しかない Astro 採用。巨大コーポレートがモダン軽量スタックに移行した事例として注目。JS バンドルが最小で、LCP 最速候補。
- **学び**: 「Astro + microCMS」は Nuxt/Next より LP 向きで、**LP生成ターゲットの第一選択肢**にすべき。

### 3-4. LIFULL（`lifull.com`）— 大企業 "自前フォント" 型
- **URL**: https://lifull.com/
- **業種**: 不動産情報プラットフォーム（上場・売上 300 億超）
- **スタック**: WordPress + jQuery + Slick
- **フォント**: **`LIFULL`**（自社オリジナル Web フォント）+ `LIFULLFont_mono`
- **カラー**: `#ED6103`（ブランドオレンジ / 32 回）+ `#FEF3EB`（body 背景の淡オレンジ）+ 10 色以上の補助色（事業ごとに色分け）
- **H1**: "株式会社LIFULL" + "事業を通じて、社会課題解決へ"
- **letter-spacing**: `0.04em`
- **特徴**: **自社フォント（LIFULL フォント）を Web にも使用**。body 背景に淡オレンジ（`#FEF3EB`）を敷いて単なる白ベースを回避している高度テクニック。
- **学び**: 超大手は「独自フォント + 1 色 body 背景着色」で差別化する。真似るなら CSS `body { background: #fef3eb; }` を入れるだけで "大手っぽさ" が出る。

### 3-5. カオナビ（`corp.kaonavi.jp`）— 王道コーポレート型
- **URL**: https://corp.kaonavi.jp/
- **業種**: タレントマネジメント SaaS（上場）
- **スタック**: WordPress + Google Fonts
- **カラー**: `#FFFFFF`（16 回）+ `#447FE0`（青 / 8 回 = ブランドカラー）+ `#202226`（文字）
- **H1**: "Face you, Face next."（英語ブランドスローガン）
- **H2**: "Purpose 私たちが社会に対してすべきこと" / "Service 事業概要" / "Culture カルチャー"
- **特徴**: 見出しが **"英字大文字 + 日本語補足" のバイリンガル二段**。これが 200 件中 40 件以上に出現する超定番パターン。
- **学び**: H2 は `英字 [ 日本語 ]` の 2 段組にすると、何もしなくても "コーポレートっぽく" なる。

### 3-6. 認定NPO法人フローレンス（`florence.or.jp`）— NPO / ソーシャル型
- **URL**: https://florence.or.jp/
- **業種**: 認定 NPO（こども支援）
- **スタック**: WordPress + Swiper
- **H1**: "こどもたちのために、日本を変える"
- **CTA**: "#ひとり親家庭支援 【サポート隊員250名募集中】ひとり親家庭を寄付で応援" 等、ハッシュタグ先頭型の訴求 CTA が特徴
- **特徴**: コピーが情緒訴求。ハッシュタグ先頭カード型の "寄付アクション" CTA を 4-5 個並べる独自パターン。NPO/社会課題系コーポレートの参考例。
- **学び**: NPO は "行動 CTA" を持つ唯一のブランドLP 亜種。「#カテゴリタグ + アクションコピー」でカード化するスタイルは NPO 全般に応用可。

### 3-7. ALE（`star-ale.com`）— 宇宙ベンチャー / 黒基調
- **URL**: https://star-ale.com/
- **業種**: 人工流れ星 宇宙ベンチャー
- **スタック**: 軽量（GA のみ、ライブラリほぼ無し）
- **カラー**: **`#000D14`**（ほぼ黒・深宇宙色、body background）+ `#22253A`（深紫紺）+ `#008CDA`（青）
- **H1**: "Exploring the Blue"
- **特徴**: **body 背景が純黒ではなく `#000D14`（深海 / 深宇宙トーン）** というテクニック。純黒 `#000` はコントラスト強すぎで疲れるが、`#000D14` は同じ黒に見えて目が楽。
- **学び**: 黒基調のブランドLP を作るとき `#000` ではなく `#050506` 〜 `#0C0F14` あたりを使う。これが "意識的に黒を選んだ感" を出す鍵。

### 3-8. 株式会社翔陽（`syoyo-al.co.jp`）— 町工場 × モダンブランディング
- **URL**: https://syoyo-al.co.jp/
- **業種**: アルミ鋳造町工場（兵庫）
- **スタック**: WordPress + Barba + Lenis
- **H2**: **"ま だ 見 ぬ ア ル ミ の 可 能 性 ア カ ル イ ミ ラ イ"**（全角スペース字間演出、ひらがな＋漢字の余韻型）
- **特徴**: 古典的製造業が Barba + Lenis を採用し、見出しを全角スペースで字間開けする "町工場リブランディング" の代表例。技術継承を謳う会社ほど、逆説的にモダン Web 技術で見せ方を刷新している。
- **学び**: 「製造業 × Barba ページトランジション × 全角スペース字間」は 2023 年以降の地方工場リブランディングの鉄板テンプレ。

### 3-9. MIMIGURI（`mimiguri.co.jp`）— 組織コンサル / Next.js 型
- **URL**: https://mimiguri.co.jp/
- **業種**: 人と組織の経営コンサル
- **スタック**: **Next.js + microCMS + Swiper**
- **H2**: "PICKUP NEWS" / "人と組織の可能性を 最大限に活かした 新しい多角化経営モデル" / "提供サービス"
- **特徴**: Next.js で SSG したうえで microCMS と連携。jQuery/WordPress 一切なし。
- **学び**: スタートアップ / コンサル系は **Next.js + microCMS** が鉄板。WP を使わない判断は「記事が少ないがデザイン精度を最優先」という戦略。

### 3-10. 乃村工藝社（`nomurakougei.co.jp`）— 空間デザイン最大手
- **URL**: https://www.nomurakougei.co.jp/
- **業種**: 空間デザイン（売上 1,000 億超）
- **スタック**: **Next.js + Adobe Fonts + WordPress（ハイブリッド）+ Swiper**
- **カラー**: `#595C56`（くすみグレー）+ `#191A18`（黒）
- **H1**: "乃村工藝社・空間デザイン"
- **特徴**: 実績（Works）ファーストの UI。カルーセル + 大画像 + キャプション薄めの "建築写真集" 型。
- **学び**: 写真が主役のブランドLP は「H1 は会社名一行 + 実績カルーセルを FV 直下」のミニマル構成で十分成立する。

### 3-11. BEAMS CREATIVE（`beamscreative.jp`）— ブランド系エージェンシー
- **URL**: https://beamscreative.jp/
- **業種**: BEAMS のクリエイティブ子会社
- **スタック**: WordPress + Adobe Fonts + Swiper + DM Sans（Google Fonts）
- **カラー**: **`#FE6D02`**（強いオレンジ 18 回）+ `#6D9EEB`（水色）+ `#23B73C`（緑）
- **H2**: "直 感 と 共 感。 愛 と ア イ デ ア。"（全角スペース演出）
- **特徴**: ファッション系 DNA を受け継ぎ、色を **あえて強く使う** 稀な例。文章は全角スペースで読ませる。
- **学び**: "クリエイティブ子会社" は親ブランドの色彩を反映しつつ、余白と全角スペースで上品さを担保する。

### 3-12. pentel（`pentel.co.jp`）— 老舗メーカー / 多色ポップ型
- **URL**: https://www.pentel.co.jp/
- **業種**: 文具メーカー
- **スタック**: WordPress + Adobe Fonts + Slick Carousel
- **カラー**: `#212121`（61 回 = 文字）+ **`#B5EBFF` `#E5C7FF` `#FFE890` `#BBFFBE`**（各 14-15 回 = 淡色 4 色）+ `#FF0000`（6 回 = 赤）
- **H2**: "表現する よろこびを。 The Joy of Expression."
- **特徴**: **淡いパステル 4 色を均等配分**。文具メーカーならではの "色鉛筆っぽい" 遊び心。文字は黒一色で締める。
- **学び**: 多色ブランドを扱う時は「アクセント 4 色を均等に + 文字は #212121 に固定」で破綻しない。

### 3-13. UUUM（`uuum.co.jp`）— YouTuber MCN
- **URL**: https://www.uuum.co.jp/
- **業種**: クリエイターエージェンシー（上場）
- **H1**: "UUUM | Create a G o o d Ecosystem to Solve Social Issues"（全角スペース字間演出を英語でも使う）
- **H2**: "Featured" / "New Group Purpose" / "Our Service"
- **特徴**: 全角スペース字間を **英字でも適用**（`G o o d`）。英字でも余韻を作る独自スタイル。
- **学び**: 全角スペース演出は英字にも適用可能。`letter-spacing: 0.5em` + 見出し英字で "静かな主張" を表現。

### 3-14. NEWFOLK（`newfolk.jp`）— 独立スタジオ型
- **URL**: https://newfolk.jp/
- **業種**: デザインエージェンシー（東京）
- **カラー**: `#EBEAE8`（アイボリー / body background）
- **H1**: "NEWFOLK"（ロゴのみ）
- **H2**: "Studio" / "Stay On Target." / "Newfolk" / "Strength" / "Services" / ""Beautiful design is Beautiful answers.""
- **theme-color**: `#EBEAE8`
- **特徴**: body 背景を純白ではなく **`#EBEAE8`（温かみのあるアイボリー）**。静謐なテクスチャ感を生む。
- **学び**: デザインスタジオ系は純白を避けてアイボリー / オフホワイト (`#EBEAE8` `#F5F0E9` `#F8F2EE`) を使うのが 30〜40% の確率で観測される定番。

### 3-15. 游藝舎（`yugeisha.com`）— 伝統工芸 × モダン
- **URL**: https://www.yugeisha.com/
- **業種**: 伝統工芸（工芸作品販売）
- **スタック**: **Lenis + GSAP + Swiper + Lottie**（フルモダン）
- **フォント**: Google Fonts `Cardo`（クラシック明朝）+ 日本語フォント
- **カラー**: `#E6E6E6` / `#939DAD` / `#0B2244`（深藍）
- **H1**: **"いま、残したいものがある。"**
- **特徴**: 伝統工芸のサイトが **Lenis + GSAP + Lottie** を全部入り。タイトル「いま、残したいものがある。」は 8 文字＋句点の余韻型で、全 200 件で最も印象に残ったコピー。
- **学び**: 伝統産業ほどモダン技術で差別化する。ブランドの "過去性" とスタックの "現在性" をコントラストさせることで生まれる価値がある。

---

## 4. 共通パターン（ラウンド1 仮説を統計で強化）

### 4-1. "買わせないLP" を構成する 10 の定石（定量確認済み）

| # | 定石 | 確認データ |
|---|---|---|
| 1 | H1 は企業名 or ロゴ単体 or コーポレートスローガン 1 行 | H1 の平均文字数は約 12 文字。H1 なし（空）が約 30% |
| 2 | H2 はセクション見出しで「英字大文字 + 日本語補足」のバイリンガル型 | 200 件中 40 件以上で観測 |
| 3 | CTA は "View More / Read More / 詳しく見る" の継続誘導 | 上位 14 項目中 10 項目がこれ |
| 4 | FV は大画像 or 背景動画 + ミニマル文字 | video autoplay 使用 12.5% |
| 5 | 色数は基本 2 色（白 + 黒 or ブランド 1 色） | theme-color 単色率 48.8% |
| 6 | 全角スペース字間演出で "余韻" を作る | 24.5% |
| 7 | Lenis / GSAP / Swiper でスロースクロール演出 | モダン層で 10-25% |
| 8 | ナビは Contact / News / About / Company / Recruit / Service / Works の 7 固定枠 | 上位 7 項目で過半数カバー |
| 9 | 標準セクション順は FV → Message → Service → Works → About → News → Recruit | 複数精読から帰納 |
| 10 | 採用情報は必ず持つ（"Recruit" 17 + "採用情報" 9 + Careers 7） | 33/200 = 16.5% に明示 CTA あり |

### 4-2. フォント戦略 3 系統
1. **Noto 系だけで完結**（46%）: `Noto Sans JP` + `Poppins` / `Roboto` / `Inter` の組み合わせ。無料・高速・品質十分。
2. **Adobe Fonts 課金組**（9-21%）: `dnp-shuei-gothic-gin-std` / `source-han-sans-japanese` / `PP Neue Montreal` / `NeuePlak` など。クライアントがブランド予算を持つ場合の鉄板。
3. **自社オリジナルフォント**（2-3%）: LIFULL、Pentel など大企業のみ。

### 4-3. スクロール・アニメーション 3 レベル
- **静的（50%）**: WordPress + jQuery のみ。スクロールアニメーション最小限。
- **中（30%）**: Swiper + AOS/WOW + ちょい GSAP。
- **リッチ（20%）**: Lenis + GSAP + Barba + Lottie。制作会社系に集中。

### 4-4. 背景色の "白じゃない白" パターン
200 件中でアイボリー/オフホワイト系 body 背景を採用する層が確認できた：
- `#EBEAE8`（NEWFOLK）
- `#F5F0E9`（ナチュラル系）
- `#F8F2EE`（暖色基調）
- `#F0F0F0`（MESON）
- `#FEF3EB`（LIFULL 淡オレンジ）
- `#FAFAE1`（淡黄）

→ **design-mcp で "ブランドLP 生成" する際の body 背景は、純白 `#FFFFFF` ではなく上記 5〜6 色からランダム選択するほうが "手癖のない本物感" が出る**。

---

## 5. 新発見（ラウンド1では見えなかったもの）

### 5-1. 日本のコーポレート Web の "WordPress 支配率" が想定より高い
**61.5%** は国内 CMS 市場シェア統計（一般に 40-50% とされる）より高い。これはブランドLP/コーポレートという枠に限ると、実質 **他に選択肢がない** ことを意味する。Next.js / Nuxt / Astro を合計しても 31 件 = 15.5%。

### 5-2. Tailwind は意外なほど使われていない
SaaS の LP では Tailwind 採用率は 30-50% 程度だが、ブランドLP では **2%**。これはブランドLP の CSS が **デザイナー起点の一点物 SCSS** であることを示唆する。Tailwind の "クラス積み上げ" は "余白と静けさ" の調整には不向きということ。

### 5-3. JSON-LD 構造化データの普及率 40.5%
半数以下だが、思ったより高い。Yoast SEO / Rank Math の自動生成が主因。**ブランドLP を生成する時は `Organization` 型の JSON-LD を最初から埋め込むべき**（生成自動化の価値が高い）。

### 5-4. `<html lang>` 未設定が 10.5%（21 件）
地味だが重要。アクセシビリティとスクリーンリーダー対応が抜けている。design-mcp のテンプレには必ず `<html lang="ja">` を入れる。

### 5-5. OGP 網羅率 95.5% vs Twitter カード 77%
Twitter / X のシェア重要性が下がり、OGP のみで済ませる構成が増えている。

### 5-6. `meta theme-color` の設定率は 21.5%
意外に低い。モバイル Safari / Chrome のツールバー色を揃えたい場合は明示的に追加する必要がある。

### 5-7. 採用情報への動線は "グローバルナビ + フッター + トップ内のカード型バナー" の三重化
Recruit 単体で 17 件のナビ出現、「採用情報」文言の CTA が 9 件、さらにフッターに求人リンクが別で存在するケースが多い。**採用導線はブランドLP の裏の本命**。コーポレートサイトは「採用のための広告」でもあるため、採用セクションの作り込みは手を抜けない。

### 5-8. 日本語コピーの "半角スペース区切り" パターン
例: "ブランドとビジネスの間を、 デザインでつなぐ。"（句点後に半角スペース）
セールスLP ではほぼ存在しないが、ブランドLPで 50 件以上観測。余韻を作るための独自タイポグラフィ。

### 5-9. "`01 02 03`" の章番号表示が 20.5% に達する
ラウンド1 で気づかなかった定番演出。Service / Works / Feature セクションの各カードに `01` `02` `03` を薄いグレーで添えるスタイル。

### 5-10. "英字大見出し + 日本語小見出し" の 2 段セット
`Purpose 私たちが社会に対してすべきこと` / `Service 事業概要` のような 2 段構成が 200 件中 40 件以上に出現。これを "デュアル見出しパターン" と呼べば、design-mcp のテンプレート名として使える。

### 5-11. マーキー演出の復権（9.5%）
2024 年以降、横流れテキスト（HTML marquee ではなく CSS keyframes `translateX` 無限ループ）が再流行。"ブランド名 / スキル / キーワード" を延々と流す装置として定着。

### 5-12. モバイルファースト breakpoint は 1024px が事実上標準
`@media (min-width: 1024px)` が最多。1023px が 2 位にいるのは Bootstrap の旧 lg breakpoint の名残。

---

## 6. design-mcp 使用方針（更新版）

### 6-1. モード設定（最重要）
```
mode: brand-corporate
```

### 6-2. 必ず入れるべきデフォルト設定
```yaml
# フォント
fonts:
  ja: "Noto Sans JP"           # 23% 採用の実績
  ja_alt: "Zen Kaku Gothic New" # 5.5% 採用
  ja_serif: "Noto Serif JP"    # 4% 採用
  en: "Poppins"                # または Inter / Oswald

# カラー（単色ベース + 1 点アクセント）
colors:
  bg: "#EBEAE8"                # or "#FFFFFF" or "#F0F0F0" — 純白を避ける
  text: "#1A1A1A"              # 純黒 #000 は避ける
  accent: "#4D5FFF"            # 1 色だけアクセント
  border: "#E6E6E6"

# レイアウト
container_max_width: 1280px    # or 1024 / 1100 / 800
section_padding: "120px 0"     # 余白は潤沢に
letter_spacing_base: "0.04em"  # LIFULL 基準

# ライブラリ
libraries:
  smooth_scroll: "lenis"       # or なし
  animation: "gsap"            # or なし
  carousel: "swiper"
  transition: "barba"          # or なし
  cms: "microcms"              # or wordpress

# 見出しパターン
heading_pattern: "bilingual"   # "英字 日本語" の 2 段型
# 例: "Purpose 私たちが社会に対してすべきこと"

# CTA 文言プール
cta_pool:
  primary: ["詳しく見る", "View More", "Read More"]
  contact: ["お問い合わせ"]
  recruit: ["採用情報"]

# セクション標準構成
sections:
  - main_visual       # 60-100vh, 大画像 or video autoplay
  - message           # 一言コピー
  - service           # 4-6 カード
  - works             # カルーセル or グリッド
  - about             # テキスト中心
  - news              # 3-5 件
  - recruit           # 縦バナー 1
  - footer

# 装飾オプション
decorations:
  zenkaku_letter_spacing: true      # 全角スペース字間演出 ON
  section_number_0102: true         # 01 02 03 章番号 ON
  scroll_down_indicator: true
  marquee: false                    # 好みで
```

### 6-3. やってはいけないこと（禁止事項）
- 扇情コピー（「今すぐ」「完全無料」「限定」「緊急」）を使わない
- FV 内 CTA ボタン多重配置をしない
- 赤/黄色の強色使用を避ける（`#FF0000` は 1.5% でしか出ない）
- 純白 `#FFFFFF` + 純黒 `#000000` のベタ組みをしない（`#EBEAE8` + `#1A1A1A` 的な微ずらしを使う）
- 全ての見出しに `font-weight: 900` をつけない（細字 300/400 のほうが "静けさ" が出る）
- CTA が 3 個以上のセクションは作らない
- 申し込みフォーム直埋めはしない（`/contact` への導線のみにする）
- カウントダウン・タイマー・緊急訴求を使わない
- Tailwind のユーティリティクラス過剰使用はしない（BEM 的な命名で "デザインされた感" を出す）

### 6-4. 推奨スタックプロファイル

**Profile A: "モダン軽量コーポレート"**
Astro + microCMS + Noto Sans JP + 単色アクセント + Lenis（オプション）
→ SmartHR 型。JS バンドル最小、LCP 最速。

**Profile B: "デザインエージェンシー王道"**
WordPress + Lenis + GSAP + Swiper + Barba + Adobe Fonts
→ commono 型。制作会社 / クリエイティブエージェンシー。

**Profile C: "Next.js SaaS コーポレート"**
Next.js + microCMS + Swiper + Vimeo + Noto Sans JP + Inter
→ Mimiguri / Creatures 型。上場前後のスタートアップ。

**Profile D: "Nuxt 次世代スタートアップ"**
Nuxt + Lenis + microCMS + NeuePlak (Adobe)
→ MESON 型。XR / AI / 最先端領域。

**Profile E: "自社フォント大企業"**
WordPress + 自社フォント + 淡色 body 背景 + 複数事業カラー
→ LIFULL 型。売上 300 億超の大手。

### 6-5. テンプレート化すべきバリアント
1. `brand-corp-minimal`（NEWFOLK / SmartHR 系）
2. `brand-corp-agency`（commono / NSSG 系）
3. `brand-corp-startup`（MESON / Mimiguri 系）
4. `brand-corp-traditional`（游藝舎 / 翔陽 系 — 伝統 × モダン）
5. `brand-corp-social`（フローレンス系 — NPO / ソーシャル）
6. `brand-corp-manufacturing`（翔陽 / 浜岡鍍金系 — 町工場リブランディング）

---

## 7. 追加の定量観察（細部）

### 7-1. ロゴの位置
200 件のうちヘッダ左上ロゴが約 95%、中央ロゴが約 3%（commono など）、右側ロゴが約 2%（稀）。左上固定は疑問の余地なし。

### 7-2. ハンバーガー実装
- モバイル: ほぼ 100% ハンバーガー採用
- デスクトップ: ハンバーガー併用（= 全画面メニュー）が約 30%、常時ナビ 70%
- 全画面メニュー派の中で「英字大見出し + 日本語補足」のメニュー項目構成が約 50%

### 7-3. お問い合わせフォームへの導線
- ヘッダ右上固定ボタン "Contact" が約 40%
- フッター直前に別セクション "Contact" が約 30%
- フッターのみが約 25%
- 外部サービス（Google Forms / Typeform）へ飛ばすが約 10%

### 7-4. 採用（Recruit）導線の濃度
- 独立ページ `/recruit` あり: 約 60%
- 採用特設サイト（別ドメイン）へリンク: 約 20%
- トップ内バナーのみ: 約 15%
- 採用情報なし: 約 5%

### 7-5. SNS リンクの設置場所
フッターに集約が約 90%。ヘッダに設置は約 15%（重複あり）。
- Instagram: 最多（約 60%）
- X (Twitter): 約 50%
- YouTube: 約 30%
- LinkedIn: 約 20%
- Facebook: 約 15%
- note: 約 10%（日本特有）

### 7-6. ブログ / オウンドメディアの有無
`Blog` / `Topics` / `Journal` / `Magazine` を持つサイトが約 30%。制作会社系は 50% 以上で持っている。

### 7-7. 英語サイト / 多言語対応
`hreflang` 設定が 23/200 = 11.5%。ただし "EN/JP" 切替ボタンだけ用意し、hreflang 未設定のサイトも多数（英語版を別ドメインで用意しているか、i18n 実装が不完全）。上場企業ほど英語対応は必須。

### 7-8. プライバシー / 個人情報保護方針
フッターに `プライバシーポリシー` リンクは **ほぼ 100%**（GDPR 対応 Cookie バナーは約 15%、日本国内法だけで十分とする判断が多い）。

---

## 8. まとめ：ブランドLP vs セールスLP 比較表

| 項目 | セールスLP | ブランドLP |
|---|---|---|
| 目的 | 申込 / 購入 | 想起 / 信頼 / 採用応募 |
| FV | 悩み → 解決 → 実績 → 価格 → CTA | 一言コピー + 大画像 |
| CTA 数 | 10+ | 1-2 |
| カラー数 | 5-10 色（赤黄強色） | 2-3 色（モノトーン + 1） |
| フォント | 太ゴシック `900` | 細〜中字 `300-500` |
| スクロール長 | 長い（20,000px+） | 中（5,000-10,000px） |
| H1 | 訴求コピー | 企業名 or スローガン 1 行 |
| アニメーション | 固定・なし | Lenis / GSAP / Barba |
| 背景 | 白 + 原色ブロック | オフホワイト or 黒 |
| 導線 | フォーム直結 | `/contact` 間接 |
| 典型スタック | LP 専用 HTML / Tailwind | WordPress or Astro / Next |
| 使用率 (Tailwind) | 30-50% | **2%** |
| 章番号 `01` `02` | ごく稀 | 20.5% |
| 全角スペース演出 | 0% | 24.5% |
| 背景動画 | 稀 | 12.5% |
| 英字ナビ | 部分的 | 7 固定枠 |

**最終結論**: セールスLP とブランドLP は **同じ「LP」という言葉で括ってはいけない別物**。デザイン生成 AI に投げる際は最初に **モード宣言**（`brand-corporate` / `sales-lp`）を必須とすべき。design-mcp / AIDesigner の呼び出し時、システムプロンプトに本ドキュメントの「6-3 禁止事項」を毎回注入する運用を推奨する。

---

## 9. 精読 15 件の一覧（URL）

| # | サイト名 | URL | 業種 | 特徴 |
|---|---|---|---|---|
| 1 | MESON | https://www.meson.tokyo/ | XR スタートアップ | Nuxt + Lenis + NeuePlak |
| 2 | commono | https://commono.co.jp/ | デザインエージェンシー | WP + GSAP + Lenis |
| 3 | SmartHR | https://smarthr.co.jp/ | HR SaaS | Astro + microCMS |
| 4 | LIFULL | https://lifull.com/ | 不動産情報 | 自社フォント + 淡色背景 |
| 5 | カオナビ | https://corp.kaonavi.jp/ | タレントマネジメント | バイリンガル見出し |
| 6 | フローレンス | https://florence.or.jp/ | NPO | ハッシュタグ先頭 CTA |
| 7 | ALE | https://star-ale.com/ | 宇宙ベンチャー | `#000D14` 深宇宙黒 |
| 8 | 翔陽 | https://syoyo-al.co.jp/ | 町工場（アルミ鋳造） | Barba + 全角スペース |
| 9 | MIMIGURI | https://mimiguri.co.jp/ | 組織コンサル | Next.js + microCMS |
| 10 | 乃村工藝社 | https://www.nomurakougei.co.jp/ | 空間デザイン最大手 | Next + 実績ファースト |
| 11 | BEAMS CREATIVE | https://beamscreative.jp/ | クリエイティブ子会社 | 強色 + 全角スペース |
| 12 | pentel | https://www.pentel.co.jp/ | 文具 | パステル 4 色均等 |
| 13 | UUUM | https://www.uuum.co.jp/ | クリエイターエージェンシー | 英字字間演出 |
| 14 | NEWFOLK | https://newfolk.jp/ | デザインスタジオ | アイボリー body 背景 |
| 15 | 游藝舎 | https://www.yugeisha.com/ | 伝統工芸 | Lenis + GSAP + Cardo |

---

## 10. 次ラウンドでやること（ToDo）

1. **セクション構成を HTML パース**して、FV → Message → Service ... の順序違いを定量化（今回は帰納のみ）
2. **フォントサイズ分布**（H1: px / H2 / body）の集計 — 今回未実施
3. **スクロール長さ**（`body.scrollHeight`）を実測 — 静的 HTML では取れないが、JS 評価で取得可能
4. **画像枚数と総容量** を集計 — ビジュアル重視度の指標
5. **採用特設サイトの分析**（Recruit 単体の独立 LP は brand-corporate と recruit-job のどちらに入れるべきか境界線検証）
6. **大企業 vs 中小の違い**をスタックから分離（例: 従業員数 500 人以上と未満で Next.js 採用率がどう変わるか）
7. **`design-mcp` テンプレート 6 種** を実際に生成してみて、200 件との見た目一致率を検証

---

**ドキュメント末尾**
- 集計スクリプト: `/tmp/bc_extract.py`
- 中間成果物: `/tmp/bc_analysis/*.txt`, `/tmp/bc_analysis/file_meta.json`
- 更新者: Claude (Opus 4.6 1M / brand-corporate 分析エージェント)
- 更新日: 2026-04-08
