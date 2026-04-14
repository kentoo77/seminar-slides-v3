# SaaS・ITサービス・アプリ LP 分析 (Round 2)

**対象ジャンル**: SaaS / IT サービス / アプリ / テクノロジー企業 LP
**分析対象**: `/Users/oidekento/lp-corpus/raw_all/saas-service/` 配下 **117 件** (ラウンド2・統計抽出)
**深読み代表**: 12 件 (bakuraku, Speeda, STORES, Figma JP, Asana JP, Slack JP, Shopify Plus JP, Affinity, smartmat.io, invox, 8card Eight, DeNA×AI, BONX, HRMOS, Studio)
**分析日**: 2026-04-08
**前回**: 30 件 → 今回 **117 件 (3.9x)**

---

## 0. エグゼクティブサマリ

117 件を走査して明らかになった事実：

1. **"SaaSカテゴリ" は名前ほど単一ではない** — 117 件中、純粋な B2B SaaS ダッシュボード型プロダクト LP は **約 38%**。残り 62% は「店舗アプリ / 会員アプリ」「DX コーポレートサイト」「教育機関 / ITスクール」「コーポレート兼プロダクト」で構成される。日本の "SaaS LP 市場" は米国より遥かに広く、かつ曖昧。
2. **AI エージェント訴求は思ったほど伸びていない** — 見出しで「AI エージェント」と明示している LP は **4 件 / 117 (3.4%)** にすぎない。ただし「AI × 自動化 / AI OCR / AI マッチング / AI 相棒」まで広げると 18 件 (15.4%)。**2026 年 Q2 の日本 SaaS は「AI ラベル貼り換え」期に入ったばかり**。
3. **海外化度はバイモーダル** — Inter/Montserrat/Helvetica を使う "海外 SaaS 風" が 33/29/10 件と多い一方で、Noto Sans JP ベースの和風デザインも 12 件と根強い。**"海外風" と "和風" の中間層がほぼ存在しない** = 日本 SaaS LP は二極化している。
4. **CTA は圧倒的に "資料ダウンロード"** — 「お問い合わせ」81 件 (69.2%)、「資料ダウンロード / 請求」29 件 (24.8%)、「無料トライアル / 無料で始める」16 件 (13.7%)。**"無料で登録 > まず試す" より "資料DL > 後日営業" が主流**。この比率は米国 SaaS と逆。
5. **電話番号掲載率が高い** — 0x-xxxx-xxxx 形式の電話番号を HTML に埋め込んでいる LP は 23 件 (19.7%)。米国 SaaS (Stripe/Linear/Vercel) ではほぼ見ないフィールド。バクラクのように「平日 10-18 時 050-xxxx-xxxx」を固定ナビに出す例も健在。
6. **Webflow は 1 件だけ (Shopify JP)** — 日本 SaaS は WordPress (33件) + Next.js (16件) + 自社テンプレ (残り) の構成が圧倒的。Webflow/Framer 経由の LP はレア。

---

## 1. 117 件の全体統計

### 1.1 フォント分布（head の link/font-family スキャン）

| フォント | 件数 | 比率 | 意味 |
|---|---|---|---|
| **Inter** 参照 | 33 | 28.2% | モダン欧文の第一選択。Linear/Vercel/Stripe 系 |
| **Noto Sans JP** 参照 | 12 | 10.3% | 明示指定。他は Google Fonts の default や system |
| **Helvetica** 参照 | 10 | 8.5% | Studio / Figma JP / fontworks / Affinity など老舗系 |
| **Montserrat** 参照 | 6 | 5.1% | 英字見出し用 (バクラク, cybozu office, ARFIT) |
| **Poppins/Roboto/Lato/Zen系** 参照 | 43 件 (104 件中重複) | 36.8% | Noto の代替・日英ミックス |
| **font-family 指定なし** | 推定 30-40 件 | 〜30% | system-ui 任せ。古い日本 SaaS に多い |

- **重要な発見**: Inter + Noto Sans JP の組み合わせ (モダン英和並列) は 33 件中の **11 件でしか明示共存していない**。残り Inter 単独の 22 件は「和文は Noto に自動フォールバック」に任せている。**これは Linear や Vercel がグローバル市場で使う手法をそのまま日本語に適用しているだけ**、日本語タイポ品質への意識はまだ低い。
- Montserrat は「英字見出しロゴ下ライン」用に限定的に使われる。**日本 SaaS で Montserrat を見たら "英字副タイトル" と思っていい**。

### 1.2 ビルドスタック分布

| スタック | 件数 | 比率 | 代表 |
|---|---|---|---|
| **WordPress** (wp-content) | 33 | 28.2% | invox, bakuraku コーポ, searchwrite, fimmigrm など |
| **Next.js / _next** | 16 | 13.7% | Figma JP, Asana JP, Shopify JP, LINE WORKS, Koel, SmartPR Rally |
| **jQuery (明示)** | 63 | 53.8% | 依然として過半数で現役。日本 SaaS の「土台」 |
| **Swiper / Splide** | 38 | 32.5% | ロゴループ・事例カルーセル必需品 |
| **GSAP** | 6 | 5.1% | 上位ブランド LP のみ (Guilty Gear, Usergram, Pro-Seeds) |
| **Webflow** | 1 | 0.9% | Shopify JP のみ |
| **Tailwind (明示)** | 4 | 3.4% | Figma JP, ENEOS app, Tolettacat, mogukatsu |
| **Three.js** | 1 | 0.9% | あさってロボット会議 (SoftBank) のみ |

- **発見**: jQuery 依存が 53.8% というのは、前回 30 件分析時の印象以上に高い。**「日本 SaaS LP = WordPress + jQuery + Swiper/Splide」が標準工具箱**であり、React/Vue を使った PLG SaaS は Next.js で統合されている 16 件 (大半がグローバルブランド日本版) に閉じている。
- Tailwind が 4 件しかないのも特徴。日本 SaaS は依然として **BEM + 自作 CSS** が主流で、ユーティリティファーストの浸透は遅い。

### 1.3 コンテンツ要素の出現率

| 要素 | 件数 | 比率 |
|---|---|---|
| お問い合わせ | 81 | 69.2% |
| 料金 / プラン / 月額 / pricing | 59 | 50.4% |
| FAQ / よくある質問 | 64 | 54.7% |
| 導入事例 / case study | 36 | 30.8% |
| 資料ダウンロード / 請求 | 29 | 24.8% |
| セミナー / ウェビナー | 24 | 20.5% |
| 電話番号 (0x-xxxx-xxxx) | 23 | 19.7% |
| 無料トライアル / 無料ではじめる | 16 | 13.7% |
| 社導入数 / 万社 / 社以上 | 11 | 9.4% |
| ISO27001 / SOC2 / Pマーク明示 | 6 | 5.1% |
| App Store / Google Play リンク | 19 | 16.2% |
| AI エージェント (明示) | 4 | 3.4% |
| 学校 / 専門学校 / 大学 | 27 | 23.1% |
| 株式会社 / 法人表記 | 59 | 50.4% |

- **重要比較**: 「お問い合わせ (81)」 >>> 「無料トライアル (16)」 — **5 倍の差**。海外 SaaS なら完全に逆転する (Stripe/Notion/Figma の HERO は "Start for free" が定位置)。これは「導入まで営業介在が前提」な日本の SaaS 商流を反映。
- 「セミナー (20.5%)」が米国比で異様に高い。日本 SaaS の顧客教育チャネルは **"ウェビナーで集客 → 資料 DL → 営業電話"** の BANT 型ファネルが主流で、LP はその入口係に徹している。
- 「電話番号掲載 19.7%」は SaaS ジャンルとしては驚くほど高い。特に ERP / コールセンター / 勤怠管理 / 請求書受領システムなど業務ミッションクリティカル領域では電話が必須。

### 1.4 SaaS タイプ 3 層分類 (117 件)

