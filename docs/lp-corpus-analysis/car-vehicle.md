# 車・バイク・乗り物LP 分析レポート（Round 2 本格版）

対象: `/Users/oidekento/lp-corpus/raw_all/car-vehicle/` 配下 **全57サイト**
分析日: 2026-04-08
分析者: Claude (Opus 4.6 1M)
前回: 30サイト版 → 今回 57サイトに拡張、業態サブパターンを細分化

---

## 0. データソース

### 収録57件の内訳（URL別カテゴリ分類）

| # | ファイル | 業態サブカテゴリ |
|---|---|---|
| 1 | 10285_www2.nissan.co.jp_SP_90TH_ | OEM 周年キャンペーン（日産） |
| 2 | 11466_toyota.jp_info_thanks-from-toyota-cp_ | OEM 販促キャンペーン（トヨタ） |
| 3 | 11468_toyota.jp_info_crownsport_phev_ | OEM 車種ティーザー（トヨタ クラウンスポーツPHEV） |
| 4 | 11690_eizandensha.co.jp_kurama_90th_recommend | 鉄道 周年特集（叡山電車） |
| 5 | 11856_www.msi-azabulb.com_ | カーライフ専門店（MSI AZABU LABO） |
| 6 | 12574_mitsubishi-motors_delica_village_ | OEM コミュニティLP（デリカ村） |
| 7 | 2499_www.shm-afeela.com_ja_ | OEM EV新ブランド（ソニー・ホンダ AFEELA） |
| 8 | 2501_www.flexnet.co.jp_renoca_ | カスタム中古車（Renoca） |
| 9 | 2502_careers.denso.com_software_ | OEM系 採用（デンソー SW） |
| 10 | 2504_linkeeth | 法人テレマティクス（NTTドコモビジネス） |
| 11 | 2506_www.woven-city.global_jpn_ | OEM 先端都市（Toyota Woven City） |
| 12 | 2507_www.nissanmotor.jobs_japan_MC_ | OEM キャリア採用（日産） |
| 13 | 2508_www.suzuki.co.jp_car_lapin_ | OEM 車種LP（スズキ ラパン） |
| 14 | 2509_www.hxxxp.com_ | サイクルショップ（HODGE×PODGE） |
| 15 | 2512_cruise-kobe.com_ | 港湾クルーズ ポータル（神戸港） |
| 16 | 2514_www.toyota-battery.com_saiyo_ | OEM系 採用（トヨタバッテリー） |
| 17 | 2521_go-gx.com_ | 商用車GX事業（GO株式会社） |
| 18 | 2522_www.hyundai.com_jp_ | OEM 日本公式（ヒョンデ） |
| 19 | 2523_www.uber.com_jp_ja_ | 配車サービス（Uber Japan） |
| 20 | 2525_www.futuretrain.jp_ | 未来列車体験（FUTURE TRAIN） |
| 21 | 2526_sabus.jp_ | 移動型サウナバス（SABUS） |
| 22 | 2527_web.auto_ja_ | 自動運転プラットフォーム（Tier IV Web.Auto） |
| 23 | 2531_lifense.jp_ | 合宿免許（Lifense） |
| 24 | 2533_admore.w3.kanazawa-u.ac.jp_ | 大学 自動運転研究所（金沢大学 ADMORE） |
| 25 | 2536_careers.denso.com_graduate_ | OEM系 新卒採用（デンソー） |
| 26 | 2538_www.amano.co.jp_Parking_ | 駐車場システム（アマノ） |
| 27 | 2541_www.sumidenshoji.co.jp_recruit_ | 商社 採用（住電商事） |
| 28 | 2544_www.hellomobility.jp_ | シェアEV（HELLO MOBILITY） |
| 29 | 2546_arc-pds.com_ | ペーパードライバースクール（ARC） |
| 30 | 2547_www.mazda.co.jp_ | OEM 日本公式（マツダ） |
| 31 | 2548_www.pasmo.co.jp_mp_and_ | 交通系電子マネー（モバイルPASMO） |
| 32 | 2550_www.flexnet.co.jp_renoca_simulator_ | 3Dシミュレータ（Renoca） |
| 33 | 2551_www.ohizumi-ds.jp_ | 指定自動車教習所（大泉） |
| 34 | 2552_www.gran-turismo.com_jp_ | レースゲーム（グランツーリスモ） |
| 35 | 2556_www.centrair.jp_ | 空港公式（中部国際空港） |
| 36 | 2559_m-o-v.jp_ | タクシー配車アプリ（GO） |
| 37 | 2561_www.hellocycling.jp_ | シェアサイクル（HELLO CYCLING） |
| 38 | 2566_www.helloscooter.jp_ | シェアスクーター（HELLO SCOOTER） |
| 39 | 2569_www.toyota-monozukuri.jp_ | OEM 技能職採用 |
| 40 | 2574_www.gqjapan.jp_ | カーライフメディア（GQ JAPAN） |
| 41 | 2579_www.sride.jp_jp_ | タクシー配車アプリ（S.RIDE） |
| 42 | 2580_www.airbuggy.com_ | ベビーカー（AIRBUGGY） |
| 43 | 2582_www.hugme.co.jp_ | ベビーカー/キャリア（hugme） |
| 44 | 6659_nissan_SP_SAKURA_PAYMENT_ | OEM BEV 購入支援（日産サクラ） |
| 45 | 6829_kintetsu_cycletrain_ | 鉄道 特別企画（近鉄 サイクルトレイン） |
| 46 | 7357_secure.georgia.jp_mizukaze_ | 飲料タイアップ（ジョージア×みずかぜ） |
| 47 | 7976_nissan_CARHEATSTROKE_ | 社会貢献CP（熱駐症ゼロ） |
| 48 | 8159_toyota_tconnectservice_ | OEM コネクテッド（T-Connect） |
| 49 | 8561_nagaden_winevalley_ | 観光列車（北信濃ワインバレー） |
| 50 | 8803_nissan_CUSTOMIZE_NISMO_ | OEM カスタマイズ（NISMO） |
| 51 | 8894_www.maildealer.jp_lpl_md02 | メール共有SaaS（車業界利用訴求） |
| 52 | 9074_toyota-monozukuri（重複） | ─ |
| 53 | 9256_nissan_EVENT_PRIZE_ | OEM 懸賞キャンペーン |
| 54 | 9372_mitsubishi_mycarplan | OEM 残価クレジット商品LP |
| 55 | 9373_mitsubishi_star-camp_2018 | OEM オフ会イベント |
| 56 | 9385_mitsubishi_delica_d5_50th_photo | OEM 周年フォトLP |
| 57 | 9997_cycle.panasonic.com_gyutto_ | 電動アシスト自転車（パナソニック Gyutto） |

