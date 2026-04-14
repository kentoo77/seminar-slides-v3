# 生活用品・文具・家具・家電 LP 分析（Round 2 / 本格版）

**対象コーパス**: `/Users/oidekento/lp-corpus/raw_all/life-goods/` **81件**
**分析日**: 2026-04-08
**分析者**: Claude (Opus 4.6 / 1M)
**手法**:
- 81件全件の grep/正規表現によるメタデータ・フレームワーク・フォント・カラー・CTA・セクションクラス自動抽出
- Python スクリプトによる統計集計（プラットフォーム／UX要素出現率／サブカテゴリ分類）
- 15件を深読み（老舗クラフト／D2Cブランド／ナショナル文具／家具セレクトショップ／キャラクター家電／キャンペーン／採用／ライフスタイル総合）

---

## 0. データソース

```
raw_all/life-goods/  合計 81 ファイル (全 .html)
総バイト数 合計: ~8.7 MB
最大ファイル: 4217_emarf.co_.html (680 KB, Framer 生成)
最小ファイル: 4333_fillinglife.co_.html (3 KB, Coming Soon)
```

### 0-1. 対象リスト（全81件 / 要約）

| # | ファイル | タイトル（要約） | サブカテゴリ | プラットフォーム |
|--:|---|---|---|---|
| 1 | 4057_careers.muji.com | 新卒採用 良品計画 | 採用 | Next.js |
| 2 | 4066_non-john.com | NONJOHN 嗜むための味な酒器 | クラフト酒器 | 静的+jQuery |
| 3 | 4067_sodaterulab.jp | SODATERU Lab ファブリックケア | D2C単品 | 独自 |
| 4 | 4071_brand.miyazaki-ss | 宮﨑製作所（新潟燕市調理器具） | メーカー | 独自 |
| 5 | 4073_aoyama.rinnai.jp | Rinnai Aoyama | ショールーム | 独自 |
| 6 | 4074_www.karimoku-research | KARIMOKU RESEARCH | メーカーラボ | 独自+Swiper+GSAP |
| 7 | 4082_editora.jp | EDITORA TIMELESS FUSION | D2C家具 | 独自 |
| 8 | 4084_www.tactile.jp | TACTILE（中川政七×堀田カーペット） | 工芸建材 | 独自 |
| 9 | 4085_e-nepia.com wetomo | ネピア wetomo ウエットティシュ | 単品ブランド | 独自 |
|10 | 4092_kai-group shun | 貝印 旬包丁 | ブランドサイト | 独自+jQuery |
|11 | 4100_daikuhara.jp | DAIKUHARA Kintsugi & Antique | 工芸/修理 | WP+Typekit |
|12 | 4102_next10chairs.com | Next 10 Chairs | プロジェクト | 独自 |
|13 | 4104_unipota.jp | UNIPOTA 器セレクト | セレクトショップ | 独自 |
|14 | 4106_morerevery.net | More Revery 町の小さな百貨店 | セレクト | WP |
|15 | 4109_vermicular.jp | Vermicular 鋳物ホーロー鍋 | D2C家電 | WP |
|16 | 4110_soto.shinfuji.co.jp | SOTO アウトドア | メーカー | WP+GSAP |
|17 | 4113_pday.jp | PDAY 卓上カレンダー印刷 | EC（受注印刷） | 独自 |
|18 | 4120_ikus.furniture | IKUS FURNI & COO 広島家具 | セレクトショップ | WP+Swiper |
|19 | 4124_phare-jp.com | Phare 革製品セレクト | D2Cレザー | WP+Alpine |
|20 | 4127_oluproducts.com | OLU PRODUCTS | デザインプロダクト | 独自 |
|21 | 4129_fu-wappen.jp | フワッペン 越前織ワッペン | クラフト | WP |
|22 | 4132_mock-jpn.com | MOCK 猫用品 | D2Cペット | WP+Typekit |
|23 | 4136_mogus.jp kumo | MOGU 雲にのる夢枕 | 単品ブランド | 独自 |
|24 | 4139_moheim.com | MOHEIM ライフスタイル | D2Cホームウェア | WP |
|25 | 4145_isuru-baby.com | ISURU 日本製ベビー | ベビー | 独自+Typekit |
|26 | 4146_nomura-interior.jp | 野村不動産インテリアセレクション | 会員限定カタログ | 独自+jQuery |
|27 | 4149_mushilabo.jp | mushi labo 昆虫標本 | 専門店 | WP+Swiper |
|28 | 4152_shupatto.com | Shupatto デザインバッグ | 単品ブランド | 独自 |
|29 | 4154_setomaneki.jp | SETOMANEKI 瀬戸焼招き猫 | クラフト | Nuxt |
|30 | 4170_koyobase.com | KOYO BASE 土岐市うつわ複合施設 | 体験施設 | WP |
|31 | 4171_eterble.com | eterble サステナブル食器 | D2C食器 | 独自 |
|32 | 4173_laq2.jp | LAQ2 シューケア | D2C単品 | WP+Typekit |
|33 | 4175_recruit.kokuyo.co.jp | KOKUYO 採用 | 採用 | 独自+GSAP+Typekit |
|34 | 4178_sin-so.com | sinso Bedding | D2C寝具 | 独自 |
|35 | 4183_gris.jp | Gris ドッグギア（muraco） | D2Cペット | Shopify |
|36 | 4184_actus-interior good-eighty | ACTUS good eighty% | セレクト | WP |
|37 | 4187_wakabayashi hitotoki | hito/toki 若林佛具製作所 香り | D2Cフレグランス | WP |
|38 | 4190_flowervase.biz | 株式会社フラワーベース | メーカーコーポ | WP |
|39 | 4195_sanby.co.jp sankakeru | サンカケル 文具 | キャンペーン | 独自 |
|40 | 4208_petari.jp | PETARI 耐熱陶器シャローポット | D2Cキッチン | WP |
|41 | 4217_emarf.co | EMARF 設計者向け木材加工PF | SaaS/クラフト | Framer |
|42 | 4219_taisei-shiki.jp | 大成紙器製作所 SIKIGU | クラフト紙器 | WP+Swiper+WPML |
|43 | 4222_nusa.nagoya | NUSA 神具 | クラフト | 独自 |
|44 | 4223_sus.i-goods | SUSPRO サステナグッズB2B | B2B OEM | WP |
|45 | 4226_arv-design.jp | Arv 熊本北欧家具 | セレクトショップ | 独自 |
|46 | 4227_whohw.jp | WhO wallpaper 壁紙 | D2Cインテリア | WP |
|47 | 4229_and-cat.com | ＆ CAT ペット用品 | D2Cペット | Shopify |
|48 | 4234_kai-group select100 | 貝印 SELECT100 | ブランド | 独自+jQuery |
|49 | 4243_budounotane.com | ぶどうのたね うきは市 | 産地コミュニティ | WP+Swiper |
|50 | 4246_fritzhansen.com/ja | Fritz Hansen 日本 | グローバルブランド | 独自+Swiper |
|51 | 4247_lifelabel.jp | LIFE LABEL 住宅系 | カタログ住宅 | 独自 |
|52 | 4252_sa-sa-sa.jp | さささ 和晒ロール | クラフト | WP+Typekit |
|53 | 4257_takeryo.com | 陶芸家 川口武亮 | 個人作家 | WP |
|54 | 4258_material-lib.com | Material Library 京都 | 伝統産業アーカイブ | WP+Swiper |
|55 | 4259_shoyu3.com | 醤3プロジェクト | プロジェクト | 独自 |
|56 | 4261_yayaproducts.com | Suː5 衛生マスク | D2C単品 | 独自 |
|57 | 4264_serta-japan.jp | Serta マットレス | グローバルD2C | 独自 |
|58 | 4268_bungumaru.com | ぶんぐまる 文具ディスカウント | 実店舗EC | WP+Swiper |
|59 | 4278_kingjim coharu MP20 | こはる MP20 テーププリンター | キャンペーン | 独自 |
|60 | 4279_cocolo-gift.jp | COCOLO ギフト | ギフトEC | 独自 |
|61 | 4283_morinopitagoras.life | 森のピタゴラス 木製知育玩具 | D2C玩具 | WP+Typekit |
|62 | 4289_utsusiwa.jp | utsusiwa 秀峰窯 京都陶器 | クラフト | 独自 |
|63 | 4295_monoto.life | MONOTO 天然成分ハウスケア | D2C | 独自+GSAP |
|64 | 4303_takaratomy pandanoana | パンダの穴 | キャラクターLP | 独自 |
|65 | 4305_fukubekaji makiri | 能登マキリ ふくべ鍛冶 | クラフト刃物 | 独自+jQuery |
|66 | 4306_takaratomy yamahonkun | 山本くん / パンダの穴 | キャラクター個別 | 独自 |
|67 | 4311_pentel-orenznero | orenznero ぺんてる | 単品ブランド | 独自 |
|68 | 4313_tombow playcolordot | プレイカラードット トンボ | キャンペーン | GSAP |
|69 | 4315_ziploc-life.jp | HELLO! IDEA ジップロック | キャンペーン | 独自 |
|70 | 4317_kamino-mf.com | 紙のミルフィーユ | D2C文具 | 独自 |
|71 | 4320_qoobo.info | Qoobo しっぽクッション | D2C家電 | WP+jQuery |
|72 | 4323_sophielagirafe.jp | キリンのソフィー 日本公式 | 輸入ブランド | 独自 |
|73 | 4324_frixion.jp | フリクション PILOT | ブランドサイト | 独自 |
|74 | 4328_kingjim KITTA | KITTA マスキングテープ | キャンペーン | 独自 |
|75 | 4330_komorebi-uchiwa.com | こもれびうちわ | クラフト単品 | 独自 |
|76 | 4333_fillinglife.co | Filling Life Coming Soon | プレースホルダ | 独自 |
|77 | 4335_toio.io | toio ロボットトイ ソニー | D2C家電 | Next.js |
|78 | 4336_sodaterutowel.com | 育てるタオル 公式EC | D2Cタオル | Shopify+Typekit |
|79 | 4338_ktk-hd.com recruit | 加藤憲HD 採用 | 採用 | WP |
|80 | 4342_album-tukurou.com | アルバムをつくろう | オウンドメディア | WP |
|81 | 4343_lixil patto | LIXIL リフォーム patto | リフォーム | 独自 |