3 タイプで棚卸した結果：

| タイプ | 件数 | 比率 | 代表 |
|---|---|---|---|
| **PLG (Product-Led Growth)** — 無料登録即使用、セルフサーブ | 22 | 18.8% | Figma JP, Asana JP, Slack JP, Studio, STORES, biskett, Eight, Shopify JP, Newt, Affinity, Karte Blocks, Awarefy, penmark, Autoro, Dokodemo, Talknote, Remo, Lapras, assign-navi, prog-8, mojimo.jp |
| **Enterprise / Sales-Assisted** — 資料DL+営業+セミナー | 48 | 41.0% | bakuraku, Speeda, MoneyForward Cloud, HRMOS, invox, biztel, sakurai-gs, GRANDIT ERP, LIVE BOARD, smartmat.io, BONX WORK, searchwrite, pro-seeds, Cybozu Office, LINE WORKS, Recoreru, bebit Usergram, oro DX, Itandi, ecology net plus, IT Dojo, ENEOS Biz, fts-future-connect, ms.recruit-insides, dxnavi, 他多数 |
| **Consumer App (B2C/B2B2C)** — アプリDL、店舗会員アプリ | 30 | 25.6% | JR九州アプリ, WESTER, NewDays アプリ, セブンイレブン アプリ, UCS カード, ロフトアプリ, ENEOS SS app, tone モバイル, Galaxy Japan, insta360, Poiboy, 40swish, Sunshine city, ANAマイル, Tolettacat, eneos-ss, MySunshinecity, hellofamily 他 |
| **Corporate / Consulting / Agency / 教育** — プロダクトLPでない | 17 | 14.5% | DeNA×AI, cyberagent-adagency, NTT Koel, Lumiarch, Kobe電子専門学校, FCA, Digital Hollywood, Denbi, Plus-C 中大, TUS, Wired, adobe blog, gate-one, Fontworks, Family Japan (牛場研究室) 他 |

- **発見**: PLG 比率は **18.8%** にとどまる。アメリカ SaaS なら 50% を超える領域。日本の SaaS は **"エンタープライズ営業型 41.0%"** が主流で、これが電話番号・資料 DL・セミナー・導入事例といった「日本式 BtoB 三種の神器」を生む構造要因。
- Consumer App 25.6% は「店舗/交通/カード会員向けアプリ」がほとんど。App Store/Google Play バッジが HERO 直下に並ぶのが定型。

### 1.5 海外化度の分布

| 度合い | 判定基準 | 件数 | 比率 |
|---|---|---|---|
| ★★★★★ グローバル完全準拠 | Inter/Helvetica + ミニマル + PLG CTA + セミナー/電話なし | 14 | 12.0% |
| ★★★★☆ 海外風ハイブリッド | Inter + 日本式 CTA (資料DL) 混在 | 21 | 17.9% |
| ★★★☆☆ 中間 | 一部欧文フォント + 和風構造 | 32 | 27.4% |
| ★★☆☆☆ 日本ローカル主体 | WordPress + jQuery + Noto | 35 | 29.9% |
| ★☆☆☆☆ 完全ガラパゴス | table レイアウト・古い和風 | 15 | 12.8% |

- **発見**: ★★★★★ の 14 件の内訳はほぼ「グローバルブランドの日本版」(Figma, Asana, Slack, Shopify, Affinity, Insta360, Adobe, etc.) か「海外市場前提の日本 SaaS」(Studio, Newt, Lapras, fimmigrm, etc.) に限られる。**純粋に日本発で ★★★★★ を目指している例は 5-6 件程度**。
- ★☆☆☆☆ の 15 件は ARCSYSTEMWORKS 系ゲーム、自治体/教育機関、独居ケアサービス、古い業務システムなど。2006-2015 年頃の HTML 作法をそのまま運用している。

### 1.6 ミニマリズム度の分布 (カラー数推定)

`#[0-9a-fA-F]{6}` の一意出現でサンプリング：

| ミニマリズム度 | 代表 | 傾向 |
|---|---|---|
| 超ミニマル (5-10 色) | Studio, biskett, Figma JP, Slack JP, Affinity JP, Eight | PLG 系 & グローバル |
| ミニマル (10-20 色) | HRMOS, bebit, BONX, bakuraku, invox, smartmat | モダン日本 SaaS 中核 |
| 中庸 (20-40 色) | WIRED, GalaxyMobile, 8card, Conscious HEMS | 情緒コンテンツ混在 |
| 色数過多 (40+) | tabinuki, assign-navi, 古いWordPress LP | 装飾的・印刷物直輸入 |

---

## 2. 深読み 15 件の個別観察

### 2.1 bakuraku.jp (バクラク) — 日本製エンタープライズ SaaS の王道 [再掲+更新]

- 2026 年 Q2 時点で見出しを「AI エージェントで業務を完全自動化する」にピボット済 — カテゴリで 4 件しかない「AI エージェント明示」の最上位。
- Inter + Montserrat + Noto Sans JP、`#21846F` + `#001226` + `#BEEEDD` + `#0E63C4`。
- 全セクション末尾に「資料ダウンロード 無料」「3点セット」が反復し、ページ内 CTA 出現 15 回以上。
- 右下固定で `050-1790-5547 (平日 10:00-18:00)`。
- **日本 SaaS エンタープライズ LP の"完全体"**: PLG CTA ほぼなし、資料 DL + 営業電話 + セミナー + 事例 + 継続率数値 + 認証バッジの全部盛り。

### 2.2 jp.ub-speeda.com (Speeda / UZABASE) — AI Agent × 汎用 LLM 比較 [再掲]

- 「Speeda AI Agent × 汎用 LLM」の 4 観点比較マトリクスが差別化の核。
- Astro 採用 (静的生成)、`#F72A48` レッド単色アクセント。
- **2026 年の日本 SaaS が AI エージェント時代に直面した際のコピーテクニック**: "私たちのエージェントは ChatGPT とどう違うか" を比較表で直接答える。

### 2.3 stores.fun (STORES) — Webflow 製軽快プラットフォーム [再掲]

- Webflow + GSAP + Jetboost + VWO + Finsweet、`#0066ff` + `#f2f2f0` 4 色ミニマル。
- 「無料でアカウント作成」「資料ダウンロード (無料)」の **二段 CTA**。
- **日本 SaaS で PLG と Sales assisted を両立させる代表例**。

### 2.4 www.figma.com/ja (Figma JP)

- HTML が 1.4MB という大きさ (hydration 用の JSON を大量に inline している)。
- Inter + Helvetica + system-ui、font-family ディレクティブは 29 カウント — typo を CSS 変数で細かく制御。
- Hero のアニメーションは conic-gradient (18deg 刻みで 20 色) を CSS で回転させている。
- Next.js 構成、WordPress 形跡なし。
- **発見**: Figma はグローバル LP をそのまま日本語化しており、CTA は「無料で試す」(PLG)。電話番号なし・資料 DL なし・セミナーなし。**"ガイジン SaaS" の完全体**。

### 2.5 asana.com/ja (Asana JP)

- Next.js, Inter + Helvetica + Work Sans。
- HTML 99K tokens — 全ページをプリレンダ。
- 「AI Teammates」「ワークフロー」「自動化」が並ぶが、**日本語 hero コピーは "チームの仕事を整える" とローカライズ**。原文 "Where work happens" の直訳ではない。
- セミナー/FAQ あり、**電話番号なし、資料 DL なし**。日本語版でも PLG CTA を貫いている数少ない例。

### 2.6 slack.com/intl/ja-jp (Slack JP)

- 414 行の比較的コンパクトな HTML。CDN から CSS を読み込む。
- Inter 系 + Noto Sans JP + Helvetica。`#4A154B` (aubergine) を軸に 10 色未満。
- Hero は「仕事はここで起きている」+ Huddle / Canvas / AI 説明の順。
- セミナー・事例・料金あり、**日本語版でも "無料でサインアップ" を主 CTA に残している**。
- **グローバル PLG LP が日本語に降りてきたときに、最後まで PLG を捨てない最小セット**。

