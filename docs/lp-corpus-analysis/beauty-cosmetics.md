# 美容・化粧品LP 構造分析レポート（ラウンド2・本格版）

> R1 (30 件) を統合し、**raw_all/beauty-cosmetics/ 全 66 件** を対象に再分析したもの。R1 の主要仮説（「ピンク×白ではない」「薬機法の静けさ」「Zen Kaku+Shippori Mincho」）を検証し、`brand-storytelling` / `d2c-skincare` / `seasonal-campaign` / `beauty-clinic` の 4 サブジャンル観点で整理する。

---

## 1. データソース

- ジャンル: `beauty-cosmetics`
- 分析対象ディレクトリ: `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/`
- ファイル数: **66 件**（R1 は 28 件で分析済み）
- 合計サイズ: 5.8 MB
- 最小: 826 B（`7897_afc-shop` = 404 ページ。以降の統計から除外）
- 最大: 647 KB（`8685_sawai_coffee` = ジャンル誤配）
- 平均本文 HTML サイズ: 約 90 KB（中央値 55 KB）
- 実質ジャンル該当件数: **約 56 件**（下記「ノイズ」参照）

### 1.1 コーパス内ノイズ（ジャンル誤配）

分類タグは beauty-cosmetics だが実内容が別ジャンルのファイル（以後の数値集計は含むが、デザイン傾向の議論からは除外）:

| # | ファイル | 実ジャンル |
|---|---|---|
| 11062 | `moto-bu.motorola.co.jp_products_razr50_` | スマホ |
| 11015 | `p-bandai.jp_item_item-1000217059_` | 玩具（ピリカピリララ） |
| 10297 | `item.rakuten.co.jp_forthon_r972_` | ハット帽子 |
| 10625 | `gomgom.world_lp2_` | スリッポン靴 |
| 10675 | `www.miniiku-trip.jp_` | スタンプラリー観光 |
| 11987 | `goshiga.biwako-visitors.jp_` | 滋賀観光 |
| 8685 | `store.shopping.yahoo.co.jp_sawaicoffee_` | コーヒー |
| 7897 | `www.afc-shop.com_content_nassure2_` | 404 Not Found |
| 11749 / 12097 | `ibiki-kenkyujyo` | 遮光日傘（UV 対策周辺だが美容化粧品ではない） |
| 12020 | `philips.co.jp_shaver-s9000_` | フェイスシェーバー（電動器具） |
| 8883 | `p-bandai_sailormoon_20thspecial_` | セーラームーン 20th（コラボコスメ周辺・境界） |

**示唆**: タグは「UV 関連・肌に触れる・女性向け」を機械的に beauty に吸い込んでおり、UV 日傘・電動シェーバー・コラボグッズが混入する。R3 以降はキーワード分類器側に「化粧品成分・薬機法語彙」でフィルタを噛ませると精度が上がる。

### 1.2 深読み実施ファイル（13 件）

1. `489_www.jillstuart-beauty.com_ja-jp_` — JILL STUART 公式（B2C EC 統合、Shippori+EB Garamond+Inter Tight）
2. `493_www.shiseido.co.jp_macherie_` — MACHERIE（FineToday 委譲のレガシー製品 LP）
3. `494_www.carjurajah.jp_` — エステサロン WP（slick スライダー、matchHeight）
4. `491_stellaeye.jp_` — まつエクサロン（Typekit esy7eoh、古式の独立 LP）
5. `490_jp.rohto.com_mens-deou_` + `492_jp.rohto.com_` — ロート（Azure Front Door + Sitecore CMS）
6. `8046_www.shiseido.co.jp_haku_` — HAKU（薬用美白美容液 21 年 No.1、slick + GTM 複数）
7. `10116_kanebo-cosmetics_twany_essence_` / `10504_milano-collection_powder_` / `12254_twany_time_refresher_` / `8350_kanebo_allie_technology_` — Kanebo AEM (Adobe Experience Manager) テンプレート
8. `11286_decon-brand.com_michiru_lp02_` — DECON（Shopify + 広告 LP、画像のみで CTA 連発）
9. `11533_sb-mitsuhada.ourservice.jp_skincarepowder_subsc6_` — mitsuhada（SquadBeyond 運用型 LP、定期初回 100 円）
10. `12535_www.lucido.jp_campaign_facecare24aw_gold_` — LUCIDO（マンダム、TypeSquare）
11. `10573_cosmedy.jp_lp_u_sen04dt_fa01_` — Cosmedy セラム（独自 LP フレームワーク）
12. `11630_www.c-roland.co.jp_products_reluce_` — ReLUCE（Swiper + AOS + loading オーバーレイ、Cormorant+Noto Serif JP）
13. `9880_www.wwdjapan.com_best-cosmetics_` — WWDBEAUTY（編集系、Typekit ezs5pbj + フルスクリーン video、Swiper）

---

## 2. 統計サマリ（全 66 件）

### 2.1 CMS / 実装基盤

| 基盤 | 件数 | 代表例 |
|---|---|---|
| WordPress（wp-content 検出） | **8** | carjurajah, borica, 3650.day, aster-one, opera-net, kamikacosmetics, kaminomoto, euglena |
| Shopify（cdn.shopify / myshopify） | **3** 明示 + 2 隠し | decon-brand, sb-mitsuhada, gomgom |
| Kanebo AEM（assetsadobe3 / clientlibs） | **6** | kanebo-twany×2, milano-collection, allie, biore(kao), sofina(kao) |
| Sitecore（azurefd + /-/media/） | **2** | rohto×2 |
| Next.js / SSR | **0** 明示（philips は別構成） |
| 静的独立 LP（フルカスタム） | **≈30** | shiseido haku/macherie/beautytopic, ampleur, rice force, sana, etvos, jillstuart, narisup, ishizawa-lab, rmsbeauty, hahanoshizuku, lucido, c-roland×4, borica, onlyminerals×3, bs-cosme, pigeon, kamika-cosmetics, wwdjapan 等 |
| 楽天ショップ HTML（item.rakuten.co.jp） | **9** | ハット帽子・日傘・コスメ混在（商品ページ形式） |
| 404 / その他 | 1 / 〜7 | afc-shop ほか |

**洞察**: 化粧品 LP は**他ジャンル以上にレガシー混在度が高い**。
- Shiseido / Kanebo / 花王 系は依然として **Adobe AEM + Adobe DTM + Dynamic Media Classic** の伝統的エンタープライズスタック。`fontplus.aem.kao.com` を全社共通で使用。
- ロートは **Sitecore on Azure Front Door**。
- 広告運用型は **Shopify + SquadBeyond / LandingHub（アスターワン系）** の「CMS ではなく LP 配信基盤」。