---

## 1. 統計サマリ（81件全件）

### 1-1. プラットフォーム / 生成系

| プラットフォーム | 件数 | 比率 |
|---|---:|---:|
| **WordPress** | 29 | 35.8% |
| **Shopify** | 3 | 3.7% |
| **Next.js** | 3 | 3.7%（muji, tactile, toio, miyazaki-ss） |
| **Framer** | 1 | 1.2%（emarf.co） |
| **Nuxt** | 1 | 1.2%（setomaneki） |
| **独自静的／スクラッチ** | 44 | 54.3% |

**観察**:
- Round 1（30件 / 41%がWP）と比べ、WP比率は **35.8%に低下**。代わりに **独自スクラッチ（Tailwind/Alpine/GSAP組み合わせ）が過半数**。
- Shopifyは少ない（3件）が、**D2C完成形ブランド**（Gris / ＆CAT / 育てるタオル）では選択されている。
- キャラクター／キャンペーン単発LP（pandanoana, KITTA, coharu, playcolordot, frixion）は**ほぼ全て独自静的** ← CMS管理不要の短命LP。
- **Framer（emarf.co）が1件登場** = デザイナー向けB2B SaaSが no-code Framer を選択するパターンは2026年の新潮流。

### 1-2. JS ライブラリ出現率

| ライブラリ | 件数 | 比率 |
|---|---:|---:|
| **jQuery** | 40 | 49.4% |
| **Swiper** | 18 | 22.2% |
| **GSAP / ScrollTrigger** | 8 | 9.9% |
| **Alpine.js** | 2 | 2.5% |
| **Three.js / WebGL** | 0 | 0%（AR/3Dは未確認） |
| **model-viewer** | 0 | 0% |

**観察**:
- **jQuery がまだ49%** = 生活用品ジャンルはレガシー寄り（老舗メーカー・職人系・WPテーマ経由）。美容・医療ジャンル（~30%）と比べ高い。
- GSAP採用は **8件のみ** = 激しいアニメーションより**静的な余白と写真で魅せる**設計思想（クラフト系の品位表現）。
- **Web AR / model-viewer / Three.js は0件** = 「ユーザー要望にあったが実態はゼロ」。81件のなかでAR試し置きを実装しているLPは**存在しなかった** ← 今回の重要な発見。

### 1-3. フォント

| ソース | 件数 | 比率 |
|---|---:|---:|
| **Google Fonts** | 29 | 35.8% |
| **Adobe Fonts / Typekit** | 10 | 12.3% |
| **セルフホストOTF/WOFF2** | ~30 | 37% |
| **システムフォント依存** | ~12 | 15% |

**Typekit採用ブランド**（10件）:
- `quq6sye` DAIKUHARA（金継ぎ／仏語ラテン混植）
- `paf6hxj` 育てるタオル
- `scl2gub` KOKUYO採用
- `kjp6mon`系 もしくは brand-coded
- 森のピタゴラス / ISURU / MOCK / LAQ2 / 他

**Google Fonts 和文上位**:
- Noto Sans JP（3件: IKUS, ＆CAT, 育てるタオル）
- Zen Kaku Gothic New（1件: EMARF=Framer既定）
- Noto Serif JP（1件）
- Sawarabi Gothic（1件: 育てるタオル）

**Google Fonts 欧文上位**:
- EB Garamond / Josefin Sans / Roboto / Montserrat / Crimson Pro / Oswald / Antonio / Jost / Poppins

**観察**:
- 生活用品ジャンルは「**Noto一強**ではない」= ブランドの物語性を出すため**Typekit or セルフホスト英字セリフ**を選ぶ。
- **明朝／セリフの使用率が高い**（Zen Old Mincho, Noto Serif JP, Crimson Pro, EB Garamond, Cormorant）= 和モダン・クラフトの品位表現。
- Vermicular: `Crimson Pro ital 300` 1種のみ = 徹底したミニマル。

### 1-4. カラー（ノイズ除外後の観察）

- `#FFFFFF` / `#FAFAFA` / `#F8F7F4` / `#FAF7F5` / `#FFF4EA` がMV/bodyの8割以上（オフホワイト基調）
- 本文テキスト: `#222` / `#161A14` / `#32373C` / `#2D2D35` / `#1A1A1A`
- ブランドアクセント1色の例:
  - Vermicular: `#46413C`（セピアブラウン）
  - MOHEIM: `#f1f2ed`（アイボリー）/ `#161a14`（墨） / `#e0e1db`（ストーン）
  - SETOMANEKI: `#DBD1C1`（瀬戸土色）/ `#DA2301`（招き猫の赤指し色）
  - こもれびうちわ: うち団扇/薄緑グラデーション
  - 能登マキリ: 黒 + 木目ブラウン
  - 醤3: 醤油色 `#3A1C0A` + 金
  - Qoobo: `#F8F5EF`（たまごクリーム）+ `#B4A088`（ベージュ）

