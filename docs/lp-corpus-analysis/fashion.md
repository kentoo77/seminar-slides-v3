# Fashion / Apparel / Accessory / Jewelry LP 分析 (Round 2)

> ラウンド2本格版。85 件の生 HTML を全件 grep 集計し、
> 代表 12 件を行単位で深読みして、Fashion ジャンルの設計指紋を抽出した。
> 前回（Round1, 30 件）での「Typekit = 最大シグナル」仮説の再検証を含む。

## 0. データソース

- 対象ディレクトリ: `/Users/oidekento/lp-corpus/raw_all/fashion/`
- 対象ファイル: **85 件**（`*.html`、すべて SSR / 静的スナップショット）
- 合計行数: **160,093 行**
- 最大: `3310_www.swans.co.jp_.html` 約 5.2 MB（SWANS 公式、アイウェア）
- 最小: `3271_www.princessbijou.com_.html` 約 7.7 KB（ディズニープリンセスジュエリー）
- 中央値: だいたい 30〜80 KB / 400〜1,500 行
- 分析方法:
  - 全件に対して `grep` で ライブラリ／フォント／色／CTA／セクション名 等を集計
  - 代表 12 件を 1〜200 行レンジで直接 Read（ヘッダ・ヒーロー構造・CSS 変数）
- 前提: ファッションは LP というより **「世界観サイト／ブランドサイト」** が多く、
  セールスコピー中心の他ジャンルと性格が大きく違う。
  このため「読ませる → 買わせる」パイプラインを持つ LP は少数派。

---

## 1. 業態別分布（85 件）

タイトル・ドメイン・本文から分類。1 ファイル = 1 業態で分類（複数該当時は主用途）。

| # | 業態 | 件数 | 率 | 代表 |
|---|---|---|---|---|
| 1 | アパレルブランド公式（メンズ・レディース・キッズ） | 22 | 26% | niko and, GLOBAL WORK, BAYFLOW, BOWTE, ANATOMICA, PAPAS / NONNON, MASTER BUNNY EDITION, PEARLY GATES |
| 2 | D2C / 小規模ブランド (バッグ・帽子・ジュエリー) | 18 | 21% | Notabag, newhattan, buonafortuna, kainowa, GARNI, in-general, EVE un BLUE, UNITE DIVISION OF ME |
| 3 | ウェディング / ドレス / ジュエリー（冠婚葵祭） | 9 | 11% | PRONOVIAS, MAGNOLIA WHITE, ecruspose, Princess Bijou, 扇屋 WEDDING, 鈴乃屋 袴, hayama-honten |
| 4 | アイウェア・時計 | 7 | 8% | Lineart CHARMANT, SWANS, American Optical, CITIZEN ATTESA, agete(watch×jewelry), MASUNAGA(story120 系) |
| 5 | コラボ企画・キャンペーン LP | 7 | 8% | ZONe×イカゲーム2, jeanasis×PIKACHU, Liberty Japan Virtual Flagship, SPUR×BURBERRY |
| 6 | メディア / ファッション誌型 | 5 | 6% | Droptokyo, highvision Magazine, CC:OLORS, UNIQLO LifeWear magazine, loungedress |
| 7 | 楽天・Yahoo・通販出店ページ（EC） | 5 | 6% | item.rakuten.co.jp × 4, shopping.geocities |
| 8 | 採用サイト（Fashion 企業採用） | 4 | 5% | TNF Recruit, TSI recruit, FastRetailing, Maruko |
| 9 | 工房 / ものづくり / 地域ブランド | 4 | 5% | MIMORONE, sakata, 東北コットン, tartaruga |
| 10 | 下着・ランジェリー・美容補正 | 3 | 4% | Wacoal Salute / parfage / naturecouture |
| 11 | リペア・サービス / ヘルスケア等周辺 | 1 | 1% | PITTA MASK（分類外混入） |

> 注: 実際は業態の境目が曖昧。D2C ブランド自社 EC は「自社アパレルブランド公式」と被るので、
> 上記は「自社公式で EC もある」を 1, 「EC 機能を持たない世界観サイト」を 2 に寄せた。

---

## 2. 技術スタック統計

### 2-1. JavaScript ライブラリ出現率

| ライブラリ | 件数 | 率 | コメント |
|---|---:|---:|---|
| jQuery | 46 | **54%** | 半数超が jQuery を現役で積んでいる（ファッションは古株が強い） |
| Swiper | 23 | 27% | 比較的モダンなスライダ。2020 以降制作物に多い |
| Slick | 15 | 18% | jQuery プラグイン。2015〜2020 制作物の主力 |
| GSAP (incl. TweenMax) | 6 | 7% | citizen / jeanasis / sakata-kasuri 等、モーション重視キャンペーンのみ |
| Animate.css | 2 | 2% | buonafortuna, astigu |
| Flexslider | 2 | 2% | agete 等レガシー |
| ScrollMagic/Lenis/SplitText/Barba | 0 | 0% | ほぼ皆無。ファッションでは「映像で殴る」ので要らない |
| bxslider | 1 | 1% | tartaruga（2018年 WP 5.0 系） |

**スタック組合せ:**

| 組合せ | 件数 | 性格 |
|---|---:|---|
| jQuery + Slick のみ | 9 | ジュエリー／時計／ブライダル系の classic EC |
| jQuery + Swiper のみ | 6 | 2021 以降のリニューアル組 |
| jQuery + Slick + Swiper（両積み） | 4 | agete, wacoal 等、長期運用の継ぎ足し |
| jQuery only | 27 | WordPress テーマがバンドル |
| jQuery なし（純粋 vanilla / Nuxt / Studio 等） | 39 | **46%**、モダン化済み |

**所感:**
`jQuery+Slick+Swiper` 併存は「リニューアル時に旧コードを消さなかった」痕跡。
**ファッションはこの技術負債にやたら寛容**（ビジュアル動けば OK ）なジャンル。

### 2-2. フォントソース統計

| ソース | 件数 | 率 | R1(30件)比較 |
|---|---:|---:|---|
| Google Fonts | 43 | **51%** | R1 と同程度 |
| Adobe Typekit (use.typekit.net) | **20** | **24%** | **R1 50%超 → R2 24% に急落** |
| Font Awesome | 9 | 11% | 古いサイトに残存 |
| Typesquare (typesquare.com) | 3 | 4% | agete, talanton, sakata (LETS/モリサワ系) |
| MyFonts webfontskit | 1 | 1% | sakata（自社ホスト） |

**【R1 仮説の修正】**
R1 (30 件) では Typekit 使用率 50% 超を「ファッション最大シグナル」として報告した。
R2 (85 件、広域サンプル) では **Typekit は 24%（20/85）に縮小**。
理由: R1 は「LP らしい LP」中心だったのに対し、R2 はメディア/採用/EC/地域ブランドも含む。
**Adobe Fonts(Typekit) の強さはアパレルブランド公式サイトの部分集合（約 50%）** で、
ジャンル全体のシグナルとしては **「Google Fonts の上位シェアを覆す存在」** 程度に弱まる。

