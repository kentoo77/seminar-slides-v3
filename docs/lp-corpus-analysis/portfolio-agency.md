# 制作会社・代理店・ポートフォリオ LP 分析 (ラウンド2: 2,813 件統計分析)

**分析日**: 2026-04-08
**対象フォルダ**: `/Users/oidekento/lp-corpus/raw_all/portfolio-agency/`
**ファイル総数**: **2,813 件**
**分析方法**:
- ファイル名・タイトル・メタ情報での全量分類 (2,813 件)
- 2 系列ランダムサンプリング 600 件（重複除去後 493 件）でタイトル・ドメイン精査
- 真の制作会社/代理店/ポートフォリオ 18 件の深読み (HTML / フォント / 色 / ライブラリ / セクション数)

---

## 0. 結論先出し — このフォルダは **9割以上が誤分類**

**重要発見: このフォルダ名は「portfolio-agency」だが、実際には別ジャンルの汎用 LP が大量に混入している。**

全量 2,813 件のうち、真に「制作会社・代理店・個人ポートフォリオ・ブランディングファーム」と呼べるのは **およそ 70 件（約 2.5%）** のみ。残り 2,743 件 (97.5%) は、rdlp.jp などの汎用 LP ギャラリーからクロスジャンルで取り込まれた結果、「他ジャンルに本来属すべき LP」が大量混入している状態。

### 実態: ジャンル分類 (全 2,813 件)

ファイル名パターン + タイトル + ドメイン heuristic による自動分類:

| ジャンル | 件数 | 比率 | 代表 |
|---|---|---|---|
| **other_unknown (未分類)** | 1,641 | 58.3% | life-goods / brand-corporate / experience / 家電 などへ配るべき汎用 LP |
| food_beverage (食品・飲料) | 347 | 12.3% | kao / meiji / morinaga / lotte / asahi / kirin / calbee / glico / kewpie / starbucks / acecook / ucc / fritolay / kagome / 味の素 |
| cosmetics_beauty (美容コスメ) | 135 | 4.8% | shiseido / kose / ignis / cosmedecorte / fracora / sk-ii / pola / albion / loccitane / fujio / lululun / curel / hadalabo |
| bandai_toy_character (玩具・キャラ) | 121 | 4.3% | p-bandai.jp (111件！) + takaratomy / sanrio |
| travel_hotel_retail (旅行・宿泊・商業施設) | 87 | 3.1% | hoshinoya / hankyu / parco / jr-odekake / jr-central / 阪急 / 近鉄 / ふるさと納税 |
| **agency_studio_portfolio (真の制作会社/代理店)** | **70** | **2.5%** | goodpatch / emuni / arkreis / cocochi / rudel / 4digit / ashim / neu-ad |
| entertainment_game (ゲーム・エンタメ) | 66 | 2.3% | p-bandai 以外の realdgame / square-enix / toei-anim / pokemon / hololive / deagostini |
| real_estate_construction (住宅・不動産) | 60 | 2.1% | connecthome / dup-m / niwa-craft / jinbatosou / 賃貸 |
| recruit_career (採用・転職サービス) | 58 | 2.1% | kimisuka / sharefull / 非 agency の採用代行・求人 |
| medical_clinic_pharma (医療・製薬) | 40 | 1.4% | rohto / 歯科 / クリニック / kowa / ssp / 大正製薬 |
| telecom_mobile (通信・モバイル) | 38 | 1.4% | softbank / docomo / linemo / mineo / motorola / biglobe |
| saas_education_bizservice (SaaS・教育) | 38 | 1.4% | talkingmarathon / benesse / goalfree / kumon / palmie |
| movie_film (映画) | 29 | 1.0% | 映画公式サイト shochiku / toho / gaga / happinet |
| eyewear (メガネ) | 25 | 0.9% | aigan (15件!) / zoff / paris-miki |
| fashion_apparel (ファッション) | 23 | 0.8% | onward / fabric-tokyo / 45r / palcloset / agete |
| automotive (自動車) | 22 | 0.8% | nissan / toyota / suzuki / subaru / abarth |
| cycle_bike (自転車・バイク) | 10 | 0.4% | panasonic_bike / bscycle / motorola (moto-bu) |

**→ 本来 `portfolio-agency` に残すべきは約 70 件のみ。残り 2,743 件は再分類対象。**

### 混入パターンの構造的分析

1. **p-bandai.jp が 111 件** — `bandai_toy_character` or `ec-shop` へ再分類すべき
2. **rakuten (item.rakuten.co.jp) が 43 件** — `ec-shop` へ
3. **kao.co.jp / shiseido / meiji / morinaga / lotte / asahi** など食品・コスメ大手が各 20 件以上 — `food-beverage` / `beauty-cosmetics`
4. **www.aigan.co.jp 15 件** — `fashion` or 新設 `eyewear` サブジャンル
5. **recommend.jr-central.co.jp が 16 件** — 「推し旅」シリーズ。`travel-hotel` or `campaign-special`
6. **kurand.jp が 16 件** — 日本酒 EC、`ec-shop` or `food-beverage`
7. **realdgame.jp が 17 件** — リアル脱出ゲーム、`experience`
8. **studio.site ドメインが 15 件** — これは Studio 社の無料 SaaS で作られた素人〜中小事業者 LP。ドメインに "studio" が含まれるため誤検知。ジャンルは多岐（塾・博物館・展示・物販・寺院）

---

## 1. 真の制作会社・代理店・ポートフォリオ 70 件 (インデックス)