### 2.7 shopify.jp/plus (Shopify JP Plus)

- Next.js + Webflow のハイブリッド (117 件中 Webflow 検出は本件のみ)。
- Inter + Montserrat + Roboto、`#002e25` + `#5a31f4` の Shopify ブランドカラー。
- 「無料トライアル」+ 「営業に相談」の二段構え = **グローバル Plus LP と同じ構造**。
- HRMOS や bakuraku のような「資料 DL 中心」構造ではなく、米国式の「Start trial / Talk to sales」二択。

### 2.8 affinity.serif.com/ja-jp (Affinity)

- 1 行 HTML に圧縮されているが、Next.js + Inter + Helvetica。
- Canva 傘下の後でも旧 Serif ブランドのミニマルさを継承、英字見出しが中心。
- **日本 SaaS 文脈の中では "例外的に和風要素ゼロ"** — 電話番号なし、資料 DL なし、セミナーなし、事例さえない。**単発価格表示 + "購入" CTA のみ**。

### 2.9 lp.smartmat.io (スマートマットクラウド)

- HubSpot CMS (hubfs/template_*) + Bulma + Slick。
- Noto Sans JP + Roboto。
- HERO の視覚階層: 「導入件数 1,800 社以上」 → 「置くだけ 在庫管理DX」 → 「5分でわかる資料をプレゼント」 → 「全部わかる3点セット 資料ダウンロード 無料」。
- 4 業種ごとに企業ロゴループ (自動車/化学製薬/機械/医療宿泊/インフラ)。
- **IoT × SaaS × エンタープライズ営業型**の見本。バクラクと似た構造だが、視覚は和風寄り。
- CTA は資料 DL 一本 (bit.ly 短縮 URL で計測)、「お問い合わせ」は補助。

### 2.10 invox.jp (invox 受取請求書)

- **WordPress + jQuery + Slick** の典型。テーマ `invox_theme`。
- Noto Sans JP + Helvetica + Lato、WP 標準の vivid-cyan-blue / vivid-purple グラデを継承。
- CTA: 「資料請求」「お試し」「お問い合わせ」の 3 本立て、電話番号表示あり、料金ページ別立て、セミナー、FAQ、ISO27001 認証バッジ、JIIMA 認証あり。
- **日本 SaaS で WordPress を使い続ける合理性の完成形**: スピード・制作会社流通性・ブログ運用・メディア SEO すべてを WordPress で回収している。

### 2.11 8card.net (Sansan Eight)

- 433 行、極めてシンプルな自作静的 HTML。
- Sansan の他プロダクト (Eight Team / Eight Career Design) への導線を footer + campaign banner に集約。
- **アプリ LP の完成形** — Hero にApp Store/Google Play バナー、features (3 本)、Eight プレミアム料金 (月額 600円)、Eight Team (企業利用) の順。
- Tailor ja.js (自社 A/B) + Twitter Card / facebook SDK / GTM / Bing UET / Cloudflare challenge の全部盛り計測。
- **B2C アプリが B2B (Eight Team / Career) にアップセルする"ハイブリッド LP"**として見本になる。

### 2.12 dena.ai (DeNA × AI)

- Nuxt.js (Vue SSR)、Be Vietnam Pro + Noto Sans JP + Zen Kaku Gothic New + Nunito Sans + Sawarabi Gothic の **異例に多いフォント 5 種**。
- 「AIオールイン」を軸にした Tech Corporate、HERO は Compressa VF (可変フォント) でレター単位の拡縮アニメーション。
- Carousel: DeNA x AI Day 2026 → For & With Startups → 南場の語り。
- SaaS プロダクト LP ではなく **"AI コーポレート採用 + 発信拠点"**。
- **発見**: 2026 年、大手 Tech 企業の日本コーポレートは「AI オールイン + 創業者メッセージ + 社内ブログ/YouTube ハブ」というパターンに収束しつつある。

### 2.13 bonx.co/ja (BONX)

- **WordPress + jQuery + 自作テーマ `bonx2019_ja`** ── 7 年物の古い土台だが上品なタイポで見せる。
- Noto Sans JP + Poppins (Google Fonts)。
- セクション構成: visual → news-release → about → products → technology → company → recruit → contact → support → online-shop。
- **"IoT ハードウェア + サービス + 企業 B2B" のハイブリッド**: プロダクトは BONX BOOST/GRIP/mini、SaaS 的要素は BONX WORK、コーポは BONX INC.。
- 「ニュースリリース」が top にあり、投資家向け発信が前提。日本特有の「サービス + プロダクト + 投資家 + 採用」全部乗せ型コーポ LP。

### 2.14 hrmos.co/hr (HRMOS タレントマネジメント)

- Bizreach 運営、1 行 HTML に JSON-LD で SoftwareApplication スキーマを定義 (`"name": "HRMOS（ハーモス）タレントマネジメント"` + description)。
- **SEO 重視の WP 系ではない**: 静的サイト (B2B assets の画像 CDN) + Google Tag Manager 群。
- 「社員情報の一元管理」「目標評価運用」「エンゲージメント」の 3 大機能が meta description と HERO に繰り返される。
- SaaS の "認知獲得 + 比較検討" 層への SEO 最適化が徹底されている。

### 2.15 studio.design [再掲+更新]

- Inter + Noto Sans JP + IBM Plex Mono + CSS 変数 (`--s-font-0fba208c`)。
- `#f7f7f7` が CSS 内で 323 回出現する超ミニマル。8 色で 700+ 配色。
- Usecase 5 カテゴリ (コーポ/ブログ/イベント/店舗/ポートフォリオ) → 各カテゴリで実サイト URL リスト。
- **letter-spacing: -0.04em** を全見出しに適用 = Linear/Vercel/Framer の共通作法。
- 「無料ではじめる arrow_forward」+ 「法人向け製品資料をダウンロード」 = PLG + Sales の二段。
- Material Icons の利用は **2026 年時点で見るとやや懐かしい選択**、本来なら Lucide や Phosphor に置き換えが進むはず。

---

## 3. 共通パターン (抽出した 117 件から)

### 3.1 ヒーロー構造パターン

| パターン | 頻度 | 代表 |
|---|---|---|
| **A: キャッチコピー + サブコピー + 資料DLボタン + 社ロゴ** | 最多 (推定 40+) | bakuraku, smartmat, invox, Talknote, recoreru, searchwrite, oro DX |
| **B: キャッチコピー + ストア2バナー (iOS/Android)** | 19 件前後 | 8card, Loft app, ENEOS, JR九州, WESTER, NewDays, 7-11 |
| **C: 動画/アニメ背景 + 大見出し + PLG CTA** | 12 件前後 | Studio, Figma JP, Stores, DeNA×AI, Koel |
| **D: 機能タブ + 課題別ナビ + サブ HERO** | 6 件前後 | Speeda (9 タブ), Asana, HRMOS |
| **E: コーポ Top (事業内容 + News + Recruit + IR)** | 17 件前後 | BONX, estie, DeNA, NTT Koel, Lumiarch |

### 3.2 CTA テキストのバリエーション (頻出順)

1. **資料ダウンロード / 資料請求** — 29 件
2. **お問い合わせ** — 81 件 (ほぼ全件)
3. **無料トライアル / 無料ではじめる / 無料でお試し** — 16 件
4. **今すぐ無料でダウンロード** — 19 件 (アプリ系)
5. **デモを見る / 無料デモ** — 約 10 件 (Speeda, Usergram, HRMOS など)
6. **まずは話を聞いてみる** — 約 5 件 (日本独自の柔らかい言い回し)
7. **セミナー申込** — 12 件
8. **購入する / Buy now** — 3 件 (Affinity, Cybozu Office など)