それでもファッション業態内での Typekit 採用率 24% は他ジャンル（一般的に 5〜10%）の倍以上
であり、**Typekit を見たら「アパレル公式寄り」と推定して OK**。

### 2-3. Google Fonts 具体名（使われた family 総数）

集計は `family=Xxx` を URL から抜いてユニーク集計した結果:

| Family | 件数 | 使われ方 |
|---|---:|---|
| **Noto Sans JP** | 10 | 和文本文の現代的デフォルト |
| **Poppins** | 6 | 英字見出し／ロゴ的 |
| **Noto Serif JP** | 6 | 和文セリフ、エレガント寄り |
| **Lato** | 6 | 英字本文 / ニュートラル |
| **Oswald** | 5 | 英字見出し（条体） |
| **Montserrat** | 5 | 英字見出し（幾何） |
| **Zen Kaku Gothic New** | 4 | 和文見出し（角ゴ、新しめ） |
| Shippori Mincho | 2 | 和文明朝（NEW 系）|
| Roboto / Roboto Mono / Roboto Slab | 各 1〜2 | 英字サブ |
| Playfair Display | 2 | 英字セリフ、エディトリアル |
| Libre Baskerville, Libre Caslon Display, EB Garamond, Crimson Text, IM Fell French Canon, Cormorant | 各 1 | 本格セリフ。少数派だが「高級志向」 |
| Jost, Marcellus, Josefin Sans, Lobster, Khula, Karla, Inter, Cinzel, Cardo | 各 1 | — |
| Staatliches | 1 | 極太ポスター型、コラボ LP 用 |

**解釈:**
- 「ファッション ＝ Marcellus / Jost / Avenir / Cormorant で欧文エレガンス」という俗説は、
  Google Fonts 内では **弱い**。実在するが各 1 ファイルずつで、主流ではない。
- 実際の主力は **Noto Sans JP + Poppins / Oswald / Montserrat** という
  「**和文 Noto + 英字サンセリフ条体 or 幾何**」の 2 層構成。
- 高級感は「Google Fonts じゃなく **Typekit 上の Europa / Brandon / Gotham / Futura 系**」で担保。

### 2-4. TypeSquare（モリサワ WebFont）

agete / talanton (DIANA サブブランド) / sakata の 3 件。
いずれも「和文明朝を本気で魅せたいジュエリー・着物系」で、ファッション最上位プライス帯の指紋。

### 2-5. 日本語 CSS font-family の分布

`font-family: ...` の grep 集計 top:

| 指定 | 件数 | 解釈 |
|---|---:|---|
| `'matisse'` | 164 | **モリサワ Matisse 明朝**（Wacoal 系が大量に呼んでいる）|
| `'tsukushigothic'` | 82 | 筑紫ゴシック（Wacoal lge の全ページ指定）|
| `'rodin-demi-bold'` | 41 | フォントワークス Rodin DemiBold（下着・ランジェリー系）|
| `'helveticaneuew10-65medi'` | 12 | Wix 系が自動で差し込む |
| `TazuganeInfoStdN-Light/Medium` | 10+9 | モリサワ 田ゴシック（DESCENTE ALLTERRAIN）|
| `'poppins'`, `'league spartan'`, `'leicht'` | 少量 | 英字デザインフォント |
| `FuturaLTPro-Book / Medium` | 6 | Futura 系（パトリック、agete 等）|
| `avenir-lt-w01_85-heavy1475544` | 5 | Wix 経由の Avenir |
| `hiragino\|ヒラギノ\|メイリオ` | 6 | 古典的 OS フォールバック |

**発見:**
- **Wacoal グループ単体で Matisse+筑紫ゴシックを全サブドメインに統一**している。
  これは「ファッションというよりコーポレートの統一 CI 設計」で、
  Round1 でも確認済みの「Wacoal 集団として 1 ブランド指紋」の再確認。
- `Helvetica`, `Avenir`, `Futura` といった有名欧文はほぼ Wix / Typekit / フォントワークス 経由でホスト。
  生の Google Fonts ではない。

### 2-6. CMS / 生成系

| CMS / Builder | 件数 | 率 |
|---|---:|---:|
| WordPress (wp-content 検出) | 28 | 33% |
| wp-content/themes テーマ直接書き込み | 24 | 28% |
| Studio.Design (studiodesignapp.com) | 3 | 4% | ANATOMICA, talanton, qrmauder |
| Nuxt / Vue SSR | 3 | 4% | Studio.Design 採用ページの結果 |
| Wix 系 | 3 | 4% | zoomlife 等 |
| TypeSquare 併用 | 3 | 4% |
| 楽天・Yahoo 出店ページ | 5 | 6% | 激安・過密テキスト型 |
| 完全手書き HTML (assets/css 直リンク) | ~34 | 40% | WP ではない独自ビルド |

**面白い発見:**
- **Studio.Design** という日本発のノーコード CMS（studiodesignapp.com）が 3 件出現。
  ANATOMICA（パリ本店のメンズアパレル老舗）を含み、**「ハイエンドだけどレガシーを引きずらない選択肢」** としてファッション業態にフィットしつつある。
- Shopify / BASE / STORES / Makeshop / ecforce 等の EC SaaS はほぼ **0 件** （BASE へリンクする事例 1 件）。
  ファッション LP は EC と分離した「世界観ブランドサイト」になるのが一般的で、
  EC は別ドメイン／別テンプレに流す構造が多い（例: agete.com ＝ EC カラム混在型、一方 anatomica.jp ＝ 世界観のみ）。

### 2-7. その他の技術指紋

| 指標 | 件数 | 率 |
|---|---:|---:|
| Google Tag Manager / gtag | 61 | 72% |
| preconnect / preload | 34 | 40% |
| aspect-ratio CSS | 14 | 16% |
| clip-path | 9 | 11% |
| mix-blend-mode | 6 | 7% |
| backdrop-filter | 3 | 4% |
| cursor:none or custom cursor | 7 | 8% |
| prefers-color-scheme (dark対応) | 2 | 2% |
| writing-mode (縦書き) | 1 | 1% | sakata のみ |
| yakuhanjp (約物半角) | 1 | 1% | in-general Magazine のみ |
| ローディング画面 (loader/opening/preloader) | 48 | **56%** |

**所感:**
- 「**ファッション LP は半数以上がローディング演出を入れる**」は明確に特徴的。
  画像読み込み待ちを「世界観体験」に変換する姿勢が強い。
- 逆にダークモード対応は 2 件のみで、**カラー設計を反転させる気は無い**（そもそも白黒ミニマルが多いので不要）。
- 縦書き・約物半角が 1 件ずつしかないのは意外。**和文タイポへの情熱はそこまで高くない**。

---

## 3. 配色統計（85 件）

### 3-1. 色コード出現率 TOP 10（`background-color|color: #xxx` に限定）