### 業態サブカテゴリ分布（57件中）

| サブカテゴリ | 件数 |
|---|---|
| OEM 車種/キャンペーンLP（トヨタ/日産/三菱/スズキ/マツダ/ヒョンデ/Sony Honda） | 19 |
| シェアモビリティ・配車アプリ（Uber/GO/S.RIDE/HELLO*） | 7 |
| 採用（OEM/Tier1/商社） | 7 |
| 中古車/カスタム/ディーラー | 3 |
| 自動車教習所/合宿/ペーパードライバー | 3 |
| 自動運転/研究/都市（Tier4/Woven/金沢大/Denso） | 4 |
| 鉄道/クルーズ/観光列車 | 5 |
| 駐車場/テレマティクス/交通電子マネー | 3 |
| ベビーカー/自転車/パーソナルモビリティ | 5 |
| メディア/ゲーム/飲料タイアップ | 3 |
| 計 | 59* |

*重複カウント（monozukuri ×2）あり

---

## 1. 統計サマリ

### 1-1. 配色 TOP10（全57HTMLからhex抽出、出現頻度順）

| 順位 | カラーコード | 出現数 | 主な用途 |
|---:|---|---:|---|
| 1 | `#ffffff` | 278 | 背景・反転文字 |
| 2 | `#e8e8e8` | 218 | UI境界・罫線グレー |
| 3 | `#000000` | 158 | 文字色・プレミアム系背景 |
| 4 | `#2b469c` | 102 | **紺ブランドカラー**（Uber系レガシー/教習所） |
| 5 | `#2d2d2d` | 85 | ダーク文字（黒に近いがわずかに淡い） |
| 6 | `#2c4198` | 62 | 紺系バリエーション |
| 7 | `#e3ebf6` | 58 | 淡いブルーグレー背景 |
| 8 | `#009fe7` | 55 | **プロセスブルー**（OEM/シェアモビ アクセント） |
| 9 | `#f3f3f3` | 51 | 薄グレー背景 |
| 10 | `#f4f4f4` | 40 | 薄グレー背景バリエ |

**補足で頻出する色**:
- `#e60020` (33) — 日産レッド系
- `#4db34c` (28) — エコ/ハイブリッド/シェアサイクル系グリーン
- `#0072bc` (27) — コーポレートブルー
- `#276ef1` (18) — **Uberブルー**（公式）
- `#d00075 / #cf3792 / #97005b` (17) — ピンク/マゼンタ系（女性向け車種 or PASMO系）
- `#f5f3f2` (34) — **オフホワイト**（LEXUS/マツダ魂動的な高級感）

**考察**: 車LP配色は **"白/黒/グレー + 1アクセント（紺 or 青 or 赤）"** が完全に定型化。原色の鮮やかさよりも、**写真・動画のメタリック感を殺さないニュートラル設計**。アクセントは企業CIカラー（日産赤/Uber青/ヒョンデ青）で、配色の個性はブランド識別記号として機能する。

### 1-2. フォント TOP10

#### Google Fonts 使用ファミリー（計35回検出）

| 順位 | family | 検出数 |
|---:|---|---:|
| 1 | `Noto Sans JP` | 15 |
| 2 | `Noto Sans` | 5 |
| 3 | `Noto Serif JP` | 4 |
| 4 | `Roboto` | 2 |
| 5 | `Poppins` | 2 |
| 6 | `Lato` | 2 |
| 7 | `Kosugi` | 2 |
| 8 | `Biryani` | 2 |
| 9 | `Zen Kaku Gothic New` | 1 |
| 10 | `Barlow / Montserrat / IBM Plex / Exo 2 / Crimson Text / Cormorant Garamond / Quicksand` | 各1 |

#### 商用/Typekit/FONTPLUS/OEM自社フォント

| タイプ | 検出サイト | 件数 |
|---|---|---:|
| **Adobe Fonts (use.typekit.net)** | Renoca, Web.Auto, Lifense, 住電商事, HELLO MOBILITY, Gran Turismo, HELLO SCOOTER, S.RIDE, 北信濃ワインバレー | 9 |
| **FONTPLUS** | go-gx.com, www.amano.co.jp/Parking | 2 |
| **TypeSquare**（fontplus同社系） | flexnet.co.jp/renoca（typesquare.com/accessor） | 1 |
| **OEM自社woff2 `brandfont.css`** | 日産全サイト（`/COMMON/GN2020/CSS/brandfont.css`） | 4 |
| **OEM自社 `MazdaTypeMedium`** | mazda.co.jp | 1 |
| **独自媒体フォント `GQSans`** | GQ JAPAN | 1 |
| **独自プロダクトフォント `UberMove`/`UberMoveText`** | Uber Japan（60回以上CSSに出現） | 1 |
| **次世代Next.js最適化woff2（`/_next/static/media/*.woff2`）** | Uber, Woven City, 未来列車, toyota-monozukuri, デリカD:5 50th | 5+ |