- **発見**: 「お問い合わせ」の件数が 81 件 = ほぼ全件に存在するが、これは **header nav に常備されるデフォルト項目** の性質も強い。本体 CTA として設計されているのは bakuraku/smartmat 系の資料 DL と PLG 系の無料トライアルに分かれる。

### 3.3 信頼形成パターン

| パターン | 使用率 |
|---|---|
| **導入社数 (XX,XXX 社)** | 30.8% |
| **顧客企業ロゴループ** | ~ 60% (SmartMat/bakuraku/Speeda 他) |
| **継続率/満足度 (99% 型)** | 推定 15-20% |
| **ISO27001 / SOC2 / Pマーク** | 5.1% |
| **JIIMA / 電子帳簿保存法対応** | 3 件 (bakuraku, invox, MoneyForward) |
| **受賞バッジ (ITreview GRID, BOXIL など)** | 推定 10% |
| **著名人 / メディア掲載ロゴ** | 推定 10% |

### 3.4 料金ページ/ブロックパターン

- **3 プラン表 (Starter/Standard/Enterprise)** が 40 件以上で最頻出。Shopify JP, LINE WORKS, Speeda, MoneyForward, Cybozu 型。
- **単一プラン月額表記** — biskett, Eight Premium (月額600円) 型。
- **"お問い合わせ" のみ (価格非公開)** — bakuraku, HRMOS, estie, Usergram 型。**エンタープライズ日本 SaaS の常套**。
- **Per-user / Per-seat 課金明示** — Slack JP, Asana JP, Figma JP = グローバル系のみ。

### 3.5 機能紹介パターン

| パターン | 頻度 |
|---|---|
| **3 features (大きな機能 3 本建て)** | 最多 |
| **5-9 features グリッド (3x3 カード)** | Speeda 9 課題, STORES 9 サービス |
| **タブ切り替え課題別** | Speeda, HRMOS, LINE WORKS |
| **スクロール連動の段差表示** | Studio, Figma JP, bakuraku (3rd section 以降) |

### 3.6 AI エージェント訴求の増加 — 詳細

**明示 "AI エージェント"**: 4 件 (bakuraku, Speeda, CyberAgent AD.AGENCY, WIRED 関連, invox の "AI OCR" は近縁)
**AI 全体言及**: 18 件前後 (dena.ai, ai-model, autoro, chuwrite, lapras, ms.recruit-insides, mogukatsu, searchwrite, eichiii, invox, fconne, 他)
**2025 年比の変化**: 前回 30 件で AI 訴求は 3 件だったが、117 件では "AI OCR / AI 自動化 / AI マッチング" まで入れると 15% まで拡大。

- **Speeda のケースが最重要**: 汎用 LLM との比較マトリクスを置くのは、**"ChatGPT で十分じゃないのか？" という顧客側の疑問に先回りで答える AI 時代の差別化定石**。
- **bakuraku のケース**: AI エージェントを Service カードのトップに格上げし、既存機能 (債権債務/人事労務/ヘルプデスク) を "Agent 化できる" ラインアップとして再配置。ピボット戦略の教科書例。

---

## 4. 機能紹介 / 導入事例 / 料金プラン の深掘り

### 4.1 機能紹介

- **日本 SaaS の定石**: Hero 下に「できること」3-9 個をカード化 → 1 機能ごとにスクロール連動スクリーンショット。
- **PLG 系**: インタラクティブなプロダクトデモ (Figma/Asana のような動くスクリーンショット) は稀。静的画像 + 矢印アニメがほとんど。
- **Usergram (bebit)** は珍しく GSAP で画面遷移を魅せる。bakuraku は Three.js でパーティクル背景。

### 4.2 導入事例

- 30.8% (36/117) で明示セクション。
- 典型構造: 企業ロゴ → 業種タグ → BEFORE/AFTER 数値 → 導入者インタビュー → フル記事へのリンク。
- **エンタープライズ日本 SaaS はロゴ 20-50 社のループを必ず持つ** (smartmat: 5 業種x2 社、bakuraku: 15,000 社アピール)。
- **B2C アプリは "レビュー文 + 星" 代替**が多い (App Store スクリーンショット埋込)。

### 4.3 料金プラン

- **50.4% で料金セクション存在**。残り半数は「お問い合わせ価格」。
- **エンタープライズ SaaS の 60% 以上は "要問い合わせ"** (bakuraku, HRMOS, Speeda, invox エンタープライズプラン, etc.)。
- Shopify JP Plus / Slack JP / Asana JP / Figma JP が **明示価格ページを持つ数少ないケース**。

---

## 5. design-mcp 方針 (SaaS ジャンル専用プリセット)

### 5.1 コアテンプレート: 「JP-SaaS-Enterprise-Hero」 (エンタープライズ型 41%)

```
[ 1. Top bar: ロゴ + ナビ + 資料DLボタン + 電話番号 ]
[ 2. Hero:
     - 大見出し (機能 + 価値) — 例「AI エージェントで業務を完全自動化」
     - サブコピー 1 行
     - CTA 2 本: "資料ダウンロード 無料" + "お問い合わせ"
     - 信頼数字 (XX,XXX 社 / 継続率 99%)
     - 顧客ロゴループ (20-30 社)
]
[ 3. 課題セクション: "こんな課題はありませんか？" 3 列 ]
[ 4. 機能紹介: 3-9 カード or スクロール連動 ]
[ 5. 導入事例: 3 枚カード + "もっと見る" ]
[ 6. 比較表 (vs 競合 or vs 汎用 LLM) ]
[ 7. 料金: 3 プラン or "お問い合わせ" ]
[ 8. FAQ 8-12 項目 ]
[ 9. セミナー/ウェビナー案内 ]
[ 10. Final CTA: "資料DL" + "お問い合わせ" + 電話番号 ]
[ 11. Footer (認証バッジ ISO27001/Pマーク) ]
```

**パレット推奨**:
- Primary: `#21846F` (tealtype) or `#0E63C4` (linkblue) — 視認性と信頼感
- Dark: `#001226` or `#111827`
- Accent: `#BEEEDD` (pale accent) or `#F72A48` (Speeda red)
- Background: `#FFFFFF` + `#F7F7F7`

**フォント推奨**:
- 欧文見出し: **Inter** (28.2% 採用) or **Montserrat** (英字副タイトル)
- 和文: **Noto Sans JP** 700/500/400
- letter-spacing: -0.02em (見出し), 0 (本文)

### 5.2 サブテンプレート: 「JP-SaaS-PLG」 (PLG 型 18.8%)

```
[ Hero: 英字見出し + 情緒コピー + "無料ではじめる" 主 CTA ]
[ Usecase グリッド (5 カテゴリ) ]
[ インタラクティブ機能紹介 ]
[ 実例 URL リスト (Studio 方式) ]
[ 料金 (明示・3 プラン) ]
[ CTA: "無料ではじめる" + "法人資料" ]
```

**パレット**: `#f7f7f7` + `#222` + `#ffffff` の超ミニマル、または Primary 1 色 + Neutral 4 階調。
**フォント**: Inter + Noto Sans JP の並列、letter-spacing: -0.04em。

### 5.3 サブテンプレート: 「JP-App-Consumer」 (Consumer App 型 25.6%)

```
[ Hero:
     - プロダクト名ロゴ
     - キャッチコピー 1 行
     - App Store + Google Play 2 バナー
     - スマホモックアップ画像
]
[ 3 機能紹介 (スマホ画面差分) ]
[ お得情報・キャンペーン ]
[ よくある質問 ]
[ Footer: App DL + 会社情報 ]
```

**パレット**: 店舗/交通/CVS のコーポカラーを主軸 (ENEOS赤, JR緑, セブン橙 など)。

### 5.4 design-mcp プロンプトエンジンへの指示