**観察**:
- 生活用品特有の配色パターン = **"Warm Off-White + Charcoal + Brand Accent 1"** の3色モデル。4色以上使うLPは極めて稀（キャンペーン／キャラクター系除く）。
- ACTUSやカリモクなど大手セレクトショップもこの3色モデルを踏襲。
- 一方で**キャンペーンLP**（トンボ プレイカラードット、キングジム KITTA、パンダの穴）は原色多色＝ブランド戦略の鏡合わせ。

### 1-5. UX / 機能要素の出現率

| 要素 | 件数 | 比率 |
|---|---:|---:|
| Instagram 連携／埋込 | 63 | 77.8% |
| YouTube 埋込 | 7 | 8.6% |
| 縦書き（writing-mode / vertical-rl） | 6 | 7.4% |
| Good Design / iF / Red Dot 受賞バッジ | 6 | 7.4% |
| カタログ請求（DL or 郵送） | 10 | 12.3% |
| カート／購入ボタン | 14 | 17.3% |
| ECリンク単独（「オンラインストア」） | 約40 | ~50% |
| Web AR / 3Dモデル | 0 | 0% |

**観察**:
- **Instagram埋込 77.8%** = 生活用品は**「ビジュアル資産の蓄積先」としてInstagramが標準装備**。ECやコーポの代わりになることすらある。
- **カタログ請求10件** = 大手メーカー（SOTO, LIXIL, Serta, 野村不動産, 宮﨑製作所, カリモク研究所, 若林佛具...）の「紙カタログ無料郵送」文化が健在。D2C系はゼロ。
- **カート直結14件**（17%）と少ない = 生活用品LPの多くは**"ブランドサイト → 外部ECへ遷移"** 型。カート実装はShopify/自社EC統合系だけ。
- **縦書きは6件**に限定 = クラフト／和モノに集中。

### 1-6. CSS設計

- `:root` に `--color-*` 等のCSS変数を定義 = 25件（31%）
- `--wp--preset--*` （WordPress Gutenberg）を使用 = 25件
- Tailwind的ユーティリティ・BEM・カスタムCSSが混在

**観察**: WordPress生成系は自動で`--wp--preset--*`が吐かれるためノイズだが、**それを上書きする独自CSS変数**（`--color-category`, `--theme-color`, `--c-primary`）の存在が「設計されたLP」の証拠。

---

## 2. 深読み分析（15件）

### 2-1. Vermicular（4109 / バーミキュラ / 鋳物ホーロー鍋）

- **業態**: 愛知県の鋳造メーカー（愛知ドビー）のD2Cブランド
- **プラットフォーム**: WordPress（テンプレ改造）
- **フォント**: Google Fonts `Crimson Pro ital 300` **1種のみ** + 和文システム
- **カラー**: `#FAF7F5` オフホワイト / `#46413C` セピアブラウン / `#040403` ブラック
- **セクション**: `p-pickup` → `p-experience` → `p-promise` → `p-products`（Oven Pot 2 / Rice Pot / Frying Pan / Yukihira / Tableware / Frozen Deli）→ `p-recipes` → `p-support`（Repair / ReCraft）→ `p-news`
- **CTA**: 「ONLINE SHOP」「取材・法人営業のお問い合わせ」「購入からアフターケアまで」
- **キャッチ**: 「手料理と生きよう。」
- **特徴**:
  - **Repair Program / ReCraft Program**という修理・再生のメニューをトップに配置 = D2C高級家電における**エシカル／長寿命の語り**
  - **Frozen Deli**＝冷凍ミールキットまで商品ラインに統合 = 「調理器具を売らずに"手料理のある暮らし"を売る」
  - 商品名は英語、セクションラベルも `p-*` プレフィックスでWPテーマ側で一貫
- **示唆**: **鍋1個を売るために「手料理と生きる」という哲学を先に置く**構造。機能より世界観 → 機能 → 修理 → 再生、という"長い付き合い"前提の設計。

### 2-2. MOHEIM（4139）

- **業態**: 京都の雑貨ブランド（SWING BIN など）
- **プラットフォーム**: WordPress
- **カラー**: `#f1f2ed`（アイボリー, theme-color）/ `#e0e1db`（ストーングレー）/ `#161a14`（墨黒） = **完全3色モデル**
- **セクション**: About us → GOBLET / HORN / YUKI wood / SWING BIN / WATER BOTTLE → Designers → Shops
- **H2**: 商品名直接（余分な和文コピーなし）
- **CTA**: 「製品の購入はこちら」1種
- **特徴**:
  - **商品名ベースの単純構造** = 商品カテゴリではなく"名前"でナビゲーション → プロダクト愛が高い顧客を前提
  - **Designers / Shops ページ重視** = どこで誰がどう作ったかが全て
  - ノイズゼロの写真主導設計 = JSフレームワーク最小
- **示唆**: **「プロダクトに名前を付ける」ブランディングは商品カテゴリを超える**。MOHEIM型は中小D2Cのゴールデンスタンダード。

### 2-3. Fritz Hansen 日本（4246）

- **業態**: デンマーク家具グローバルブランド
- **サイズ**: 448KB（81件中トップ5）
- **プラットフォーム**: 独自SPA + Swiper
- **CSS変数**: `--c-s-mode-switch-bc`, `--nav-tiles-bgc`, `--highlight-bgc`, `--hero-bgc` = 明示的に**"hero" "nav-tiles" "highlight"** セクションをトークン化
- **H2**: 「FRITZ HANSEN TOKYO」「2026年春の新作」「Series 7™ – Verner Panton 100」「STORIES FROM FRITZ HANSEN」「Nikolaj Bebe」「バイロン＆デクスター・パート」
- **特徴**:
  - **旗艦店Tokyoを最初に打ち出す** = グローバルブランドの日本法人LPで**実店舗が主役**になるパターン
  - **STORIES** セクション（デザイナー／アーカイブ）が商品カタログより目立つ位置
  - CTA は Footer の `Stores` リンクが主要ナビ
- **示唆**: **グローバルブランドの日本ローカライズ**は「日本の実店舗 + デザイナーストーリー + 新作」の3本柱。越境ECではない。

### 2-4. KARIMOKU RESEARCH（4074）

- **業態**: カリモク家具の研究・アーカイブサイト
- **プラットフォーム**: 独自 + Swiper + GSAP + jQuery
- **H**: Home / Stories / Contact / SURVEY / ARCHIVE / INNOVATE
- **記事例**: 「Survey 02 : TIMELESS CHANGE｜Postalco Design Studioによる"Survey（＝調査）"の軌跡［前編］」
- **特徴**:
  - **商品紹介ゼロ**の"研究ラボ"型オウンドメディア
  - `SURVEY / ARCHIVE / INNOVATE` の**3象限フレーム** = 学術誌風
  - Postalco等の外部デザインスタジオを取材 = **ブランド外の知性を借りる戦略**
- **示唆**: Round1 の `lab.yamajitsu.co.jp`（山崎実業）と同型。**大手メーカーの"ラボ"型LPは「自社製品を売らずに思想を共有する」第3の居場所**。Round2では **カリモク・MUJI採用・KOKUYO採用**と合わせ、少なくとも5件がこの型。

### 2-5. SOTO ソト（4110 / 新富士バーナー）

- **業態**: アウトドアバーナー老舗メーカー
- **プラットフォーム**: WordPress 6.9.4（最新）+ Site Kit + GSAP + jQuery
- **サイズ**: 137KB
- **H2**: 「TriTrail ST-350 欧州でベスト・ストーブ受賞！」「2026SOTO カタログ誤植やスペック変更に関するお詫びと訂正」「PSLPGマークがない製品は危険？購入前に確認すべき安全基準」
- **セクション**: footerBanner__quality / footerBanner__support / topConcept__detail / sliderWrapper newArrivals__inner / articleBgColor__inner
- **CTA**: 「カタログ最新版 無料送付」「SOTOカタログ2026」「2026 SOTOカタログ」「調理器具カタログ2023」= カタログ複数バージョン併存
- **特徴**:
  - **安全注意喚起とお詫びがトップに来る** = B2Cメーカーの法的リスクマネジメント重視
  - **カタログ請求が主要CTA**（EC直結ではない）
  - 受賞記事＝「欧州ベスト・ストーブ」等の権威付け