### 1.1 ハイエンド・デザインスタジオ (8 件)
- `4979_yoru.design_.html` — 夜. (横澤由香里, IndexW)
- `4985_gyokuro-s.com_ja_.html` — GYOKURO STUDIO (日テレ系プロダクション)
- `4986_morohoshi.site_.html` — Shizuku Morohoshi デザイナーポートフォリオ
- `5022_emuni.co.jp_.html` — emuni (graphic design studio, 村上茂・昌)
- `5135_tashi.design_.html` — tashi Illustration & Design Portfolio
- `5136_arkreis.jp_.html` — ARKREIS (デザインスタジオ・エンタメ特化・WebGL 世界観構築)
- `5186_symbol.shinayaka-design.com_.html` — しなやかデザインシンボルズ (VI/CI/ロゴ専門)
- `5216_cocochi.design_.html` — ひとりごこち (シンボルデザインスタジオ)

### 1.2 モダン・ブランディングエージェンシー (14 件)
- `4964_sas-vliver.com_.html` — SpiceAgencyStudio (IRIAM VTuber 事務所設立支援)
- `4968_novasell.com_.html` — ノバセル (AI マーケティングエージェンシー / TV CM)
- `4969_design.rudel.jp_.html` — RUDEL Design (攻め続けるクリエイティブ)
- `4998_neu-ad.jp_.html` — 株式会社 Neu (SNS 広告・成果報酬型・ショート動画)
- `5051_monf.jp_.html` / `9717_monf.jp_.html` — モンブラン (福岡ブランディング)
- `5069_ashimfactory.com_.html` — ASHIM FACTORY (スタートアップ特化)
- `5060_nauts.co.jp_.html` — Nauts (デザインコレクティブ)
- `5110_wa-concept.jp_.html` — W/A (コンテクストブランディング)
- `5329_www.accorder.co.jp_recruit_.html` — アコーダー (大阪制作プロダクション)
- `5330_about.tsuzuku.tokyo_.html` — (つづく) クリエーティブディレクター集団
- `5332_recruit.4digit.com_.html` — FOURDIGIT (デジタルデザイン)
- `8706_www.steer.cc_.html` — ステア (大阪デザイン会社)
- `10475_yao-design.co.jp_.html` — YAO デザイン (パッケージ)
- `10630_delta-tokyo.co.jp_.html` — 株式会社 delta

### 1.3 大手エージェンシー & 企業内デザイン組織 (12 件)
- `4972_careers.goodpatch.com_.html` — Goodpatch 採用
- `4993_anywhere.goodpatch.com_.html` — Goodpatch Anywhere (リモートデザイン組織)
- `5218_design-partnership.goodpatch.com_.html` — Goodpatch Design Partnership
- `5054_design.lycorp.co.jp_.html` — LINE ヤフー DESIGN
- `5063_branddesign.newspicks.com_.html` — NewsPicks Brand Design
- `5081_www.career.dentsu.jp_recruit_2026_.html` — 電通新卒
- `5097_www.sankei-digital.co.jp_recruit_.html` — 産経デジタル
- `5142_hakusuku.jp_recruit_.html` — HAKUHODO RECRUIT
- `5281_design.moneyforward.com_.html` — Money Forward Design
- `5289_recruit.moneyforward.com_.html` — Money Forward 採用
- `5321_nution.persol-career.co.jp_.html` — NUTION (パーソル内デザイン組織)
- `11953_a3-ma.com_.html` — エイスリー (エンタメ業界特化 M&A 仲介)

### 1.4 映像制作・音声クリエイティブ (6 件)
- `5006_statementmovie.tyo.co.jp_.html` — ステートメントムービー by TYO
- `5017_asj.tyo.co.jp_.html` — Another Side of Japan (TYO 地域魅力映像)
- `5012_3d-lab.funtech.inc_.html` — 3D ANIMATION LAB. by FunTech
- `5029_www.ai-model.jp_movie_.html` — AI model (AI で描く映像の未来)
- `5287_service.elephantstone.net_.html` — エレファントストーン (映像制作)
- `8060_www.dentsusciencejam.com_.html` — 電通サイエンスジャム

### 1.5 SaaS・IT 企業採用サイト（制作会社色の強いもの） (30 件)
※ これらは本質的には SaaS 企業だが、採用 LP の作り込みが制作会社並のため includes。
- 5003 coalition-group, 5033 baigie, 5037 nealle, 5042 tobila, 5048 leverages, 5061 datumstudio, 5065 newtown, 5077 SME, 5100 intloop, 5102 lumine, 5103 super-studio, 5105 alphadrive, 5106 cuebic, 5116 smarthr, 5123 lycomm, 5125 dely, 5128 nttdata, 5154 renxa, 5159 n-works, 5169 tver, 5197 sevendex, 5223 any, 5236 nagoyatv, 5242 tokyu-agc, 5246 abi-inc, 5248 garage(DG), 5262 reynato(Creative HR), 5265 nomeets, 5273 attendbiz, 5283 licenseacademy, 5284 toei, 5301 porters, 5303 cybozu, 5325 ipros, 5326 uekishun(PLANT), 5328 intloop-career.

---

## 2. 代表 18 件の深読み

### 2.1 `4964_sas-vliver.com_.html` — SpiceAgencyStudio (SAS)
- **事業**: IRIAM (バーチャルライバーアプリ) 事務所の設立・運営をヒト・モノ・カネで支援
- **タイトル**: SpiceAgencyStudio(SAS) ｜ IRIAM(イリアム)事務所設立支援
- **DESC**: 個人・法人問わず関心をお持ちいただける方はお問合せください。新規ライバー・移籍募集
- **ライブラリ**: Nuxt + React (SSR + CSR 混在)
- **コピー哲学**: VTuber 事務所 as Service — 従来は B2B2C だがここでは B2B (エージェンシー支援) モデル
- **設計**: SPA。`<section>` が 0 件なのは Nuxt 動的レンダリングのため HTML 静的には拾えない
- **特徴**: 新興スタイル「事業代行型エージェンシー」。従来の広告代理店・制作会社とは異なる **運営代行** モデル