### 2.2 フォント（R1 主要仮説の検証）

| 種別 | 件数 | 備考 |
|---|---|---|
| Google Fonts（`fonts.googleapis.com`） | **16** | R1 で主役だった Noto Sans JP 依存はやはり強い |
| Adobe Typekit（`use.typekit.net`） | **8** | stellaeye, rmsbeauty, wwdjapan, jillstuart, ishizawa-lab, rakuten-lancome, decon, hahanoshizuku |
| Kao 内製 FontPlus（`fontplus.aem.kao.com`） | **6** | Kanebo/花王系全社共通 |
| TypeSquare（モリサワ `typesquare.com`） | **1** | lucido（マンダム系の典型） |
| Web フォント非使用（システム游ゴシック） | **≈25** | SquadBeyond 系、多くの Shopify LP、古い item.rakuten |

**Google Fonts の具体的書体**:

- **Noto Sans JP**: 10 ファイル以上（bs-cosme, c-roland/reluce, ishizawa-lab, kamika, mitsuhada, narisup, hahanoshizuku, naris, motorola, borica 周辺）
- **Noto Serif JP**: `c-roland/reluce`, `kamikacosmetics` のみ（2 件）
- **Shippori Mincho**: `jillstuart-beauty` の 1 件のみ
- **Zen Kaku Gothic New**: `decon-brand` の 1 件のみ
- **Cormorant Garamond**（ラテン系 serif）: `c-roland/reluce` の 1 件
- **EB Garamond + Inter Tight**: `jillstuart-beauty` の 1 件
- **Abril Fatface**: `kaminomoto` の 1 件
- **Marcellus + Hanken Grotesk**: `narisup` の 1 件
- **Montserrat + Poppins**: `narisup`, `motorola`
- **Libre Baskerville + Roboto**: `kamikacosmetics`
- **Questrial + Tauri**: `borica`
- **Work Sans 200**: `rmsbeauty`（ナチュラルコスメらしく 1 ウェイトだけ）

**R1 検証結果**:
- R1 の「**Zen Kaku Gothic New + Shippori Mincho が主役**」という言い切りは **誤り**。実際には Zen Kaku Gothic New は 1 件、Shippori Mincho も 1 件のみ。
- 正しくは「**Noto Sans JP が 10 件以上で圧倒的デファクト**、和文セリフを使う LP 自体が少数（Noto Serif JP 2 件、Shippori Mincho 1 件）」。
- R1 で拾われた Zen Kaku/Shippori は R1 の 28 件サブセット（Shopify・ブランド特設中心）でたまたま偏って現れたもの。**66 件の真の重心は Noto Sans JP モノカルチャーと、Kanebo/花王の AEM+FontPlus 閉域**。

### 2.3 アニメーション / インタラクション・ライブラリ

| ライブラリ | 件数 | 代表 |
|---|---|---|
| **Swiper** | **19** | shiseido×3, jillstuart, rohto×2, kanebo allie, wwdjapan, c-roland/airy, decon, lucido, naris, cosmedy, motorola, p-bandai, bs-cosme, 3650.day, miniiku, kaminomoto |
| **slick**（jQuery） | **14** | haku, macherie, shiseido trio, naris, carjurajah, ampleur, narisup, riceforce, kaminomoto, jillstuart(flexslider), c-roland/reluce, 3650, euglena, sb-mitsuhada |
| **bxslider** | **2** | borica, carjurajah |
| **flexslider** | **1** | jillstuart |
| **AOS**（scroll reveal） | **4** | c-roland×4（reluce, truest, airy, bample）|
| **Lenis**（慣性スクロール） | **2** | philips shaver, wwdjapan |
| **GSAP / ScrollTrigger** | **2** | sb-mitsuhada, decon-brand |
| **anime.js** | **0** | 該当なし |
| **jQuery（全バージョン）** | **38** | 圧倒的多数。ほぼ半分以上が jQuery ベース |

**R1 検証結果**:
- R1 の「AnimeJS / Lenis が主流」仮説は **誤り**。66 件で AnimeJS は 0 件、Lenis は 2 件（しかも片方は非 beauty の philips）。
- 美容 LP の実態は **「Swiper + slick + jQuery」時代を引きずっている**。モダンな Lenis/GSAP は WWDBEAUTY など編集系 LP の少数ケースに集中する。
- **「静かな」ミニマル演出はあっても、それは Lenis ではなく『画像を重ねてスライドさせるだけの slick』で作られている**。

### 2.4 メディア表現

| 表現 | 件数 | 備考 |
|---|---|---|
| `<video autoplay muted loop>` によるヒーロー動画 | **5** | sb-mitsuhada, rakuten-lancome, cosmedy, wwdjapan, narisup |
| ローディングオーバーレイ（loader） | **45** 相当（`loading` 文字列ヒット） | うち実際の loading 演出は C-Roland×4, WWDBEAUTY, HAKU など 10 件程度 |
| スライダー FV（slick / swiper / bxslider） | **≈35** | 美容 LP の標準は**動画より静止画カルーセル** |
| `picture + srcset + webp` | **≈30** | Shiseido, Kanebo, 花王系はほぼ全滅で webp 未対応のまま。独自実装の小規模ブランドの方が webp 採用率が高い |
| Adobe Dynamic Media Classic（`s7responsiveContainer`） | **6** | Kanebo/花王系が全社統一で採用 |

**R1 検証結果**:
- R1 の「**フルスクリーン動画 FV** が増えている」仮説は **部分的に誤り**。実際には 66 件中 5 件のみで、採用は (a) 広告運用型の PV 素材流用（cosmedy, sb-mitsuhada, rakuten-lancome）と (b) 編集系ブランドジャーナル（WWDBEAUTY）に二極化。中堅ブランドの新作特設は依然として**静止画 slick ヒーロー**が多数派。

### 2.5 薬機法「安全動詞 / 危険動詞」検出