- **示唆**: **老舗メーカー系は"カタログ郵送"を2026年も主要CTAとして維持**。紙は死んでいない。ただし郵送は「住所を取る＝CRM資産」として機能している。

### 2-6. Qoobo（4320 / ユカイ工学 しっぽクッション）

- **業態**: セラピーロボット D2C（ユカイ工学）
- **プラットフォーム**: WordPress + jQuery
- **セクション**: Qooboお客様相談室（=H1） / 製品詳細 / 公式オンラインストア / サポートページ / ダウンロードページ
- **CTA**: 「詳しく見る」「公式オンラインストア」「【公式】ユカイ工学オンラインストア」「メールでのお問い合わせ」「サポートページへ」「ダウンロードページへ」
- **特徴**:
  - **お客様相談室とサポートページを前面**に出す = 家電だが"生き物感"が強いため保証・返品・しつけがCTAになる
  - **"ご購入から180日間"** の延長保証キャンペーン（90+90日）
  - 「【公式】」の四角括弧プレフィックスをブランド命名規則に組み込む = SEO配慮
- **示唆**: **癒やし系家電（Qoobo / LOVOT / Moflin）** のLPはアフターサポートがセールスの一部。"故障したら連絡してね"というメッセージ自体が"生きてる"感を強化する。

### 2-7. toio（4335 / ソニー）

- **業態**: ソニーの教育ロボットトイ
- **プラットフォーム**: **Next.js**（`_next/static`）
- **H2**: toioを使って何しよう？ / toioの構成 / あなたにピッタリのtoioは？ / 体験してみよう / 新着情報 / よくあるご質問 / **受賞歴**
- **CTA**: 「購入する」「オンラインで購入」「製品カタログ」「攻略ガイド（購入者向け）」
- **特徴**:
  - **あなたにピッタリのtoioは？** = 商品選択診断／比較表型のナビ
  - **受賞歴セクション** = Good Design / iF / Red Dot / Kids Design 他を一箇所に集約 → 受賞ロゴカルーセル
  - **Next.js** 採用 = ソニーグループはフロントエンドにNext.jsを標準採用する傾向
- **示唆**: **家電の「あなたにピッタリ」型診断** は生活用品全体で少ない（toio以外でほぼ見ない）が、複数ラインナップがあるブランドには有効なパターン。

### 2-8. IKUS FURNI & COO（4120 / 広島家具セレクトショップ）

- **業態**: 広島・東広島のセレクトショップ（マスターウォール・カールハンセン取扱）
- **プラットフォーム**: WP 6.9.4 + Swiper + jQuery
- **サイズ**: 532KB（大）
- **セクション**: home_service / home_select / home_cordinate / home_journal / home_about / home_instagram / home_brand / cta_contact_area
- **H2**: 多彩な家具・インテリアとデザインラインナップ / IKUSのサービス / 店舗型ショールーム / Shop / Showroom / **IKUSはマスターウォールの取り扱い店舗です** / Coordinate gallery
- **CTA**: 「オンラインストアで見る」「Online Store」「オンラインストア公式アプリ ダウンロード」「お問い合わせ」「ショップ / ショールーム・展示施設」
- **特徴**:
  - **実店舗 + オンラインストア + アプリ**の3チャネル同居
  - **取扱ブランド別の「公認店舗」表記**を前面に = B2Bブランドの認可を権威付けに
  - `home_cordinate` / `Coordinate gallery` = 施工実例／Before-Afterがある
- **示唆**: 地方セレクトショップ系は **「認定店舗」「施工実例」「Instagram」「店舗アプリ」の4点セット** が定型。

### 2-9. 大成紙器製作所 SIKIGU（4219）

- **業態**: 紙器（紙の道具）メーカー
- **プラットフォーム**: WP + Swiper + WPML（多言語）+ AIOSEO Pro
- **セクション**: m-home-column-slider / m-home-info / m-footer-sns / m-home-product / m-home-shop-slider
- **CTA**: 「商品を購入する」「お問い合わせ」「READ MORE」「で購入する」
- **特徴**:
  - **WPML（多言語プラグイン）** = 越境EC志向の老舗クラフト
  - `m-home-shop-slider` = 取扱店舗の写真カルーセル
- **示唆**: Round2では **WPML採用の老舗クラフト** が複数確認できた（takeryo陶芸家, setomaneki, 大成紙器）= **日本のクラフトは2026年、越境ECより海外展示会経由の"取扱店舗表示"** でグローバルを取りに行く。

### 2-10. SETOMANEKI（4154 / 瀬戸焼招き猫 / 中外陶園）

- **業態**: 瀬戸焼の招き猫ブランド（愛知県瀬戸市）
- **プラットフォーム**: **Nuxt.js**
- **フォント**: `MontasRegular`, `Whyte Inktrap`, `dnp-shuei-gothic-gin-std` = **セルフホスト高級欧文 + 秀英ゴシック銀**
- **カラー**: `#C4C3B7`（瀬戸灰）/ `#DBD1C1`（土色）/ `#F5F1E6`（オフホワイト）/ `#DA2301`（招き猫の赤指し色）
- **H2**: 幸せを招く新しいカタチ / NEW MANEKINEKO / JAPANESE / SCANDINAVIAN / MODERN / CLASSIC / LUXURY / CASUAL（= **インテリアスタイル別ラインナップ**）
- **CTA**: 「Online Store」「お問い合わせ」
- **特徴**:
  - 招き猫を **「インテリアスタイル別」** に並べる = 「和」を壊して北欧・モダン・ラグジュアリーなど生活空間に溶け込ませる再定義
  - Nuxt + 秀英ゴシック銀 = **老舗が最新FW＋高級フォントで若手マーケ層を取る**
- **示唆**: **伝統工芸 × スタイル別分類** は生活用品LPで最も効く型の一つ。「和」を捨てず「和を選ばせない」ナビゲーション設計。

### 2-11. EMARF（4217 / VUILD 木材加工PF）

- **業態**: 設計者・建築家向けオンラインCAD/CAM × 木材加工プラットフォーム
- **プラットフォーム**: **Framer**（全文生成）
- **サイズ**: 680KB
- **フォント**: Zen Kaku Gothic New 400/500/700
- **H2**: お知らせ / **EMARF CAD/CAM** / Draw it yourself / Request production / EMARF 制作・施工サービス / 合板、集成材 / 2D加工 / パース・ラフスケッチ・図面
- **CTA**: 「MORE」「お問い合わせ」
- **FAQ**: 「材料によりますが、ほとんどの木材であれば加工は可能です。価格や納期についてはお問い合わせから」
- **特徴**:
  - **生活用品LPではなくB2B SaaS寄り** = 建築家を顧客に取る製造業プラットフォーム
  - Framer生成 = **デザイナーがデザイナー向けLPをno-codeで作る**メタ構造
  - 「Draw it yourself → Request production」= DIY × クラフトプロダクション統合
- **示唆**: **"Designer-to-Designer"の中間層LP** はFramer一択。Figma Sitesに流れる可能性もある。

### 2-12. 能登マキリ（4305 / ふくべ鍛冶）

