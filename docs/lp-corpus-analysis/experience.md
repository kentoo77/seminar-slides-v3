# Experience / Interactive LP 分析 - Round 2 (本格版)

## 0. データソース

- 対象ディレクトリ: `/Users/oidekento/lp-corpus/raw_all/experience/`
- 総ファイル数: **96 HTML**（+1 は須坂まるごとミュージアムの 1KB リダイレクトページ、+1 は bandai の子向けキャラ特設で実質サイズ 8KB、計 97 ファイル中 1 ファイル除外）
- 集計手段: Python スクリプト + ripgrep による全件 grep 統計
- 深読み対象: 15 ファイル（ジャンル別に代表を選定）
- サイズ分布（トップ抜粋）:
  - 最大: `2901_andsaunafarm.com` 1.15MB、`2863_matsurito.jp` 983KB、`2944_dive-hiroshima.com` 782KB
  - 最大画像DL系: `2951_airbnb.jp` 560KB、`2937_tapple.me` 546KB、`2962_brutus.jp` 413KB
  - 最小: `2879_hakonature.jp` 13KB、`2880_muroom.chicabi.jp` 10KB、`2883_designershygge` 13KB
  - 中央値は **60〜100KB 帯**（WordPress テーマ系が多いため）

この Round 2 は R1（30件）から対象を **96 件へ 3.2 倍拡張**し、統計ベースで "体験 LP の現場で実際に選ばれている装置" を検証する。R1 で仮説だった「WebGL/Three.js ゴリゴリ系はほぼ存在しない」を数値で裏取りする。

---

## 1. 統計サマリ（全96件 grep 集計）

### 1-1. ライブラリ / 技術スタック使用率

| 技術 | 使用ファイル数 | 比率 | コメント |
|------|------|------|------|
| **jQuery** | 47 | **49.0%** | ほぼ半数。WP テーマ同梱ケースが多数 |
| **WordPress（wp-content/wp-includes）** | 56 | **58.3%** | 体験LPの主要CMS。独自テーマ上の個別実装が基本形 |
| **Swiper** | 35 | **36.5%** | 画像/施設カード/記事カルーセルの定番 |
| **Next.js / next/static** | 16 | 16.7% | 地域メディア＋ブランド寄りで採用 |
| **Nuxt.js** | 14 | 14.6% | Studio.Design（STUDIO）系の出力が大半 |
| **GSAP**（ScrollTrigger 含む） | 6 | **6.3%** | R1 と比べ比率は下がった（18/30 → 6/96） |
| **Splide** | 9 | 9.4% | Swiper の代替として次点採用 |
| **`<video>` タグ** | 21 | **21.9%** | ヒーロー映像サイトはほぼ常にこれ |
| **`<video autoplay>`（無音ループ）** | 13 | **13.5%** | ヒーロー映像で autoplay muted loop の典型 |
| **Lottie** | 3 | 3.1% | inadani-sees / Airbnb / people-trip-guide-shibuya / yamashita-fruit |
| **lenis（慣性スクロール）** | 2 | 2.1% | `dorokyo.info` / `tomioka-silk-mill` のみ |
| **AOS / animate.css / data-aos** | 3 | 3.1% | 極少。体験LPはAOSを避ける傾向 |
| **Tailwind CSS** | 2 | 2.1% | `tapple.me` / `camplus.camp` のみ |
| **Three.js / WebGL** | **0** | **0.0%** | ★ **R1 の仮説 100% 裏取り完了** |
| **Canvas 要素（SVG以外）** | 1〜2 | <2% | chart/グラフ用途のみ、3D演出なし |
| **Google Maps iframe** | 58+ | 60%+ | アクセスセクションでの埋め込みが基本 |
| **Google Fonts CDN** | 29 | 30.2% | のこり70%は Typekit/FontPlus/独自 |
| **Adobe Fonts (typekit)** | 29 | 30.2% | Google Fonts と拮抗。和文フォントで優位 |
| **Instagram 埋め込み / リンク** | 85 | **88.5%** | 体験LPはほぼ必ず Instagram を出口にする |

### 1-2. "体験特有の検証" 結果

- **WebGL / Three.js 率: 0.0%**（96 / 96 で未使用）
  - `qino.jp` に "webgl" の文字列があったが、中身はロゴ SVG path の coincidental match で実装なし
  - R1 (30件) の 0% が、R2 (96件) でも **厳密に 0%** で再確認された
  - → **体験 LP ≠ クリエイティブコーディング**。この領域は "awwwards 系デジタルエージェンシー" の世界で、地方観光/体験施設 LP の現場には降りてきていない
- **Canvas 3D 演出率: 0%**（SVG/DOM アニメに寄り切っている）
- **GSAP/ScrollTrigger 率: 6.3%**（R1 の 60%+ からは激減）
  - R1 は先行サンプリングで "演出強め" に偏っていたため、R2 の 6.3% が **現場の実数**
  - GSAP を使うのは `dorokyo.info`、`kyoto-iju.com`、`potel.jp`、`hirakata-elcl.jp`、`portla-mag.com`、`tobichi.jp` の 6 件のみ
- **`<video autoplay>` 率: 13.5%**
  - ヒーロー動画は "欲しい場面" でしか使われず、全員が乗せているわけではない
  - 採用組はサウナ（and sauna FARM）、田舎体験（nu-kuju）、神社体験（iai-yabusame）、祭（matsurito）など "動きで伝わる被写体" を持つ案件
- **Swiper 率: 36.5%**（やや過半数未満）
  - 体験LPはカルーセルを **必須だとは思っていない**。縦スクロール＋画像敷き詰めの方が主流
- **地方観光ジャンルは "WordPress + Swiper + jQuery" が圧倒的多数派**

### 1-3. 配色の傾向（深読み15件 + 統計抽出）

WordPress の Gutenberg デフォルトパレット（`#0693e3` `#9b51e0` 等）がノイズとして多数ヒットするため、深読みで確認した **実ブランド色** ベースで整理する。

**TOP 10 カラーパレット（深読みと目視確認ベース、頻度ではなく "典型" ベース）:**