| カテゴリ | 正規表現 | 検出総数 | 検出ファイル数 |
|---|---|---|---|
| 安全寄り語彙（医薬部外品・薬用・効能・効果・承認） | `医薬部外品\|薬用\|効能\|効果\|承認\|認可` | **204** | **41** |
| ポジティブ接続語（うるおい・ハリ・ツヤ・透明感） | `うるおい\|ハリ\|ツヤ\|透明感\|澄む\|潤す` | **192** | **26** |
| 過剰表現（最高・世界初・No.1・奇跡・完全） | `最高\|世界初\|No\.1\|ナンバーワン\|業界初\|完全\|驚き\|奇跡` | **36** | **16** |

**含意**:
- 美容 LP は **「医薬部外品・薬用・効能」のような用語を避けない**。むしろ大手・中堅ブランドは 6 割以上で使う。これは薬事表現規制が「定型の用語だけは逃げ道として使える」構造を許しているため。
- 一方「**最高・世界初・No.1**」のような過剰表現は 16 ファイル / 36 ヒットに留まる。HAKU（「美白美容液市場 21 年連続売上 No.1」）や LUCIDO（「純金が当たるキャンペーン」）のように**根拠付きの No.1 訴求**が大半。
- R1 の「**薬機法の静けさ**」仮説は **半分正解**。静けさは「No.1／世界初などのブラック語彙の抑制」に現れるが、「うるおい／ハリ／ツヤ／透明感」という **定型の『ポエジー語彙』には強く依存**しており（192 ヒット / 26 ファイル）、静けさというより「**別の語彙で賑わっている**」と表現する方が正確。
- TWANY seasonal essence で 25 回 "うるおい" 系語彙がヒットするなど、**季節キャンペーンほどポエジー語彙の反復が極端**。

### 2.6 色面（pink / white / #fff 系）

| 検出 | 件数 |
|---|---|
| `#fff` / `background: #f[a-f]` 系 | **30 ファイル / 121 ヒット** |

R1 の「ピンク×白ではない」検証:

- **pink という単語**は全 66 件で直接検出ゼロ（キーワード変数や中国語リテラルは除外）。
- CSS で `#fce` `#fcd`（ピンク系） を厳密に使っているのは `4 ファイル未満`。
- 実際の支配色は「**#fff / #f8f4ef / #f6f0eb / #fafafa / #eeeae3 などのオフホワイト〜アイボリー系**」。TWANY は `cnn-bg-f6f0eb.png` 背景、Milano Collection は `#f6f0eb` 系、HAKU は純白ベース。
- **結論**: R1 仮説「ピンク×白ではない」は **正しい**。実際はオフホワイト〜アイボリー、あるいは純白 + 商品ビジュアルの色、あるいはシャンパンゴールド（Milano Collection）・モスグリーン（HAKU）などブランド固有のアクセント 1 色。**フラッシー色面は広告運用型 LP（sb-mitsuhada の黄色ガムマーカー、mitsuhada の赤帯）にしか出ない**。

---

## 3. 深読み 13 件

### 3.1 JILL STUART Beauty（`489_`）— EC トップ兼ブランド

- 構成: `jillstuart-beauty.com/ja-jp/` = 公式 EC トップ
- フォント: `EB Garamond + Inter Tight + Shippori Mincho`（3 種ミックス）
- 技術: jQuery 1.11.1 + jQuery UI 1.12.1 + flexslider 2.7.1 + Shoplive（ライブコマース SDK）+ Kaizen Platform + Lightning Recommend（レコメンド SDK）
- CSS ロード戦略: **ページ種別（top/list/detail/search）で CSS を JS で動的削除**する古典的最適化（現代なら Next.js SSR + Tailwind で済む話）
- 含意: ブランド側はデザインセンスこそ現代的（Shippori + EB Garamond）だが、実装は **10 年モノの jQuery + EC カートフレームワーク**。フロント全面リプレイスはできない／しない。

### 3.2 Shiseido HAKU（`8046_`）— 大手薬用美白

- 「美白美容液市場 21 年連続売上 No.1」「ベストコスメ累計 174 受賞」とエビデンス系コピーで固める。
- スライダーは slick。画像は **picture + webp** 対応。
- 構成: `kv(大画像・薬機コピー)` → `TOPICS(スライダー)` → `BEST SELLER` → `CAMPAIGN` → `ABOUT(ブランドストーリー)`
- 注目: KV alt テキスト = 「**美容医療か。美白美容液か。**」という二項対立コピー。美容医療台頭への挑戦状としてのブランド表現が KV に入っているのが 2025-2026 の大手化粧品 LP の新潮流。

### 3.3 Kanebo TWANY シーズナルエッセンス（`10116_` / `12254_`）

- Kanebo/花王の **AEM (Adobe Experience Manager)** 出力。クラス名に `g-Area`, `g-Column`, `g-HeadingTitle`, `opt-lg-pt100--imp` など AEM コンポーネント名がダダ漏れ。
- フォント: FontPlus（AEM Font 連携）。代表指定: `"Ryumin Regular KL"` を CSS `font-family` で直指定。**リュウミンを Web で使う** という他業種では滅多に見ない贅沢な組版。
- KV: 「春の"乾燥ゆらぎ肌"にうるおいバリア集中ケア美容液」= 季節＋悩み＋製品カテゴリの 3 連
- 色: `/twany/renew/lineup/special/260113_essence/bg_lead.png` の淡いピンクベージュグラデーション背景
- sticky 追従バナー（店頭誘導、店舗検索へ）= 購買よりも**実店舗カウンセリング送客**が主要 CVR
- 含意: 中高年〜シニア向け百貨店ブランドは「EC CV」よりも「**店頭体験予約**」を設計のゴールに置いている。Floating bnr も `clamp()` で 3 ブレイクポイント対応する手間をかけて作られている。

### 3.4 Kanebo Milano Collection（`10504_`）— 復刻高級パウダー

- コピー: 「名画に描かれる女神たちの、神々しいまでになめらかな肌を一途にめざして」「"女神カバーおしろい"」
- 用語: `opt-fontfamily--01` クラスでリュウミン強調。`opt-fontsize--l` で視覚ピラミッド。
- 背景: `cnn-bg-f6f0eb.png`（#F6F0EB = アイボリーグレー）と商品背景画像の 2 枚重ね
- ストーリー構造: 「一人の研究員がミラノ出張で…」という**起源伝説(オリジンストーリー)**の 1 段落。化粧品における"**ロマン純度**"を最大化する語り口。「ピンク×白」ではなく「アイボリー×絵画色」の設計。

### 3.5 Kanebo ALLIE technology（`8350_`）— 日焼け止めブランド