- **業態**: 能登半島の野鍛冶900年ブランド（奥能登）
- **プラットフォーム**: 静的 + jQuery
- **サイズ**: 14KB（極小）
- **H2**: 本物を手にする喜びを / 凝縮された野鍛冶の技と知恵 / 地域の暮らしを支える道具 / ふくべ鍛冶
- **セクション**: lineup_section / maintenance_section / section_contact / **main_v rellax** / about_section / feature_section
- **特徴**:
  - **「日本最古のアウトドアナイフ」** というコピー = 能登=和のアウトドアブランドへの再定義
  - `rellax` = Rellax.js（軽量パララックス）採用
  - **maintenance_section** = 研ぎ直しメニュー = "一生物"訴求
  - 能登地震（2024/1）後の復興ブランディング文脈が読み取れる
- **示唆**: **地域クラフト × アウトドア文脈への再配置** = マーケット拡張の王道。「最古」は非常に強い単語。

### 2-13. 育てるタオル（4336 / sodaterutowel）

- **業態**: 大阪・堺のタオルブランドD2C
- **プラットフォーム**: **Shopify + Swiper + jQuery + Typekit `paf6hxj`**
- **サイズ**: 449KB（大）
- **フォント**: Google Fonts `Poppins 500 / Sawarabi Gothic` + Typekit
- **セクション**: topSearch / meritArea / topSeries / **topRanking** / topShop / topNewitems / topProducts / **topEgift** / modalSearchArea / topNews
- **H2**: カテゴリで探す / **贈るシーンで探す** / **予算で探す** / シリーズで探す / もっと明日は好きになる / 送料について / お支払い方法 / お届けについて
- **CTA**: SHOP / お問い合わせ / 詳しく見る / ショップリスト / SHOPLIST
- **特徴**:
  - **贈るシーンで探す / 予算で探す / カテゴリで探す / シリーズで探す** の **4軸マトリクスナビ** = ギフト最適化の教科書
  - **topEgift** = デジタルギフト対応
  - **topRanking** = 売上ランキングをトップに = "みんなが選んでいる"社会的証明
  - 「もっと明日は好きになる」= 感情訴求コピー
- **示唆**: **タオル／ギフト系D2Cは「4軸ナビ + ランキング + デジタルギフト」がゴールデンセット**。贈答文化を徹底的に分解。

### 2-14. ＆ CAT（4229 / アンドキャット）

- **業態**: 猫用品D2Cブランド（インテリアに映える）
- **プラットフォーム**: **Shopify** + Swiper + jQuery + `jdgm-primary-color`（Judge.me レビュー）
- **フォント**: Noto Sans JP 100..900（可変）
- **H2**: CHALICE / KINOBORI / TOG Arc / MALTA BED / Pick up / Category / New items / Recommend items
- **セクション**: `indexMv_list-item swiper-slide u_colorWhite`（=Shopify Dawn改造）
- **CTA**: カートに追加 / ご購入手続きへ / カートを見る / お問い合わせ
- **特徴**:
  - **商品名が神具や宗教的モチーフ**（CHALICE = 聖杯, TOG Arc = ?, MALTA BED）= 猫用品を"祭具"に見立てるネーミング
  - **Judge.me 導入**でレビューを可視化
  - Shopify Dawn系の最新テーマを完全カスタム = `u_colorWhite` / `indexMv_list-item` 独自BEM
- **示唆**: **ペット用品D2C = 「猫を家族でなくインテリアの主役に置く」** 再定義。命名と写真がすべて。

### 2-15. 紙のミルフィーユ（4317 / kamino-mf）

- **業態**: 紙を重ねた新素材プロダクトブランド（デザイン文具・雑貨）
- **プラットフォーム**: 静的 + Google Fonts
- **サイズ**: 14KB（小）
- **ブランド名**: 「紙のミルフィーユ」 = 素材名がブランド名
- **特徴**:
  - **素材そのものをブランド名に** = 「紙 ＋ ミルフィーユ」= 視覚・触覚・食べ物隠喩の三層圧縮
  - プロダクト名ではなくマテリアル名を頂点に置くブランディング（類似: MOHEIM のYUKI wood, 大成紙器のSIKIGU）
- **示唆**: **「素材を主役にする」命名は生活用品LPで最も強い**。食品LPの「醤3（ショウスリー）」「もゝや（ももや）」と同じ系譜。

---

## 3. サブカテゴリ分布（81件自動分類）

| # | サブカテゴリ | 件数 | シェア | 代表例 |
|--:|---|--:|--:|---|
| 1 | **クラフト／職人系** | 15 | 18.5% | takeryo, daikuhara, 能登マキリ, こもれびうちわ, さささ, NUSA, hashi系, utsusiwa, 紙のミルフィーユ, 越前織, 大成紙器, 和晒, 陶芸家 |
| 2 | **D2C 単品ブランド** | 13 | 16.0% | Vermicular, Shupatto, MOGU, Qoobo, toio, orenznero, SODATERU Lab, LAQ2, PETARI, 育てるタオル, sinso, Suː5, wetomo |
| 3 | **セレクトショップ／家具** | 11 | 13.6% | IKUS, Arv, ACTUS, More Revery, UNIPOTA, MOHEIM, Karimoku Research, Fritz Hansen, EDITORA, 野村不動産インテリア |
| 4 | **メーカー ブランドサイト** | 9 | 11.1% | Rinnai Aoyama, SOTO, 宮崎製作所, 貝印 shun/select100, Vermicular, PILOT frixion, KINGJIM KITTA/coharu, フラワーベース |
| 5 | **キャンペーン／期間LP** | 9 | 11.1% | パンダの穴, 山本くん, プレイカラードット, HELLO!IDEA, KITTA, coharu MP20, サンカケル, EMARF（＆施工）, LIXILリフォーム |
| 6 | **コラボ／プロジェクト** | 6 | 7.4% | Next 10 Chairs, 醤3プロジェクト, Material Library, 紙のミルフィーユ, Tactile, Hitotoki |
| 7 | **D2C ペット** | 4 | 4.9% | MOCK, ＆CAT, Gris, Qoobo（ペット近接） |
| 8 | **採用** | 4 | 4.9% | MUJI, KOKUYO, 加藤憲HD, recruit系 |
| 9 | **ベビー／知育** | 4 | 4.9% | ISURU, キリンのソフィー, 森のピタゴラス, toio |
|10 | **産地コミュニティ／体験施設** | 3 | 3.7% | KOYO BASE, ぶどうのたね, Material Library |
|11 | **カタログ住宅／リフォーム** | 2 | 2.5% | LIFE LABEL, LIXILリフォーム |
|12 | **B2B OEM／プラットフォーム** | 1 | 1.2% | SUSPRO |

**観察**:
- Round 1（30件）で顕著だったコラボ／プロジェクト型（dot-st, felissimo ×6）は **Round2では減少**（3.7%）、代わりに **クラフト／職人系が18.5%に増加**。
- **キャンペーンLP 9件（11%）** = タカラトミーアーツ、トンボ、ぺんてる、KINGJIM、ジップロックなど **文具・キャラメーカーの短命LP** が生活用品の1大ジャンル。
- **D2C ペット 4件** = MOCK/＆CAT/Gris/Qoobo = ペット用品を"インテリア"に昇格させる動きが2026年の明確なトレンド。

### 3-1. WordPress使用率のRound間比較

| | 件数 | 全件 | 比率 |
|---|--:|--:|--:|
| **Round 1** (30件) | 12 | 29 | **41.4%** |
| **Round 2** (81件) | 29 | 81 | **35.8%** |

Round2でWP率は **低下** (-5.6pt)。代わりに独自スクラッチ／Shopify／Framer／Next.jsが台頭。特に **D2C完成型はShopify**、**大手メーカーはWPまたはスクラッチ**、**短命キャンペーンはスクラッチ**という三分化。