**考察**:
- **Noto Sans JP 一強**は変わらないが、「お金をかける場所」として車業界は **和文商用Webフォント** に投資する傾向が強い（9/57がAdobe Fonts、3/57がFONTPLUS/TypeSquare系）
- **OEMは独自フォントを資産化**: 日産 `brandfont.css`、マツダ `MazdaTypeMedium`、Uber `UberMove` はCI一貫性を超えて**プロダクト全体のタイポグラフィを1ファイルで掌握**する思想
- **Biryani は toyota-monozukuri（技能職採用）固有**: 通常のOEMではなくインドの欧文フォントを採用 → 工場の力強さ表現狙い
- レクサスだけは前ラウンドで `FONTPLUS fonts.fontplus.dev/v1/css/U8MhQyOR` 使用（今回の57件にはLexus不在）

### 1-3. ライブラリ・プラットフォーム使用率

| ライブラリ | 検出数 | 普及率 |
|---|---:|---:|
| jQuery | 28 | 49% |
| swiper | 15 | 26% |
| Next.js (`_next/static` / `__NEXT`) | 6+ | 11% |
| splide | 5 | 9% |
| barba.js | 4 | 7% |
| Vue.js / Nuxt (`_nuxt`) | 4 / 2 | 7% / 3% |
| React (生DOM出力含む) | 4 | 7% |
| bootstrap | 4 | 7% |
| Astro | 3 | 5% |
| GSAP | 3 | 5% |
| Lenis | 3 | 5% |
| AOS | 2 | 3% |
| **owl.carousel** | **0** | **0%** |
| tailwind (class直接出力) | 0 | 0% |

**考察 (前回30件との差分)**:
- **owl.carousel 消滅**: 前ラウンドでは Suzuki OEM系に見られたが、今回のSuzuki Lapinは`mf-search`（Marsflag）のみで carousel ライブラリに直接依存せず。OEMがオーガニック遷移の軽量化を進めた可能性
- **Next.js 普及拡大**: 前回5件 → 今回6件+ に。Woven City, Uber, 未来列車, toyota-monozukuri, デリカD:5 50th, Web.Auto と **「未来志向/ブランドサイト」系が全面Next化**
- **Astro** は採用/商用車GX系（デンソーSW採用近縁、go-gx.com）で定着
- **barba.js 4件** は全て「リッチなページ遷移演出」を必要とするサイト（デンソーSW採用、日産キャリア、HELLO CYCLING、Web.Auto）で、ハイエンドWeb制作の指標
- **jQuery 49% は高い**: 車LPは寿命が長く旧サイトも残る → 新規案件でも jQuery 互換を維持するケースが多い

### 1-4. CTAタイプ分布（キーワード出現サイト数）

| CTA種別 | キーワード | 検出サイト数 | 検出率 |
|---|---|---:|---:|
| 問い合わせ | "問い合わせ" | 22 | 39% |
| アプリ/ダウンロード | "アプリ" / "ダウンロード" | 14 / 9 | 25% / 16% |
| 無料（資料請求/試乗） | "無料" | 11 | 19% |
| 試乗 | "試乗" | 9 | 16% |
| 見積 | "見積" | 8 | 14% |
| 販売店（店舗検索） | "販売店" | 6 | 11% |
| 応募/エントリー | "応募" / "エントリー" | 6 / 3 | 11% / 5% |
| マイページ | "マイページ" | 3 | 5% |
| 資料請求 | "資料請求" | 3 | 5% |
| 店舗検索（地図） | "店舗検索" | 2 | 4% |
| デジタルカタログ | "デジタルカタログ" | 1 | 2% |
| カタログ請求 | "カタログ請求" | 1 | 2% |

**5大OEMヘッダー固定CTA**（カタログ/試乗/見積/店舗/マイページ）は **OEM公式サイトに限定** すると4〜5個が必ず同時に揃う定型。ただし57件全体で見ると「アプリDL」「問い合わせ」「応募」が分散し、**車カテゴリは必ずしも5大CTAが全てではない**ことが明確に。

**header固定 (`fixed` or `sticky`)**: 検出 11/57（約19%） — PC版では上部固定ヘッダーに5大CTAを並べる定型、SPでは下部固定フッターCTA or ハンバーガー収納に二極化。

### 1-5. アナリティクス・計測

| タグ | 検出数 | 備考 |
|---|---:|---|
| GA4 (`G-` prefix) | 45 | ほぼ全普及 |
| GTM (`GTM-`) | 33 | 58% |
| gtag | 14 | GA4直書き |
| Adobe Analytics / DTM | 12 | OEM定番（日産/マツダ/トヨタ） |
| Adobe Launch (`_satellite`) | 9 | ↑の後継 |
| Meta Pixel (`fbq` / facebook) | 4 / 27 | OGP経由のFBメタは27、実Pixel 4件 |
| Twitter/X (`twitter` / `x.com`) | 43 / 13 | 主にOGタグ経由 |
| TikTok Pixel | 4 | Uber/HELLO系 |

**考察**: OEM系は **Adobe Analytics + Adobe Launch** が完全定番。新興プロダクト系（Uber/GO/AFEELA/Woven）は GA4+GTM+Meta Pixel+TikTok の **D2C的オーディエンス作りスタック**。

---

## 2. 深読みケーススタディ（15件）

### 2-1. toyota.jp/info/crownsport/phev/ — クラウンスポーツPHEV「4つのファクト」
- **業態**: OEM 車種ティーザーLP（購入検討深掘り層向け）
- **行数**: 1,819行
- **プラットフォーム**: トヨタ共通CMS（`/pages/_system/common/`）＋ Tailwind風ユーティリティ（`pt-[98px]` `fixed inset-0` 等のJIT記法が出力済み）
- **フォント**: トヨタ共通 `tjp_common.css` 内で定義、Google Fonts不使用
- **共通CSS**: `tjp_reset.css` / `tjp_common.css` / `tjp_print.css` — **"印刷"用CSSを別読み込み**しているのが車業界の特徴（カタログ文化の名残）
- **セクション**: トヨタお馴染みの `#section1`..`#section4` アンカーナビ + PC左固定縦型メニュー（SVGの英字縦書き）
- **CTA**: `onclick="sc('toyotajp:tjp:crownsport_phev_anchor_1')"` — **Adobe Analytics `sc()` トラッキング関数** を全アンカークリックに埋める
- **特徴**: 「4つのファクト」という**知識系コンテンツフォーマット**。スペック訴求ではなく『読み物LP』。アンカー式サイト内誘導は車業界のローラー式構造