- タグライン: 「Think Sustainability Be Beautiful.」
- AEM テンプレートは TWANY と共通だが、ALLIE 系は **技術訴求** のページ設計。メニューに `技術` `商品ラインナップ` `About ALLIE` `GLOBAL` があり、グローバル展開（`allie-global.net`）への導線。
- 日焼け止めは**機能カテゴリ化粧品**なので、文章量比率は季節エッセンス系より圧倒的に高い。

### 3.6 DECON michiru LP02（`11286_`）— Shopify + 広告 LP

- URL: `?sb_tracking=true&utm_creative=soku_biyo_s41_michiru&utm_source=fb&utm_medium=cpc&utm_campaign=at&fbclid=...`
- 構造: **画像 100%** の縦長 LP。`lp02_08.jpg` 〜 `lp03_12.jpg` と連番画像を並べ、Photoshop で作ったコピー・装飾・根拠図を**全て画像として流し込む**。
- コピー装置: `posAbs elm01_01`（absolute 要素）に小さなバッジ画像（「43 歳」「朝食代わりに」）を被せる**ユーザーボイス + 年齢バッジ**パターン
- CTA: `cta01_02-btn01_01.png` alt=「今すぐ 60%OFF でお得に初めてみる！」 = **値引きだけで押す典型**
- Shopify への連携: CTA は直接 Shopify カートの商品 ID に cart/add クエリ
- `mixlogue.jp` + Firebase `subscription-script2-pr` で**定期購入 subscription スクリプト**を外部から注入
- 含意: R1 で見ていた「ブランド DECON 本体」とは別人格。**同一ドメイン内に高級ブランディングページと広告 LP が共存**。広告 LP 側は Zen Kaku Gothic New を読み込みながらも**実コンテンツは全部画像**なので Web フォントは装飾要素以外には効かない。

### 3.7 mitsuhada スキンケアパウダー（`11533_`）— SquadBeyond 運用型

- `sb-mitsuhada.ourservice.jp` = SquadBeyond 配信ドメイン
- `<body class="article-body">` = SquadBeyond の記事型 LP フレーム。`sb-custom`, `sb-bg-gum-marker-animated`, `sb-fs-*`, `sb-bg-yellow`, `sb-color-red` など**配信基盤側が提供する 50 種類以上の inline CSS クラス**が全て bake-in されている
- body CSS: `font-family: 'YuGo*', "游ゴシック"...` + `font-feature-settings: 'palt'` + `letter-spacing: 0.1em`
- CTA: `https://mitsuhada.myshopify.com/cart/clear?return_to=/cart/add?items[0][id]=...&selling_plan=2526249160` — **定期購入 selling_plan** を直指定して即時カート投入
- オファー: **定期初回 100 円**（広告運用型コスメの定石）
- コンテンツ: 全部画像。`fv.png` `coupon_title.png` `cta_bg.png` ...
- 実装スタイル: `position: absolute` でスクリーン 750px グリッドに画像パーツを重ねる **古典的 LP 設計**（`.contents { max-width: 750px }`）
- 含意: 運用型化粧品 LP は現代 CSS（Grid/Flex）では**なく**、2015 年頃の 750px 固定幅 + 絶対配置 + PNG 書き出しという「**画像ペーストアップ方式**」がまだ現役。Web フォントもほぼ効かず、**Photoshop の級数と書体設定がそのまま画像として焼き込まれる**。

### 3.8 cosmedy（`10573_`）— Cosmedy 独自 LP + 画像主義

- `page.cosmedy.jp/lp/senuru/t04/images/` 配下の連番画像（`senuru_LP_36-1980.png` ... ）
- mitsuhada と同じ**定期コース 5 大特典** / **初回 60%OFF** の定型オファー
- フォーム: `/shop/customers/sign_in?customer_return_to=%2Flp?u=sen04dt_fa01...` — 独自 EC 基盤
- 含意: 運用型コスメには**インフラの選択肢が 3 つ**ある:
  1) **Shopify + SquadBeyond**（mitsuhada）
  2) **自社 EC + 独自 LP 基盤**（cosmedy = `cosmedy.jp`、aster-one = `lp.aster-one.com` / LandingHub）
  3) **WordPress プラグイン配信**（kamika, aster-one の別系統）

### 3.9 ReLUCE by コスメテックスローランド（`11630_`）— 香水系ボディミルク

- フォント: `Cormorant Garamond + Noto Sans JP + Noto Serif JP`
- ライブラリ: `Swiper + AOS (data-aos)` + 独自 loading オーバーレイ
- loading は SVG `textPath` で円状に "Loading Loading" を回す仕込みも埋まっている（コメントアウトされているが意図が見える）
- 構成: loading → header(nav+SVG logo) → FV (Swiper) → concept → lineup → instagram → management
- 含意: **中堅コスメ系ブランドの「プロダクト単独 LP」の最頻度テンプレ**。Swiper FV + AOS スクロール reveal + Cormorant Garamond で"**少しお洒落で量産品質**"を狙う。c-roland は同じテンプレを `truest` `bample` `airy-and-easy` 4 ブランドで再利用している。

### 3.10 WWDBEAUTY 2024 下半期ベストコスメ（`9880_`）— 編集系メディア LP

- `www.wwdjapan.com/c/best-cosmetics/`
- フォント: Typekit `ezs5pbj`（WWD ブランド専用キット。おそらく Freight Sans / Utopia 系）
- ライブラリ: **Swiper 9** + ress.css（モダン reset）+ **Lenis 慣性スクロール**（唯一クラスファイル内で使用）
- FV: **フルスクリーン `<video>` 自動再生**（`preload=auto playsinline muted loop autoplay webkit-playsinline`）
- loading: `<div id="loading"><div class="progressBar"></div></div>`
- 構成: top（video + SVG logo）→ new-products → hero-products → campaign → about → archive
- ナビ: `drawer-nav` + `cursor` カスタムカーソル
- 含意: 編集系ブランドジャーナル LP は **化粧品 LP の最先端実装**。だが影響範囲はこの 1 件だけで、大手ブランドに横展開されていない。「最先端は WWDBEAUTY が握り、その下は 3〜5 年遅れの Swiper+slick」という 2 層構造。

### 3.11 LUCIDO（`12535_`、マンダム）— 40 代男性 + 純金キャンペーン