| 順位 | カラーパターン | 代表ファイル | 使われ方 |
|---|---|---|---|
| 1 | **墨黒 #000 / #0a0a0a / #131417 / #181818** | qino / brutus / popeyemag / tapple | ヒーロー背景・大字ロゴ・写真の上の文字 |
| 2 | **生成り/和紙 #fcfaf3 / #fdfcf9 / #f5efe0 / #ede5dc** | byaku / mori-no-oto / shinpaku / hinuihitohi | 本文背景。差し色 1 色で成立させる |
| 3 | **こげ茶/土 #231815 / #28271D / #3b3938 / #ab9a86** | maruoka-castle / brutus / byaku | 本文テキスト・見出し |
| 4 | **抑えた緑/苔 #67a671 / #16390a / #1f9f60** | qino / nu-kuju / matsurito `#739221` | 自然・森・農のアクセント |
| 5 | **水青 #2198d0 / #005a87 / #2874fc / #3269f5** | aoao-sapporo / nifrel / matsurito `#7CC1CC` / sailjp | 水系・海系・"空気" |
| 6 | **朱/赤 #e6373c / #cd2653 / #e63946 / #df2323** | niaulab / taa-fdn / brutus / airbnb | 特集・ロゴ・"和の赤" |
| 7 | **オレンジ系 #ff5f4a / #ffa700 / #dfbc93** | (brutus) / popeye | カルチャー寄せのPOP感 |
| 8 | **青紫/紺 #102f72 / #0015ff / #2f1a71 / #1e1040** | brutus / popeye / airbnb | ナイト感・アート系 |
| 9 | **ピンク/マゼンタ #fc5c6c / #e64c5b / #ff0044 / #ffbfe4** | tapple / popeye / airbnb | サービス系・若者向け |
| 10 | **エメラルド/ターコイズ #00c6ac / #37d8c6 / #b3dadc / #eff9f9** | brutus / tapple / airbnb | 新規サービス・海外感 |

**体験LPの配色ルール（観察）:**
1. **配色数は 2〜3 色**。メディア系（brutus, popeye）のみ特集ごとに切替えて10色以上
2. 背景は **"紙の色" を 1 枚**（真っ白 `#ffffff` より `#fcfaf3` 系が好まれる）
3. 差し色は被写体（海・森・道・職人）から採る → "フィールドの色" がブランドカラーになる
4. **真っ黒 `#000` は写真の上で使うときだけ**。広告のように派手に使わない
5. ピュアな蛍光色はメディア/都市カルチャー系（brutus, popeye, 404shibuya）に限定

### 1-4. フォント使用統計

明朝・ゴシック別の集計（ファイル内 CSS 宣言または Google Fonts URL から検出）:

| フォント族 | カテゴリ | 出現ファイル |
|---|---|---|
| **Noto Sans JP** | ゴシック（Google） | 13 |
| **Zen Kaku Gothic New** | ゴシック（Google） | 3+ |
| **Zen Maru Gothic** / **Kosugi Maru** | 丸ゴシック（Google） | 数件 |
| **Shippori Mincho / Noto Serif JP / Hina Mincho** | 明朝（Google） | 3 |
| **Klee One / Yuji Syuku / Sawarabi / Kaisei** | 装飾明朝（Google） | 0〜1 |
| **FontPlus（webfont.fontplus.jp）** | 和文 SaaS | `byaku.site`、`shinpaku.co`、`suu-haa.jp`、`dorokyo.info` 等多数 |
| **Adobe Fonts (typekit)** | 和文 SaaS | 29 件 |
| **Morisawa UD / TypeSquare** | 和文 SaaS | `inadani-sees` 等 |
| **Montserrat / Poppins / Outfit** | 欧文サンセリフ | 32 件以上 |
| **Roboto / Inter / Jost** | 欧文サンセリフ | 数件 |
| **EB Garamond / Cormorant / Playfair / Marcellus** | 欧文セリフ | 数件 |
| **Barlow / Caveat / Signika / Oswald / Sen** | 装飾欧文 | 数件 |

**重要な発見: "和文を外部 SaaS で買う" 文化**

体験LPは **FontPlus / Typekit / Morisawa TypeSquare** といった有料 Web フォントを Google Fonts と同等以上の比率で使う。
- Google Fonts 比率は **30.2%**
- Typekit/FontPlus 比率は **30.2%**（完全に拮抗）
- 広告ロゴは **カスタム実装のまま画像書き出し** が多い

理由:
- 「空気感」を出すには Shippori Mincho B1 / A1 明朝 / リュウミン / 筑紫明朝 など **Google Fonts にない和文明朝** が必要
- 地方観光はディレクター主導で "このフォントで書く" が最終決裁されるため、課金前提になる

### 1-5. セクション構成（H2 集計）

全96件から H2 を収集し、英字/和字で集計:

**英字 H2 上位（頻度順）:**
1. `News` (12)
2. `About` (9)
3. `Contact` (8)
4. `Articles` (7)
5. `Events` (6)
6. `Projects` (3)
7. `About Us` (3)
8. `Facility` (3)
9. `Products` (2)
10. `Event` / `Goods` / `Experience` / `Room` / `Regulars` / `Tag` (各 2)

**和字 H2 上位:**
1. `お知らせ` (9)
2. `宿泊` / `アクセス` / `できること` / `お問い合わせ` (3)
3. `体験` / `おまつり` / `お札・お守り` / `トピックス` / `特集` / `ニュース` (2)

**体験LPのセクション基本形 6 パーツ（観察された共通骨格）:**

```
[01] Hero（ヒーロー映像 or 一枚画像）← 全員必須
[02] About / Concept / 私たちの想い
[03] Experience / Projects / Room / Menu ← "何ができるか" を大カードで並べる
[04] News / Articles / Events ← 時系列の更新枠（WPあるいは手動）
[05] Access / Map（Google Maps iframe が 60%+）
[06] Contact / Reservation / Instagram フォロー ← "帰す場所" は予約 or Instagram
```

追加セクション（頻度順）:
- `Facility` / `Room` / `温泉16種` のようなプログラムカード群 (50%+)
- `Gallery / Photo` (Swiperカルーセル、40%+)
- `よくあるご質問 / FAQ` (30%+)
- `取扱店 / Shop list` (QINO 等の物販系のみ)
- `English / 繁体 / 한국어 / ภาษาไทย` の言語切替 (nifrel, narita-akihabara, airbnb 等の観光寄り、10%+)