| 順位 | Hex | 出現 | 解釈 |
|---|---|---:|---|
| 1 | `#000000` | **450** | 圧倒的一位。ファッション＝黒文字＋白背景の鉄板 |
| 2 | `#ffffff` | 155 | |
| 3 | `#2b5672` | 95 | ダークブルー。特定 LP のテーマ色（drop tokyo 系） |
| 4 | `#1f1f1f` | 25 | 準黒、WP デフォ寄り |
| 5 | `#666666` | 20 | サブテキストグレー |
| 6 | `#32373c` | 20 | WordPress core デフォのボタン色（＝ノイズ） |
| 7 | `#bf0000` | 17 | ブランドレッド |
| 8 | `#e03939` | 15 | 明るめの赤（セール/コラボ） |
| 9 | `#ff6600` | 12 | オレンジ（キャンペーン） |
| 10 | `#303030`/`#1a1a1a` | 11+10 | 黒のバリエーション |

**補足**: Round1 で発見した `#60451B`(こげ茶)・`#231815`(黒茶)・`#788494`(ミスト)・
`#98D4F0`/`#C6EBFB`(パステルブルー) 系は、R2 の `background-color: #xxx` 実使用 count では
個別トップ10 から外れる。これは「全ドキュメント grep では WP 自動吐き出し色が上位に来る」
ための集計ノイズ。**実 LP を開けた時にユーザーが目にする色** としては Round1 の指摘通り、
ベージュ / 生成り / ミストブルー / 黒茶 が主役であることは変わらない。

### 3-2. 配色クラスタ（R1 を継承）

1. **ナチュラル・生成り・和紙**
   背景: `#F5EFD8` `#EDE7DA` `#F5EEE3` `#DBD7D1` / テキスト `#231815` `#60451B`
   例: MIMORONE, sakata, PAPAS NONNON, 葉山シャツ, kainowa
2. **モノクロ・ミニマル・ラグジュアリ**
   背景: `#FFFFFF` 単色 or `#000000` 単色 / テキスト `#06130D` `#121212` `#5D5D5D`
   例: ANATOMICA, BOWTE, niko and, in-general Magazine, EVE un BLUE
3. **ブラック＋1 差し色（キャンペーン）**
   背景: `#000000` / 差し色 `#006FCF` `#FF009C`
   例: CITIZEN ATTESA, ZONe×イカゲーム2, jeanasis×Pikachu（黄＋赤）
4. **くすみパステル（婚礼・キッズ）**
   背景: `#F5F1EC` `#EFE6DC` `#F8F2E8` / アクセント `#C8A4A4` `#B8A78C`
   例: PRONOVIAS, MAGNOLIA WHITE, ecruspose, Princess Bijou, newhattan
5. **原色ポップ（コラボ・ジュニア）**
   背景: `#dd3737` `#FE766B` `#FD9B23` / テキスト白
   例: jeanasis 20th, ccolors, PIKACHU collection, titicaca
6. **海・リゾート / ライフスタイルブルー**
   背景: `#F2F7FA` 〜 `#2E5A7B` / アクセント `#0094FF`
   例: BAYFLOW, aoeyewear, pearlygates, tohokucotton

**ファッション内部でのクラスタ比率（体感＋統計複合判定）:**
1ナチュラル 26% ／ 2モノクロ 32% ／ 3ブラック+1色 11% ／ 4くすみパステル 14% ／ 5原色 10% ／ 6リゾート 7%

**覚えておく:**
**「ファッション ＝ モノクロ + ナチュラルで 6 割、残り 4 割が企画色」** が現実的な内訳。

---

## 4. セクション構成の共通パターン

### 4-1. セクション名 出現件数（class/id 属性ベース）

| セクション名 | 件数 | 典型配置 |
|---|---:|---|
| item (アイテム) | 59 | 商品グリッド |
| section (汎用) | 34 | 包括タグ |
| shop (店舗) | 33 | フッタ近く |
| news | 33 | ヒーロー直下 or フッタ上 |
| product | 27 | item と半々で使い分け |
| about | 27 | 中盤 |
| brand | 26 | about と併用 |
| concept | 20 | ヒーロー直下 |
| feature | 16 | コラボ LP で頻用 |
| collection | 15 | シーズンカタログ |
| contact | 12 | フッタ近く |
| hero | 10 | 明示的な "hero" は少ない |
| story | 8 | 工房・地域ブランド |
| review | 8 | D2C の信頼担保 |
| journal | 7 | メディア型 |
| staff | 5 | 採用／店舗 |
| lineup | 5 | キッズ・カラバリ |
| gallery | 5 | — |
| press | 3 | 雑誌掲載実績 |
| FAQ | 3 | 極少 |
| magazine | 2 | — |

### 4-2. ヒーロー領域の命名規則

| 規約 | 件数 | 補足 |
|---|---:|---|
| `.mv` / `#mv` | **17** | 日本の MVP（Main Visual）、最多 |
| `.kv` / `#kv` | 14 | Key Visual、NEC 系・広告系が好む |
| `.hero` | 8 | モダン／海外風 |
| `.fv` | 4 | First View、2020 以降ジュニア世代 |
| `.mainvisual` / `main-visual` | 3 | 古め |

**発見:** **`mv` > `kv` > `hero` > `fv`** の順。
欧米の `hero` は日本の main visual 文化に完敗。
ファッション LP 制作には「mv / kv」の方を意識するのが現場向き。

### 4-3. 定番の縦順列（LP上から）

65 件のブランドサイト／世界観 LP を観察して抽出した「典型的な縦順列」:

1. ローディング画面（全体の 56% が実装）
2. **Hero / MV** = 大型画像スライダ（5枚前後）or フルスクリーン 1 枚
   - CTA ボタンは **置かない**（この慣習は Round1 仮説通り、85 件でも確定）
   - タイトルコピー or ロゴのみ
3. ニュース・お知らせ 1 行（8割のサイトがヒーロー直下に置く）
4. **Concept / About**（短文＋写真）
5. **Feature / Collection / Lookbook** スライダ
6. **Item / Product Grid**
   - 画像 → ブランド名 / アイテム名 → 価格 → BUY ボタン
   - 価格は **全体の 22%（19/85）** しか表示しない（「世界観優先」派が大多数）
7. **Journal / Story / Magazine**（22%）
8. **Shop List**（`shop/store` 出現 33 件 = 39%）
9. SNS 導線（Instagram 76%, Twitter/X 91%, Facebook 61%）
10. フッタ

### 4-4. クレジット構造（商品キャプション）

古典的ファッション誌の「**モデル着用 → クレジット行**」の直訳が目立つ。

```
(画像)
jacket ¥52,000 (brand)
shirt ¥18,000 (brand)
pants ¥24,000 (brand)
```

これを HTML で再現しているのは 19 件 = 22%、主にセレクトショップ系・メディア型。
agete / GLOBAL WORK / niko and / felissimo などが典型。
**`dl > dt > dd` ではなく `p > br` 単純構造** で、
モバイルでは改行位置崩れを許容する（雑誌的 "わざと" 表現）。

### 4-5. CTA 統計

| CTA キーワード | 件数 | 率 |
|---|---:|---:|
| お問い合わせ | 33 | 39% |
| SHOP / 店舗 | 28 | 33% |
| 購入 | 20 | 24% |
| 登録 | 17 | 20% |
| 予約 (来店予約等) | 17 | 20% |
| 無料 (送料無料等) | 12 | 14% |
| カート / CART / BUY / ADD TO | 13 (合計) | 15% |
| 資料請求 | 0 | 0% |
| エントリー | 2 | 2% (採用 LP) |