### 2-2. www.shm-afeela.com/ja/ — ソニー・ホンダモビリティ AFEELA
- **業態**: 新興EVブランド 公式
- **プラットフォーム**: 独自SSR + Web Components (`<script type="module" src="/components/web-lib.js">`) — 新興ブランドらしいヘッドレス構成
- **フォント**: `/share/v2.0/common/css/font.css` + `/share/v2.0/common/js/fonts.js` の**自社フォントローダー**（Honda/Sonyどちらかの和文プロプラ）
- **スタイル分割**: `swiper.css` 専用、`style.css`, `pages/top/css/style.css`, `pages/discover/css/style.css` — **SPAのようなルート別CSS分割**
- **Cookie同意**: **OneTrust `cookielaw.org`** — グローバル基準（EU/CCPA対応）
- **キャッチ**: 「知性を持った存在として人がモビリティを感じること」→ **体験価値の宣言型トップ**。スペックも試乗もカタログも一切出さない
- **特徴**: **"新車発表前のビジョン共有LP"** という独自カテゴリ。クラウンスポーツが「ファクト」なら AFEELA は「フィロソフィー」

### 2-3. www.mazda.co.jp/ — マツダ オフィシャル
- **業態**: OEM 日本公式トップ
- **プラットフォーム**: **Episerver (Optimizely) CMS**（`data-mdp-ref` 属性が目印、`/assets/styles/addons.css?v=10.0.1.24889`）
- **レンダリング**: サーバーで React SSR された DOM を **静的HTMLとして配信**（`data-reactroot` 複数、`Radium` による inline style）
- **フォント**: `MazdaTypeMedium` + Noto Sans CJK JP フォールバック（`font-family: MazdaTypeMedium,Noto Sans CJK JP,Hiragino Kaku Gothic ProN,...`）
- **ナビ構造**: `Header / GlobalNavigation / PrimaryNavigation / SiteSearch / MyMazda` の独立コンポーネント（各々 BEM 的 `Header__layout2-right` 命名）
- **Hero**: `HeroCarousel`（Slick 0.x DOM出力：`slick-slide slick-active slick-current`）
- **CTA**: **販売店 / 中古車 / リコール情報 / ニュースリリース / 問い合わせ/FAQ / 企業・IR・採用** — 「中古車」「リコール」をグローバルナビに置くのはOEM共通（オーナー保護）
- **PC幅固定対応**: UAスニッフィングで iPad/Android タブレット時は `width=1024px` に強制 → **車LPはタブレット最適化が未だに生きている**

### 2-4. www.suzuki.co.jp/car/lapin/ — スズキ ラパン／ラパンLC
- **業態**: 軽自動車 OEM 車種LP
- **行数**: 1,886行
- **プラットフォーム**: 独自CMS + **Marsflag検索** (`mf-search`)
- **フォント**: Google Fonts `Hind` + `Noto Sans` (前回と同じ思想、Noto Sans JPではない)
- **スクリプト**: owl.carouselは消滅。現在はスズキオリジナルCSSのみ
- **特徴**: 女性向け車種 (`#ededed` ベージュ系) でありながらCIの「スカイブルー」は維持、スペーシアLP（男女両性）と差別化

### 2-5. www.hyundai.com/jp/ — ヒョンデ日本公式
- **業態**: OEM再参入ブランド（2022〜）
- **プラットフォーム**: WordPress（Hyundai本国ヘッドレスの可能性あり）
- **Meta des**: **「新型スモールEV INSTER の車両情報をはじめ、実施中のイベント・キャンペーンや見積り、試乗予約についてご確認いただけます。｜Hyundai Mobility Japan」** → meta description自体がCTAのショーケース
- **ブランド表記**: 日本語ブランド名を **"ヒョンデ"** に統一（2022年リブランディング）
- **CTA**: 見積り / 試乗予約（OEM定型の5大うち2つ）
- **特徴**: 「Hyundai Mobility Japan」として **会社名にMobility を含める** 新興参入組の戦略。車を売るのではなく「モビリティ事業者」を名乗る

### 2-6. www.uber.com/jp/ja/ — Uber Japan
- **業態**: 配車/デリバリー統合プラットフォーム
- **行数**: 667行（Next.js のSSR 出力）
- **プラットフォーム**: **Next.js**（`_next/static` パス多数）
- **フォント**: **`UberMove` / `UberMoveText` 自社プロプラ**（CSSに60回以上出現）→ `font-family:UberMoveText, system-ui, ...` が本文、見出しは `UberMove, UberMoveText, system-ui`
- **アクセント色**: `#276ef1` (Uberブルー) 18回出現
- **構造**: `<title>search` が複数あることから、**SEO用セクションごとの自動タイトル生成**が行われている
- **2大LP統合**: 「運転して収入を獲得、または今すぐ配車をリクエスト」と **ドライバー採用と乗客獲得を1トップで並列訴求** する世界標準構造

### 2-7. m-o-v.jp（GO タクシーアプリ） — GO株式会社
- **業態**: タクシー配車アプリ（旧MOV + 旧JapanTaxi統合ブランド）
- **行数**: 125行（Nuxt SSG が極限まで圧縮）
- **プラットフォーム**: **Nuxt.js**（`data-n-head=ssr` 属性で確定）
- **Meta des**: **「今なら新規ダウンロードで500円OFFクーポンプレゼント中！」** → trim末、**オファーをメタタグ内でも訴求**（SERP上でのクリック率最適化）
- **旧ユーザー誘導**: 「"JapanTaxi" "MOV" のお客様は、今後 "GO" をご利用ください」とbrandingのmigration告知
- **特徴**: アプリDL誘導に全振り、Webでの予約機能を排除（アプリ専用）