- マンダム（`lucido.jp`）は **TypeSquare（モリサワ）** を typesquare.com で呼び出し
- FV: 「ルシード スキンケア│純金が当たるキャンペーン」
- モーダル系: `remodal` + `swiper` + `slick`（3 種同居）
- グローバルナビ: TOP / ABOUT / PRODUCTS / SPECIAL / LIBRARY / SHOP / MENU（PC/SP 切替）
- 含意: 男性化粧品は**「賞品訴求（純金）」 + 「40 才から」という年齢セグメンテーション**のコンボで女性化粧品 LP とは異なる文脈設計。

### 3.12 etvos ミネラルファンデ お試し（`9552_`）— お試しセット特化 LP

- `<meta name="viewport" content="width=device-width, ...">` だが CSS 内では `body { max-width: 100pc }` `#wrap { min-width: 750pt; ... }` = **pt/pc 指定**という超レガシー
- スマホ判定: `if(navigator.userAgent.match(/iPhone|iPod|Android/))` → `location.href` で完全別ドメイン `etvos.com/smart/lp/s-112/18/index_pen4.html` へ転送
- アドタグ: EBiS / Criteo / Tealium utag.js + `adcent.jp` の**4 系統 CV トラッカー**
- `moveArea01-05` で画像を左右スライドさせる CSS アニメ
- 含意: **お試しセット LP** は今でも 2015 年以前の設計思想が現役。pt/pc 指定と UA 振り分けは 10 年前ならモバイル対応のベストプラクティスだった。

### 3.13 Borica カラーセラムライナー（`10120_` + `12330_` 楽天版）

- ブランド公式（borica.jp）は WordPress 5.8.2 + bxslider + drawer.css + animate.min.css + instafeed.min.js
- フォント: `Questrial + Tauri`（和文は指定なし＝ヒラギノ）
- 楽天版（`item.rakuten.co.jp/shibuyawalker/`）は**文字コード化け**で `ڳŷԾBorica...` と出力される = Shift_JIS → UTF-8 変換事故で、楽天ショップ HTML に共通する現象
- 含意: 楽天出店型コスメは**文字化けコーパス**として今回の分析では text マイニングが困難。しかし画像アセット中心の LP なので UI 設計の観点ではむしろ画像構造を見る方が良い。

---

## 4. 4 サブジャンル別パターン

### 4.1 brand-storytelling（ブランド公式トップ・世界観提示）

**該当**: JILL STUART, Shiseido HAKU, Kanebo Milano Collection, Kanebo TWANY, rmsbeauty, Shiseido Macherie, SANA Honeyshca, SENSAI, lucido, rohto, ishizawa keana, etvos 本体, onlyminerals 公式, narisup by365, ampleur, rice force, hahanoshizuku, pigeon skincare, sofina lift, biore, bs-cosme FLUFFY, opera

**構造の定型**:
1. ブランドロゴ → グローバルナビ（ABOUT / PRODUCTS / CAMPAIGN / SHOP / STORY）
2. KV = 大画像 slick カルーセル（平均 3〜5 スライド）
3. TOPICS / NEWS / PICK UP 3〜4 枠
4. BEST SELLER または PRODUCT LINEUP 2〜4 点
5. BRAND STORY / ABOUT への導線
6. キャンペーン or フォトギャラリー
7. SNS / Instagram 埋め込み
8. フッター（企業情報 / お問い合わせ / SNS アイコン）

**デザイン言語**:
- 書体: **Noto Sans JP** 400/500/700 三段階 + 欧文 serif を 1 種（Shippori, EB Garamond, Cormorant, Marcellus のいずれか）
- 色: **#fff / オフホワイト** ベース + ブランドカラー 1 色（ゴールド・ブロンズ・モスグリーン・バーガンディ・ペールピンク）
- 画像: 製品モック + モデルポートレート + テクスチャ（液体・パウダー）
- アニメーション: **slick フェード(2000-4000ms)** が 9 割。モダンな Lenis/GSAP は例外

**CTA**:
- 「オンラインショップ」「店頭を探す」= **即購入より店頭誘導**
- `floating-bnr`（sticky 右下バナー）でブランドサイト→店頭送客が主流

### 4.2 d2c-skincare / 広告運用型（ダイレクトレスポンス LP）

**該当**: DECON michiru, mitsuhada スキンケアパウダー, cosmedy senuru, KAMIKA スティックファンデ（aster-one + kamikacosmetics）, manara 楽天, DEBEAUS 楽天, santemina 楽天, 3650×GENIC, afc nassure（404）

**構造の定型**:
1. **FV**: 商品写真 + キャッチコピー（画像）+ **「定期初回○○円」「60% OFF」「100 円」などの値引き帯**
2. **クーポン煽り**: 「今なら特別クーポンプレゼント！」「残り○○日」のタイマー演出
3. **プロブレム提起**: 「こんなお悩みありませんか？」3〜5 項目チェックリスト画像
4. **商品誕生秘話**: 「美しく、健やかにと願うあなたへ」「誕生」
5. **USER VOICE**: 35 歳 / 43 歳 / 36 歳 などの**年齢バッジ + 顔写真 + 体験談画像**
6. **科学的根拠**: グラフ・成分図・受賞歴
7. **競合比較表**: 他社製品との横並び
8. **CTA 大バナー** ×複数箇所（画像ボタン・追従フッター）
9. **FAQ** + 特商法表記

**デザイン言語**:
- **全て画像で構成**。テキストはほぼ alt のみ。
- 書体: Web フォントは読み込むがほぼ使われず、Photoshop で焼き込んだ **游ゴシック / 筑紫明朝 / 小塚 / ヒラギノ**
- 色: **黄色ガムマーカー背景** + 赤文字強調 + 緑色「安心」バッジ + ピンクの「初回限定」帯
- アニメーション: `sb-bg-gum-marker-animated` (background-position スライドイン) 程度
- レイアウト: **750px 固定幅 + 絶対配置**（2015 年式 LP）

**CTA**:
- 画像 CTA ボタンを **画面内に 5〜10 個**配置。すべて同じ「申込みフォーム or Shopify カート」へ
- selling_plan（定期購入プラン ID）を query で直指定してカート即投入

**ホスティング**:
- **SquadBeyond**（`*.ourservice.jp` / `bp-viewer.mysquadbeyond.com`）
- **LandingHub**（`airport.landinghub.cloud/dispatcher`）
- **Shopify themes Dawn 改造** + 画像 only
- **自社 EC（cosmedy, aster-one）**

### 4.3 seasonal-campaign / 限定・特設 LP