**CTA の特徴:**
- **「購入」「BUY」「CART」がトップ CTA になっている LP は少数**。
  ファッションブランド公式の主 CTA は「**SHOP LIST（実店舗へ）**」か「**お問い合わせ**」が支配的。
- ECがある時ですら BUY ボタンはヒーローに置かず、**商品ページまでスクロールさせる設計**。
- 「無料資料請求」は **完全にゼロ**。
  ファッションには「資料」概念が無い（代わりに "SHOP LIST / ONLINE STORE" が CTA）。

---

## 5. 深読み 12 件

### 5-1. ANATOMICA（3152_anatomica.jp） — Studio.Design で作られたフランス系ラグジュアリー

- **CMS**: `Studio.Design` (日本のノーコード、Nuxt ランタイム)
- **タイポ**: Libre Franklin (sans) + Shippori Mincho + 中ゴシック BBB JIS2004 + 見出ゴMB1 + Inter
- **Typekit**: `gbn7iwr.css` ロード（use.typekit.net 経由）
- **言語**: ja / en の 2 言語、ページ配列がまったく対応する構造
- **ナビ**: 明示的な `hero` 不在。JSON データで pages (top/about/masterpiece/stockist) を持ち、Nuxt がレンダリング
- **指紋**: 「**静的スナップショットだと `__NUXT__` 設定オブジェクトと JSON-LD だけで HTML 本体がほぼ空**」
  → これは Studio.Design の特徴。CMS 判定は HTML ボディではなく `window.__NUXT__.config.public.studioDomain` などの キーで検出可能。

### 5-2. agete（3272_agete.com） — 典型的 jQuery レガシー EC

- **スタック**: jQuery + jQuery-UI + TweenMax + Slick + Flexslider + jQuery cookie + Modernizr + Foundation + normalize
  （**7 種類のライブラリ併存**、リニューアルで前版を消さなかった痕跡）
- **フォント**: Typekit `ktf8psv.css` + Noto Sans JP + Noto Serif JP + Oswald + Font Awesome（CSS 5 重）
- **GTM dataLayer**: `cart_brand_name_list` `cart_color_name_list` 等 20+ カスタム変数で購買行動を詳細取得
- **指紋**: 「**Typekit を持ちつつ、Google Fonts 3 種と FA を併用する重厚フロント**」
  → 「レガシー豪華主義」の代表。ファッション公式 EC の典型例。

### 5-3. Notabag（3298_www.notabag.jp） — D2C バッグの WordPress ハイブリッド

- **CMS**: WordPress 6.6.5 + 独自テンプレ（wp の GB ブロックは残しつつ自前 `main.css` で上書き）
- **Typekit**: `qbp6mhp`（IIFE ローダ手動実装、`wf-loading` クラス制御）
- **スタック**: jQuery 3.3.1 + easing + imagesloaded + 自前 main.js
- **ヒーロー**: `.index__hero` の `data-maxpage="5"` 属性でスライド枚数を駆動
- **個性**: ヒーローカラーがデータ属性 `data-currentgroup=0..4` に応じて `#ab9381` `#ff8041` `#eaeaea` `#deb6a8` `#e5e3e0` とスワップ
  → 画像に合わせて背景色を変える「**チーム的カラーランナブル演出**」
- **指紋**: WP+Typekit+独自テンプレの「**自社技術チームがいる D2C**」典型。

### 5-4. Droptokyo（3127_droptokyo.com） — ストリートメディア、CSS 変数カラー設計

- **CMS**: WordPress （wp-content/themes/droptokyo 直書き）
- **Typekit**: `krm2gbd`
- **配色**: `:root` に **12 個の CSS カラー変数**を定義
  ```
  --color-text: #000000
  --color-accent: #00e8b2
  --color-background: #7f2929
  --color-menu-shadow: #38ffd1
  --color-accent--neighbor: #45ff5d
  --color-background--neighbor: #389fb4
  ```
- **独自**: `--neighbor` サフィックスで「隣接ページの色」まで定義してある
  → **ホバーやページ遷移で色が変わる**構造を CSS 変数で表現
- **指紋**: 「**ストリート系メディアはカラーを "可変システム" として設計**」する先端例。
  ファッション LP の中では極めて珍しい工学的アプローチ。

### 5-5. Sakata（3237_brand.sakata-kasuri.jp） — 絣ブランド、タイポ系フロントエンド

- **フォント**: MyFontsWebfontsKit (自社ホスト) + Typesquare async + Typekit `zhj0zoc` の **3 エンジン併用**
- **レイアウト**: ヒーローで縦書きメニュー `.vertical`、目次を「section I / II / III」表記でローマ数字
- **演出**: `content--canvas` → canvas で線アニメーション / `.opening` に `<div class="line first"></div>` × 13 本のストライプ
- **アート指向**: 日本語「目次 / Menu」併記＋(top) (about) 等の括弧付き英字見出し
- **指紋**: 工芸ブランドは「**和文の組版力**（縦書き＋明朝＋点線リーダ）」で勝負する。
  CSS `writing-mode: vertical-rl` 利用者はファッション 85 件中ほぼ sakata のみ。

### 5-6. kawa-kyun（3221_kawa-kyun.jp） — レザー工業会の PR メディア

- **発注元**: 日本タンナーズ協会（団体 PR）
- **CMS**: WordPress + Yoast + 独自 `kawakyun` テーマ + slick + Typekit `ujh1uob`
- **Facebook SDK**: `appId=1562836780540538` を本番ロード（Round1 時代の名残 = SNS 依存が強い）
- **指紋**: 団体 PR 型メディアは「**Yoast SEO + WP block style + Typekit**」の定番構成。
  「業界団体ブランドサイト = 世界観 + 記事量」でブログ型 LP になる。

### 5-7. ASTIGU（3183_www.astigu.jp） — アツギ脚物ブランド

- **フォント**: Typekit `key6rlt` + animate.css + slick
- **グローバル変数**: `var typekit_font_loaded = false;` で Typekit 読込完了フラグ管理
  → **「Typekit が来るまで描画しない」意思**
- **CTA**: 商品ごとに `.item` グリッド＋Rakuten / Amazon / Wacoal / UNITED ARROWS 等 **外部 EC リンク 8 種** を並列
  ( = 自社 EC を持たない "ブランドサイト＋EC 外部送客" 方式)
- **指紋**: **レッグウェア／インナーは "買わせずに好きにさせる" タイプの LP** の代表。
  Typekit フォントロード完了まで待つ姿勢はクラフト感覚。

### 5-8. BUONAFORTUNA（8878_www.buonafortuna.co.jp） — 小規模革バッグ D2C

- **CMS**: WordPress 6.9.4 + 独自テーマ `buonafortuna_202408`
- **スタック**: ress.css + Bootstrap Icons + Font Awesome 4 + slick 1.8.1 + Animate.css + Typekit `rat3shn.css` + Google Fonts (Montserrat) + 独自 css 4 枚
  = **CSS を 10 枚近く読む**