### 1-6. CTA ボタン頻出ラベル（集計）

「btn/button/cta」クラスの anchor テキストを集計した上位:

| 順位 | ラベル | 件数 | 用途 |
|---|---|---|---|
| 1 | `閉じる` | 30 | モーダル用、広告ではない |
| 2 | `マップに戻る` | 10 | 地図UI |
| 3 | `もっと見る` | 8 | 記事送り |
| 4 | `View all` | 5 | 記事送り（英字） |
| 5 | `詳細を見る` / `詳しくはこちら` / `詳しく見る` | 13 | 汎用 |
| 6 | `お問い合わせ` | 4 | ゴール |
| 7 | `View More` | 4 | 汎用 |
| 8 | `施設紹介` | 3 | 導線 |
| 9 | `記事を読む` / `記事をよむ` | 6 | メディア型 |
| 10 | **`予約する` / `ご予約へ` / `ご宿泊予約`** | 7 | **体験LPの真のゴール** |
| 11 | `Google map` | 2 | アクセス |
| 12 | **`#アイヌのくらし` `#伝統的コタン` などハッシュタグ型** | 20+ | upopoy-magazine のタグナビ方式 |

**観察:**
- 体験LPの CTA は **"予約する / 詳しくはこちら" の2語でほぼ済む**
- 広告的な「今すぐ無料お試し」「限定」などの CTA は **0**
- 代わりに `閉じる` `マップに戻る` のような **UI CTA** が目立つ → モーダル/マップUIを必ず作っている

---

## 2. 深読み 15 ファイル

R1 と重複しない（R1 は `/raw/experience/html/` 30件対象）ファイルを中心に、ジャンル別に代表を選んで詳細確認。

### 2-1. `2856_qino.jp_.html` — 白山麓・木のプレミアム地域共創
- **ジャンル**: 地方創生 × 飲食 × 教育の複合ブランド（QINO SODA / QINO Restaurant / QINO School / 森の庭）
- **サイズ**: 68KB
- **スタック**: 独自実装（`cdn.qino.jp/assets/js/script.js` 単発、CSS 1ファイル）
- **特徴**:
  - R1 で仮説だった「WebGL 使ってる？」の検証対象。結果 → **使っていない**（"webgl" は SVG ロゴパスの偶然ヒット）
  - 完全オリジナルの軽量 SPA。フレームワーク非依存の手書きに近い
  - グロナビ: HOME / ABOUT / PROJECTS (QINO SODA / Restaurant / School / 森の庭) / News / Contact
  - キャッチコピー: **「木の使いみちに、驚きを。」** — 8文字で成立する和文タイポ
  - "木の使い道を創造する" の補助。"地域共創" を全面に出さず、商品から語る
- **学び**: **フレームワークを使わない判断は、重量コピーとロゴデザインでページを持たせる覚悟とセット**

### 2-2. `2894_dorokyo.info_.html` — 奈良県瀞峡ツーリズム
- **ジャンル**: 観光ツーリズム（秘境体験）
- **サイズ**: 55KB
- **スタック**: **Nuxt 3 + GSAP + ScrollTrigger + Lenis**（全96件で唯一の "フルスタック演出" コンボ）
- **特徴**:
  - Lenis の慣性スクロールを使った 96 件中の **2件のうちの 1 件**
  - CDN 経由で `lenis@1.1.18` + `gsap@3.12.5` + `ScrollTrigger` をロード
  - フォントは FontPlus (`fonts.fontplus.dev/v1/css/r8xDY8Kw`)
  - キャッチ: `瀞峡を中心とする観光ツーリズム "瀞 toro"`
  - 一語ブランドの造語 "瀞 toro"（音読み・訓読みを併記）
- **学び**: **lenis + GSAP の "なめらか演出" は、どこにでも効くが、そこまでやる案件は全体の 2% しかない**。逆に言うとやれば差別化になる

### 2-3. `2909_iai-yabusame.com_.html` — 居合・抜刀 体験（戸山流備前会）
- **ジャンル**: 神社/寺社/剣術体験
- **サイズ**: 122KB
- **スタック**: WordPress + Swiper + jQuery 2.2.2（レガシー）+ lazysizes + headroom + micromodal + `<video>`
- **特徴**:
  - ヒーローは **日本刀を抜く動画** を autoplay muted loop
  - セクション: Know（戸山流備前会を知る）/ Samurai Experience（個人/団体/法人向け）/ For Foreign Visitor
  - CTA: **「居合の予約をする」「予約する」** の一貫化
  - 英字セクション名に **和字サブタイトル** を必ず併置 → "Know / 戸山流備前会を知る"
- **学び**: **英字大文字 H2 + 和字説明** は、体験 LP の"品格"を出す最もローコストな装置

### 2-4. `2906_byaku.site_.html` — BYAKU Narai（奈良井宿の宿）
- **ジャンル**: 旅館/ホテル/宿 × 地方文化体験
- **サイズ**: 61KB
- **スタック**: jQuery 3.6.0 + slick-carousel 1.8.1 + easing + FontPlus + 独自 progressbar.min.js
- **特徴**:
  - **EB Garamond**（唯一の Google Font）+ FontPlus の和文 → 「和洋折衷の高級宿」テンプレ
  - セクション: ご宿泊 / お食事（kura / TASTING BAR suginomori）/ 温浴施設（SAN-SEN）/ ギャラリー（hoihoi）/ 提携施設（suginomori brewery）
  - **各施設に固有名詞**（kura, SAN-SEN, hoihoi, suginomori brewery）を付与 → ただの部屋ではなく "物語" にする
  - お知らせが日付＋カテゴリ入り: `2026.02.20 / 季節のおすすめ` `2026.02.19 / 施設からのご案内`
- **学び**: **高級宿系は施設に人格（固有名詞）を付与する**。BYAKU の場合は "百の物語" というコンセプトを先に立てて、中の部屋・Bar・ギャラリーにそれぞれ名付けていく