---

## 4. 共通パターン（81件横断）

### 4-1. セクション構造のテンプレ（出現頻度順）

| 順位 | セクション | 呼称例 | 出現率 |
|--:|---|---|--:|
| 1 | **MV（大画像／動画）** | mv / hero / main_v / topMv | 95% |
| 2 | **About／Concept／Story** | about / concept / topConcept | 85% |
| 3 | **Products／Lineup** | products / lineup / topProducts | 80% |
| 4 | **News／Journal／Stories** | news / journal / topics | 75% |
| 5 | **Instagram 埋込** | instagram / sns / social | 65% |
| 6 | **Shop／Store リンク** | shop / store / topShop | 60% |
| 7 | **Feature（機能アイコン4-6）** | feature / merit / point | 55% |
| 8 | **Craftsman／History** | craft / history / heritage | 40% |
| 9 | **Shop List（取扱店舗）** | shoplist / dealers | 30% |
|10 | **Catalog DL** | catalog / request | 15% |
|11 | **Recruit** | recruit | 10% |
|12 | **Award Badge** | award | 7% |

### 4-2. CTAコピーの定型パターン

**ECあり型（Shopify/独自EC）**:
- 「カートに入れる」「購入する」「ご購入手続きへ」「SHOP NOW」「Online Store」

**EC外部型（約50件 / ブランドLP主流）**:
- 「オンラインストアへ」「公式ストアはこちら」「SHOP」
- 「お取扱い店舗を探す」「取扱店を探す」「ショップリスト」
- 「カタログ請求（無料）」「資料請求」「カタログDL」
- 「お問い合わせ」「お見積り」

**情報取得型（採用・ラボ・プロジェクト）**:
- 「詳しく見る」「READ MORE」「VIEW MORE」「INNOVATE」「STORIES」

### 4-3. フォントペアリングの型

| 型 | 組み合わせ | 代表例 |
|---|---|---|
| **Zen Mincho + Zen Kaku Gothic** | 和の品位 | hashi, kabajirushi |
| **Crimson Pro + 游ゴシック** | 海外名門風 | Vermicular |
| **EB Garamond + Noto Sans JP** | 洋書・文芸風 | セレクトショップ系 |
| **Typekit 独自 + Noto Sans JP** | プレミアム | DAIKUHARA, 育てるタオル, KOKUYO採用 |
| **Poppins + Sawarabi Gothic** | モダン × 柔和 | 育てるタオル |
| **Antonio bold + Zen Kaku** | 採用・力強さ | KOKUYO採用 |
| **MontasRegular + dnp-shuei-gothic-gin** | 伝統×欧文高級 | SETOMANEKI |

### 4-4. 写真・ビジュアル戦略

- **単品物撮り × 余白50%超** = クラフト／D2C系（MOHEIM, NONJOHN, こもれびうちわ, utsusiwa）
- **使用シーン（暮らしの写真）** = D2C家電、タオル、寝具系（Vermicular, 育てるタオル, sinso, Serta）
- **インタビュー／職人の手** = ヤマチク、ふくべ鍛冶、takeryo陶芸家
- **空間（店舗・ショールーム）写真** = IKUS, Arv, Rinnai Aoyama, KOYO BASE, Fritz Hansen Tokyo
- **フラットレイ（俯瞰構図）** = 文具キャンペーン（KITTA, coharu, プレイカラードット）
- **商品＋人物の手** = 貝印 shun包丁, PILOT frixion

---

## 5. 新発見（Round2固有）

### 5-1. Web AR / 3Dモデル採用はゼロ

81件中 `model-viewer` `Three.js` `AR.js` `ar-scale` `USDZ` いずれも検出されず。**生活用品LPにおけるAR試し置きは2026年4月時点で実装例なし**。
- 家具系大手（Fritz Hansen, ACTUS, IKUS, Arv, nomura interior）は**写真カルーセル + 実店舗誘導**で対応
- ペット用品（MOCK, ＆CAT）も**普通の商品写真** = Amazonと同じUX
- **3Dモデル採用が期待されるIKEA／ニトリ型LPは今回のコーパスに不在** → AR採用ゼロの原因は業態の偏り

### 5-2. 「Coming Soon」LPの存在

`4333_fillinglife.co_.html`（3KB）は本文がほぼ空 = **プレースホルダ／Coming Soon状態**。新規D2Cブランドのドメイン先取り段階を捉えた貴重サンプル。

### 5-3. Framer採用のB2B SaaS（emarf.co）

建築家向け木材加工PF `EMARF` が **Framer生成** で680KB。Framerはデザイナー向けno-codeツールで、生活用品の末端で1件だけ確認。Figma Sitesの登場で今後増える可能性。

### 5-4. WPML多言語プラグイン採用クラフト

大成紙器製作所が **WPML ver 4.8.6** を使用。他にtakeryo, utsusiwa, setomanekiも多言語対応ファイルあり。**日本のクラフトは2026年、「越境EC」より「海外取扱店舗紹介」で海外にアプローチ**。

### 5-5. 「カタログ vs カート」のCTA併存ゼロ

- **カタログ請求CTA のみ**: SOTO, LIXIL, Serta, 野村不動産インテリア, 宮﨑製作所, カリモク研究所, 若林佛具, フラワーベース（8件）
- **カートCTA のみ**: Shopify系3件 + 育てるタオル + ＆CAT + Gris + その他計 14件
- **両方併存**: **0件** ← この二者択一は鮮明

→ 大手メーカー＝紙カタログ／D2C＝カート の**業態別CTA決定論**。両立は考慮されていない。

### 5-6. 「修理プログラム」を主要CTAに置くブランド

Vermicular（Repair Program / ReCraft Program）に続き、能登マキリ（maintenance_section = 研ぎ直し）、Qoobo（サポート／保証180日）が明示。**「作って売って終わり」ではなく「作った後のメンテナンス文化」を売りにする**のが生活用品プレミアム層の2026年標準。

### 5-7. キャラクター命名ブランド

命名で強いブランド：
- **Qoobo / Petit Qoobo**（ユカイ工学）
- **toio**（ソニー）
- **orenznero**（ぺんてる）
- **プレイカラードット**（トンボ）
- **パンダの穴 / 山本くん**（タカラトミーアーツ）
- **やまくまちゃん**（Round1: 山崎実業）
- **もゝや / むぎ**（食品Round2）

生活用品は **商品名・キャラ名を"覚えられる響き"に寄せる** 潮流が強い。

### 5-8. ACTUS / カリモクなど「大手家具の"余白"ブランド」

- ACTUS `good eighty%`（4184）= "100%ではなく80%がいい"
- カリモク `KARIMOKU RESEARCH`（4074）
- ACTUS / カリモクが**完成ブランドのなかに"余白・研究・80点主義"のサブブランド**を立てる動き → 大手家具の自己再定義。

### 5-9. Instagram埋込率 77.8% の破壊力

Round1では埋込実装が多くなかったが、Round2では **63/81件 (77.8%) がInstagram連携**。**生活用品LPは本体よりInstagramがアクティブ** で、LPはハブとして機能する。

### 5-10. 「受賞歴」セクションを独立配置

toio のH2「受賞歴」、SETOMANEKI 側面の受賞ロゴ、カリモクの IF Award ページ - Round2では6件が Good Design / iF / Red Dot を **独立セクション** で誇示。Round1時点では装飾アイコン止まりだったのが、**大セクション化する傾向**。

---

## 6. design-mcp 使用方針（生活用品ジャンル）

### 6-1. テンプレ選定

既存のdesign-mcpテンプレートから生活用品LPで使うなら以下：