### 2-8. www.sride.jp/jp/ — S.RIDE タクシー
- **業態**: タクシー配車アプリ（東京4社連合）
- **プラットフォーム**: 独自静的 + **Typekit `pau6rxs.css`** + Google Fonts Noto Sans JP + Noto Sans
- **ライブラリ**: GSAP + swiper + Adobe Fonts（モダンスタック3種併用）
- **構造**: iOS向け meta 全サイズ touch-icon プリセット、`apple-mobile-web-app-capable` **PWA対応フラグ**
- **特徴**: タクシー配車アプリ3社（Uber / GO / S.RIDE）で **フォント戦略** がはっきり分岐：Uber=自社プロプラ / GO=システムフォント / S.RIDE=Adobe Fonts → 企業文化の反映

### 2-9. www.hellomobility.jp / www.hellocycling.jp / www.helloscooter.jp — HELLO シリーズ
- **業態**: シェアモビリティ3プロダクト（EV / 自転車 / スクーター）
- **プラットフォーム**: 共通UIシステム（親会社 OpenStreet）
- **フォント**: **Typekit `kitId: 'qul5pcu'`**（全HELLOプロダクト共通）— 遅延ロード付き（`wf-loading` → `wf-inactive`）
- **ライブラリ**: HELLO MOBILITY → swiper / HELLO CYCLING → **barba.js + Lenis**（最上位プロダクト）/ HELLO SCOOTER → Typekit のみ
- **共通Loading UI**: 「携帯電話をタップする」アニメーションを全サイトで統一（`loading-phone-container > loading-phone` + swiper内蔵）
- **特徴**: **プロダクト間のブランドDNA統一** を Webfont + Loading UI で実現した好例。3サイト並行運用LPデザインシステムのリファレンス

### 2-10. www.woven-city.global/jpn/ — Toyota Woven City
- **業態**: トヨタの未来都市プロジェクト公式
- **プラットフォーム**: **Next.js**（`_next/static/media/` 大量woff2）
- **特徴**: 「未来を想像する」タイプの完全ブランドLP。CTAは試乗でもカタログでもなく **"Learn More"** 型。OEMであっても車種を売らない方向性

### 2-11. web.auto/ja/ — Tier IV Web.Auto（自動運転プラットフォーム）
- **業態**: 自動運転SaaSプラットフォーム（B2B）
- **プラットフォーム**: **Next.js + barba.js（ページ遷移演出）+ Typekit**
- **フォント**: Typekit（ダークブルー×グレーのエンジニアリング美学）
- **特徴**: オープンソース自動運転 Autoware の商用化版。LPは **"開発者/エンタープライズ向け"** にシフトし、車業界の中で最も"SaaS然とした"UI

### 2-12. www.flexnet.co.jp/renoca/ — Renoca（リノベーションカー）
- **業態**: 中古車ベースのカスタム車ブランド
- **行数**: 約3000行規模
- **プラットフォーム**: **WordPress + Next.js（カスタマイザー別途）+ TypeSquare + GSAP + Typekit**
- **フォント**: Google `Crimson Text` + `Noto Sans JP 700` + TypeSquare(typesquare.com/accessor)
- **GTM二重設定**: `GTM-KDQLKZZP` と `GTM-N65QHH9` 両方読み込み（Renoca単体 + FLEX本体の2層計測）
- **Facebook Pixel**: 有効
- **特徴**: **"自分だけの1台"** を軸に、シミュレーター LP (`/renoca_simulator/`) をSPA別ドメイン化 → **WordPressの記事系 + Next.jsのインタラクション系 を明確に分けた構成**

### 2-13. careers.denso.com/software/ — デンソー ソフトウェア採用
- **業態**: Tier1部品メーカー 採用サイト
- **プラットフォーム**: 独自静的 + **barba.js + Lenis + Splide**（モダンWeb制作スタック）
- **viewport トリッキー処理**: iPad/Android タブレット検出時に `new ViewportExtra(1180)` で強制1180幅 → **PC専用デザインを1180pxで最適化**（自動運転/制御系エンジニアPCユーザー想定）
- **Dark Mode**: `theme-color: #0e0e0e` 指定
- **data-barba**: `data-barba="wrapper"` ルート + ページ遷移ブロック
- **特徴**: 採用サイトなのに **"プロダクト級"** の演出。ソフトウェア人材獲得にUI/UX投資を惜しまないスタンス

### 2-14. go-gx.com — GO株式会社 脱炭素GX事業
- **業態**: タクシー配車のGO（m-o-v.jp）がEV/脱炭素ソリューションを法人向けに展開
- **プラットフォーム**: **Astro + Splide + FONTPLUS**
- **フォント**: FONTPLUS（高級感重視の和文）
- **CTA**: 法人企業の脱炭素サービス紹介 → 問い合わせフォーム誘導型
- **特徴**: **コンシューマーアプリとB2Bサイトで別ブランド・別スタック運用**（Nuxt vs Astro）

### 2-15. 2502/2536 デンソー採用 × 2569 トヨタ技能職 × 2514 トヨタバッテリー
- **OEM/Tier1採用サイト群の共通点**:
  - すべて **swiper または splide** でグレードスライダー的にスタッフボイスを見せる
  - **トヨタ技能職** (Next.js) は **Biryani フォント** で「ものづくりの力強さ」を欧文で表現（Noto Sans JP と併用）
  - **トヨタバッテリー** (`saiyo`) は **Astro + Next.js + swiper** の3スタック混成（サブドメイン構成）
  - **日産キャリア** は barba.js + splide で**ページ遷移にホワイトマスクアニメ**

---

## 3. 業態別サブパターン（10カテゴリ）