**該当**: TWANY シーズナルエッセンス 2026SS, TWANY タイムリフレッシャー, Milano Collection 2026, ランコム Rakuten キャンペーン, LUCIDO 純金キャンペーン, HAKU 継続実感プログラム 2026, Borica 楽天, opera 2024 oct

**構造の定型**:
1. KV = **季節 × 悩み × 製品カテゴリ** 3 段重ねのコピー画像
2. 「なぜ今、この製品か」= 季節的背景（春の揺らぎ、夏の UV、秋の乾燥、冬のごわつき）
3. 製品特長 3〜5 点
4. 使用シーン写真
5. **キャンペーン詳細**: 応募条件・プレゼント・期間
6. 店舗検索 + オンラインショップ誘導

**特異性**:
- Kanebo 系は「**リュウミン Regular KL**」を Web で直指定。AEM+FontPlus 連携がなければ実現不能な組版贅沢
- スタンプラリー型・レシート応募型のキャンペーンは LINE 連携が標準
- 「ルシード 純金」「ランコム 特別な 7 日間」など**期間限定の賞品フック**が多い

### 4.4 beauty-clinic / salon（エステ・サロン）

**該当**: carjurajah（エステスパ）, stellaeye（まつエクサロン）, + 周辺（aloop clinic は R1 分析済み）

**構造の定型**:
1. KV = slick で店舗写真を 3〜5 枚ローテ（各店舗の個性を平等に並べる）
2. メニュー表（施術内容 + 時間 + 価格）
3. 「こだわり」技術哲学 3〜5 項目
4. 店舗一覧 + アクセス（JSON-LD で LocalBusiness 構造化）
5. 予約 CTA（外部予約システム: square, hotpepper, リザーブリンク）
6. スタッフ紹介（顔写真）
7. ブログ / お客様の声

**デザイン言語**:
- 書体: carjurajah は Web フォント非使用、stellaeye は Typekit（少数派）
- 色: ベージュ・モカ・白・ダークブラウン系。**美容医療クリニックと違い "清潔感" 一辺倒ではなく "秘匿感・隠れ家" の演出**
- 画像: 施術風景・個室・ロビーなど "空間" 重視
- WordPress テーマベース（carjurajah = 独自 WP テーマ）が多い

**CTA**:
- 予約ボタン = 外部システム（Square, HotPepper, Calendly 系）
- 電話番号 + Google Maps
- LINE 公式友だち追加

---

## 5. 共通パターン（4 サブジャンル横断）

### 5.1 **「他ジャンル以上にレガシー互換性が高い」**
- jQuery 1.x/2.x 系がまだ現役（38 ファイル）
- 楽天出店店舗は Shift_JIS 化け・絶対配置・テーブルレイアウト
- Shiseido / 花王 / Kanebo の AEM は classes 名だけで 20 年前の Web ベンダーフレームワーク臭を残す
- etvos のような中堅 EC は `body { max-width: 100pc }` で `pc`(pica) 単位を使う
- **モダン化が進んでいるのは DECON, WWDBEAUTY, 一部 Shopify だけ**

### 5.2 **「画像組版主義」**
- デジタル組版で美しく文字を流し込むのではなく、**Photoshop で書体を焼いた PNG を並べる**
- Web フォントを読み込んでもテキスト要素に効かない（装飾・メニューだけ）
- 薬機法・ブランド統制で文字校正を画像で一括管理したい意図
- この主義のおかげで検索性は悪いが、**視覚的完全性**は保たれる

### 5.3 **「sticky 追従 floating banner」**
- 右下 or 右下隅に sticky で「お試し注文」「店頭検索」「キャンペーン応募」への追従導線
- TWANY は sticky の位置を `clamp()` 関数で 3 ブレイクポイント対応
- Shopify 系は `js-floatingAra`（ローマ字ミスは decon の実例）

### 5.4 **「季節性の反復」**
- 春夏秋冬ごとに KV を撮り直す → ブランド側は年 4 回の LP リフレッシュを前提設計
- 命名規則: `240701_essence` `20240801_time_refresher` `260113_essence` = **日付 prefix**で世代管理
- Kanebo は AEM テンプレに同じコンポーネントをシーズンごとに差し替える運用

### 5.5 **「エビデンス積み」**
- 「21 年連続 No.1」「ベストコスメ累計 174 受賞」「インテージ SRI データ」「全国 43 店舗調査」
- `<sup>*1</sup>` `<sup>*2</sup>` で注釈リンク → 下部に根拠データ箇条書き
- **薬機法が許す数字**をとことん使う美学

### 5.6 **「SNS/InstaFeed 埋め込み」**
- instafeed.min.js, Facebook Page Plugin, Twitter Tweet Button, LINE share
- 新しい LP ほど LINE 公式、古い LP ほど Facebook

---

## 6. 新発見（R2 で見えてきたこと）

### 6.1 **化粧品 LP の"三層構造"**

コーパスを俯瞰すると、化粧品 LP は 3 つの異なる世界に分かれて共存している:

| 層 | 主体 | 技術 | 目的 |
|---|---|---|---|
| **Enterprise 層** | Shiseido / 花王 / Kanebo / ロート / マンダム | AEM / Sitecore / 独自 CMS + FontPlus / TypeSquare | ブランドエクイティ・店頭誘導 |
| **Mid-tier 層** | 中堅単独ブランド（c-roland 4 ブランド, borica, onlyminerals, etvos, ampleur, riceforce, ishizawa 毛穴撫子, sana, sofina 単独, bs-cosme）| WordPress + jQuery + Swiper/slick + Noto Sans JP | EC 誘導・ブランディング |
| **Performance 層** | DECON, mitsuhada, cosmedy, KAMIKA, manara, 楽天出店型 | Shopify / SquadBeyond / LandingHub / 自社 LP 基盤 + 画像 100% | 定期購入 CVR 最大化 |

**この 3 層は同じ"化粧品"というカテゴリでも、まったく異なるデザイン言語**を持っている。design-mcp にとって大事なのは「**どの層の LP を生成したいか**」を明示的に指定できるインターフェースを設けること。

### 6.2 **「R1 のサンプル偏り」が判明**

R1（30 件）は Shopify + D2C ブランド寄りの偏りで、「Shippori Mincho / Zen Kaku Gothic New 主役」という結論を出していたが、66 件コーパス全体ではこれは少数派。**Web フォント使用率は全体で 30/66 ≒ 45%** しかなく、半数以上は Web フォント不使用の画像組版 LP である。

### 6.3 **「Lenis/AnimeJS は美容ではほぼ使われていない」**