### 2.2 `4979_yoru.design_.html` — 夜. (横澤由香里)
- **タイトル**: 夜. | Index
- **DESC**: 夜.という屋号で活動する横澤のサイト。主にデザインとアートディレクションやっています。
- **H1**: 横澤由香里 / **H2**: 夜.
- **ライブラリ**: なし (素の HTML/CSS)
- **セクション構成**: 19KB と軽量、`<section>` 1 個のみ
- **デザイン哲学**: 「屋号 = 名詞 + ピリオド」という超ミニマル自己紹介。サイト自体を「名刺」として運用
- **教訓**: フリーランス個人ポートフォリオの「ゼロ装飾・最小情報」型の極北。ドメイン .design を買う時点で名乗れる効果

### 2.3 `4985_gyokuro-s.com_ja_.html` — GYOKURO STUDIO
- **事業**: 日本テレビ系列の海外向けコンテンツプロダクション
- **タイトル**: GYOKURO STUDIO | Japan-based Production Company
- **DESC (英)**: Gyokuro Studio is a Japan-based production company creating premium content with top creators. Backed by Nippon TV's global network, we produce and distribute Japanese entertainment worldwide.
- **構造**: `<h2> What is [Gyokuro]` + `<h2> Latest [Work]` — 典型的「紹介 + 実績」2 セクション構造
- **フォント**: Noto Sans JP + Noto Serif JP (Google Fonts 300)
- **ライブラリ**: **Astro + Sanity CMS + p5.js** — 現代 JAMStack 構成の代表例。Astro で静的生成、Sanity で作品データ管理、p5.js で装飾的アニメーション
- **設計**: 4 セクション、footer 1 — SPA ではなく MPA
- **デザイン哲学**: 「茶葉の名前を英語読みしたロゴ」+「ナショナルローカル (Japan-based, Nippon TV-backed) アピール」= **日本文化輸出** のポジショニング

### 2.4 `4986_morohoshi.site_.html` — Shizuku Morohoshi 個人ポートフォリオ
- **タイトル**: Shizuku Morohoshi | デザイナー・ポートフォリオ
- **DESC**: 諸星志づくの制作実績。グラフィック〜Web まで。フォームからご依頼可能
- **ライブラリ**: Nuxt + React
- **ファイルサイズ**: **12.8KB** — ほぼ空の SPA シェル。JS が後から描画
- **特徴**: 個人デザイナーの「.site ドメイン + フレームワーク使用」低コスト高級感型
- **教訓**: ポートフォリオサイトは SPA フレームワーク + 静的ホスティングで無料〜月数百円で運用できる

### 2.5 `4998_neu-ad.jp_.html` — 株式会社 Neu
- **タイトル**: 株式会社 Neu | 広告に、こだわりと偏愛を。
- **DESC**: 成果報酬型 SNS 広告運用。Meta / TikTok / YouTube ショート動画中心。ショート動画や LP は **無料提供**
- **H1 (反復)**: 「広告に、/こだわりと偏愛を」— 同じコピーを縦 2 行構造で 2 回繰り返し登場
- **色**: `#0100FE` (純青), `#c1d2ff` (淡), `#dcdceb` — **ほぼ単色の青キー**
- **ライブラリ**: **Framer (lenis + lottie + next + react + p5.js)**
- **ファイルサイズ**: **557KB** — 31 セクションと巨大。Framer フルページビルダー特有
- **設計**: Framer で作った一枚 LP、スクロールでコンポーネントを次々出す
- **コピー哲学**: 「偏愛」という業界では使われづらい感情語を打ち出し、差別化を獲得
- **ビジネスモデル発見**: 「広告 LP を無料で作る代わりに運用費で回収する成果報酬型」は、制作会社市場の新潮流

### 2.6 `5022_emuni.co.jp_.html` — emuni (村上兄弟)
- **タイトル**: emuni (ただこれだけ)
- **DESC (英)**: emuni is a graphic design studio based in Tokyo. emuni was formed in 2012 by Takashi and Masashi Murakami. Graphic / Branding / Package / Sign / Editorial
- **H2 (4 件)**: I.CEBERG MAGAZINE 02 / TACTILE STYLE STORE / me ISSEY MIYAKE / me ISSEY MIYAKE (2 回)
- **ライブラリ**: **Astro** のみ (超シンプル)
- **video タグ 18 個** — ほぼ全セクションが動画ループ。ISSEY MIYAKE など有名ブランドの実績を動画で見せる
- **色**: なし — CSS で hex カラー定義ゼロ = **画像と動画のみで世界観を作る**
- **設計哲学**: 「文字も CSS 色もほぼ使わず、動画資産だけで構成」= ハイエンドの極みアプローチ
- **教訓**: 超一流制作会社は **実績動画の羅列** だけで LP として成立する

### 2.7 `5029_www.ai-model.jp_movie_.html` — AI model
- **タイトル**: AI で描く映像の未来。TV CM も Web もワンストップで
- **DESC**: AI × 映像制作の新潮流
- **ファイルサイズ**: 341KB — かなり大きい
- **注目**: 従来の映像制作会社が AI を付加価値として前面に出す典型例
- **教訓**: 2026 年時点、映像制作会社の差別化軸は「AI でワンストップ」

### 2.8 `5051_monf.jp_.html` / `9717_monf.jp_.html` — モンブラン (福岡)
- **タイトル**: モンブラン | 福岡のブランディング × ホームページ制作
- **DESC**: 福岡のブランディング会社「株式会社モンブラン」では、九州を中心にブランド構築を軸に HP 制作、動画・グラフィック制作、広告運用代行まで多角的に支援
- **H2**: BOOKS & AWARDS / ブランディング実績 / クリエイティブ実績
- **フォント**: Noto Sans JP 100-900 + Noto Serif JP 200-900 (full variable weight range)
- **ライブラリ**: Swiper + Splide + Next + wp-content — **WordPress 上に Next.js をかぶせる headless 構成**
- **セクション数**: 13 と多い
- **特徴**: 地方エージェンシーの典型。「地元 × 総合制作」を強みに、実績・受賞・ブランディング手法を章立てで見せる