### 3-A. OEM 車種/キャンペーンLP（19件、33%）
- **標準テンプレ**: KV動画 or 大判写真 → 4〜6ファクト/ストーリー → グレード・価格 → ADAS/安全 → 販売店検索 → CTA集約フッター
- **フォント**: 自社ブランドフォント（日産 brandfont.css、マツダ MazdaTypeMedium）＋ Noto Sans CJK JP フォールバック
- **計測**: Adobe Analytics DTM/Launch が必須
- **CTA**: 5大（カタログ/試乗/見積/販売店/マイページ）の **ヘッダー固定** が定型。デリカ村のようなコミュニティLPだけ例外的にCTAレス
- **スペック脚注嵐**: 全HTMLで `※` が平均 ~15回出現、燃費・価格・乗員人数・寸法に全て注記付き（PL法・景表法対応）
- **印刷用CSS**: 車業界は `tjp_print.css` のような **印刷CSSを別ファイルで持つのが残存（カタログ印刷文化の名残）**

### 3-B. ディーラー / 中古車 / カスタム（3件）
- **Renoca / MSI AZABU LABO / HODGE×PODGE**
- **WordPress率 100%**（woocommerce入っているケースもあり）
- **CTA**: LINE予約、電話、問い合わせフォーム — 個人事業規模も多く、OEMと比べCTA設計が素朴
- **フォント**: Google Fontsのみで済ませる vs Typekit + TypeSquareを併用するRenocaの二極

### 3-C. 試乗/体験/ショールーム
- **OEM内に統合**されており独立カテゴリサイトは少ない
- キャッチコピー頻出: 「見て、触れて、感じて」「あなたの一台に会いにきて」

### 3-D. 自動車保険
- **本57件には保険単独サイトなし**（別カテゴリ finance-insurance に所属）
- 一部OEMページ内で自動車保険のバナーが差し込まれている程度

### 3-E. 教習所（3件）: Lifense / 大泉DS / ARC ペーパー
- **共通点**: 合宿/通学/ペーパードライバーで **訴求軸が完全に分岐**
- Lifense（合宿）: Typekit + WordPress + "滞在型"押し、**若者向けデザイン**（食事・レジャーの写真多数）
- 大泉（通学）: 軽WP + 地元アクセス訴求（西武池袋線大泉学園駅から徒歩5分）
- ARC（ペーパー）: WP + swiper、**「名古屋・愛知・岐阜・三重の運転講習」**でローカルSEO訴求
- **共通CTA**: 資料請求/お申込み/料金表PDF/LINE
- **決済**: 分割ローン案内・カード対応など、スクール独特の金融訴求

### 3-F. シェアモビリティ / 配車アプリ（7件）
- **全員アプリDL がKPI**
- **フォント戦略で差別化**: Uber=自社 / GO=システム / S.RIDE=Typekit / HELLO=Typekit共通
- **Loading UI に個性**: HELLO系の「タップする電話」アニメが好例
- **CTA集約**: App Store / Google Play バッジ2個 + QRコード が最下部固定

### 3-G. タクシー/ライドシェア（Uber/GO/S.RIDE 3件）
- 「運転手募集」と「お客様利用」の **二面LP** が標準
- GO は旧ブランド（MOV / JapanTaxi）からの**ブランド移行告知**が残っている

### 3-H. 自動運転/研究/未来都市（4件）: Web.Auto / Woven / ADMORE / GX
- **全てNext.js or Astro** の **"SaaS/エンタープライズ級"** UI
- フォント: Typekit / FONTPLUS多用 → **"エンジニアリングの誠実さ"をタイポで語る**
- KPI: 採用応募 or 問い合わせフォーム（CVRより**認知度**重視）

### 3-I. 駐車場/テレマティクス/交通IC（3件）: アマノ/LINKEETH/PASMO
- **B2B駐車場（アマノ）** は FONTPLUS を採用、法人カタログのような堅実なUI
- **LINKEETH (NTTドコモビジネス)** は B2B SaaS と車業界の交差点、NTT共通テンプレート
- **モバイルPASMO** は iPhone/Android切り替えボタンありの**プラットフォームLP**

### 3-J. 自転車/ベビーカー/パーソナル（5件）: airbuggy/hugme/HODGE×POD/Gyutto/9997
- **airbuggy (WP+swiper)**: GMPインターナショナル、description 文字数150字超える長尺SEO
- **hugme (swiper)**: mamaとパパ訴求、エアバギーよりもカジュアル
- **Panasonic Gyutto**: jQueryベースの伝統的WP、商品ランアップ比較表中心
- **特徴**: 「安全」「軽量」「3輪」「エアタイヤ」が差別化軸、**乗り物カテゴリだがCVが"店舗一覧"**

### 3-K. 鉄道/クルーズ/観光列車（5件）: 叡山電車/近鉄サイクルトレイン/ワインバレー列車/神戸クルーズ/センレア
- **叡山電車**: WordPress、周年特集ページ
- **近鉄サイクルトレイン**: 単一施策ページ、**CTA=運行日カレンダー**
- **北信濃ワインバレー列車**: Typekit + jQuery、**「ワインを飲みながら車窓の旅」** という体験ラグジュアリー
- **神戸港クルーズ (WP+Lenis+Splide)**: ポータル構造で複数クルーズ船をまとめる
- **特徴**: **体験型旅の"乗り物LP"**という独特の立ち位置。travel-hotel カテゴリと重なるが**車両そのもの**を主役化する

### 3-L. その他（GQ/Gran Turismo/メディア/飲料タイアップ）
- **GQ JAPAN**: メディアサイトだがカテゴリ「高級車」でヒット、独自フォント `GQSans`
- **Gran Turismo**: レースゲームでTypekit使用
- **ジョージア×みずかぜ**: コカ・コーラの飲料LPが「トワイライトエクスプレス瑞風」と**タイアップ** → タイアップで車両カテゴリに流入
- **メールディーラー**: SaaSだが車業界顧客向けセクションがあり検索ヒット
- **特徴**: 「乗り物」カテゴリは **ノイズも多い** が、それぞれ**車両文化との接点**を持ちブランド価値に利用

---

## 4. 共通パターン

### 4-1. 全体構造の定型
```
Hero（大判動画/写真 + コピー1〜2行）
  ↓
4〜6項目のファクト/USP（アイコン + 見出し + 短文）
  ↓
ストーリー/技術訴求（スクロールテリング or タブ切替）
  ↓
ラインナップ/グレード比較（swiper / splide / 自社carousel）
  ↓
信頼指標（販売台数、受賞、○年保証、No.1）
  ↓
ADAS/安全装備独立セクション
  ↓
販売店検索 + News/FAQ
  ↓
固定フッター5大CTA or アプリDLバッジ
```