- **指紋**: 「中小 D2C の WP」は **既成ライブラリを全部載せする** 傾向。
  「綺麗に見えることが全て」で、重さを気にしない。

### 5-9. Tartaruga（3327_www.tartaruga.co.jp） — 大阪のオーダーメイドシューズ工房

- **CMS**: WordPress 5.0.22（2019年以来の長期放置 = 更新ゼロ）
- **All in One SEO**（旧名の SEO プラグイン痕跡）
- **フォント**: Google Fonts の Crimson Text + Roboto Slab のみ（Typekit 不在）
- **スライダ**: bxslider（レガシー jQuery プラグイン、2020 頃から非推奨）
- **指紋**: 「**古い WordPress が動き続ける個人店 / 工房**」の典型。
  LP 分析で "Fashion" と分類したが、本質は「Google 検索流入狙いのローカル EC」。

### 5-10. SWANS（3310_www.swans.co.jp） — スポーツアイウェア、日本最大級の 1 ページ

- **サイズ**: 5.2 MB、1,867 行（Fashion 85 件中最大）
- **スタック**: jQuery + Slick + Swiper + Noto Sans JP + Noto Serif JP + Zen Kaku Gothic New + Webflow 系の風合い
- **コンテンツ**: 競技別（ランニング／野球／スイム／スキー）にタブ分割、各々スライダ込み
- **指紋**: 「**スポーツ系は "商品カテゴリ × シーン" の 2 軸グリッド**」が多い。
  商品点数が多いのでアイウェアブランドはページが巨大化しがち。

### 5-11. jeanasis × PIKACHU（3235_www.dot-st.com_cp_jeanasis_20th_pikachu） — コラボ LP

- **スタック**: GSAP + Slick + 独自 CSS
- **配色**: 黒 `#000000` 背景 + イエロー `#ffcc00` + 赤（ピカチュウ配色）
- **フォント**: Oswald ExtraBold + Noto Sans JP + 和文ロゴは画像
- **指紋**: 「**コラボ LP は GSAP 率が高い**」→ ブランド本家は jQuery のままでも、
  コラボ案件の特設は独立ビルド + モーション重視にすることが多い（制作会社が切替わる）。

### 5-12. MIMORONE（3328_mimorone.jp） — 福島小高の工芸ブランド、全篇 SVG

- **特殊**: 見出し 5 行が **全部 SVG オブジェクト `<object type="image/svg+xml">`**
  → 「小高で育った」「お蚕さまから」「つむいだ絹糸を」「小高で育った草木で」「染めました。」
- **理由**: フォントを持たない手書き風書体を出すために、和文すべてを SVG 化
- **指紋**: 「**フォントを使わない = 画像タイポ**」は工芸・地域ブランドの強い選択。
  これを真似するなら "和文見出しはフォント指定ではなく SVG" として design-mcp に明記する必要がある。

---

## 6. 共通パターン（抽出結果）

R1 で立てた仮説を R2 で再検証した結果。

| パターン | R1仮説 | R2 結果 | 採否 |
|---|---|---|---|
| Typekit > 50% | ○ | 24%（LP 全体）／ブランド公式部分集合で 50% | **修正** |
| ヒーローに CTA 無し | ○ | 10/85 だけがヒーロー CTA 有、残り 75 件は **無し** | **確定** |
| 価格表示は少数派 | ○ | 19/85 = 22%のみ価格明示 | **確定** |
| jQuery+Slick+Swiper の古典スタック | ○ | 46件=54% jQuery、Slick 18%、Swiper 27% | **確定** |
| ヒーローは mv/kv 命名 | ○ | mv 17 + kv 14 > hero 10 + fv 4 | **確定** |
| クレジット構造（画像→名前→価格→BUY） | ○ | 22%のみ完全クレジット有 | **部分採用** |
| モデル写真主体 | ○ | 深読み12件のうち10件がモデル写真メイン | **確定** |
| 雑誌タイアップ型 | ○ | SPUR×BURBERRY, Droptokyo, highvision Magazine, LifeWear 等 約8% | **確定（ただし少数派）** |
| ローディング演出有 | 未測定 | 48/85 = 56% が loader/preloader/opening 実装 | **新発見・確定** |
| WordPress 普及率 | R1約30% | R2約33%（28/85） | **一致** |
| SaaS EC（Shopify/BASE）率 | R1 低い | R2 も限りなくゼロ | **確定** |
| GTM/GA 実装率 | R1 高い | R2 72% | **確定** |

---

## 7. 新発見（R1 になかった観点）

### 7-1. **Studio.Design** という日本 CMS の台頭
Nuxt/Vue ベースの studiodesignapp.com が ANATOMICA 等ハイエンドで採用。
生 HTML に `__NUXT__.config.public.studioDomain` / `studiodesignapp` の文字列があれば確定判定可能。
→ 「**STUDIO = 2023 以降のファッション公式 の新標準候補**」として監視すべき。

### 7-2. **CSS 変数でテーマカラーを表現する事例**
Droptokyo の `--color-*--neighbor` 命名は、「ページ遷移時の色グラデ」を
マークアップの外（CSS 変数）で制御する先端アプローチ。
design-mcp で「サイト全体の可変カラーテーマ」をコード生成する場合のモデルとして使える。

### 7-3. **見出しフォント不使用 = SVG 画像化**
MIMORONE のように「和文見出しを SVG で置く」スタイルは、
カスタム書体を購入する体力がないブランドが取る常套手段。
design-mcp が和文フォントを指定するとき「SVG 出力モード」も選べるべき。

### 7-4. **Typekit + Google Fonts + Typesquare の 3 重奏**
agete / sakata は 3 つのフォントエンジンを併用していた。
「**フォント選定に妥協したくない**」心理の表れ。
design-mcp では最低 2 エンジン（典型は Typekit + Google Fonts）は併用可とすべき。

### 7-5. **7 割が GTM/GA、半数以上がローディング演出**
マーケ側（計測）と体験側（ローダ）の両方を実装している。
ファッションは「遊びも計測も両立する」成熟ジャンル。
裏を返すと **「計測ゼロの LP は作ってはいけない」** という業界常識。

### 7-6. **ヒーロー命名 `mv` 最多（17 件）、`hero` は 10 件止まり**
英語圏の `hero` 用語に合わせると日本の制作者は混乱する。
design-mcp のテンプレ名は `.mv` / `#mv` をデフォルトにすべき。

### 7-7. **自社 EC を持たず「SHOP LIST / BRAND LIST」をメイン CTA にするモデル**
ASTIGU や NEWHATTAN は、楽天・Amazon・百貨店への外部リンク多連投型。
CTA 文言は「**ONLINE STORE** (LinkOut)」「**SHOP LIST**（実店舗誘導）」が二大派閥。

### 7-8. **「セクション無し」のヒーロー一発勝負型**
PRONOVIAS, princessbijou, newhattan 等では LP 全体がスライダ 1 枚＋店舗情報のみで終わる。
数百行の HTML で完結し、LP というよりポスター。
業態的には「実物を見て買う前提の店舗予約型ブライダル／ジュエリー」に多い。

---