### 2-5. `2985_mukawaryu.com_.html` — むかわ恐竜ワールド
- **ジャンル**: 恐竜テーマパーク/地域観光ハブ
- **サイズ**: 120KB
- **スタック**: 独自 vendor.bundle.js + common.bundle.js + `<video>`
- **特徴**:
  - フレームワーク非依存の自社 Webpack 束 → 独特
  - **MOVIE / MORE** のリピートが多く、カードグリッドごとに動画を配置
  - 「化石発掘体験ツアー」「穂別キャンプ場」など複数サブコンテンツを横並び
- **学び**: 自治体系の "複数事業ハブ型 LP" は **カードグリッド + MOVIE プレビュー** が基本テンプレ

### 2-6. `2863_matsurito.jp_.html` — まつりと（日本のまつり探検）
- **ジャンル**: フェス/イベント/地域文化アーカイブ
- **サイズ**: **983KB**（2番目の巨大ファイル）
- **スタック**: **Astro + Swiper + 独自 hoisted.*.js** + `<video>`（autoplay loop）
- **特徴**:
  - 21 の CSS ファイル（Astro の自動分割）
  - ナビカラー: 緑 `#739221` + 青 `#7CC1CC` の 2 色運用
  - タグシステム:「わら・俵」「異文化」「つくりもの」「参加型」「市町村指定重要無形文化財」「ユネスコ」「山車・曳山」「鬼・天狗」「来訪神」「子ども」「演じる」「かけ声」「異界とつながる」「大迫力」「はなやか」「おごそか」「にぎやか」
  - **形容詞タグが豊富**（大迫力/はなやか/おごそか/にぎやか）→ 感情で探す設計
- **学び**: **"タグで絞り込める" 設計は、文化系アーカイブLPの強さの源泉**。カテゴリではなく感情・属性ベース

### 2-7. `2901_andsaunafarm.com_.html` — &sauna FARM
- **ジャンル**: サウナ × 地域共創プラットフォーム
- **サイズ**: **1.15MB**（最大ファイル）
- **スタック**: WordPress + Swiper + `<video>` + Google Fonts（**Sen + Noto Sans JP**）
- **特徴**:
  - 「**サウナで、日本を温かく。**」のキャッチフレーズで地域事業化
  - ナビ: プロジェクト一覧 / サウナリスト / パートナー募集 / 会員登録
  - `now loading` のプリローダー
  - タグ: music / fashion / people / travel / local / food / culture — サウナ単独ではなく **ライフスタイル総合** で見せる
- **学び**: **専門領域（サウナ）× 他ライフスタイル（音楽/ファッション/食）のタグ併置** で "読めるメディア化" する戦略

### 2-8. `2942_popeyemagazine.jp_.html` — POPEYE Web
- **ジャンル**: 雑誌/カルチャーメディア
- **サイズ**: 173KB
- **スタック**: WordPress + Next.js + Swiper
- **特徴**:
  - CSS 変数: `#0015ff` `#ff0044` `#ffc6c6` `#dd3333` `#eded00` `#154525` `#dfbc93` — **特集ごとに色を切り替える**
  - 記事見出しに **絵文字** を混ぜる（🎞️ 🥽 🌸）
  - サブタイトルに「文・メイ・カーショウ (BC,NR)」のように筆者クレジットを先出し
  - カテゴリ: POPEYE / ポッドキャスト / カルチャー / エフェメラを探して
- **学び**: **雑誌型メディアは、カラーパレットを記事ごとに切り替え、"特集ごとに別の世界" を作る**

### 2-9. `2995_mado.cinra.net_.html` — MADO（渋谷ヒカリエ8Fカルチャースペース）
- **ジャンル**: アート/カルチャーハブ
- **サイズ**: 44KB
- **スタック**: WordPress + 独自 SVG Morpheus + SVG アニメ + slick + main.js
- **特徴**:
  - **SVG Morpheus で形状変化アニメ** を実装（独自）
  - `LOADING...` → EVENTS / NEWS / ARTICLES / CONTACT / ABOUT の 5 ナビ
  - イベント列挙: EXHIBITION / SCREENING / TALK / SHOP + 日付範囲
  - 各セクションで EVENTS を連呼する → **"開催中イベントのタイル壁"** 的見せ方
- **学び**: **カルチャースペース系は "今やってる" を大量表示することで "来る理由" を常時提供する**。定期更新型

### 2-10. `2968_suu-haa.jp_.html` — SuuHaa 長野移住メディア
- **ジャンル**: 移住/地方創生/関係人口
- **サイズ**: 59KB
- **スタック**: WordPress + Signika (Google Fonts) + FontPlus + wordpress-popular-posts プラグイン
- **特徴**:
  - **「長野の空気を深く吸い込もう」** の呼吸メタファー → サービス名が "スーハー"
  - カテゴリ: 暮らす / 働く / つながる の 3 本柱
  - エリア別: 北信 / 中信 / 東信 / 南信
  - 長野県庁・信濃毎日新聞社・Huuu の共同運営明記 → **地域メディアの信頼設計**
- **学び**: **移住メディアは "エリア別 × 切り口別" のマトリクスナビ**。運営団体の実名を出すことで自治体系バイアスを回避

### 2-11. `3012_www.nifrel.jp_.html` — ニフレル（大阪・生きているミュージアム）
- **ジャンル**: 水族館/動物/生体展示
- **サイズ**: 58KB
- **スタック**: Swiper + jQuery 3.2.1 + velocity.min.js + **Google Fonts: Barlow + Caveat + Zen Kaku Gothic New**
- **特徴**:
  - 4言語対応: 简体中文 / 繁体中文 / 한국어 / ภาษาไทย + Google Translate リンク
  - ナビ: ご利用情報 / 営業時間 / チケット（入館券/Webチケット/年間パスポート/セット券/団体）/ 交通アクセス / 館内サービス / バリアフリー / FAQ / お問い合わせ
  - **Produce by KAIYUKAN** で運営母体を明記
  - **Caveat（手書き風英字）** を効かせに使う → 堅い施設情報 LP に人間味を出す