### 4-2. Viewport戦略
- **PC幅固定 1180px**（デンソー採用）や **1024px強制**（マツダ）など、**iPadをPCデザインで表示** させる指定が残る
- モバイルは `viewport fit=cover` + Safe Area 対応

### 4-3. 計測二重化
- OEM: **Adobe Analytics + GA4** の二重計測（DTM/Launch）
- 新興: **GTM + Meta Pixel + TikTok Pixel** のD2Cスタック
- B2B車系: **GA4 + Marketo/HubSpot**（LinkedIn Insight含む）

### 4-4. フォントローディング戦略
- `<link rel="preconnect" href="https://fonts.googleapis.com">` + `crossorigin` 2段構え
- Typekit は **非同期ローダー `(function(d){...})(document)`** パターンが今も主流（Adobe Fonts推奨の古い方法）
- OEM自社フォント: 単純`<link>`先読み + FOUT許容

### 4-5. CTAの細分化
前ラウンドで導出した5大CTAは **OEM車種LP限定** で完結する定型だが、57件全体での実態は:
- **OEM車種LP（19件）**: 5大CTA固定 ～ カタログ/試乗/見積/販売店/マイページ
- **シェアモビリティ（7件）**: アプリDLバッジ2個 + QR
- **採用（7件）**: エントリー/マイページ/募集要項PDF
- **観光・体験列車（5件）**: 予約（運行日カレンダー）/ チケット購入
- **B2B（3件）**: 資料請求 / 無料相談 / デモ予約
- **中古車/カスタム（3件）**: LINE / 問い合わせフォーム / 電話

---

## 5. 新発見（前回30件版からの差分）

### 5-1. 「乗り物」カテゴリは **7業態のパッチワーク**
前ラウンドで「モビリティ全域に広がる」と推測した通りだが、57件で拡張すると:
- **OEM 33%（19件）**
- **シェア配車 12%（7件）**
- **採用 12%（7件）**
- **鉄道/クルーズ/観光列車 9%（5件）**
- **パーソナル/自転車/ベビーカー 9%（5件）**
- **自動運転/未来 7%（4件）**
- **中古/カスタム 5%（3件）**
- **教習所 5%（3件）**
- **B2B (駐車場/テレマ/IC) 5%（3件）**
- **その他 4%（3件）**

→ **"乗り物"ラベルはあまりに広すぎ、LP分析を一色に塗るのは不可能**。サブパターン別の設計ルールが必須。

### 5-2. owl.carousel の完全消滅
前ラウンドで Suzuki OEM系の定番として言及したが、今回の57件では **0件**。swiper/splideに完全に置換されたか、OEM独自carouselに移行済み。**2024〜2026にOEMがフロントエンド技術を更新**した象徴。

### 5-3. Next.js + 自社woff2 の台頭
- Woven City / 未来列車 / toyota-monozukuri / Web.Auto / Uber / デリカD:5 50th → すべてNext.js
- `_next/static/media/*.woff2` の大量woff2プリロードは **Next.js `next/font/local`** の仕組みが標準化された証拠
- **2026年のOEM新規案件はNext.js + 自社フォント localファイル化が標準**

### 5-4. 商用Webフォント投資率の高さ
Typekit(Adobe Fonts) 9件 + FONTPLUS 2件 + TypeSquare 1件 + OEM自社 5件 = **30% 近くが有料Webフォント**
- 他カテゴリと比較して **車は"高級感と信頼感"への投資意識が高い**
- 特に**シェアモビリティ共通Typekit運用**（HELLOシリーズ共通 `kitId: qul5pcu`）は **ブランド資産管理のベストプラクティス**

### 5-5. B2B/SaaSへの越境
- **Tier IV Web.Auto** は自動運転SaaS
- **LINKEETH (NTTドコモビジネス)** はテレマティクスSaaS
- **アマノ Parking** は駐車場管理SaaS
- **メールディーラー** はカスタマーサポートSaaSだが車業界セグメントで流入
→ **"モビリティ×SaaS"が独立カテゴリ化**。LP設計は「問い合わせCVR最適化」に寄り、OEM文化とは別物

### 5-6. 印刷CSSが残存
`tjp_print.css` (Toyota) / マツダも print 用 CSS を別読み込み — **カタログ文化の名残** で、他カテゴリではほぼ絶滅した「印刷用CSS」が車業界には残存。

### 5-7. タブレット強制1024/1180幅
マツダ (1024) / デンソー採用 (1180) が現役 — **車業界の顧客には車内ディスプレイ/iPad商談機がある** ことを想定したUA分岐が今も残る。

### 5-8. ヘッダー固定率は意外と低い（19%）
前回想定では「OEMのヘッダー固定5大CTA」を主要パターンと見ていたが、57件中 `fixed/sticky` ヘッダーは **11件のみ**。**多くは初期は大判Heroにスクロール追従せず、スクロール開始時点でJSでsticky化** する実装 → 静的HTMLへの出力だとclass名からは検出しきれない。

### 5-9. ADASブランド名の独自化が進行
- トヨタ "Toyota Safety Sense" / スズキ "SUZUKI Safety Support" / 日産 "ProPILOT" / ホンダ "Honda SENSING" / マツダ "i-ACTIVSENSE" / ヒョンデ "HYUNDAI SMARTSENSE"
- **今回の57件ではこれらの独自ブランド名を直接検出できない**（キャッシュ時点の簡略化LPだった or `※` 脚注内のみ記載）
- 一方で **「衝突被害軽減」** のような法律用語は1件でヒット → **ADASはブランド名 > 技術用語 の優位性がある**

---

## 6. design-mcp 使用方針（更新版）

### 6-1. テンプレート選定ガイド