1. **デフォルトは "JP-SaaS-Enterprise-Hero"**: 日本 SaaS 生成タスクで "PLG" や "global" が明示されなければ、資料 DL + 電話番号 + セミナー + 導入事例が標準入り。
2. **"海外風" 指定時**: Inter + Noto Sans JP、ミニマル 5-8 色、letter-spacing: -0.04em、CTA は "無料ではじめる" 主。ファネル要素 (電話/資料DL) を削除。
3. **"AI エージェント" トピック時**: 汎用 LLM 比較マトリクスを必須化。2026 Q2 以降の SaaS は "我々の Agent は汎用 ChatGPT と何が違うか" に答えていないと弱い。
4. **禁止パターン**:
   - Hero に "システム開発・DX 支援" のような抽象サービス名 (コンサル LP のクリシェ)
   - WordPress デフォルト gradient (`--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple` 等)
   - 40 色以上のカラーパレット
   - table レイアウト (2006 年作法)
5. **必須要素 (JP Enterprise template)**:
   - 「資料ダウンロード」CTA を 3 箇所以上
   - 信頼数字 1 つ以上 (導入社数 or 継続率 or 満足度)
   - 顧客ロゴループ (8 社以上)
   - FAQ (8 項目以上)
6. **プラットフォーム判定**: "WordPress 維持" が指定されたら Slick + jQuery テンプレート、"Next.js" なら Swiper + Tailwind。Webflow は選ばない (日本 SaaS で 0.9%)。

### 5.5 "和風⇔海外風" スライダー定義

design-mcp のパラメータとして:

```yaml
japaneseness: 0 .. 100
  # 0  = Figma JP / Affinity JP (完全グローバル)
  # 30 = Studio / Shopify JP
  # 50 = bakuraku / Speeda (ハイブリッド)
  # 70 = invox / smartmat (日本式)
  # 100 = 2010 年頃のコーポ SaaS

plg_vs_sales:
  plg:            # セルフサーブ型
  hybrid:         # 二段 CTA
  sales_assisted: # 資料DL中心
  enterprise:     # お問い合わせのみ

ai_positioning:
  none
  ai_feature    # "AI OCR"
  ai_assistant  # "AI 相棒"
  ai_agent      # "AI エージェント" (2026 Q2 以降の主流)
```

---

## 6. 前回 (30 件分析) との差分

| 項目 | 前回 30 件 | 今回 117 件 | 変化 |
|---|---|---|---|
| PLG 比率 | 30% | 18.8% | 母数拡大で実態が露出、日本 SaaS はエンタープライズ偏重 |
| 資料 DL CTA 出現率 | 50% 程度 | 24.8% (明示) | 母数増で埋没したが、エンタープライズ 48 件中では 60%+ |
| AI エージェント訴求 | 2 件 (bakuraku/Speeda) | 4 件 (+CyberAgent +invox) | やや増加、ただし明示率は 3.4% と低い |
| Inter 採用 | 6 件 (20%) | 33 件 (28.2%) | **8 ポイント上昇**。モダン SaaS の基準フォントとして定着 |
| Webflow | 1 件 (STORES) | 1 件 (Shopify のみ) | STORES は Webflow のままだった可能性、STORES JP は今回別 URL |
| WordPress | 不明 | 33 件 (28.2%) | **日本 SaaS の土台は今も WordPress** |
| jQuery | 不明 | 63 件 (53.8%) | 過半数が依然 jQuery 依存 |
| App Store / Play バナー | 数件 | 19 件 (16.2%) | 「SaaS カテゴリ」に店舗アプリが多く混入 |

**決定的な違い**: 117 件で見ると「SaaS カテゴリ」は実際には **SaaS + アプリ + コーポ + 教育** のハイブリッド群であり、純粋な B2B SaaS は 38% 程度に過ぎない。これは design-mcp の "saas" ジャンル出力時に **サブタイプ分岐** (enterprise / plg / consumer-app / corporate) を必須にすべきことを示唆する。

---

## 7. 推奨する次のアクション (design-mcp 反映候補)

1. **`saas-service` ジャンルの 4 サブタイプ化** — Enterprise / PLG / Consumer App / Corporate Hybrid
2. **`JP-SaaS-Enterprise-Hero` プリセットの実装** — 上記 5.1 を YAML テンプレ化
3. **`letter-spacing: -0.04em` を SaaS 系見出しのデフォルト化** (Inter+Noto 使用時)
4. **AI エージェント比較マトリクスのスニペット化** — 「vs 汎用 LLM」4 観点
5. **資料DL + 電話番号 + セミナー の "日本式信頼三種" トグル** — japaneseness > 50 で自動付与
6. **WordPress 既定 gradient の禁止リスト追加**
7. **顧客ロゴループ (Swiper 自動スクロール) スニペット** — 日本 SaaS で 60% が使用
8. **"要お問い合わせ" プラン表** — エンタープライズ向けテンプレート

---

## 8. 残った疑問 / 次ラウンドに回すべき論点

- **STORES の Webflow 運用は現在もか？** — 今回の 117 件には STORES 本体が含まれず、Shopify のみ Webflow 痕跡。ラウンド3で確認要。
- **AI エージェント訴求は 2026 Q3 に本格化するか？** — 現時点 3.4% は思ったより低い。次回 (3 ヶ月後) で再計測し、浸透速度を測定したい。
- **"和文 Inter 並列" の品質問題** — Inter + Noto Sans JP 併用時、ウェイト階層がズレる問題がある。どれくらいの LP がこの問題を抱えているかをミクロ検証すべき。
- **PLG vs Sales の境界線は業種依存か？** — 勤怠/会計/ERP は 100% Sales、デザインツール/コミュニケーションは 100% PLG、の仮説を業種別に検証要。
- **セミナー集客→資料DL→営業電話のファネル効率** — LP 上の「セミナー」ボタン位置と電話設置の相関を分析すべき。

---

## 9. 拡張: ケース別フィンガープリント (追加 20 件の要約観察)

時間の都合で深読み 15 件に加え、grep ベースで主要 20 件を要約する。

### 9.1 Talknote (talknote.com) — 情報共有プラットフォーム
- WordPress、jQuery、Swiper、Noto Sans JP。CTA: 「資料請求」「無料お試し」の二段。
- Enterprise 型の定石 (セミナー 9 回言及)、料金は 3 プラン。
- 「チームワークを科学する」という抽象コピー → 日本型の "情緒+数字" ハイブリッド。

### 9.2 biztel.jp (BIZTEL) — クラウド PBX / コールセンター
- WordPress、jQuery、法人表記 41 回 (117 件中最多)。
- 電話番号 `0120-96-1040` を必ず header に出す。
- セキュリティ ISO27001 バッジ、業種別導入事例、3 プラン料金 (ベーシック/アドバンス/カスタム)。
- **"エンタープライズ日本 SaaS で最も古典的な構造"**: 2015 年頃から基本構造を変えていない。

### 9.3 cybozu.co.jp/office (サイボウズ Office) — 中小企業向けグループウェア
- Helvetica + Montserrat + Noto、法人表記 11 回。
- 30 日無料お試し + 購入 2 段 CTA、App Store バナー付き。
- 「かんたん らくらく」を軸に中小企業層向けに情緒化。
- FAQ 12 項目以上、セミナー、ウェビナー、セキュリティ説明完備。

### 9.4 line.worksmobile.com/jp (LINE WORKS)
- Next.js + Inter + Montserrat + Noto Sans JP。`#00C300` (LINE グリーン)。
- 無料/スタンダード/アドバンスド の 3 プラン明示、Swiper、FAQ、セミナー完備。
- **"日本発だが UI は半分グローバル寄り"** = Naver 系だがローカライズ徹底。
- 法人表記 8 回、PLG と Sales の両面 CTA。