- **学び**: **施設型 LP は "チケット種別" を最上位に出す必要がある**。Web チケット / 年間パス / 団体 / セット券 の粒度で設計する

### 2-12. `2874_shinpaku.co_.html` — 心拍（奈良の米農家滞在）
- **ジャンル**: 農家滞在型宿泊
- **サイズ**: 180KB
- **スタック**: WordPress (shinpaku2025 テーマ) + FontPlus + Splide
- **特徴**:
  - **1日1組、1泊2食付完全予約制** の究極絞り込み
  - 「山田錦特A地区、奈良時代から千三百年続く米農家集落」の文化訴求
  - ナビ: Home / About / Story / News / Access / Faq / Contact + Instagram / LINE
  - セクション英字統一（Stay / Reservation / Online Shop すべて英字）
  - コピー: **「つくることも、いただくことも分かち合う」「つくること」**
- **学び**: **1日1組系の宿は、機能訴求より "共に" の動詞で語る**。つくる、いただく、分かち合う

### 2-13. `2987_snow-cat.jp_.html` — スノーキャットツアー（菅平高原）
- **ジャンル**: 冬期限定/野外体験
- **サイズ**: 39KB
- **スタック**: jQuery 3.2.1 + jquery-migrate + normalize + modernizr + `<video>` + lazysizes
- **特徴**:
  - 典型的な「期間限定アクティビティLP」
  - セクション: TOUR（ツアー内容）/ WHAT'S SNOWCAT（スノーキャットとは）
  - H1: `冬の絶景を体験しよう！観光タクシーで行くスノーキャットツアー！長野県上田市の標高2,000m以上の冬の美しい世界へ` ← **これが体験LPで最長クラスのH1**
  - LINE / Line it 共有ボタン → LINE 層を取りに行く
- **学び**: **アクティビティ単発LPは、SEO H1 でロケーション・標高・期間・体験名を全部詰める**。体験LP全体では珍しい SEO ベタ書き型

### 2-14. `2964_kinarito.net_.html` — きなりと（下北山村）
- **ジャンル**: 移住/関係人口
- **サイズ**: 173KB
- **スタック**: WordPress + Next.js + Swiper + `<video>` + theme-color: `#00a0e9`
- **特徴**:
  - 「下北山村の暮らしと関わりを届ける」 ← **"移住" と言わず "関わり" と言い換える**
  - 奈良県最南端、人口約800人の小さな山村
  - ニュース / 下北山村の四季 の 2 本柱ナビ
  - **関係人口を取りにいく文脈**（いきなり移住を迫らない）
- **学び**: **"移住" ではなく "関わり" "暮らし" と言い換えるコピー戦略**は、地方創生LPの2024-2026年トレンド

### 2-15. `2899_upopoy-magazine.jp_.html` — ウポポイマガジン（アイヌ文化）
- **ジャンル**: 文化アーカイブ/地域文化メディア
- **サイズ**: 67KB
- **スタック**: Swiper + Google Fonts（**Kiwi Maru + Montserrat**）+ 独自 app.js
- **特徴**:
  - ハッシュタグ CTA: `#アイヌのくらし` `#伝統的コタン` `#体験学習館` `#アイヌ伝統料理` `#アイヌ伝統楽器` `#アイヌ伝統工芸` `#工房` `#アイヌ古式舞踊` `#トゥレッポん` `#国立アイヌ民族博物館`
  - Kiwi Maru の丸ゴシック → 親しみやすさ
  - 北海道白老町・民族共生象徴空間の明記
- **学び**: **文化アーカイブ系は "ハッシュタグでアプローチを複数用意"**。カテゴリーではなくハッシュタグの方が "文化的複層性" を表現できる

---

## 3. サブジャンル分布（96件内訳）

自動分類（title + description ベース）+ 手動補正:

| # | サブジャンル | 件数 | 比率 | 代表ファイル |
|---|---|---|---|---|
| 1 | **旅館 / ホテル / 宿 / ゲストハウス** | 15 | 15.6% | transit, byaku, potel, airbnb, nipponia-kosuge, hinuihitohi, tomatoto |
| 2 | **移住 / 地方創生 / 関係人口** | 10 | 10.4% | matsurito, kyoto-iju, kinarito, suu-haa, saito-hajimeru, hitoyoshikuma-workcation |
| 3 | **観光メディア / マガジン / 地域WEB媒体** | 8 | 8.3% | popeye, brutus, cinra/mado, herenow, sendai-inc, motokurashi, upopoy-magazine, meandyou |
| 4 | **野外 / アウトドア / キャンプ / 登山** | 8 | 8.3% | logos, YAMAP, earthboat, darksky-tour, hakonature, kids-ns (north face), okuyoro, camplus |
| 5 | **サウナ / 温泉 / スパ** | 7 | 7.3% | andsaunafarm, sauna-ikitai, snowpeak fieldsuite spa, unzen, siobara, sloth, kochisusaki |
| 6 | **飲食 / カフェ / グルメ / 酒** | 7 | 7.3% | nu-kuju, kobeurbanfarming, shinpaku, fukanuma-uminohiroba, socialcoffeehouse, nicoe, shimofuri-ginza |
| 7 | **神社 / 寺社 / 剣術 / 祭事** | 5 | 5.2% | dazaifutenmangu, iai-yabusame, zenandbed, dive-hiroshima, tadanoyamajanai（御岳山） |
| 8 | **探究学習 / スクール / 図書館** | 4 | 4.2% | 8books, qino school, homeworkvillage, hirakata-elcl |
| 9 | **水族館 / 動物 / 恐竜 / 遊園地** | 4 | 4.2% | nifrel, mukawaryu, seibu-leisure, (litpla 次世代テーマパーク) |
| 10 | **アート / カルチャーハブ / ギャラリー** | 4 | 4.2% | artscouncil-kanazawa, taa-fdn (ANB Tokyo), designershygge, mado |
| 11 | **ワークスペース / コワーキング / 複合施設** | 3 | 3.1% | the-campus, sloth, codateru |
| 12 | **伝統工芸 / 工場見学 / 体験施設** | 3 | 3.1% | tomioka-silk / tomioka-silk-mill / casastella / nakagawa-masashichi |
| 13 | **フェス / 音楽 / eスポーツ / コスプレ** | 2 | 2.1% | fennel-esports, (cosmeet) |
| 14 | **観光ポータル / DMO / 道の駅** | 6 | 6.3% | unzen, gooone, siobara, tomatoto, dive-hiroshima, michinoeki-*（R1で詳細） |
| 15 | **その他 / 複合 / 単体プロジェクト** | 10 | 10.4% | tapple, niaulab (ZOZO), sailjp, tobichi, muroom, talkme, sauna-ikitai, etc |