Lenis 2 件（1 件は philips = 非 beauty、もう 1 件は WWDBEAUTY）、AnimeJS 0 件。**美容 LP のスクロール体験はネイティブスクロール + slick 切替で充分**とされていて、GSAP/ScrollTrigger も 2 件（sb-mitsuhada, decon）のみ。**「静かで品のある演出 = Lenis」という先入観は、少なくとも美容 LP には当てはまらない**。

### 6.4 **「色のロジックは "オフホワイト + ブランド色 1 色" 」**

- ブランド公式: #fff〜#f6f0eb（アイボリー）+ ブランドロゴカラー
- 広告 LP: #fff + 黄色ガムマーカー + 赤強調（Dagger 型の視線誘導）
- クリニック: ベージュ + モカ + ダークブラウン
- 編集系: 純白 + ブランドビデオの色 + ブラックテキスト

**真にピンクな LP は 1 件もない。ピンクは"化粧品の色"ではなく"ロマンチックコラボ"の色**（Sailormoon 20th や Borica カラーリップ楽天）に寄っている。

### 6.5 **「運用型 LP のカスタマージャーニー圧縮」**

SquadBeyond 式 LP は以下を 1 画面の画像縦列で圧縮する:

1. 気づき → 2. 興味 → 3. 比較 → 4. 検討 → 5. 決定

これを **FV → 悩み共感 → 成分科学 → ユーザー体験 → 料金 → FAQ → 特商法** という**8-12 枚の画像**で実現する。**時間にして 30 秒のスクロールで購入判断を引き出す設計**であり、ブランド LP の"読まれる前提"とは根本的に思想が違う。

### 6.6 **「楽天出店型」は独自コーパスとして別扱いすべき**

9 件の楽天ショップ HTML は:
- 文字コード化け（Shift_JIS → UTF-8 変換事故）
- 画像 alt もすべて文字化け
- `div class="posAbs"` の 10 年前式コーディング
- 楽天広場テンプレを継承した古い table-layout

**これらは R3 以降の分析で `rakuten-shop` というサブジャンルに切り出すべき**。今回は beauty-cosmetics タグで拾ってしまっているが、デザイン傾向としてはまったく別のクラスター。

### 6.7 **「店頭誘導型 KPI」の発見**

TWANY の floating-bnr リンク先が `https://twany.sl.goga.jp/`（店舗検索の外部サービス）であるように、**大手百貨店ブランドは EC CV ではなく "カウンセリング予約" を主要 KPI にしている**。LP の CTA ボタンで購入させないブランドは美容業界の中に確実に存在し、むしろ「カウンターへ来てもらう」ことが商品単価的に正解というブランドは多い。

---

## 7. design-mcp 使用方針

R2 での実測を踏まえた design-mcp 活用ガイド:

### 7.1 テンプレート分岐

design-mcp に以下 **4 つの beauty-cosmetics プリセット**を用意する:

| プリセット名 | 用途 | デフォルト技術スタック |
|---|---|---|
| `beauty/brand-heritage` | 大手・中堅ブランド公式 | Noto Sans JP + Shippori Mincho + Swiper/slick + オフホワイト + ブランド 1 色 |
| `beauty/d2c-performance` | 定期購入型運用 LP | 画像 100% 構成 + 黄マーカー + 固定 750px + Shopify カート連携 |
| `beauty/seasonal-campaign` | 限定・季節特設 | KV 3 段コピー + リュウミン系 serif + sticky 追従バナー + 店頭検索 |
| `beauty/clinic-salon` | エステ・クリニック | JSON-LD LocalBusiness + 予約 CTA + ベージュ配色 + 店舗スライダー |

**絶対にやってはいけない**: 4 つを 1 つのテンプレに統合しようとすること。Enterprise と Performance は**デザイン言語が逆**なので、同じ生成器で扱うと両方とも中途半端になる。

### 7.2 フォント指定

- デフォルトは **Noto Sans JP 400/500/700** 一択（66 件中最頻値）
- ブランド格式を上げたい場合: **Shippori Mincho**（Jillstuart 的）または **Cormorant Garamond**（中堅ブランド的）
- Zen Kaku Gothic New は採用例が 1 件しかないので、**R1 の誤誘導を避けるため明示的なオプション指定時のみ使う**
- Kanebo 的高級感を出したい場合のみ、**FontPlus 契約下で Ryumin 直指定**というオプションを別枠で

### 7.3 色パレット

```
base:        #fff  / #faf8f4 / #f6f0eb   (純白〜アイボリー)
accent1:     #b8a179 / #9a6f3c / #4f3622  (ブロンズ〜ダークブラウン)
accent2:     #2d4a32 / #6e8a5a             (モスグリーン - HAKU 系)
accent3:     #8a1c2b / #c43b5a             (バーガンディ - メイクアップ系)
text:        #1a1a1a / #333                (黒ではなく濃グレー)
warning/tag: #d40f26 / #ffd400              (運用 LP 専用)
```

**ピンクはデフォルトから外す**。R1 の直感と違い、美容 LP の 95% はピンクを使わない。

### 7.4 アニメーション規約

- デフォルト: **slick フェード 2000-4000ms**（jQuery + slick or Swiper）
- モダンスタック要求時のみ: **Swiper 9 + Lenis**（編集系）
- GSAP/ScrollTrigger は**広告運用 LP**または**編集系**のどちらかに限定
- AnimeJS は beauty では使用実績ゼロのため**提案しない**

### 7.5 薬機法バリデーター

design-mcp の生成結果に対し、**以下の辞書ベース検証**を組み込む:

**BAN 語彙**（広告表現ガイドライン違反の典型）:
- 「世界初」「日本初」「最先端」「業界初」（客観根拠必須）
- 「完全」「絶対」「永久」「万能」
- 「医師が推奨」「医薬品と同等」
- 「ニキビが治る」「シミが消える」（効能の言い切り）

**推奨語彙**（美容 LP で頻出の"安全"表現）:
- 「うるおい」「ハリ」「ツヤ」「透明感」「キメ」
- 「薬用 ○○（医薬部外品）」
- 「肌印象」「肌コンディション」
- 「年齢印象ケア」（"アンチエイジング" を避ける言い換え）

**数字 No.1 ルール**:
- 「○○市場 ○○年連続売上 No.1」は**必ず出典と期間を併記**（インテージ SRI 型）
- 「ベストコスメ受賞」は受賞媒体と年を明記

### 7.6 CMS 想定の明示