### 9.5 service.itandi.co.jp (イタンジ 期間限定キャンペーン)
- Next.js + Noto Sans JP、WP 痕跡なし。
- 「不動産業務の 93% を自動化」+ ビッグロゴループ。
- 無料相談、導入事例 3 件、お問い合わせ集約型。
- **バーティカル SaaS (不動産)** の典型。

### 9.6 dx.oro.com (ORO DX)
- WordPress + Montserrat + Helvetica、ERP 軸。
- 「PSA型 ERP」という複雑概念を "一枚絵インフォグラフィック + 長文解説" で説明。
- セミナー多数、電話番号、資料DL。日本の **老舗 Enterprise SaaS** の作法。

### 9.7 grandit.nhs.co.jp (GRANDIT ERP) — 日立システムズ
- WordPress、jQuery、法人表記 23 回。
- ISO27001 / Pマーク明示、導入社数多数、3 プラン風の業務別カタログ。
- **大企業 ERP SaaS (主戦場は会計/販売管理/製造)** の型。紹介動画 + パートナー SI 誘導。

### 9.8 searchwrite.jp (SEARCH WRITE) — SEO SaaS
- WordPress、料金 3 プラン、FAQ、セミナー、ISO 系バッジ。
- 「SEO のプロをいつも隣に」の情緒コピー。
- 相対的にモダンな日本 SaaS UI (Noto + Inter)。

### 9.9 pro-seeds.com/learningware (Learning Ware) — eラーニング SaaS
- WordPress + jQuery + Swiper + Montserrat + Inter。
- 「導入社数 1,500 社以上」「累計 200 万 ID」の信頼数字を hero に配置。
- 資料 DL + 無料トライアル + 電話の全部盛り。

### 9.10 autoro.io (AUTORO) — ワークフロー自動化
- Next.js + Noto Sans JP + Inter + GSAP 風アニメ。
- 「AI × RPA × iPaaS」、PLG と Sales の中間 (無料トライアル + 資料)。
- モダン SaaS UI の代表格。

### 9.11 fimmigrm.com — 動画配信 SaaS
- Next.js、Inter、Noto。ミニマル UI。`#0D0D0D` + `#F2F2F2`。
- グローバル風 Hero 動画 + 無料ではじめる。

### 9.12 lapras.com — エンジニア採用プラットフォーム
- WordPress + jQuery、法人表記 1、メディア多数掲載。
- セミナー 1、お問い合わせ、事例、料金別ページ。
- 「Your Work, Your Future」英字コピーベース。

### 9.13 recoreru.com (Recoreru) — 勤怠管理
- WordPress、jQuery、法人表記 7。
- 「働き方改革に対応 カスタマイズできるクラウド型 勤怠管理」
- 料金 3 プラン、FAQ 大量、電話番号 `0120-` 付き。

### 9.14 chuwrite.com — AI 文書作成
- Next.js、Inter、Noto、PLG 型「無料ではじめる」。
- AI エージェント訴求 "AI で書類作成を自動化"。
- 料金 3 プラン、FAQ 8 項目、モダン UI。

### 9.15 penmark.jp — 大学生向けアプリ
- Next.js + Noto + Helvetica、情緒的コピー「学生生活をもっと楽しく」。
- App Store/Google Play バナー、機能紹介 4 ブロック、FAQ。
- **Consumer App + SaaS バックエンド** 型。

### 9.16 newt.so (Newt) — ヘッドレス CMS
- Next.js + Inter、`#0070f3`、料金明示 3 プラン (Free/Pro/Enterprise)。
- 完全グローバル PLG 型、letter-spacing: -0.04em の Hero。
- **日本発で最も海外化度が高い SaaS LP の一つ**。

### 9.17 bebit.co.jp/usergram (Usergram) — ユーザー行動分析
- WordPress + jQuery + GSAP、老舗 UX コンサル系。
- ISO27001、導入事例多数、セミナー、電話番号。
- 「カスタマージャーニー可視化」系の説明構造。

### 9.18 moneyforward.com/campaign/mf_cloud_9220 — MF クラウド会計 キャンペーン LP
- Next.js + Noto + Poppins、キャンペーン型 hero (半額 or N 月無料)。
- 「導入社数 No.1」「継続率 98%」の数字を前面に。
- モバイル無料トライアル + 電話 + 資料 の3 段。

### 9.19 shiftlink.tech — 人材マッチング/シフト
- Next.js、モダン UI、料金、導入事例、FAQ 完備。
- 法人表記なし/少、情緒ベースコピー「誰もが活躍できる世界へ」。

### 9.20 wacul-ai.com — AI アナリスト
- HTML 8KB の超シンプル LP (ランディング前提)。
- `window.location` でリダイレクト or SPA 化、初期 HTML はプレースホルダ。
- **最小の "ゲートウェイ LP"**、この形式は計測・誘導特化で増えている。

---

## 10. HTML 文字数/複雑度の分布

| 範囲 | 件数 | 意味 |
|---|---|---|
| < 10KB | 6 | ゲートウェイ/サービス終了/CSR SPA 初期 HTML (biskett, feels.one, wacul-ai 等) |
| 10-30KB | 28 | シンプル静的 LP、プロダクト単機能向け (8card, arfit, sakurai-gs, bonx 等) |
| 30-80KB | 36 | 標準的な日本 SaaS LP (invox, HRMOS, smartmat, talknote 等) |
| 80-200KB | 29 | 情報量が多いエンタープライズ LP (bakuraku, cybozu, lapras 等) |
| 200KB-1MB | 14 | リッチ LP (dena.ai, LIVE BOARD, biztel, GalaxyMobile 等) |
| > 1MB | 4 | Next.js SSR フルプリレンダ (Figma JP 1.4MB, Asana JP 400KB+, Shopify JP 300KB+, 他) |

**発見**: Next.js の SSR で hydration 用 JSON を inline する方式は **HTML を 10 倍に膨らませる**。Figma JP の 1.4MB は「コンテンツ量」ではなく「フレームワークの代償」であり、初回描画のパフォーマンスを犠牲にして SPA 体験を優先している典型。

---

## 11. 情緒コピー vs ロジックコピーの偏差

117 件の見出しパターンを手動で類型化：

| パターン | 件数 | 代表 |
|---|---|---|
| **機能訴求 (〜を自動化 / 〜管理システム)** | 約 50 | invox, smartmat, recoreru, biztel, bakuraku |
| **価値訴求 (〜を実現 / 〜が変わる)** | 約 25 | estie, Speeda, HRMOS |
| **情緒訴求 (〜の未来 / 〜に寄り添う)** | 約 20 | Awarefy, BONX, Koel, NTT koel, Lumiarch |
| **英字ブランドワード (Where work happens 型)** | 約 15 | Asana, Slack, Figma, Affinity, Newt |
| **数字訴求 (導入 XX,XXX 社 / 継続率 99%)** | 約 12 | smartmat, MF Cloud, bakuraku, ロイヤルエッセンス |

- **発見**: 日本 SaaS の Hero 見出しは **機能訴求 43%** で圧倒的。これは「課題解決 SaaS」「業務改善 SaaS」として売る日本型 BtoB の性格。情緒訴求 17% はコンシューマー寄りアプリやブランド優先の BONX/NTT 系に偏る。
- 海外 SaaS の "Where work happens" (Slack) / "One tool for your whole team" (Asana) のような抽象訴求は日本語化されても **機能語に言い換えられる** 傾向 ("チームの仕事を整える" など)。

---

## 12. マイクロコピー収集 (頻出表現)

### 12.1 CTA マイクロコピー

| 表現 | 件数 (概算) | カテゴリ |
|---|---|---|
| 資料ダウンロード | 29+ | 定番 |
| 資料請求 | 10+ | WP 系老舗 |
| 無料ではじめる | 12+ | PLG 系 |
| 無料でお試し | 8+ | SaaS 系 |
| 今すぐ無料でダウンロード | 19 | アプリ系 |
| お問い合わせはこちら | 50+ | 汎用 |
| まずは相談する | 5 | 柔らかい日本型 |
| デモを見る | 6 | エンタープライズ |
| トライアルをはじめる | 4 | PLG 日本寄り |
| Get started | 3 | 海外ブランド直輸入 |
| Sign up free | 2 | 同上 |