| サブカテゴリ | 推奨 design-mcp テンプレ | 色調 | フォント |
|---|---|---|---|
| OEM 車種LP | `luxury-hero-story` 系 + `spec-comparison-table` | 白/黒/グレー + CIアクセント | Noto Sans JP + 英字Condensed系 |
| OEM キャンペーンLP | `event-countdown` + `form-embed` | CIアクセント強め | Noto Sans JP + Barlow Condensed |
| OEM ブランドストーリー | `editorial-scroll` + `full-bleed-media` | モノトーン | 自社プロプラ or Typekit |
| シェアモビ/配車 | `app-download-hero` + `store-badges` | CI1色アクセント | Typekit or sans-serif |
| 採用 | `recruit-narrative` + `interview-slider` | ブルーグレー | Noto Sans JP + Biryani |
| 中古/カスタム | `product-catalog-grid` + `faq-accordion` | 黒+木目/写真 | Crimson Text + Noto Sans JP |
| 教習所 | `local-business-hero` + `pricing-table` | 若者向け | Kosugi or Zen Kaku |
| 観光列車 | `travel-gallery` + `booking-calendar` | 写真フル幅 | Noto Serif JP |
| 自動運転/B2B | `saas-landing` + `case-study` | ダークブルー | Typekit欧文 |
| パーソナル/自転車 | `product-showcase` + `comparison-matrix` | パステル+写真 | Poppins + Noto Sans JP |

### 6-2. 配色トークン

```yaml
tokens:
  color:
    neutral:
      white: "#ffffff"
      off_white: "#f5f3f2"   # LEXUS/マツダ高級系
      grey_50: "#f4f4f4"
      grey_100: "#e8e8e8"
      grey_300: "#bdbdbd"
      grey_700: "#4d5859"
      grey_900: "#2d2d2d"
      black: "#000000"
    brand_accent:
      nissan_red: "#e60020"
      uber_blue: "#276ef1"
      hyundai_blue: "#009fe7"
      hello_green: "#4db34c"
      corporate_navy: "#2b469c"
      pasmo_pink: "#d00075"
```

### 6-3. フォント選定フロー

```
[車LP作成リクエスト]
  ↓
OEM公式？ → YES → 自社ブランドフォント推奨 (+ Noto Sans CJK JP fallback)
  ↓ NO
B2B/SaaS？ → YES → Typekit or FONTPLUS
  ↓ NO
中小ディーラー？ → YES → Google Fonts (Noto Sans JP + Barlow Condensed)
  ↓ NO
シェアモビ/アプリ？ → YES → Typekit (HELLO系) or 自社woff2 (Uber系)
```

### 6-4. レイアウト指針（車LP特有）

1. **Hero は大判（16:9 以上）**、動画 + オートループ、ポスター画像はJPEG 1920×1080
2. **USPは4〜6項目**、3項目以下だと物足りない印象（スペック文化）
3. **比較表は必須**（グレード / 競合 / 燃費）— swiper-less な素の tableが多い
4. **脚注 `※` は全ての数値に**（燃費/価格/乗員/寸法/安全性能）— 景表法対応必須
5. **ADAS は独立セクション**、OEM独自ブランド名を大きく打ち出す
6. **販売店検索は地図モーダル** or 別ページへのリンク（車LPでは地図APIを直接埋めず、別システム連携）
7. **マイページ/ログイン** はPC右上の定位置、SPでは非表示 or ハンバーガー内

### 6-5. アンチパターン

- **カートCV直付けNG**: ECのような「カゴに入れる」は車LPに存在しない。必ず**資料請求→試乗→商談**のファネル
- **スペック表を画像化するのはNG**: テキスト選択可能にする（コピペで比較する購買行動に対応）
- **ローマ字企業名の小文字多用**: OEMでは小文字化は避ける（LEXUSは全大文字、NISSAN/TOYOTAも大文字）
- **ド派手な原色多用**: 車の金属感を殺す。必ずニュートラルベース + 1アクセント
- **印刷を想定しない設計**: 車業界のBtoC営業フローでは**印刷して渡す**文化が残るため、印刷CSSを用意

---

## 7. まとめ

### 7-1. 車・バイク・乗り物LPの本質

- **"乗り物"は業態ラベルではない**。実態は OEM / シェア / 採用 / 鉄道 / 中古 / 教習 / 自動運転 / パーソナル / B2B の **9業態が1カテゴリに同居**
- 各業態で **主CV・CTA・フォント戦略・計測スタックが別物**。統一テンプレは存在しない
- それでも共通するのは **「品質と信頼」を支えるニュートラル配色 + 高機能Webフォント投資 + スペック脚注文化**

### 7-2. 次ラウンドで掘るべき論点

1. **Honda Global / Lexus（今回57件に不在）** の独自フォントcss の設計詳細
2. **Adobe Launch の car業界タグ設計** — clickイベント命名規則（`sc('toyotajp:tjp:crownsport_phev_anchor_1')`）
3. **OEM共通フッター構成** — news / recall / IR / カタログ請求 の配置順序
4. **ADASブランドLPセクション**のHTML構造（今回は単純簡略版のためデータ不足）
5. **「試乗予約」フォームのフィールド設計** — 日時/店舗/車種/名前/電話/免許有無 のどこまで事前入力させるか

### 7-3. design-mcp への入力例

```yaml
brief:
  category: car-vehicle
  subcategory: OEM_model_page  # 9業態から選択
  brand:
    name: "Example Motors"
    primary_color: "#e60020"
    logo_kind: "wordmark"
  content:
    hero_copy: "走る、という歓び"
    usp_count: 5
    has_adas_section: true
    has_spec_table: true
    has_dealer_finder: true
    cta:
      - カタログ請求
      - 試乗予約
      - オンライン見積り
      - 販売店検索
      - マイページ
  constraints:
    require_print_css: true
    require_fonts_jp_premium: true  # 自社 or Typekit
    require_footnotes_marker: "※"
    tablet_fixed_width_px: 1180  # or null
```

---

**(End of Round 2 car-vehicle analysis — 57 sites, 2026-04-08)**