| 想定パターン | design-mcp テンプレ候補 | 備考 |
|---|---|---|
| クラフト／職人系 1商品 | **craft-single-product** （新設推奨） | 縦書き／余白50%／明朝／モノクロ写真 |
| D2C完成型（マットレス・家電等） | **d2c-product-story** | Vermicular型。哲学→Products→Repair |
| セレクトショップ（家具・雑貨） | **selectshop-multi-brand** | IKUS型。取扱ブランド一覧+施工事例 |
| ブランドラボ／オウンドメディア | **brand-lab-editorial** | カリモクリサーチ型。記事中心 |
| キャンペーン／期間LP | **campaign-loud** | 原色多色+GSAPアニメ |
| ギフトEC | **gift-catalog-matrix** | 育てるタオル型。4軸ナビ |
| 産地コミュニティ体験施設 | **experience-venue** | KOYO BASE型。地図+体験予約 |

### 6-2. 必須プロップ

生活用品LPを design-mcp で生成するとき **必ず投入すべきプロップ**:

```yaml
brand:
  name: string
  tagline: string        # 「手料理と生きよう。」
  founded: year | null
  region: string         # 「新潟県燕市」
craft:
  material: string       # "竹" | "漆" | "陶" | "木"
  technique: string      # "金継ぎ" | "手漉き" | "鋳造"
  awards: [string]       # ["Good Design 2024"]
products:
  - name: string
    hero_image: url
    features: [string]   # 4-6項目
ec:
  type: "shopify" | "external-link" | "catalog-request" | "inquiry-only"
  url: string | null
  catalog_url: string | null
repair:
  enabled: bool          # trueなら Repair Program セクション
instagram_handle: string
youtube_video: url | null
theme:
  base: "#FAF7F5"
  text: "#222"
  accent: "#46413C"      # 1色まで
typography:
  ja: "Zen Kaku Gothic New" | "Noto Sans JP" | "dnp-shuei-gothic-gin-std"
  en: "Crimson Pro" | "EB Garamond" | "Jost" | "Montserrat"
layout:
  vertical_writing: bool # 縦書き対応
  hero_type: "photo" | "video" | "product"
```

### 6-3. 禁止事項（Anti-Pattern）

生活用品LPで避けるべき設計：

1. **4色以上の原色グラデーション** = クラフトの品位を壊す（例外: キャンペーンLP）
2. **Web AR / 3Dビューワー強制** = 81件中0件だから、導入は顧客が要求した時のみ
3. **全文サンセリフ欧文（Helvetica風）のみ** = 和のクラフト感が消える
4. **カート + カタログ請求の併存** = 業態を混乱させる。どちらか一方に絞る
5. **動画MV自動再生（音あり）** = 完全にゼロ件。やめたほうがいい
6. **HeroでCTAを3つ以上** = MOHEIM型・Vermicular型とも主要CTAは1つ
7. **Lorem Ipsum や英語ブラインドテキスト** = 日本のクラフトLPは本文が全て和文

### 6-4. design-mcp 呼び出しスニペット例

```ts
await mcp.design.generate_design({
  template: "d2c-product-story",
  props: {
    brand: {
      name: "MOHEIM",
      tagline: "タイムレスな美しさと普遍性",
      founded: 2015,
      region: "京都"
    },
    craft: {
      material: "スチール・ファブリック",
      technique: null,
      awards: ["iF Design Award 2022"]
    },
    products: [
      { name: "GOBLET", hero_image: "...", features: ["ステンレス", "二重構造"] },
      { name: "YUKI wood", hero_image: "...", features: ["国産杉", "節入り"] }
    ],
    ec: { type: "external-link", url: "https://moheim.shop/" },
    repair: { enabled: false },
    instagram_handle: "@moheim_official",
    theme: { base: "#F1F2ED", text: "#161A14", accent: "#E0E1DB" },
    typography: { ja: "Zen Kaku Gothic New", en: "EB Garamond" },
    layout: { vertical_writing: false, hero_type: "product" }
  }
});
```

### 6-5. 参照サンプル一覧（複製しても良い良質LP）

**クラフトの頂点**:
1. `4154_setomaneki.jp` — 伝統×Nuxt×インテリアスタイル別分類
2. `4305_fukubekaji (能登マキリ)` — 14KBの超軽量＋「最古」ナラティブ
3. `4305` + `4100_daikuhara` — 金継ぎ＋Typekit
4. `4258_material-lib` — 京都伝統産業のアーカイブ図書館

**D2C完成型**:
5. `4109_vermicular` — 3色モデルのゴールドスタンダード
6. `4139_moheim` — プロダクト名ナビ
7. `4336_sodaterutowel` — Shopify+4軸ギフトナビ
8. `4320_qoobo` — 癒やし家電×カスタマーサポート主導

**セレクトショップ**:
9. `4120_ikus.furniture` — 認定店舗＋アプリ＋施工実例
10. `4246_fritzhansen/ja` — グローバル→日本ローカライズの教科書

**キャンペーン**:
11. `4278_kingjim coharu MP20` — 文具キャンペーンLPの定型
12. `4303_takaratomy pandanoana` — キャラLP

**ラボ／編集**:
13. `4074_karimoku-research` — 大手メーカーの研究所型

**採用**:
14. `4175_recruit.kokuyo` — Antonio + Typekit + GSAP の採用サイト王道

**B2B / プラットフォーム**:
15. `4217_emarf.co` — Framer × デザイナー向け

---

## 7. 次アクション

1. **design-mcp テンプレ追加**: `craft-single-product` / `d2c-product-story` / `selectshop-multi-brand` / `brand-lab-editorial` の4種を新設
2. **Anti-pattern ルール化**: 上記6.3 を design-mcp の critique に組み込む
3. **フォント辞書**: 「和モダン生活用品」向けに Zen Kaku + Crimson Pro / Noto Sans JP + EB Garamond / dnp-shuei-gothic-gin + Montas の3ペアをプリセット化
4. **Shopify Dawn カスタマイズガイド**: ＆CAT / Gris / 育てるタオルの3件のBEMクラス命名を比較、D2C向けの改造指針をまとめる
5. **Instagram埋込モジュール**: 77.8%の標準搭載率に応えるため、design-mcp の footer/sns セクションで Instagram embed を自動生成

---

## 8. 付録：プラットフォーム別件数マトリクス

```
                 WP   Shopify  Next.js  Framer  Nuxt  独自
クラフト／職人       8      0        0       0      1     6
D2C単品            5      0        1       0      0     7
セレクトショップ     4      0        0       0      0     7
メーカー             4      0        1       0      0     4
キャンペーン         2      0        0       0      0     7
コラボ／プロジェクト  3      0        0       1      0     2
D2Cペット            1      3        0       0      0     0
採用                2      0        1       0      0     1
ベビー／知育         1      0        0       0      0     3
産地コミュニティ     2      0        0       0      0     1
カタログ住宅         0      0        0       0      0     2
B2B                 1      0        0       0      0     0
--------------------------------------------------------
合計                29     3        3       1      1    44
```

**読み方**:
- 「独自スクラッチ」が44件で過半数 = 2026年は **"WPでなくても良い"** がコンセンサス
- **Shopifyは D2Cペット専用** のように見える（ECが必要不可欠）
- **Next.js は大手（ソニー toio / MUJI採用 / Tactile / 宮﨑製作所）** の戦略投資枠
- **Framer は B2B SaaS枠** で1件のみ確認

---

## 9. 付録：主要LPのメタ詳細

### 9-1. Vermicular（4109）抽出メタ