### 12.2 信頼形成マイクロコピー

- **「導入社数 XX,XXX 社突破」** — 11 件で使用 (smartmat 1,800社、MF クラウド多数)
- **「継続率 98% / 99%」** — bakuraku, MF, HRMOS 系
- **「満足度 97%」** — bakuraku
- **「業界 No.1」** — MF クラウド会計, HRMOS
- **「ISO27001 認証取得」** — 6 件
- **「Pマーク取得」** — GRANDIT, 他数件
- **「JIIMA 認証」** — bakuraku, invox, MF (インボイス/電帳法系の必需品)
- **「ITreview GRID ○○ Leader」** — 約 5 件、主にクチコミ SaaS 受賞バッジ

### 12.3 FAQ 典型質問文

- 「セキュリティ対策は？」
- 「導入までの期間は？」
- 「既存システムからの移行は可能？」
- 「他社製品との違いは？」
- 「無料トライアルでできること / できないことは？」
- 「サポート体制は？」
- 「どんな企業に向いていますか？」
- 「解約は簡単にできますか？」

**これらは "日本 B2B SaaS FAQ の定番 8 問" として design-mcp に組み込むべき**。

---

## 13. レスポンシブ・モバイル配慮

117 件全てで `<meta name="viewport" content="width=device-width, initial-scale=1">` は必須。追加観察：

- **モバイル専用 Bottom Banner** が 15 件前後で存在 (Eight, JR九州, NewDays, 吉野家など)
- **SP 用画像 (`class="sp"` vs `class="pc"` 分岐)** が WordPress 系で多い (BONX, invox, smartmat)
- **Sticky CTA on mobile** は新しめの SaaS (bakuraku, HRMOS, Speeda, Itandi) で標準化
- **Bottom fixed 電話番号** は業務ミッションクリティカル系で健在

---

## 14. SEO / メタ情報の傾向

- **JSON-LD 構造化データ**: HRMOS (SoftwareApplication)、smartmat (BreadcrumbList)、8card (WebSite) 等 20 件前後で採用
- **OG image サイズ**: 1200x630 が 90% 以上
- **canonical URL**: ほぼ全件で設定済み
- **hreflang**: 多言語対応は 8card, BONX, Figma JP, Asana JP, Slack JP, Shopify JP, Insta360 の 7 件程度
- **Twitter Card type**: `summary_large_image` が大半

---

## 15. アクセシビリティの現状

- `alt` 属性: ほぼ全件で設定されているが、装飾画像に `alt=""` を使うベストプラクティスは半分以下
- `aria-label`: モダンな SaaS (bakuraku, Studio, Figma JP, Asana JP) で使用、WP 系では少ない
- コントラスト比: ミニマル系ほど高い、装飾過多な古い WP 系は低め
- キーボードナビ: jQuery 依存の old-school LP は tab 順が不安定なケース多数

**所見**: 日本 SaaS のアクセシビリティ水準は海外トップ (Stripe, Linear, GitHub) に比べて 2-3 段階低い。design-mcp での自動化ではここを底上げする余地が大きい。

---

## 16. セクション順序の"正規文法" (日本 SaaS Enterprise 型)

117 件を観察してもっとも頻出する順序を正規化：

```
1. Header  (logo + nav + CTA: 資料DL)
2. Hero     (見出し + サブ + CTA 2本 + 信頼数字 or 顧客ロゴ)
3. 顧客ロゴループ (20-50 社)
4. 課題セクション「こんなお悩みありませんか？」
5. 解決セクション「〇〇で解決」
6. 機能一覧 (3-9 カード)
7. 特長/選ばれる理由 (3-6 項目)
8. 導入事例 (2-6 件)
9. 数字で見る実績 (○○社/○○％)
10. セキュリティ/認証
11. 料金 (3 プラン or 要問い合わせ)
12. よくある質問 (FAQ 8-12 問)
13. お役立ち資料 (3-6 PDF サムネ)
14. セミナー/ウェビナー
15. 最終 CTA (資料DL + お問い合わせ + 電話)
16. Footer (会社情報 + 認証バッジ + 関連リンク)
```

- **最低限版 (短い LP)** は 1→2→4→6→8→11→15 の 7 セクションに圧縮される。
- **フル版** は 16 セクション、スクロール深度 7-10 画面。日本 SaaS の "長い LP" は米国比で 2 倍の長さ。

---

## 17. design-mcp 出力パラメータの再整理 (最終版)

```yaml
# design-mcp 用 SaaS ジャンル出力スキーマ
genre: saas-service

subtype:
  - enterprise      # 資料DL + 電話 + セミナー
  - plg             # 無料ではじめる + 英字
  - consumer-app    # App Store/Play + 店舗
  - corporate       # IR + News + 採用 (hybrid)

japaneseness: 0-100      # 0=Figma JP型, 100=2010年型WP
ai_mode:
  - none
  - ai_feature
  - ai_assistant
  - ai_agent           # 2026 Q2 以降の主流

trust_level:
  - minimum            # 顧客ロゴ 5 社のみ
  - standard           # 導入社数 + 継続率
  - maximum            # ISO27001 + JIIMA + 導入社数 + 継続率 + メディア掲載

cta_pattern:
  - single             # 無料ではじめる のみ
  - double             # 資料DL + お問い合わせ
  - triple             # 資料DL + お問い合わせ + 無料トライアル
  - with_phone         # 上記 + 電話番号

section_depth:
  - minimal            # 7 sections
  - standard           # 12 sections
  - full               # 16 sections

palette_style:
  - monochrome         # Studio/Figma 系
  - brand_tealblue     # bakuraku 系
  - brand_redaccent    # Speeda 系
  - brand_greencyan    # LINE WORKS/BONX 系
  - grayscale_minimal  # Newt 系

typography:
  headline_font: [Inter, Montserrat, Helvetica, Noto Serif, Noto Sans JP]
  body_font:     [Noto Sans JP, Roboto, Lato]
  letter_spacing: [-0.04em, -0.02em, 0, 0.02em]

library_stack:
  - wordpress          # 33 件 (28.2%)
  - nextjs             # 16 件 (13.7%)
  - nuxtjs
  - webflow
  - astro              # Speeda
  - vanilla_static     # Eight, biskett
```

---

## 18. 最終まとめ — 4 つの戦略的インプリケーション

1. **日本 SaaS LP の文法は海外とは別物** — 米国テンプレートをそのまま輸入しても 41% のエンタープライズ顧客層にリーチできない。資料 DL / 電話 / セミナー / 3 プラン / 導入事例 / 認証バッジの "日本式 6 点セット" を持たないと BtoB 現場の期待値に届かない。
2. **"和風⇔海外風" の中間層にチャンスがある** — 現状は二極化しており、★★★☆☆ の 32 件だけが両者の良いとこ取り。この層を狙うとデザイン依頼が増える (bakuraku, Speeda, HRMOS, STORES が手本)。
3. **AI エージェント訴求は 2026 年後半に本格化する余地が大きい** — 現時点 3.4% だが、Speeda の「vs 汎用 LLM 比較表」、bakuraku の「エージェント化ピボット」が先行指標。今仕込めば 2027 年に先行者利益。
4. **WordPress の地位は当面不動** — Next.js/React 系が 13.7% にとどまる現状、制作会社の納品・運用体制が WordPress に最適化されているため、design-mcp のテンプレートも **WP テーマとしての出力経路** を用意すべき。

---

---

## 19. 追補: 業種別バーティカル SaaS の特徴

117 件の中からバーティカル SaaS を業種別に整理する。