**サブジャンル観察:**

1. **圧倒的な宿泊偏重**：旅館/ホテル/宿/ゲストハウス + サウナ + 野外キャンプ を合計すると **30 件 (31%)** で 1/3 を占める
2. **メディア型 LP の多さ**：観光メディア + 地域 WEB 媒体 + アーカイブ系で **12 件 (12.5%)** → "売る LP" ではなく "読ませる LP" が極めて多い
3. **水族館/動物園は意外と少ない**：4 件のみ。R1 で見た aoao-sapporo や kobesuma-seaworld と合わせても全体の 5% 未満
4. **神社/寺社系体験は 5 件のみ**：想像より少なかった。体験LP市場全体では "自然体験" の方が主流

---

## 4. 共通パターン 8 選

### 4-1. パターン A: **"英字セクション名 + 和字サブタイトル" の2行構造**

```
About
 私たちについて
```

**出現率: 推定 70%+**

iai-yabusame の `Know / 戸山流備前会を知る` `Samurai Experience / 居合・弓術・剣術を体験する` 等、ほぼ全ジャンルで見られる。

### 4-2. パターン B: **"新聞型 / 雑誌型" のお知らせ表記**

```
2026.02.20 / 季節のおすすめ  嵓 × suginomori brewery 6種日本酒ペアリングのご案内
2026.02.19 / 施設からのご案内  奈良井宿表通りの一部交通規制のお知らせ
```

日付 / カテゴリ / タイトル の **スラッシュ区切り 3 カラム**が体験LPの標準形。広告LPが使う箱組タイトルは体験LPにはほぼ存在しない。

### 4-3. パターン C: **Google Maps iframe によるアクセスセクション**

60%+ のファイルに含まれる（grep の iframe ヒット 82件中多数がマップ）。
典型パターン:
```
Access
│ Google Maps iframe
│ 住所
│ 電車: ○○駅 徒歩○分
│ 車: ○○IC から○km
│ 駐車場: あり（○台 / 無料）
```

### 4-4. パターン D: **"SNS Pivot" - 出口を Instagram にする**

Instagram 埋め込み or フォローボタンが **88.5%** で出現。
`Contact` ≠ `お問い合わせフォーム` であり、実質的に **Instagram フォロー → DM** がメインゴール。
ファイルによってはお問い合わせフォームが無く、LINE / Instagram のみの2択。

### 4-5. パターン E: **"プログラムカード" グリッド**

施設・ルーム・ツアーの単位でカードを並べる。典型は 3 列 × 複数段のグリッド。
- 体験LPは **「What's Here（ここで何ができる）」セクションを必ず持つ**
- カードには施設固有名詞、写真 1 枚、短い説明、`詳細を見る` ボタン
- 例: BYAKU の `kura / TASTING BAR suginomori / SAN-SEN / hoihoi` / `&sauna` の `プロジェクト一覧` / iai-yabusame の `個人 / 団体 / 法人`

### 4-6. パターン F: **"`now loading` プリローダー"**

ヒーロー画像が重いことが多いため、`now loading` or `LOADING...` のテキストプリローダーが頻出。
- `andsaunafarm.com` → `now loading`
- `mado.cinra.net` → `LOADING...`
- R1 で見た城系サイトも採用
- 技術的には `document.readyState === 'complete'` or `window.load` フックで消去するシンプル実装

### 4-7. パターン G: **モーダル閉じるボタン**

CTA ラベル 1 位が `閉じる`（30件）、2 位が `マップに戻る`（10件）という集計結果 → 体験LPは **モーダル / ライトボックスを積極的に使う**。

- 画像拡大モーダル
- プログラム詳細モーダル
- アクセスマップモーダル
- `micromodal.min.js` 等の軽量ライブラリが定番

### 4-8. パターン H: **"造語コンセプト命名"**

体験LPの固有名詞化戦略:
- `QINO`（キノ、木の意味 + 名詞化）
- `瀞 toro`（既存地名を音読みブランド化）
- `&sauna FARM`（記号 & を使う）
- `SuuHaa（スーハー）`（呼吸音の擬音語）
- `きなりと`（"生成り" + "と" の地域詞）
- `ひとよしくまワーケーション`（地名＋外来語）
- `ei-to`（エイト、数字との掛詞）
- `BYAKU Narai`（和字 + 英字 + 地名）

**造語ルール:**
1. 2〜5 音節の短さ
2. カタカナ・ひらがな・英字の混合
3. 「音の響き」優先で意味は後付け
4. ドメインと一致するブランド名

---

## 5. 新発見 (Round 1 との差分)

### 5-1. **GSAP/ScrollTrigger の使用率は 60% ではなく 6%**

R1（30件）ではサンプリング偏りで GSAP を使ったサイトが過大評価されていた。R2（96件）での実数は **6/96 = 6.3%**。
R1 でフィーチャーした `inadani-sees` `404shibuya` `kouba-fes` 等はむしろ少数派で、体験LPの大多数は **WP + jQuery + Swiper の "枯れたスタック"**。

### 5-2. **WebGL / Three.js は 0% で確定**

R1 で「仮説」だった "Web デザイナーアワード系フル WebGL サイトは体験 LP にはない" が、96件で **厳密に 0%** と確認された。
体験 LP = 現場の人が運用するコンテンツ系サイト であり、クリエイティブコーディング案件は棲み分けが別。

### 5-3. **Adobe Fonts / FontPlus の存在感が Google Fonts と拮抗**

R1 では Google Fonts 使用率が目立って見えたが、R2 では **Typekit 29件 = Google Fonts 29件 = 拮抗**。
特に和文明朝（Shippori / A1 / リュウミン / 筑紫）を使いたい案件は **ほぼ必ず有料 Web フォント**。
→ **design-mcp で和文を扱うなら、FontPlus と Typekit の選択肢を提示すべき**。