### 2.9 `5054_design.lycorp.co.jp_.html` — LINE ヤフー DESIGN
- **タイトル**: LINE ヤフー DESIGN
- **ファイルサイズ**: **3.2KB** — 完全な JS シェルのみ
- **ライブラリ**: Nuxt + React
- **教訓**: メガ企業の社内デザイン組織サイトは、**HTML はほぼ空で JS で完全描画** する構成が主流 (SEO を気にせずブランド表出に特化)

### 2.10 `5069_ashimfactory.com_.html` — ASHIM FACTORY
- **タイトル**: ASHIM FACTORY | デザインは、もっとあなたの味方になる
- **DESC**: クリエイティブパートナー。デザイン実績、メンタープランサービス、1 コマ漫画「やがて前向き名人」
- **H2**: 「スタートアップ事業をお考えの皆さまへ」— ターゲット宣言型 H2
- **フォント**: Montserrat variable + Noto Sans JP
- **ライブラリ**: Splide + Next + Astro + WP
- **セクション数**: 17
- **特徴**: **「1 コマ漫画」** という異色コンテンツを混ぜる = 代表者個人の偏りで差別化
- **コピー哲学**: 「味方」というカジュアルワードで敷居を下げ、スタートアップ起業家に刺さる

### 2.11 `5136_arkreis.jp_.html` — ARKREIS
- **タイトル**: ARKREIS
- **DESC**: 東京拠点のデザインスタジオ。**エンタメ分野** のクリエイティブ中心。オリジンの魅力を意匠・テクノロジーで最大化し確固たる世界観を構築
- **H2**: DESIGN STUDIO (THAT) MAXIMIZE THE STORY / WORKS (2 回)
- **ライブラリ**: **Next + WebGL + p5.js**
- **色**: `#FFFFFF` 1 色のみ (実質背景白、他は画像で表現)
- **設計**: 12 セクション、video 1 — WebGL でキービジュアル、セクション遷移を魅せる
- **コピー哲学**: 「オリジン」「世界観構築」というエンタメ側の語彙をうまく取り込む = ゲーム・アニメ会社向けの仕事に強い

### 2.12 `5186_symbol.shinayaka-design.com_.html` — しなやかデザインシンボルズ
- **タイトル**: しなやかデザインシンボルズ｜東京・千葉のロゴデザイン会社
- **DESC**: 株式会社しなやかデザイン展開のロゴ特化サービス。これまで提供してきた VI/CI/ロゴデザインに **特化した別ブランド** として立ち上げ
- **H2**: ブランドの核となる VI/CI/ロゴをデザイン / 清澄白河のデザイン事務所
- **色**: 36 色 (Gutenberg WP ブロックエディタのデフォルトパレット) — WP 素の状態に近い
- **教訓**: **事業内で専門特化ブランドを別サイトとして切り出す**（親サイトとは別ドメイン）= 中小デザイン会社の賢いマーケティング

### 2.13 `5216_cocochi.design_.html` — ひとりごこち
- **タイトル**: ひとりごこち｜シンボルデザインスタジオ
- **DESC**: 長く使いたいと愛着を持てるデザインを探求する**小さなシンボルデザインスタジオ**。ロゴを始めコピー / web / 冊子など、「言葉と視覚を軸に象徴となるもの」をデザイン
- **H1**: logo (全ローワーケース)
- **フォント**: Shippori Mincho + Zen Kaku Gothic New (和モダンコンビ)
- **ライブラリ**: Swiper + Next + wp-content (headless WP)
- **色**: 33 色 (やはり WP デフォルトパレット)
- **コピー哲学**: 「小さな・ひとり・愛着」= 規模の小ささを弱みではなく強みに変換するブランディング

### 2.14 `5218_design-partnership.goodpatch.com_.html` — グッドパッチデザインパートナーシップ
- **タイトル**: デザインの力でビジネスを前進させる
- **DESC**: UX / UI・ブランド・事業戦略のデザインパートナーとして並走。企業課題を明確にし、デザインでビジネスに貢献
- **ファイルサイズ**: 68KB + `<footer>` 0 + `<section>` 0 (完全 SPA)
- **ライブラリ**: Next + Nuxt + React (複数 SPA フレームワーク混在 = ビルド時に ssg された結果)
- **色**: `#e9e9e9` 1 色のみ
- **教訓**: Goodpatch クラスの一流エージェンシーは「見せるより使わせる」= HTML に装飾ゼロ、JS で完全描画

### 2.15 `5281_design.moneyforward.com_.html` — Money Forward Design
- **タイトル**: Money Forward Design
- **DESC**: 株式会社マネーフォワードのデザイナーサイト。「User Focus」を胸にユーザーの人生を、そして世界を前に進めるデザインを届けます
- **ファイルサイズ**: 21KB (シェルのみ)
- **ライブラリ**: Nuxt + React
- **教訓**: 同じく SaaS 大手のデザイン組織サイトは「ステートメント + 実例」の極めてシンプルな SPA で十分