生成する LP が **どの CMS 上で動くか** を design-mcp に入力として渡せるようにする:

- `cms: shopify` → Liquid tag 出力、Swiper 埋め込み
- `cms: wordpress` → functions.php/theme 想定 + slick
- `cms: static` → Next.js App Router or 素の HTML
- `cms: squadbeyond` → 画像 only、inline style、固定 750px
- `cms: aem-kao-enterprise` → 想定外のため**生成禁止**（AEM テンプレに後付け移植）

### 7.7 「層間クロスオーバー」警告

生成依頼時に、**Enterprise 層と Performance 層のクロスを検知**してユーザーに警告する:

```
⚠ "ブランディング LP" として発注されましたが、
   "定期初回 100 円" "60%OFF" "申込フォーム" の CTA が含まれています。
   これは 'brand-heritage' ではなく 'd2c-performance' プリセットに切り替えた方が
   自然な設計になります。
```

この層の混在は R2 で実測した**最大の設計破綻源**（DECON が同じドメインで 2 層を共存させて混乱している例など）。

### 7.8 R3 以降の追加分析方針

- **rakuten-shop** サブジャンルを `beauty-cosmetics` から切り出して別コーパス化
- **kanebo-aem-enterprise** の AEM テンプレ群を**別リポジトリで構造保全**（リュウミン等の独自組版資源として）
- **SquadBeyond LP の 画像命名規則** を自動抽出 → Photoshop テンプレとしてレコンストラクション
- **薬機法 NG 辞書** の継続更新（厚労省ガイドライン改訂追随）

---

## 8. 付録: 統計まとめ早見表

| 指標 | 値 |
|---|---|
| 総ファイル数 | 66 |
| 実質 beauty 該当 | ~56 |
| ノイズ除外（非 beauty） | ~10 |
| 平均 HTML サイズ | 90 KB |
| Google Fonts 使用 | 16 / 66 (24%) |
| Typekit 使用 | 8 / 66 (12%) |
| FontPlus (Kao/Kanebo) | 6 / 66 (9%) |
| TypeSquare (Morisawa) | 1 / 66 (2%) |
| Web フォント不使用 | ~35 / 66 (53%) |
| Swiper 採用 | 19 / 66 (29%) |
| slick 採用 | 14 / 66 (21%) |
| jQuery 使用 | 38 / 66 (58%) |
| フルスクリーン video FV | 5 / 66 (8%) |
| Shopify 確認 | 3 / 66 (5%) |
| WordPress 確認 | 8 / 66 (12%) |
| Kanebo/花王 AEM | 6 / 66 (9%) |
| 医薬部外品・薬用語彙あり | 41 / 66 (62%) |
| ポエジー語彙（うるおい系）あり | 26 / 66 (39%) |
| 過剰表現あり（No.1 含） | 16 / 66 (24%) |
| Lenis 慣性スクロール | 2 / 66 (3%) |
| AnimeJS | 0 / 66 (0%) |
| AOS スクロール reveal | 4 / 66 (6%) |
| GSAP / ScrollTrigger | 2 / 66 (3%) |

---

## 9. R1 → R2 の差分まとめ

| R1 仮説 | R2 検証結果 |
|---|---|
| 「Zen Kaku Gothic New + Shippori Mincho が主役」 | **誤り**。実際は Noto Sans JP 支配。Zen Kaku/Shippori はそれぞれ 1 件のみ |
| 「ピンク×白ではない」 | **正しい**。実際はオフホワイト + ブランド 1 色。ピンクは皆無に近い |
| 「薬機法の静けさ」 | **半分正しい**。過剰表現は抑制されているが、"うるおい/ハリ/ツヤ/透明感" 系ポエジー語彙は爆発的に頻出。「静か」ではなく「別の語彙に置き換わっている」 |
| 「フルスクリーン動画 FV が増えている」 | **誤り**。66 件中 5 件のみ。主流は slick 画像カルーセル |
| 「Typekit 使用率は高い」 | **誤り**。8 件のみ。Google Fonts が 2 倍多い |
| 「Lenis / AnimeJS が主流」 | **誤り**。AnimeJS 0 件、Lenis 2 件（1 件は非 beauty） |
| 「Shopify 比率が高い」 | **部分的正しい**。直接検出は 3 件だが、SquadBeyond や Shopify theme 派生を含めると 7-8 件 |

R1 の偏りの原因: サンプル 30 件が **Shopify ブランド・D2C 特設中心** に寄っており、Kanebo/花王/Shiseido のような大手エンタープライズや、楽天出店型の古い LP が含まれていなかった。R2 で 66 件に拡大したことで、**化粧品 LP の真の重心は「レガシー jQuery + 画像組版 + Noto Sans JP」にある**ことが判明した。

---

## 10. 主要参照ファイル（絶対パス）

- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/489_www.jillstuart-beauty.com_ja-jp_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/8046_www.shiseido.co.jp_haku_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/10116_www.kanebo-cosmetics.jp_twany_lineup_special_240701_essence_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/10504_www.kanebo-cosmetics.jp_milano-collection_powder_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/12254_www.kanebo-cosmetics.jp_twany_lineup_special_20240801_time_r.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/8350_www.kanebo-cosmetics.jp_allie_technology_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/11286_decon-brand.com_pages_michiru_lp02_fv1_sb_tracking_true_utm_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/11533_sb-mitsuhada.ourservice.jp_ab_skincarepowder_subsc6_utm_medi.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/10573_cosmedy.jp_lp_u_sen04dt_fa01_sb_tracking_true_argument_ZB22X.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/12535_www.lucido.jp_campaign_facecare24aw_gold_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/11630_www.c-roland.co.jp_products_reluce_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/9880_www.wwdjapan.com_c_best-cosmetics__766.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/9552_etvos.com_lp_s-112_18_index_pen4.html.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/493_www.shiseido.co.jp_macherie_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/494_www.carjurajah.jp_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/491_stellaeye.jp_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/490_jp.rohto.com_mens-deou_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/12445_lp.aster-one.com_lp_kamikastf_tk_w_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/7744_www.rmsbeauty.jp_beautyoil_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/9364_www.sana.jp_honeyshca_.html`
- `/Users/oidekento/lp-corpus/raw_all/beauty-cosmetics/10120_borica.jp_serum-color-liner_sp_1.html`

---

（R2 作成日: 2026-04-08 / 対象: 66 件 / 更新: `analysis/beauty-cosmetics.md` 上書き）