### 5-4. **Lenis（慣性スクロール）はたった 2 件**

慣性スクロールライブラリが話題だが、96件中 2 件（dorokyo.info / tomioka-silk-mill）。
体験LPでは **既存の native scroll を尊重** する設計が主流で、慣性スクロール = "やりすぎ演出" と見なされる空気がある。

### 5-5. **"関係人口メディア" というジャンルの確立**

R1 では「移住」カテゴリだったものが、R2 では **"移住と言わず 関わり と言う" メディア群** が独立したパターンとして浮上。
- `kinarito.net`（下北山村の暮らしと関わり）
- `suu-haa.jp`（長野の空気を吸い込む）
- `kyoto-iju.com`
- `saito-hajimeru.com`（西都はじめるPROJECT）

**コピー戦略の共通点:**
- `移住` → `はじめる` `くらす` `かかわる`
- `定住` → `通う` `二拠点`
- `地方` → 地名を大きく出す
- `人口減少` → 言わない

### 5-6. **"タグナビ" が体験LPの新しい標準**

upopoy-magazine の `#アイヌのくらし` 等、matsurito の `#わら・俵 #異文化 #鬼・天狗`、and sauna FARM の `music / fashion / people / travel / local / food / culture` のように、**ハッシュタグ/キーワードタグ** でコンテンツを横断するナビが多発している。
従来のグロナビ（About / News / Contact）と**併置**されている点が特徴。

### 5-7. **体験LP特有の "形容詞タグ"**

matsurito の発見: `大迫力 / はなやか / おごそか / にぎやか` という **感情形容詞タグ** 。
- 通常のジャンルタグ（神事、祭、伝統芸能）とは別のレイヤー
- 「どういう気分の時に行きたいか」で絞り込ませる
- **これは他ジャンル LP にほぼ存在しない体験LP 特有の UX**

### 5-8. **"運営母体の実名明記" が信頼設計の要**

- `SuuHaa`: 長野県庁 × 信濃毎日新聞社 × Huuu
- `nifrel`: Produce by KAIYUKAN
- `matsurito`: プロジェクト発起団体明記
- `kinarito`: 下北山村役場

体験LPの信頼は「ブランドの背後に実在の自治体/新聞社/大手企業がいる」ことで成立。SaaS LP が VC ロゴを並べるのと同じ構造。

### 5-9. **Next.js / Nuxt 採用の二極化**

- **Next.js 採用組**（16件、17%）: brutus, popeye, niaulab, meandyou（中規模ブランド系 or CMS刷新済みメディア）
- **Nuxt.js 採用組**（14件、15%）: dorokyo, unzen, hakonature, muroom, talkme, darksky-tour, senrogai（**Studio.Design = STUDIO による NoCode 出力が大半**）

→ **Nuxt 14件のうち半数以上が STUDIO 製のノーコード出力**。自社でフルカスタム Nuxt は少数。

### 5-10. **物販 LP 的装飾は体験LPに持ち込まれない**

- `新規お申し込み` `今だけ無料` `キャンペーン中` のような**広告CTA**は 0 件
- 価格表示も **予約ページに遷移するまで出ない** ケースが多数
- "売る" より "読ませる → 来させる" の設計

---

## 6. design-mcp 使用方針（体験ジャンル向け）

### 6-1. デフォルトプリセット推奨

design-mcp で体験LP を生成するときの初期値:

```yaml
category: experience
framework: WordPress_or_Astro  # React/Next.js は上級オプション
scroll: native  # lenis 等の慣性スクロールは避ける
animation: minimal  # GSAP は hero の視差 + intersection observer のみ
carousel: swiper  # splide は代替
hero:
  style: [video_autoplay_muted_loop, single_photo_with_catch]
  catch_length: 6-14_chars_jp
sections:
  - hero
  - about_concept
  - experience_cards_grid  # "What's Here" 型プログラム列挙
  - news_articles  # 日付/カテゴリ/タイトルの新聞型
  - gallery_swiper
  - access_with_gmaps_iframe
  - faq  # optional
  - contact_or_instagram
typography:
  ja_primary: [Shippori_Mincho, Noto_Serif_JP, Zen_Kaku_Gothic_New, FontPlus]
  en_accent: [EB_Garamond, Marcellus, Cormorant, Outfit, Montserrat]
  h2_pattern: EN_caps_line1_JP_subtitle_line2
palette:
  background: [#fcfaf3, #fdfcf9, #f5efe0, #ede5dc, #ffffff]
  text: [#231815, #28271D, #3b3938, #0a0a0a]
  accent_natural_forest: [#67a671, #16390a, #1f9f60]
  accent_water_sea: [#005a87, #2198d0, #2874fc]
  accent_traditional_red: [#e6373c, #cd2653]
cta:
  primary_label: [予約する, ご予約へ, 詳しくはこちら]
  avoid: [今すぐ無料, キャンペーン中, 限定特価]  # 広告CTAは体験LPで使わない
instagram_required: true  # 88.5% は Instagram を出口にしている
tag_navigation: optional  # upopoy/matsurito 風 ハッシュタグ
```

### 6-2. 避けるべきもの

以下は体験LPでは **"やりすぎ" または"ミスマッチ"** として design-mcp では避ける:

1. **Three.js / WebGL**（96件で 0%）
2. **広告LPの CTA 文言**（「今なら初月無料」等）
3. **カウントダウンタイマー**
4. **ポップアップ Exit Intent**
5. **慣性スクロール（lenis）をデフォルト化**（やるなら意図的に明示）
6. **動画背景のフルスクリーン自動音付き再生**（体験LPは muted が鉄則）
7. **Gutenberg デフォルトのビビッドカラー** （`#7a00df` `#00d084` 等）
8. **動的価格比較表**
9. **カルーセルを 5 段以上重ねる**
10. **ヒーローに白抜き大文字英字だけ**（体験LPは和字のキャッチが必須）

### 6-3. ジャンル別 design-mcp プリセット