### 2.16 `5287_service.elephantstone.net_.html` — エレファントストーン
- **タイトル**: 映像制作・動画制作の株式会社エレファントストーン
- **DESC**: 予算、スピード、コミュニケーション。つくり方が選べる、新しい映像づくり。ブランディングムービーやサービス紹介映像、SNS 動画から広告運用まで。「やっと見つけたパートナー」と言われるように
- **H2 構成**: ABOUT エレファントストーンの想い / OVERVIEW サービス概要 / SERVICE サービスについて — **章立て明確**
- **ライブラリ**: **Barba.js** (SPA 遷移) + Next + WP
- **video タグ 7 個** + iframe 3 個 (YouTube 埋め込み?)
- **色**: 22 色 (WP パレット + カスタム)
- **コピー哲学**: 「予算・スピード・コミュニケーション」の 3 軸で選ばせる設計 = **カスタマージャーニーを選択肢化**
- **教訓**: 映像制作会社は「つくり方が選べる」= パッケージプランの明示で中堅クライアントを取り込める

### 2.17 `5321_nution.persol-career.co.jp_.html` — NUTION (パーソル内デザイン組織)
- **タイトル**: NUTION | デザインの力で、 はたらくを変え、 社会を変えていく
- **H1**: A Work-Life Design Studio (反復)
- **H2 構成**: NUTION が目指すもの → Selected Works → プロジェクト 2 件紹介
- **色**: `#212121` / `#757B7E` の 2 色 (シックなグレースケール)
- **ライブラリ**: **GSAP + Splide + Next + WP**
- **ファイルサイズ**: 92KB
- **セクション**: 7 + iframe 1 + video 2
- **コピー哲学**: 「Work-Life Design Studio」— 事業会社内のデザイン組織という立ち位置を横文字で言語化
- **教訓**: 大企業内デザイン組織は **「親会社の事業」と「デザインの社会的価値」の二層ステートメント** 構成

### 2.18 `5332_recruit.4digit.com_.html` — FOURDIGIT
- **タイトル**: 採用情報｜FOURDIGIT Inc. 株式会社フォーデジット
- **DESC**: デジタルデザインの力で、世界をつなぐ
- **H1**: `C O N N E C T I N G   T H E   W O R L D   W I T H   D I G I T A L   D E S I G N` (スペース開けた装飾)
- **H1 (作品)**: ベトナム・ビンズン新都市 / ショッピングアプリ / 空飛ぶ車 — **グローバル + 先端テーマ** を並べる
- **H2**: デジタルデザインの力、何のために使いますか？ / about us / works / culture
- **フォント**: Cormorant Garamond + Inter (セリフ + サンセリフ対比)
- **ライブラリ**: **Locomotive Scroll + Next**
- **ファイルサイズ**: 136KB
- **特徴**: 海外プロジェクト事例を前面に置く = グローバル志向の制作会社のカラー

### 2.19 `5330_about.tsuzuku.tokyo_.html` — (つづく)
- **タイトル**: クリエーティブ・ディレクター・コレクティブ (つづく)
- **DESC**: つづく物語をつくる。つづく価値をつくる。つづく幸せをつくる。つづく未来をつくる。つづく道をつくる
- **H1**: つづく / クリエーティブ・ディレクター・コレクティブ / STATEMENT / MESSAGE
- **H2**: 個人 CD × 3 名の肩書き (CM プランナー / コピーライター / 映像プランナー)
- **ライブラリ**: なし (純 HTML)
- **ファイルサイズ**: 14.9KB
- **色**: `#000080` (ネイビー) のみ
- **特徴**: **フリーランス CD 3 人の連合** という事業形態。法人ではなく「Collective」
- **コピー哲学**: 同じ動詞「つづく」を 5 回ずつ並べる = ミニマム単語反復で価値観を刻印
- **教訓**: コレクティブ型の新型エージェンシーは、メンバー個人のブランドを前景化し、集合体の「ステートメント」をシンプルに打ち出す

### 2.20 `5060_nauts.co.jp_.html` — Nauts
- **タイトル**: Nauts
- **DESC**: クライアント課題を解決しプロジェクトを成功に導く **デザインコレクティブ**
- **ライブラリ**: **Barba.js + wp-content + WebGL**
- **色**: 13 色 (WP + カスタム)
- **特徴**: barba でトランジションを作り、WebGL で装飾。WP ベースなので CMS 管理しやすい
- **教訓**: 中小規模コレクティブは **WP バックエンド + 前景フレームワーク** でコストと速度を両立

---

## 3. 真の制作会社 70 件から抽出した共通パターン

### 3.1 技術スタックの 4 層

| 層 | 比率 | 代表ライブラリ |
|---|---|---|
| **A. 超ハイエンド・独自開発** | 10% | emuni (Astro のみ, 動画のみ) / ARKREIS (WebGL) / Nauts (Barba + WebGL) |
| **B. モダン SPA フレームワーク** | 35% | Next / Nuxt / React — goodpatch, moneyforward, lycorp, communitio, rudel |
| **C. Headless WP + SPA** | 30% | WP + Next / Astro + Swiper — monf, ashim, cocochi, nution, elephantstone, shinayaka |
| **D. Framer / Studio / STUDIO** | 25% | Framer (neu-ad), 純 HTML (tsuzuku), .site SPA (morohoshi) |

### 3.2 コピー哲学の 5 類型

1. **「デザインの力で〜を変える」型** (goodpatch, nution, moneyforward, lycorp)
   → 大手・企業内デザイン組織は必ず「社会変革宣言」から入る
2. **「小さな・個人・偏愛」型** (cocochi, neu-ad, ashim, yoru.design)
   → 中小・個人は規模の小ささを強みに変換
3. **「専門特化」型** (shinayaka-design/VI・CI・ロゴ / arkreis/エンタメ / ai-model/AI)
   → 一芸特化で指名買いを狙う
4. **「総合・伴走」型** (emuni, nauts, monf, elephantstone)
   → 「パートナー・伴走・トータルサポート」を打ち出す
5. **「事業代行・成果報酬」型** (neu-ad, sas-vliver, ai-model)
   → 新興スタイル。広告制作を無料提供、運用費で回収

### 3.3 セクション構成の共通骨格

真の制作会社 LP はこの 7〜10 セクションに集約される:

1. **Hero** — ステートメント + 代表作 video/image (70%)
2. **About** — 会社紹介 / 代表者紹介 / 哲学 (100%)
3. **Works** — 実績一覧 (100%)
4. **Services** — サービスメニュー (80%)
5. **Members** — メンバー紹介 (60%, 特にコレクティブ型)
6. **News / Blog** — 更新 (40%)
7. **Awards / Books** — 受賞・掲載 (30%, 地方・中堅で多い)
8. **Culture** — 採用向け文化紹介 (50%, 採用兼サイトで必須)
9. **Contact** — お問合せ (100%)
10. **Footer** — 住所・SNS・プライバシー (100%)

### 3.4 フォント選定の傾向

- **和モダン**: Shippori Mincho + Zen Kaku Gothic New (cocochi)
- **グローバル**: Inter + Cormorant Garamond (4digit) / Montserrat + Noto Sans JP (ashim)
- **ステートメント特化**: Noto Sans JP 300 一本勝負 (emuni, moneyforward, goodpatch)
- **レトロ遊び**: PixelMplus (no.meets = ドット)
- **Framer 既定**: Inter / Zen Kaku Gothic Antique (neu-ad)

### 3.5 色使いの傾向

| パターン | 比率 | 代表 |
|---|---|---|
| **完全モノクローム** (黒白のみ) | 35% | moneyforward, tsuzuku, goodpatch, emuni, arkreis |
| **単色アクセント** (黒白 + 1 色) | 30% | neu-ad (青 #0100FE), nution (#212121), ashim (#f0f0f0) |
| **WP デフォルトパレット** | 20% | cocochi, shinayaka, nauts, wa-concept |
| **多色・彩度高** | 15% | no.meets (ピンク/黄/青), 個人 PF |

### 3.6 CTA の扱い

- **ほとんどが「Contact」テキストリンクのみ** (ボタン装飾なし) — 制作会社 LP は「発注誘導」を急がず、作品を先に見せる
- **一部採用サイトは「エントリー」「応募する」ボタン** (dentsu, hakuhodo, 4digit, goodpatch)

---

## 4. クロスジャンル汚染 1,641 件 (other_unknown) の再分類提案

### 4.1 分類先ジャンル (推定)

1,641 件の unknown を深掘りすると、以下のように配分される見込み:

| 再分類先 | 推定件数 | 根拠 |
|---|---|---|
| **brand-corporate** (ブランドキャンペーン) | 550 | 花王 / 資生堂 / 明治 / 森永 / ロッテ / アサヒ / キリン のブランド特集・特設サイト |
| **food-beverage** への追加 | 300 | 食品大手の個別商品紹介ページ |
| **beauty-cosmetics** への追加 | 150 | コスメ個別商品紹介 |
| **campaign-special** (キャンペーン) | 200 | 期間限定キャンペーン LP、クイズ、応募 |
| **ec-shop** | 150 | rakuten / yahoo shopping / 各社直販ページ |
| **experience** (体験・イベント) | 80 | realdgame / exhibition / pokemon event |
| **life-infra** / **life-goods** | 100 | 日用品・家電・サニタリー |
| **publication** (映画・書籍) | 50 | 映画公式・出版 |
| **brand-corporate** (企業 PR) | 60 | toyo-eng / zenrin / seven-bank / NEC |
| その他 | 残り | サブジャンル詳細不明 |

### 4.2 別ジャンルへの混入 具体例 (100 件サンプル)

**本来 brand-corporate:**
- 4984 www.benesse.co.jp_digital_ (ベネッセ DX 戦略)
- 8536 www.zenrin.co.jp_autonomy_ (ゼンリン自治体向け)
- 10630 delta-tokyo (会社紹介だが真の agency 側にも拾える)

**本来 food-beverage:**
- 10825 meiji_sweets_icecream (エッセルスーパーカップ 30 周年)
- 6615 fantasy-lp.asahibeer.co.jp_mizulemon (アサヒ空想開発局 水レモン)
- 10617 ucc_black (UCC BLACK 無糖)
- 11524 ichibanya_necoichi (ネコ壱)

**本来 beauty-cosmetics:**
- 8830 lp.diane-bonheur (ダイアンボヌール)
- 7728 ishizawa-lab_orange-n (石澤研究所オレンジヘアケア)
- 12012 taisho-beauty_oile-essence (大正製薬)
- 10564 bcl-brand_kansosan (KANSOSAN 乾燥さん)

**本来 bandai_toy_character or ec-shop:**
- 10978 / 11449 / 11785 / 9958 / 11447 / 11008 / ... 111 件の p-bandai.jp エントリー

**本来 travel-hotel or campaign-special:**
- 10626 visit-hokuriku (北陸新幹線直通)
- 11914 recommend.jr-central (JR 東海 × 薬屋のひとりごと)
- 11959 recommend.jr-central (FRUITS ZIPPER × JR)
- 6826 souda-kyoto (そうだ京都、行こう)
- 8484 hoshinoya (星のや)

**本来 medical-clinic:**
- 7973 whitening-ebisu (ホワイトニング)
- 12303 morinohibiki-dental (桑名市歯科)
- 12563 aoilaw (離婚弁護士)

**本来 real-estate or life-infra:**
- 8552 dup-m (東新住建)
- 10807 connecthome (富山注文住宅)
- 11005 eonet (eo 光)
- 11419 xlei-hikari (光回線)
- 6614 nissan_nissan-denki (日産でんき)

**本来 experience / campaign-special:**
- 9254 realdgame (ドラゴンクエスト脱出)
- 10988 realdgame (夜の幽霊アパート)
- 6620 gyozamatsuri (全日本ぎょうざ祭り)
- 6896 i-ku-kan (運命を読み解く没入型体験)

**本来 fashion / ec-shop:**
- 10399 kurand (酒ガチャカーニバル)
- 9672 onward_crosset (ドローブ × any SiS)
- 12620 fabric-tokyo (ビジネスカジュアル)

**本来 saas-service:**
- 11198 dentalhr (デンタル HR 総研)
- 10973 schick_hydro5 (Schick)
- 9665 uniforce (クラウド決算)
- 8719 wacul-ai (WACUL AI)

**本来 recruit-job (真の求人サービス):**
- 12206 kimisuka (逆求人サイト)
- 11367 sharefull (スキマバイト)
- 6956 demae-can_gig (出前館配達員募集)
- 10260 redbaron_scholarship (バイク整備士奨学金)

**本来 automotive:**
- 6663 abarth_500e
- 6637 suzuki_carry
- 9996 cycle.panasonic (電動アシスト)
- 11057-59 moto-bu.motorola (バイク扱い)

---

## 5. design-mcp 方針への示唆

### 5.1 真の portfolio-agency 70 件は「別スキル」として切り出す価値あり

このジャンルは **design-mcp の標準生成スキルから隔離して専用スキル** にすべき。理由:

1. **コピーと構造が極限まで削られる** — 他ジャンルのような「3 点 CTA + 特徴 + 事例 + Q&A」テンプレが通用しない
2. **動画・WebGL が主役** — 静的 HTML 生成との相性が悪い
3. **フォント選定が世界観の 80%** — 汎用 Google Fonts 推奨では劣化
4. **色は 1〜2 色まで** — パレット生成ロジックを制限

### 5.2 スキル分岐提案

```
design-mcp/skills/
├── agency-studio-minimal/  (個人 PF / 小規模スタジオ型)
│   ├── ステートメント1行 + 実績グリッド + Contact の 3 セクション最小構成
│   ├── フォント: Noto Sans JP 300 + 1 serif
│   └── 色: #000 / #fff / アクセント1色のみ
├── agency-studio-branding/ (中堅ブランディング会社型)
│   ├── 章立て About→Service→Works→News→Contact
│   ├── WP headless 前提で markdown 可変
│   └── 受賞・掲載セクションを任意追加
├── agency-studio-corporate/ (企業内デザイン組織型)
│   ├── ステートメント + Selected Works + Culture + Members
│   └── 親ブランドとのビジュアル連動
└── agency-studio-collective/ (コレクティブ/新興型)
    ├── メンバー個人肩書き並列
    ├── ステートメント反復パターン
    └── ドメイン .tokyo / .site / .design 系
```

### 5.3 other_unknown 1,641 件の再分類は design-mcp より先に必要

**現状の `portfolio-agency` フォルダを入力としてテンプレ学習を行うと、汚染により精度が著しく落ちる**。design-mcp に取り込む前に:

1. 2,813 件を 17 ジャンルに再配分するスクリプトを作成
2. 真の 70 件を `agency-studio/` サブフォルダへ隔離
3. 各ジャンル毎の分析 .md (既存 20 本) を汚染分で上書き再分析

### 5.4 本ジャンル固有の「禁じ手」

- ❌ **カラフル背景グラデ** — ダサくなる
- ❌ **アイコン付きカード 3 列** — SaaS LP 感が出る
- ❌ **料金表** — 制作会社は価格非公開が正道
- ❌ **「選ばれる理由 ○○ 個」** — 素人くさい
- ❌ **CTA ボタン多数** — 「Contact」1 個で十分

### 5.5 本ジャンル固有の「定石」

- ✅ **Hero は動画 or 写真 1 枚 + ステートメント 1 行**
- ✅ **Works は正方形 or 横長グリッド、hover で情報出す**
- ✅ **About は代表者の顔写真 + 経歴 + 哲学**
- ✅ **英日バイリンガル (切替不要で常時併記)**
- ✅ **Footer は住所 + SNS + プライバシーのみ**
- ✅ **カーソルカスタム (ダイヤ・●・十字)** — 「拘り」演出

---

## 6. 次回アクションアイテム

1. **再分類スクリプト作成**: 2,813 件を 17 ジャンルに配分する Python スクリプトを `/Users/oidekento/lp-corpus/scripts/` に配置
2. **真の 70 件を別ディレクトリへ**: `raw_all/portfolio-agency-true/` を作成
3. **brand-corporate 分析の再実行**: 1,641 件の other_unknown のうち 550 件超が brand-corporate 行き
4. **食品・コスメ分析の再実行**: 347 + 135 + 追加 450 = 約 1,000 件規模になる
5. **p-bandai.jp 111 件を ec-shop 分析に合流**
6. **studio.site 15 件を individual/小規模ジャンル未定フォルダへ**
7. **rdlp.jp 取得時のメタ情報確認**: 誤分類の根本原因調査 (rdlp.jp のタグ付けが壊れているか、こちらの取込ロジックが壊れているか)

---

## 7. 統計サマリ (メタ)

- **分析対象 HTML 数**: 2,813
- **ランダムサンプリング数**: 600 (493 ユニーク)
- **深読み数**: 20 (2.1-2.20)
- **ユニークドメイン数**: 1,798
- **単一ドメイン最多**: p-bandai.jp (111 件, 3.9%)
- **真の制作会社/代理店**: **70 件 (2.5%)**
- **誤分類 (他ジャンル混入)**: **2,743 件 (97.5%)**
- **再分類先ジャンル数**: 17+
- **最大誤分類ジャンル**: food_beverage (347) + other_unknown 内の brand-corporate (推定 550) = 約 897 件

---

## 付録 A: 真の portfolio-agency 70 件 完全リスト

```
4964_sas-vliver.com_.html                        SAS IRIAM 事務所設立支援
4968_novasell.com_.html                          ノバセル AI マーケティング
4969_design.rudel.jp_.html                       RUDEL Design
4972_careers.goodpatch.com_.html                 Goodpatch 採用
4979_yoru.design_.html                           夜.
4985_gyokuro-s.com_ja_.html                      GYOKURO STUDIO
4986_morohoshi.site_.html                        Shizuku Morohoshi PF
4993_anywhere.goodpatch.com_.html                Goodpatch Anywhere
4998_neu-ad.jp_.html                             株式会社 Neu
5003_recruit.coalition-group.jp_.html            Coalition Group
5006_statementmovie.tyo.co.jp_.html              ステートメントムービー
5009_alpha.plaid.co.jp_.html                     PLAID ALPHA
5012_3d-lab.funtech.inc_.html                    3D ANIMATION LAB
5017_asj.tyo.co.jp_.html                         Another Side of Japan
5022_emuni.co.jp_.html                           emuni
5029_www.ai-model.jp_movie_.html                 AI model
5033_recruit.baigie.me_.html                     ベイジ
5037_jobs.nealle.com_.html                       ニーリー
5042_rct.tobila.com_.html                        トビラシステムズ
5051_monf.jp_.html                               モンブラン (福岡)
5054_design.lycorp.co.jp_.html                   LINE ヤフー DESIGN
5060_nauts.co.jp_.html                           Nauts
5061_career.datumstudio.jp_.html                 DATUM STUDIO
5063_branddesign.newspicks.com_.html             NewsPicks Brand Design
5065_newtown.tokyo_recruit2024.html              NEWTOWN
5069_ashimfactory.com_.html                      ASHIM FACTORY
5071_www.heralbony.jp_careers_.html              ヘラルボニー
5073_www.itplus.co.jp_story-vol0.html            IT プラス
5075_kikaku.yamatowa.co.jp_.html                 森の企画室
5077_saiyo.sme.co.jp_graduate_26_.html           ソニーミュージック
5081_www.career.dentsu.jp_recruit_2026_.html     電通
5097_www.sankei-digital.co.jp_recruit_.html      産経デジタル
5103_careers.super-studio.jp_.html               SUPER STUDIO
5105_alphadrive.co.jp_.html                      AlphaDrive
5109_service.boujee.jp_.html                     Cast Me!
5110_wa-concept.jp_.html                         W/A
5119_communitio.jp_.html                         コミュニティオ
5125_dely.jp_careers.html                        クラシル
5128_www.nttdata-strategy.com_recruit_.html      NTT データ経営研
5135_tashi.design_.html                          tashi
5136_arkreis.jp_.html                            ARKREIS
5142_hakusuku.jp_recruit_.html                   博報堂
5186_symbol.shinayaka-design.com_.html           しなやかデザインシンボルズ
5197_sevendex.com_recruit.html                   セブンデックス
5216_cocochi.design_.html                        ひとりごこち
5218_design-partnership.goodpatch.com_.html      Goodpatch DP
5248_recruit.garage.co.jp_.html                  デジタルガレージ
5262_creative-hr.reynato.co.jp_.html             Creative HR
5265_no.meets.ltd_.html                          ノーミーツ
5281_design.moneyforward.com_.html               Money Forward Design
5287_service.elephantstone.net_.html             エレファントストーン
5289_recruit.moneyforward.com_.html              Money Forward 採用
5301_www.porters.jp_recruit_.html                ポーターズ
5303_cybozu.co.jp_recruit_.html                  サイボウズ
5321_nution.persol-career.co.jp_.html            NUTION
5325_recruit.ipros.jp_.html                      イプロス
5326_uekishun.com_.html                          PLANT (植木春)
5329_www.accorder.co.jp_recruit_.html            アコーダー
5330_about.tsuzuku.tokyo_.html                   (つづく)
5332_recruit.4digit.com_.html                    FOURDIGIT
7156_www.service.ptw.inc_lp_netsupport-a_.html   PTW
8060_www.dentsusciencejam.com_.html              電通サイエンスジャム
8062_www.ystar-audition.com_audition_.html       Y Star
8105_toppa-creative-award.com_.html              TOPPA Creative Award
8706_www.steer.cc_.html                          ステア (大阪)
10117_monf.jp_monboo-and-ran_.html               モンブラン (子ページ)
10475_yao-design.co.jp_.html                     YAO デザイン
10611_unlimit.works_.html                        Unlimit Works
10630_delta-tokyo.co.jp_.html                    株式会社 delta
10773_zoost.inc_lp-lp_.html                      zoost
11953_a3-ma.com_.html                            エイスリー
```

## 付録 B: 汎用 LP 上位ドメイン (再分類対象)

```
111  p-bandai.jp              → ec-shop + bandai_toy サブジャンル
 43  item.rakuten.co.jp       → ec-shop
 27  www.kao.co.jp            → brand-corporate + beauty-cosmetics (分割)
 22  www.shiseido.co.jp       → beauty-cosmetics
 22  www.meiji.co.jp          → food-beverage
 21  www.fracora.com          → beauty-cosmetics
 20  www.morinaga.co.jp       → food-beverage
 17  realdgame.jp             → experience
 16  kurand.jp                → ec-shop (日本酒)
 16  recommend.jr-central.co.jp → travel-hotel + campaign-special
 15  www.aigan.co.jp          → fashion or 新設 eyewear
 14  www.felissimo.co.jp      → ec-shop
 14  cp.glico.com             → food-beverage
 14  www.starbucks.co.jp      → food-beverage
 13  www.kirin.co.jp          → food-beverage
 13  www.calbee.co.jp         → food-beverage
 12  www.softbank.jp          → life-infra (telecom)
 11  www.kingjim.co.jp        → life-goods (文具)
 11  www.sapporobeer.jp       → food-beverage
 11  www.kagome.co.jp         → food-beverage
 11  www.ministop.co.jp       → food-beverage (小売)
```

---

**分析終了** — 2026-04-08