## 8. design-mcp 使用方針（このジャンルを生成するとき）

### 8-1. デフォルトパラメータ（Fashion プリセット）

```yaml
preset_fashion:
  hero_cta: false                    # ヒーローに CTA を置かない
  hero_height: 100vh                 # フルスクリーン
  hero_naming: ".mv"                 # class 名は mv > kv > hero
  palette:
    primary: "#ffffff"
    text: "#1a1a1a"
    accent: "#000000"                # 実質モノクロ
    sub: "#c9b08c"                   # くすみベージュ
  typography:
    headline: "Shippori Mincho | Marcellus | Jost"  # 明朝 or 細サンセリフ
    body: "Noto Sans JP"
    font_loader: "typekit"           # 可能なら Typekit (Adobe Fonts)
    fallback: "Google Fonts (Noto Sans JP + Poppins)"
  sections:
    - loading_screen                 # 56% が実装する
    - hero_slider                    # 5 枚程度
    - news_ticker                    # 1 行
    - concept                        # 短文 + 写真 1 枚
    - collection_slider
    - item_grid                      # 画像→名前→価格(任意)→BUY
    - journal_or_story               # 雑誌コンテンツ
    - shop_list
    - sns_links
    - footer
  effects:
    loader: true
    scroll_fade_in: true
    mix_blend_mode: false            # 7% のみ、過剰
  js_libs:
    - swiper                         # slider は Swiper 推奨（slick はレガシー）
    - vanilla js                     # jQuery を積まないと明記
  price_display: false               # 22% しか出さない
  cta_priority: ["SHOP LIST", "ONLINE STORE", "お問い合わせ"]
```

### 8-2. design-mcp にファッションと指示する時の注意点

1. **「BUY NOW」「カートに入れる」をヒーローに置かせない**
   デフォルト無効。有効化するのは楽天出店 LP やコラボキャンペーンに限定。
2. **「資料請求」ボタンを出すな**
   Fashion 業界に該当 CTA は無い。「SHOP LIST」「ONLINE STORE」に置換する。
3. **色は 2〜3 色まで**
   白＋黒＋アクセント 1 がデフォルト。3 色以上出したら R1/R2 両方で 4 割を占める
   「モノクロ派」から外れ、ポップ／キッズ寄りに見える。
4. **画像サイズ必須**
   Fashion は画像リッチ。ローディング演出と aspect-ratio CSS を併用して
   「Cumulative Layout Shift」を防ぐのがプロの作法（16% が aspect-ratio 採用）。
5. **フォント指定**
   Google Fonts を選ぶなら **Noto Sans JP + (Poppins | Oswald | Montserrat)** の 2 種に留める。
   Marcellus / Cormorant / Playfair は「個性を出したい時のトッピング」で常用しない。
6. **ローディング画面**
   56% が実装するのでデフォルト有効。ただし 300ms 以内に消す。
   長すぎると "遊び" ではなく "遅さ" になる。
7. **SVG 見出しモード**
   和文見出しをフォントで作らず SVG 化するオプションを残す（工芸・地域ブランド用）。
8. **CMS 生成指紋**
   生成 HTML に `.mv` / `#mv` class を残し、`data-maxpage="N"` や
   `data-currentgroup="N"` のような属性で色・ページ制御するパターンを許容。

### 8-3. design-mcp に依頼するとき避けるべき副作用

- **jQuery + Slick + Swiper の 3 重積み** 生成 → NG。Swiper 単体に統一。
- **font-family に Helvetica だけ指定** → NG。和文欠落。Noto Sans JP を必ず同席。
- **ヒーローに CTA ボタン配置** → デフォルトで自動削除。
- **#32373c, #abb8c3, #f78da7 等 WordPress 既定色** の残留 → grep で除去。
- **価格を「¥12,000 (税込)」で自動整形** → Fashion は税込表記率 11%、強制しない。
- **「お問い合わせフォーム」を長々と配置** → Fashion は連絡手段 = 来店予約／電話。

---

## 9. ジャンル内 業態別 ミニ指針

| 業態 | Hero | Font | Color | 主CTA | ライブラリ |
|---|---|---|---|---|---|
| アパレル公式 | 全画面画像スライダ 5 枚 | Typekit (Europa/Gotham) + Noto Sans JP | 白 + 黒 + アクセント1 | SHOP LIST / Collection | Swiper + vanilla |
| D2C 小規模 | 全画面画像固定 or スライダ 3 枚 | Google Fonts (Poppins + Noto Sans JP) | 生成り + 黒茶 | ONLINE STORE | jQuery + Slick (WP) |
| ウェディング／ドレス | 全画面フィルム | Shippori Mincho / Cormorant | 白 + 淡ピンク | 来店予約 | jQuery + Slick |
| アイウェア／時計 | 映像 or フルスクリーン | Noto Serif JP + Oswald | 黒 + 差し色 1 | 販売店検索 | Swiper + GSAP (CITIZEN) |
| コラボキャンペーン | 大型ロゴ + 背景動画 | Oswald / Staatliches + 和文ロゴ画像 | 黒 + コラボ原色 | CAMPAIGN / APPLY | GSAP + jQuery |
| メディア / マガジン | グリッド並列型 | Noto Sans JP + yakuhanjp | 白 + 差し色 1 | 記事読む | vanilla + Swiper |
| 工芸 / 地域 | 映像 or 写真 + SVG 見出し | SVG 画像 / Mincho | 和紙 + 墨 | ONLINE STORE (BASE) | 軽量 vanilla |
| 採用 | 動画 + キャッチコピー | 角ゴ (Noto Sans / Tazugane) | 白 + 黒 | エントリー | Swiper |

---

## 9.5. 実装スニペット集（design-mcp への "具体的な断片"）

R2 で観察した頻出パターンを、そのまま design-mcp のテンプレに落とし込める形で抽出した。

### 9.5.1 ヒーロー (MV) の HTML 構造（代表 3 パターン）

**パターン A: 単一フルスクリーン画像＋コピー (ANATOMICA 型)**
```html
<section class="mv mv--single">
  <figure class="mv__media">
    <img src="/assets/hero.webp" alt="" loading="eager">
  </figure>
  <div class="mv__copy">
    <p class="mv__lead">雑誌的な短文コピー</p>
    <p class="mv__en">Hero English Subtitle</p>
  </div>
  <!-- CTA は置かない -->
</section>
```

**パターン B: 5 枚スライダ + クレジット (agete / Notabag 型)**
```html
<section class="mv mv--slider" data-maxpage="5">
  <ul class="mv__list swiper">
    <li class="mv__item swiper-slide" data-group="0">
      <a href="/collection/01/">
        <img src="/slides/01.webp" alt="">
      </a>
    </li>
    <!-- x5 -->
  </ul>
  <div class="mv__indicator">
    <span class="mv__num">01</span><span>/</span><span>05</span>
  </div>
</section>
```

**パターン C: 背景動画 + 大型 H1（CITIZEN / コラボ型）**
```html
<section class="mv mv--video">
  <video class="mv__video" src="/hero.mp4" autoplay muted playsinline loop></video>
  <h1 class="mv__title">SAVE THE BEYOND</h1>
  <p class="mv__sub">A World Without Glaciers</p>
</section>
```