design-mcp で "experience" カテゴリを選んだあと、サブジャンルで分岐:

**A. 旅館/ホテル/宿プリセット**
- 参考: `byaku.site` `shinpaku.co` `nipponia-kosuge.jp`
- キー: 施設固有名詞、英字＋和字併記、予約CTA、プログラムカード、EB Garamond + Shippori Mincho、生成り背景、1泊2食完全予約制 等の"絞り込み訴求"

**B. 地域メディア/関係人口プリセット**
- 参考: `suu-haa.jp` `kinarito.net` `popeyemagazine.jp`
- キー: エリア別 × 切り口別マトリクス、運営母体の実名、記事リスト日付型、カテゴリ形容詞タグ、特集ごとの配色切替

**C. 施設型体験（水族館/遊園地/ミュージアム）プリセット**
- 参考: `nifrel.jp` `mukawaryu.com` `litpla.com`
- キー: 多言語切替（4言語+）、チケット種別（Webチケット/年間パス/団体/セット券）、営業時間、FAQ、アクセス詳細、Barlow/Zen Kaku Gothic New、ポップな色 1 点差し

**D. 地方創生/複合プロジェクトプリセット**
- 参考: `qino.jp` `matsurito.jp` `andsaunafarm.com`
- キー: 造語コンセプト、SUB プロジェクト並列（QINO SODA / Restaurant / School / 森の庭）、タグナビ、ライフスタイルタグ（music / food / travel）、運営母体

**E. アクティビティ単発（スノーキャット/ダイビング/サウナツアー）プリセット**
- 参考: `snow-cat.jp` `dorokyo.info` `iai-yabusame.com`
- キー: SEO ベタ書き H1（ロケーション＋標高＋期間）、`<video autoplay muted>` ヒーロー、期間限定バッジ、LINE/Instagram 誘導、個人/団体/法人の 3 段階料金、予約フォーム直結

**F. 神社/寺社/文化体験プリセット**
- 参考: `dazaifutenmangu.or.jp` `iai-yabusame.com` `zenandbed.com`
- キー: 日本刀/座禅/祭祀の被写体、和紙背景、墨黒本文、Shippori Mincho B1 級の骨太明朝、英字キャプションは Marcellus、お札/お守り/ご祈願のナビ、授与品カタログ

**G. メディアハブ/アーカイブプリセット**
- 参考: `mado.cinra.net` `meandyou.net` `upopoy-magazine.jp`
- キー: EVENTS / ARTICLES / NEWS の 3 ナビ、タイル壁大量更新、ハッシュタグ絞り込み、EXHIBITION/SCREENING/TALK のジャンルバッジ、常時更新インジケータ

### 6-4. design-mcp 実装時の優先プロンプト例

```
generate_design with:
  category: experience
  subgenre: ryokan_hotel
  style: japanese_hygge  # 生成り + こげ茶 + 森の緑
  hero: video_muted_loop with hero_catch_jp 6-10 chars
  must_include:
    - program_cards_grid (3-5 cards with facility proper nouns)
    - news_feed (date/category/title newspaper style)
    - access_section (gmaps_iframe + address + train/car + parking)
    - instagram_follow_cta
  must_avoid:
    - webgl_threejs
    - countdown_timer
    - exit_intent_popup
    - discount_cta_labels
  typography:
    ja: Shippori_Mincho_B1
    en: EB_Garamond
    pattern: en_h2_caps + jp_subtitle
  palette: natural_paper_earth
```

### 6-5. 体験LP生成の禁則事項チェックリスト

design-mcp 生成後に自動検査すべき項目:

- [ ] Three.js / WebGL を参照していないか
- [ ] lenis を参照していないか（意図して true なら OK）
- [ ] 広告 CTA 文言（`無料` `限定` `キャンペーン`）が入っていないか
- [ ] 価格が 1 screen 目に出ていないか（体験LPは予約導線の奥に置く）
- [ ] ヒーローに和字キャッチ が入っているか
- [ ] Google Maps iframe のアクセスセクションがあるか
- [ ] Instagram リンクがあるか（88.5% で存在する標準装備）
- [ ] 日付/カテゴリ/タイトルの新聞型ニュースセクションがあるか
- [ ] H2 が英字大文字 + 和字サブタイトルの 2 行構造になっているか
- [ ] プログラムカードに **固有名詞** が付与されているか（"客室A" ではなく "kura"）

---

## 7. まとめ — 体験LPの本質

R2 (96件) の深読み + 統計検証で浮かび上がった、体験 LP ジャンルの本質:

1. **体験 LP は "読ませる LP" ではなく "歩かせる LP"**、ただし "歩かせる" は Three.js ではなく **縦スクロール + 画像力 + 短いコピー** で実現されている
2. **"枯れたスタック" で戦っている**：WordPress + jQuery + Swiper が半数以上。技術トレンドは降りてこない
3. **FontPlus / Typekit の存在感が和文体験 LP の品質を支えている**：Google Fonts 単独では出せない空気がある
4. **Instagram が最終 CTA**：お問い合わせフォームより先に Instagram フォロー
5. **造語コンセプト + 固有名詞の施設命名** が体験 LP の差別化装置
6. **"移住" とは言わず "関わり" と言う** 関係人口コピー戦略が確立しつつある
7. **ハッシュタグナビ + 形容詞タグ（大迫力/おごそか/にぎやか）** が新しい体験 LP の UX
8. **"自由な生き方" × 地方文化** のコンセプトが 2024-2026 年の最大トレンド

design-mcp 実装方針としては、**"Three.js 演出やら慣性スクロールやらの派手装置を用意しつつ、デフォルトは抑える"** のが現場適合性が高い。
体験LPはむしろ **"何を入れないか"** の判断の方が重要なジャンル。

---

**データソース**: `/Users/oidekento/lp-corpus/raw_all/experience/` 96 HTML
**分析方法**: Python/ripgrep 集計 + 15 ファイル深読み
**Round**: R2 (本格版)
**前版との差分**: R1 (30件, `/raw/experience/html/`) → R2 (96件, `/raw_all/experience/`) で 3.2 倍データ拡張、サブジャンル分布/ライブラリ率/フォント戦略の数値裏取り完了