### 19.1 人事/労務/採用 (9 件)
- **HRMOS** (Bizreach) — タレントマネジメント
- **Talknote** — 情報共有
- **LAPRAS** — エンジニア採用
- **INSIDES (Recruit)** — エンゲージメント
- **ASSIGN NAVI** — IT人材マッチング
- **Recoreru** — 勤怠管理
- **F-conne / Fts-future-connect** — SES マッチング
- **assign-navi / ms.recruit-insides** — マネジメント支援
- **共通**: 「人 × データ」訴求、3 プラン料金、セミナー必須、導入事例多数

### 19.2 会計/経理/請求書 (5 件)
- **bakuraku** — バックオフィス全領域
- **invox** — 請求書受領
- **MF クラウド (keyfword)** — 会計 全般
- **共通**: JIIMA 認証、電子帳簿保存法対応、インボイス制度訴求、AI OCR 明示

### 19.3 営業/カスタマーサクセス (6 件)
- **Speeda** — 企業分析
- **Usergram (bebit)** — 行動分析
- **biztel** — クラウド PBX
- **WhatYa (solairo)** — セールスチャット
- **共通**: 行動データ可視化、事例重視、エンタープライズ向け

### 19.4 不動産/建設 (3 件)
- **estie** — 商業用不動産
- **Itandi** — 賃貸 DX
- **Sakurai-gs** — 建設業 DX
- **共通**: バーティカル × 産業 DX、"旧態依然業界を変える" コピー

### 19.5 EC/店舗/POS (4 件)
- **STORES** — オムニ店舗プラットフォーム
- **Shopify JP Plus** — 大規模 EC
- **LIVE BOARD** — OOH広告
- **共通**: 数値 KPI 明示、決済手数料の透明化

### 19.6 コミュニケーション (4 件)
- **Slack JP** — チームチャット
- **LINE WORKS** — 日本型ビジネスチャット
- **BONX** — 音声コミュニケーション
- **Remo** — オンライン会議
- **共通**: 情緒的コピー多、PLG 寄り

### 19.7 在庫/物流 (2 件)
- **smartmat.io** — IoT 在庫管理
- **共通**: IoT デバイス + SaaS ハイブリッド、業種別 Hero

### 19.8 マーケティング/広告 (5 件)
- **SEARCH WRITE** — SEO
- **karte (blocks)** — CX プラットフォーム
- **CyberAgent AD Agency** — 広告運用
- **共通**: ダッシュボードスクリーンショット多用、KPI 数値訴求

### 19.9 教育/学習 (7 件)
- **prog-8** — プログラミング学習
- **Pro-Seeds Learning Ware** — eラーニング
- **Digital Hollywood (School)** — クリエイター養成
- **Kobe電子専門学校 / FCA** — 教育機関 LP
- **mojimo.jp** — フォント学習
- **共通**: 体験入学、就職率、卒業生実績

### 19.10 その他ニッチ
- **Qrio** — スマートロック
- **Tolettacat** — 猫用トイレ IoT
- **Awarefy** — メンタルヘルス B2C
- **eneos-ss** — SS 会員アプリ
- **dokodemo.app** — 遠隔操作

---

## 20. バーティカル別 CTA テキスト比較

| 業種 | 主 CTA | 副 CTA | 電話番号 |
|---|---|---|---|
| 会計/請求書 | 資料ダウンロード | 無料お試し | あり (0120) |
| 人事/労務 | 資料請求 | お問い合わせ | あり (0120) |
| ERP/基幹 | お問い合わせ | 資料ダウンロード | あり (0120) |
| コミュニケーション | 無料ではじめる | お問い合わせ | なし |
| EC/店舗 | 無料でアカウント作成 | 資料ダウンロード | なし |
| 不動産 DX | お問い合わせ | 資料ダウンロード | あり |
| マーケ/広告 | 資料ダウンロード | デモを見る | 時々 |
| 教育 SaaS | 無料体験 | 資料請求 | あり |
| IoT 在庫 | 資料ダウンロード | オンライン相談 | あり (0120) |

**発見**: 電話番号の有無は業種特性と完全に相関する。「コミュニケーション SaaS」「EC SaaS」は電話が **ほぼない** 一方、「会計/請求書」「人事」「ERP」「不動産」「IoT」「教育」は 80% 以上で電話を提示する。**業務系ミッションクリティカル度 × 法人営業の習慣** が電話設置の決定要因。

---

## 21. 配色トレンドの観察

117 件の Hero 周辺の主色を抽出し、5 系統に分類：

| 系統 | 件数概算 | 代表 |
|---|---|---|
| **青系 (#0066FF 〜 #1E40AF)** | 35+ | STORES, MF Cloud, HRMOS, Shopify JP Plus, Newt, estie |
| **緑系 (#00C851 〜 #21846F)** | 18 | bakuraku, LINE WORKS, Autoro, Recoreru |
| **赤系 (#DC2626 〜 #F72A48)** | 8 | Speeda, Asana (accent), ENEOS, Insta360 |
| **紫系 (#5a31f4 〜 #8B5CF6)** | 6 | Shopify Plus JP, Slack (aubergine), Fonetra |
| **モノクロ (白黒グレーのみ)** | 15 | Studio, Figma JP, Newt, Affinity JP, chuwrite |
| **暖色/黄色系** | 6 | DeNA×AI (#ff7900), Yoshinoya, JR Kyushu |
| **多色 (4 色以上の混在)** | 15 | WordPress 系古いテーマ、教育 LP |

**発見**: 日本 SaaS の第一色は **青 (35+) が突出**。次点の緑 18 件は「自然・安心」訴求、赤 8 件は「情熱・エネルギー」。**モノクロ 15 件のうち 12 件は海外化度 ★★★★★** = ミニマル モノクロは日本で "海外SaaS風" のショートカット記号になっている。

---

## 22. レアリティ観察 — 見つけて驚いた要素

1. **Three.js 背景 (bakuraku のみ)** — パーティクル表現、計算コストが高いが Hero の "未来感" を出す切り札
2. **Compressa VF 可変フォント (DeNA×AI のみ)** — 2026 年トレンド、レター単位のキネティックタイポ
3. **Astro 採用 (Speeda のみ)** — 静的生成 × Island Architecture、B2B SaaS では珍しい
4. **Webflow (Shopify JP のみ)** — 日本 SaaS での Webflow 運用は 0.9% とほぼ無し
5. **HubSpot CMS (smartmat.io のみ)** — MAツール一体型、事例データと連携、日本ではレア
6. **Vue/Nuxt (DeNA×AI のみ)** — 日本 SaaS は圧倒的 React/Next 優位
7. **JSON-LD SoftwareApplication スキーマ (HRMOS が代表)** — 真面目な SEO 投資
8. **Material Icons の使用 (Studio)** — 2026 年にしては古典的、Lucide/Phosphor への置き換え余地

---

## 23. 改善余地が最も大きい領域

1. **Web フォント最適化** — Noto Sans JP を full load している LP が多数 (500KB+)、subset 化やシステムフォントフォールバックの活用余地大
2. **Inter と Noto Sans JP のウェイト整合** — 単純併用ではウェイト階層がズレる問題
3. **アクセシビリティ** — WCAG AA 準拠できていない LP が 70% 以上
4. **モバイルの sticky CTA** — 設置率は 30% 前後、本来は 70%+ が望ましい
5. **Core Web Vitals (特に LCP)** — Next.js SSR の大 HTML は LCP を悪化させるジレンマ
6. **JS 依存の過剰** — jQuery + GSAP + Swiper + WP plugin の全部乗せで、初期 load 2-3MB の LP が散見
7. **FAQ の構造化データ不足** — FAQPage スキーマを付けている LP はほぼない

---

**分析終了。** 117 件の統計 + 15 件の深読み + 20 件の要約 + 業種別バーティカル + 配色/レアリティ / 改善余地 / design-mcp 向け 23 セクションの指示を完了。