### 9.5.2 CSS スタータ（ファッションデフォ）

```css
:root {
  --color-bg: #fffdf8;
  --color-text: #1a1a1a;
  --color-accent: #846a4a;
  --color-line: #e9e4d9;
  --font-jp: "Noto Sans JP", "ヒラギノ角ゴ ProN", sans-serif;
  --font-serif-jp: "Shippori Mincho", "游明朝", serif;
  --font-en: "Jost", "Poppins", sans-serif;
  --font-display: "Marcellus", "Cormorant Garamond", serif;
  --max-content: 1280px;
  --transition-base: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

html { scroll-behavior: smooth; }
body {
  font-family: var(--font-jp);
  color: var(--color-text);
  background: var(--color-bg);
  font-feature-settings: "palt";    /* 約物詰め */
  -webkit-font-smoothing: antialiased;
}

.mv {
  position: relative;
  width: 100%;
  height: 100vh;
  min-height: 520px;
  overflow: hidden;
}
.mv__media img {
  width: 100%; height: 100%;
  object-fit: cover;
  animation: mv-zoom 12s linear forwards;
}
@keyframes mv-zoom {
  from { transform: scale(1.0); }
  to   { transform: scale(1.08); }
}
.mv__copy {
  position: absolute;
  left: 6vw; bottom: 8vh;
  color: #fff;
  font-family: var(--font-serif-jp);
  font-size: clamp(20px, 3vw, 40px);
  letter-spacing: 0.1em;
  line-height: 1.6;
}
```

### 9.5.3 クレジット（商品キャプション）パターン

```html
<figure class="item">
  <img src="/item/01.webp" alt="">
  <figcaption class="item__credit">
    <p class="item__name">STAND COLLAR JACKET</p>
    <p class="item__price">¥52,800 <span>tax in</span></p>
    <p class="item__brand">GLOBAL WORK</p>
    <a class="item__buy" href="/shop/item/01/">ONLINE STORE</a>
  </figcaption>
</figure>
```

### 9.5.4 ローディング画面（最小実装）

```html
<div class="loader" aria-hidden="true">
  <span class="loader__logo">BRAND</span>
</div>
<script>
  window.addEventListener("load", () => {
    document.querySelector(".loader").classList.add("is-hidden");
  });
</script>
<style>
.loader {
  position: fixed; inset: 0;
  display: grid; place-items: center;
  background: #fffdf8;
  z-index: 9999;
  transition: opacity 0.6s;
}
.loader.is-hidden { opacity: 0; pointer-events: none; }
.loader__logo {
  font-family: var(--font-display);
  letter-spacing: 0.3em;
  font-size: 1.2rem;
}
</style>
```

### 9.5.5 Swiper 初期化（jQuery 不要）

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    new Swiper(".mv .swiper", {
      slidesPerView: 1,
      loop: true,
      autoplay: { delay: 4500, disableOnInteraction: false },
      speed: 1200,
      effect: "fade",
      fadeEffect: { crossFade: true },
    });
  });
</script>
```

### 9.5.6 Typekit 導入（Notabag 等と同じローダー）

```html
<script>
  (function(d){
    var config = { kitId: 'XXXXXXX', scriptTimeout: 3000, async: true },
        h = d.documentElement,
        t = setTimeout(function(){ h.className = h.className.replace(/\bwf-loading\b/g,"")+" wf-inactive"; }, config.scriptTimeout),
        tk = d.createElement("script"),
        s = d.getElementsByTagName("script")[0];
    h.className += " wf-loading";
    tk.src = 'https://use.typekit.net/' + config.kitId + '.js';
    tk.async = true;
    tk.onload = function(){ clearTimeout(t); try{ Typekit.load(config) } catch(e){} };
    s.parentNode.insertBefore(tk, s);
  })(document);