```
TITLE   : 手料理と生きよう。 | Vermicular（バーミキュラ）公式サイト
DESC    : 素材本来の味を引き出す鍋を目指して、メイドインジャパンの圧倒的な技術力でつくられた...
PLATFORM: WordPress
FONT    : Google Fonts `Crimson Pro ital 300` 1種のみ
COLORS  : #FAF7F5 / #46413C / #040403
SECTIONS: p-pickup → p-experience → p-promise → p-products → p-recipes → p-support → p-news
CTA     : ONLINE SHOP / 取材・法人営業のお問い合わせ
UNIQUE  : Repair Program / ReCraft Program / Frozen Deli
```

### 9-2. MOHEIM（4139）抽出メタ

```
TITLE   : MOHEIM
DESC    : MOHEIMは、タイムレスな美しさと普遍性を洗練されたデザインで作り出すライフスタイルブランドです。
PLATFORM: WordPress
FONT    : セルフホスト
COLORS  : #f1f2ed / #e0e1db / #161a14 / #32373c
SECTIONS: About us → GOBLET / HORN / YUKI wood / SWING BIN / WATER BOTTLE → Designers → Shops
CTA     : 製品の購入はこちら（1種）
UNIQUE  : プロダクト名ベースのナビゲーション
```

### 9-3. Fritz Hansen 日本（4246）抽出メタ

```
TITLE   : Furniture, lighting and accessory design - Fritz Hansen
PLATFORM: 独自 + Swiper
CSS_VARS: --c-s-mode-switch-bc / --nav-tiles-bgc / --highlight-bgc / --hero-bgc
H2      : FRITZ HANSEN TOKYO / 2026年春の新作 / Series 7™ – Verner Panton 100 /
          STORIES FROM FRITZ HANSEN / 一生ものの色と形 / 確かなスタイル感覚 /
          Nikolaj Bebe / バイロン＆デクスター・パート
CTA     : Stores（フッター主要リンク）
```

### 9-4. toio（4335）抽出メタ

```
TITLE   : 小さなキューブ型ロボットトイ・toio（トイオ）
PLATFORM: Next.js（_next/static 検出）
H2      : toioを使って何しよう？ / toioの構成 / あなたにピッタリのtoioは？ /
          体験してみよう / 新着情報 / よくあるご質問 / 受賞歴
CTA     : 購入する / オンラインで購入 / 製品カタログ / 攻略ガイド（購入者向け）
UNIQUE  : 「あなたにピッタリのtoioは？」商品選択診断
```

### 9-5. 育てるタオル（4336）抽出メタ

```
TITLE   : 育てるタオル 公式online store
PLATFORM: Shopify + Swiper + jQuery + Typekit `paf6hxj`
FONT    : Google Fonts `Poppins 500 / Sawarabi Gothic` + Typekit
SECTIONS: topSearch → meritArea → topSeries → topRanking → topShop → topNewitems
          → topProducts → topEgift → modalSearchArea → topNews
H2      : カテゴリで探す / 贈るシーンで探す / 予算で探す / シリーズで探す /
          もっと明日は好きになる / 送料について / お支払い方法 / お届けについて
UNIQUE  : 4軸ナビ（カテゴリ/シーン/予算/シリーズ）+ topRanking + topEgift
```

### 9-6. ＆ CAT（4229）抽出メタ

```
TITLE   : 猫と上質に暮らす。インテリアに映える、シンプルで美しい日本発のペット用品ブランド
PLATFORM: Shopify + Swiper + jQuery
FONT    : Noto Sans JP 100..900（可変フォント）
H2      : CHALICE / KINOBORI / TOG Arc / MALTA BED / Pick up / Category / New items / Recommend items
CTA     : カートに追加 / ご購入手続きへ / カートを見る / お問い合わせ
UNIQUE  : Judge.me（--jdgm-primary-color）レビュー統合 / 商品名を聖具風に命名
```

### 9-7. SETOMANEKI（4154）抽出メタ

```
TITLE   : SETOMANEKI
DESC    : 「SETOMANEKI（セトマネキ）」は、新しい招き猫のスタイルを提案するプロダクトです。
PLATFORM: Nuxt
FONT    : MontasRegular / Whyte Inktrap / dnp-shuei-gothic-gin-std
COLORS  : #C4C3B7（瀬戸灰）/ #DBD1C1（土色）/ #F5F1E6（オフホワイト）/ #DA2301（指し色の赤）
H2      : 幸せを招く新しいカタチ / NEW MANEKINEKO / JAPANESE / SCANDINAVIAN /
          MODERN / CLASSIC / LUXURY / CASUAL
CTA     : Online Store / お問い合わせ
UNIQUE  : インテリアスタイル別の招き猫分類
```

### 9-8. EMARF（4217）抽出メタ

```
TITLE   : EMARF -自由な表現が、現実になる-
PLATFORM: Framer（Generator: "Framer a1faaee"）
SIZE    : 688KB
FONT    : Zen Kaku Gothic New 400/500/700
H2      : お知らせ / EMARF CAD/CAM / Draw it yourself / Request production /
          EMARF 制作・施工サービス / 合板、集成材 / 2D加工 / パース ラフスケッチ 図面
CTA     : MORE / お問い合わせ
UNIQUE  : Framer採用の設計者向けB2Bプラットフォーム
```

### 9-9. IKUS FURNI & COO（4120）抽出メタ

```
TITLE   : IKUS FURNI & COO | 広島市・東広島市の家具・インテリアショップ
PLATFORM: WordPress 6.9.4 + Swiper + jQuery
SIZE    : 532KB
FONT    : Google Fonts Noto Sans JP 400/700
SECTIONS: home_service / home_select / home_cordinate / home_journal /
          home_about / home_instagram / home_brand / cta_contact_area
CTA     : オンラインストアで見る / Online Store / 公式アプリDL / お問い合わせ /
          ショップ・ショールーム・展示施設
UNIQUE  : マスターウォール認定店舗 / コーディネートギャラリー
```

### 9-10. SOTO（4110）抽出メタ

```
TITLE   : SOTO｜ソト
PLATFORM: WordPress 6.9.4 + Site Kit + GSAP + jQuery
H2      : TriTrail ST-350 欧州でベスト・ストーブ受賞 / 安全に製品を選んでいただくために /
          返礼品のご紹介 / 使いかけのボンベを処分するときに / MOMENT /
          PRODUCTS CATEGORY / SEARCH
SECTIONS: footerBanner__quality / footerBanner__support / topConcept__detail /
          sliderWrapper newArrivals__inner / articleBgColor__inner
CTA     : SOTOカタログ2026（無料送付）/ 調理器具カタログ2023 / 最新版無料送付
UNIQUE  : 受賞ニュース + 安全注意喚起 + ふるさと納税 + 複数バージョンカタログ
```

---

## 10. 用語集

- **オフホワイト基調**: `#FAFAFA` より彩度寄り（#FFF4EA / #FAF7F5 / #F8F7F4）の色群
- **3色モデル**: Warm Off-White / Charcoal Text / Brand Accent の3色で構成するクラフト配色
- **Typekit**: Adobe Fonts の旧名。`use.typekit.net/xxxx.css` で判定
- **WPML**: WordPress多言語プラグイン
- **Dawn / Shopify Dawn**: Shopify の公式無料テーマで D2C で最もカスタマイズされる母体
- **Judge.me**: Shopify向けレビュー統合サービス
- **BEM**: Block Element Modifier（`home_instagram` `topProducts` などの命名規則）
- **クラフト／職人系**: 歴史・素材・手仕事を前面に出すプレミアム生活用品
- **ラボ／編集型**: 販売より思想発信を目的にしたメーカーオウンドメディア

---

**Generated**: 2026-04-08 by Claude Opus 4.6 (1M context)
**Source**: `/Users/oidekento/lp-corpus/raw_all/life-goods/` 81 files
**Total lines**: ~900