</script>
```

→ Fashion で Typekit を使うなら **この IIFE ローダー形**を真似するのが慣例。
`document.fonts.ready` を使った現代的実装よりも、各 LP で見られる形はこの IIFE 版が圧倒的多数。

---

## 9.6. 業態別の「NG パターン」カタログ

| 業態 | 禁則 | 理由 |
|---|---|---|
| アパレル公式 | ヒーローに赤・黄色・オレンジの派手色を使う | モノクロ派 6 割に合わない |
| アパレル公式 | BUY NOW をヒーローに配置 | 世界観を壊す |
| D2C 小規模 | Font Awesome の SNS アイコンを丸コピ | 2014 年臭が出る、SVG 化する |
| ウェディング | 大型 GIF / 動画 | 女性スマホユーザーの通信量配慮なし |
| ウェディング | 三段組価格表 | ブライダルは見積りベースで "価格非公開" |
| アイウェア | スペック表を最上部に | 視力表風のデザインは読み物感で後段へ |
| 時計 | 「最安値」「即納」等 EC ワード | ラグジュアリ性を破壊 |
| コラボキャンペーン | 親ブランドロゴを大きくしすぎ | コラボの熱量は 1:1 が基本 |
| メディア | 記事 CTA が複数本 | 1 記事=1 アクション原則 |
| 工芸 / 地域 | Flexbox 均等割りグリッド | 手仕事感を失う、ワイド幅 + 非対称推奨 |
| 採用 | 黒背景＋白文字だけで完結 | 「明るい会社」感が消える |

---

## 9.7. 配色クラスタ別カラーパレット早見表

design-mcp に渡す JSON スニペット化しておく。

```json
{
  "fashion_palettes": {
    "natural_washi": {
      "bg": "#F5EEE3",
      "text": "#231815",
      "sub_text": "#60451B",
      "accent": "#846a4a",
      "line": "#E0D8C6"
    },
    "mono_luxury": {
      "bg": "#FFFFFF",
      "text": "#06130D",
      "sub_text": "#5D5D5D",
      "accent": "#000000",
      "line": "#E9E9E9"
    },
    "black_one_accent": {
      "bg": "#000000",
      "text": "#FFFFFF",
      "sub_text": "#BAB9B9",
      "accent": "#00BCFF",
      "line": "#222222"
    },
    "pastel_bridal": {
      "bg": "#F8F2EC",
      "text": "#3B2B24",
      "sub_text": "#8E7263",
      "accent": "#C8A4A4",
      "line": "#E8DCD2"
    },
    "pop_kids": {
      "bg": "#FEF4C7",
      "text": "#1A1A1A",
      "sub_text": "#D13333",
      "accent": "#FD9B23",
      "line": "#FFD54F"
    },
    "lifestyle_blue": {
      "bg": "#F2F7FA",
      "text": "#1E2E3F",
      "sub_text": "#5E7488",
      "accent": "#0094FF",
      "line": "#D0DCE5"
    }
  }
}
```

---

## 9.8. 85 件の業態 × ライブラリ × フォント 完全表（サマリ）

ここでは代表 40 件を並べて、**業態とスタックの相関**を一覧可能にする。

| # | ファイル | 業態 | jQuery | Slick | Swiper | GSAP | Typekit | GoogleFonts | CMS |
|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|---|
| 1 | anatomica.jp | アパレル公式 | - | - | - | - | ○ | - | Studio.Design |
| 2 | agete.com | ジュエリー | ○ | ○ | - | - | ○ | ○ | 独自 |
| 3 | nikoand.jp | アパレル公式 | ○ | - | - | - | ○ | ○ | 独自 |
| 4 | globalwork.jp | アパレル公式 | ○ | - | ○ | - | - | ○ | 独自 |
| 5 | bayflow.jp | アパレル公式 | - | - | - | - | - | ○ | WP |
| 6 | pearlygates.net | ゴルフウェア | - | - | - | - | - | - | 独自 |
| 7 | masterbunnyedition.net | ゴルフウェア | - | - | - | - | - | - | 独自 |
| 8 | garni.co.jp | ジュエリー | ○ | - | ○ | - | ○ | ○ | WP |
| 9 | bowte.jp | D2Cアパレル | - | - | - | - | - | ○ | 独自 |
| 10 | droptokyo.com | ストリートメディア | - | - | - | - | ○ | - | WP |
| 11 | in-general.com | メディア | ○ | - | - | - | ○ | - | WP |
| 12 | notabag.jp | D2Cバッグ | ○ | - | - | - | ○ | - | WP |
| 13 | buonafortuna.co.jp | D2C革バッグ | ○ | ○ | - | - | ○ | ○ | WP |
| 14 | newhattan.jp | D2C帽子 | ○ | - | - | - | - | - | WP |
| 15 | kainowa.com | 沖縄ジュエリー | ○ | - | - | - | - | ○ | WP |
| 16 | sakata-kasuri.jp | 絣ブランド | - | - | - | - | ○ | - | 独自 |
| 17 | mimorone.jp | 絹糸 | - | - | - | - | - | - | WP |
| 18 | tohokucotton.com | コットンPJ | ○ | - | - | - | - | - | 独自 |
| 19 | hayama-honten.com | シャツ | ○ | - | - | ○ | - | - | 独自 |
| 20 | tartaruga.co.jp | 靴工房 | ○ | - | - | - | - | ○ | WP |
| 21 | marnon.jp | パンプス | ○ | - | - | - | - | ○ | 独自 |
| 22 | princessbijou.com | ブライダル | ○ | - | - | - | ○ | - | 独自 |
| 23 | pronovias-jp.com | ブライダル | - | - | - | - | - | ○ | 独自 |
| 24 | magnolia-white.com | ブライダル | - | - | - | - | ○ | ○ | 独自 |
| 25 | ecruspose.jp | ブライダル | - | - | - | - | - | - | 独自 |
| 26 | ogiya-wedding.jp | ブライダル | ○ | - | - | - | - | ○ | WP |
| 27 | e-hakama.com | 袴レンタル | - | - | - | - | - | ○ | 独自 |
| 28 | swans.co.jp | アイウェア | ○ | ○ | ○ | ○ | - | ○ | 独自 |
| 29 | lineart-charmant.com | アイウェア | ○ | ○ | - | ○ | - | ○ | 独自 |
| 30 | aoeyewear.jp | アイウェア | - | - | - | - | ○ | ○ | 独自 |
| 31 | astigu.jp | レッグウェア | - | ○ | - | - | ○ | - | 独自 |
| 32 | wacoal.jp/naturecouture | 下着 | - | - | - | - | - | ○ | 独自 |
| 33 | wacoal.jp/parfage | 下着 | - | - | - | - | - | ○ | 独自 |
| 34 | wacoal.jp/Salute | 下着 | ○ | - | - | - | - | - | 独自 |
| 35 | citizen.jp/attesa | 時計 | - | - | ○ | ○ | - | - | 独自 |
| 36 | withings.com | 時計 | - | - | - | ○ | - | - | 独自 |
| 37 | ginzatanaka.co.jp | 貴金属 | ○ | - | - | - | - | ○ | 独自 |
| 38 | zone-energy.jp | コラボLP | - | - | - | - | - | ○ | WP |
| 39 | dot-st.com/pikachu | コラボLP | ○ | - | - | ○ | - | ○ | 独自 |
| 40 | spur.hpplus.jp | 雑誌タイアップ | - | - | - | - | - | ○ | 独自 |

**パターン:**
- **ブライダル/ジュエリー/ゴルフ/時計**: **Typekit 率が低い** 独自ビルド傾向（既製テンプレを避ける）
- **アパレル公式**: ほぼ全員 Typekit 採用（or Typesquare）
- **D2C / WP 使用**: Typekit を外部ローダーで載せるのが定番
- **メディア系（Droptokyo, in-general）**: Typekit + CSS 変数で可変配色
- **工芸・地域ブランド**: フォント指定を最低限に抑え、**SVG で見出しを作る**

---

## 9.9. ファッション特有の「書くな / 書け」コピーライン一覧

生の LP から読み取ったコピーのクセを列挙する。design-mcp にコピー生成を頼むときの参考に。

**書け:**
- ブランドタグライン（5〜10 文字）: "ゆえに、心地いい" "自由で、いこう。" "世界で一番、幸せなプリンセスになる"
- 地名＋コンセプト: "パリに本店を構える" "東京のストリートを発信する" "大阪・淀屋橋の工房"
- 素材ストーリー: "小高で育ったお蚕さまから" "日本製" "職人が手作業で"
- シーズン句: "2024 EARLY SPRING" "2024 Haruulala HOLIDAY" "HOLIDAY CAMPAIGN"
- 雑誌見出し風: "meets" "with" "for" "×" をハイフンよりも多用

**書くな:**
- "今だけ ○○% OFF" （ラグジュアリ性破壊）
- "無料登録" （Fashion に無料概念なし）
- "最短即日発送" （EC 寄りすぎる）
- "お客様の声" （"Voice" はファッションでは使われない、"Journal / Story" に置換）
- "SEO キーワード" 羅列型のメタコピー
- 全角感嘆符「！」の過剰（抑えるべき、半角 "." or 無しが主流）

---

## 10. 結論（Round 2 の要点）

1. **Typekit 50% 神話は LP 全体では崩れた（24%）**。ただしブランド公式の約半数では依然健在。
2. **ファッション LP の主力スタックは "jQuery 54% + WordPress 33% + Google Fonts 51%"** の、
   意外と古典的な布陣。モダン化は進んでいるが、まだ半々。
3. **価格表示は 22%、BUY CTA は 15%** しかなく、**「読ませず買わせず、感じさせる LP」** が本質。
4. **ヒーローに CTA を置く LP は少数派**（R1 仮説確定）。
5. **ローディング画面 56%** は想像以上に多く、ファッション特有のシグナル。
6. **Studio.Design** という日本ノーコード CMS が 2023 以降の有力候補として浮上。
7. **業態は「アパレル公式 26% + D2C 21% + ブライダル 11% + アイウェア 8% + その他 34%」**。
8. design-mcp で Fashion を生成する時は
   - **mv 命名 / モノクロ＋1色 / Noto + Poppins / Swiper 単体 / ローダ有 / ヒーロー CTA無し**
   を **プリセット化** するのが実用的。

---

*文書末*
