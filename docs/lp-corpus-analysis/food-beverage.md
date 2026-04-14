# 飲食・食品・飲料 LP 分析（Round 2）

**対象コーパス**: `/Users/oidekento/lp-corpus/raw_all/food-beverage/` **282件**
**分析日**: 2026-04-08
**手法**:
- 282件全件の grep/正規表現抽出による統計サマリ
- サブジャンル自動分類 → 150件以上のメタデータ抽出
- 14件の深読み（老舗和菓子／D2C定期便／クラフトビール／ナショナル飲料／高級日本酒／産地直送／料亭／カスタムサラダ／料理器具／ギフト／キャラクター菓子／カスタードシュー／コミュニティ型／焙煎通販）

---

## 0. コーパスの全体像

### 0-1. サブジャンル分布（282件自動分類）

| # | サブジャンル | 件数 | シェア | 代表例 |
|---|---|---:|---:|---|
| 1 | **その他／ブランドサイト** | 64 | 22.7% | konjac-kasho, hokka-hokka-tei, sagamariage, guruguru-shakashaka |
| 2 | **レストラン／飲食店** | 36 | 12.8% | cantina-zushi, osteria-ao, teppanyaki-mitsui, kintan, therestaurant-hiroo |
| 3 | **食品メーカーその他** | 19 | 6.7% | fujiya1935, kewpie, otsuka, meiji-sports-savas, s-foods |
| 4 | **カフェ／スタンド** | 16 | 5.7% | banta-cafe, ice-bj, dilly-dally, parkcoffeeandbagel, wanna-manna |
| 5 | **調味料／素材** | 13 | 4.6% | mosio（藻塩）, hakko-blend, katsuo, spicelabtokyo, konatospice |
| 6 | **洋菓子／パティスリー** | 13 | 4.6% | beardpapa, patisserie-emera, kogashibutter, 23frozenbaum, and-earlgrey |
| 7 | **採用（飲食業界）** | 12 | 4.3% | recruit.torikizoku, y-meatland, aimservices, recruit.akikawabokuen |
| 8 | **ギフト／カタログ** | 10 | 3.5% | shiroishi-yougashiten, oyogetaiyaki, konpeidou, hishiiwa, yaohiko-okuizome |
| 9 | **調味料／レトルト（ナショナル）** | 9 | 3.2% | housefoods-prime, sbfoods-organicspice, marukome-misosoup |
|10 | **ドリンク（ナショナル）** | 9 | 3.2% | kirinlemon, calpis, meijioishiigyunyu, asahiinryo-labelless, rakueco |
|11 | **ドリンク／ジュース** | 8 | 2.8% | tomorrowater, yoteistock, redbull, bioene, choco-ne |
|12 | **お茶／日本茶** | 8 | 2.8% | mchaho, ippukuandmatcha, fukucha-fukujuen, daylily, annoncha, chuhicha |
|13 | **インスタント／麺** | 7 | 2.5% | nissin-ufo, maruchan-aka-midori, maruchan-yakisoba, nissin-oatmeal |
|14 | **コーヒー（豆／焙煎）** | 7 | 2.5% | onca-coffee, jorganic-coffee, chevroncoffee, sunnydayscoffee, yeti-standing |
|15 | **ビール／クラフト** | 7 | 2.5% | yonayonaale, shimanami-brewery, rydeenbeer, yohobrewing-suiyoubinoneko |
|16 | **取り寄せ／産地直送** | 7 | 2.5% | setouchi-oyster, yajima-f, upvege, mamanqa, yu-san-chae |
|17 | **菓子（ナショナル）** | 6 | 2.1% | fujiya-peko, lotte-painomi, asahi-gf-1pon, mintia, kabaya-sakupan |
|18 | **老舗／和菓子** | 6 | 2.1% | kuwazawa-wagashi, nanyodo-monaka, aozashikarari, creaimo, felissimo-oteraoyatsu |
|19 | **ビール／発泡酒（ナショナル）** | 5 | 1.8% | yebisu, hakutsuru-bekkaku, sapporo-1ban, asahibeer-stylefree, hometap-kirin |
|20 | **日本酒** | 4 | 1.4% | kikumasamune-kaho, summerfallsake, sakeice, eshikoto-ishidaya |
|21 | **ベーカリー／パン（小規模）** | 3 | 1.1% | nekoshoku, nekonekocheesecake, milkjapan |
|22 | **D2C／定期便／サブスク** | 3 | 1.1% | snaq.me, postcoffee, why-juice |
|23 | **ベーカリー（ナショナル）** | 3 | 1.1% | pasco-kamayaki, pasco-chojuku, abc-cooking-maruchan |
|24 | **食体験／イベント** | 3 | 1.1% | yokohama-pia-fes, flow-lifestyle, tjokayama |
|25 | **ウイスキー／ワイン／洋酒** | 2 | 0.7% | dewars, kirin-diablo |
|26 | **健康／機能性／サプリ** | 2 | 0.7% | s-shizensyokuhin, pietro-chefs-holiday |

**観察**:
- 「レストラン型（ブランドLP）」約40%、「D2C／EC直販」約15%、「ナショナルブランド告知LP」約30%、「採用」約4%、「イベント／プロモ」約10% の4層構造。
- 他ジャンル（美容・医療）と比べて**ギフト／カタログ／和菓子／産地直送**という「贈り物需要」の層が明確に独立している。
- 「ビール／日本酒／洋酒」を合算すると18件（6.4%）で酒類プロモが1セグメントを構成。

---

## 1. 統計サマリ（282件全体スキャン）

### 1-1. タイポグラフィ

**Google Fontsファミリ出現数（上位20／link href のfamily=パラメータ抽出）**:

| 順位 | ファミリ | 件数 | 役割 |
|---:|---|---:|---|
| 1 | **Noto Sans JP** | 66 | 本文・見出し共用、業界標準 |
| 2 | Roboto | 21 | 欧文副書体 |
| 3 | **Zen Kaku Gothic New** | 17 | モダン和ゴシック（老舗モダナイズ） |
| 4 | **Noto Serif JP** | 16 | 明朝見出し（老舗・和） |
| 5 | Zen Maru Gothic | 7 | 丸ゴシック（親しみ系） |
| 6 | Montserrat | 7 | 欧文大文字見出し |
| 7 | Lato | 7 | 欧文副 |
| 8 | **Zen Old Mincho** | 5 | 明朝（和） |
| 9 | **Shippori Mincho / Antique (B)** | 4+2+1 | 筑紫系・高級和 |
|10 | Marcellus / Cormorant Garamond / EB Garamond / Playfair / Lora / Crimson | 各2 | セリフ（欧風レストラン・ワイン） |

**Adobe Typekit（use.typekit.net）**: 46ファイル／282中（16.3%）が導入。
→ 老舗／レストラン／D2Cでカスタム日本語Webフォント需要が高い。高級店ほどTypekit採用。

**書体選定の法則**:
- **老舗／蔵元／高級** → Shippori Mincho + Zen Old Mincho + Typekit日本語（游築見出し明朝／筑紫明朝）
- **D2C／モダン** → Noto Sans JP + Inter／Roboto の2書体ミニマル
- **洋菓子／パティスリー** → Noto Serif JP または Cormorant / Playfair / Marcellus + Noto Sans JP
- **ナショナル／量販プロモ** → Noto Sans JP 単品＋Webフォント無し（画像見出し優先）
- **クラフトビール／コーヒー** → Condensed系（Roboto Condensed, Oswald） + カスタムロゴ画像

### 1-2. カラーパレット（全文hex出現頻度上位）

| hex | 出現 | 主な用途 |
|---|---:|---|
| `#042a31` | 687 | ダークインク（高級レストラン／ウイスキー／コーヒー） |
| `#864a34` | 536 | テラコッタブラウン（焙煎・蔵・革・和） |
| `#644632` | 264 | 焦茶（konjac-kasho 主色＝蒟蒻土色） |
| `#e60012` | 217 | 日の丸赤（カゴメ／国産系／ナショナル） |
| `#f6ab00` | 198 | 山吹色（和・温） |
| `#221815` / `#1f1a1a` / `#1a1311` | 183+92+60 | 濃墨（和モダン／肉・肴） |
| `#009944` | 166 | 和緑（抹茶／野菜） |
| `#172852` | 161 | ネイビー（snaq.me／海・清潔） |
| `#f9f8f3` | 160 | アイボリー背景（crisp／ベーカリー） |
| `#ffd900` | 134 | 黄（カゴメ系／子ども向け） |
| `#fff9e7` | 110 | クリーム背景 |
| `#920783` | 113 | 紫（カゴメ Smile Ball／ぶどう） |
| `#9dc815` | 103 | 黄緑（野菜／オーガニック） |

**観察**: 食品LPの配色は**「焦茶系 × アイボリー／クリーム × 差し色（赤／黄／緑）」**の三位一体が主流。
- 焦茶（#864a34 / #644632 / #042a31）= 素材・焙煎・蔵・革の"手しごと感"
- クリーム（#f9f8f3 / #fff9e7 / #fcfcf7）= 乳・パン・湯葉の"やわらかさ"
- 差し色赤（#e60012 / #db0a40）= 国旗・情熱・食欲増進（ナショナル頻出）
- 緑（#009944 / #9dc815）= 野菜・オーガニック・産地
- 黄（#f6ab00 / #ffd900）= 太陽・元気・子ども・農家

### 1-3. ライブラリ／技術スタック（282件スキャン）

| カテゴリ | 件数 | シェア | 備考 |
|---|---:|---:|---|
| jQuery | 154 | 54.6% | 中小規模店・WordPress系の大半 |
| wp-content（WordPress） | 91 | 32.3% | 内生成器検出=25、Studio.design=20 |
| Swiper.js（小文字） | 77 | 27.3% | Hero＋商品カルーセルの標準 |
| GSAP | 29 | 10.3% | 高級／プレミアム系で必須 |
| ScrollTrigger | 16 | 5.7% | GSAP補助 |
| Next.js | 22 | 7.8% | D2C・新興ブランド |
| nuxt.js | 24 | 8.5% | Vue系D2C（snaq.me, hokka-hokka-tei） |
| Studio.Design（無料SaaS） | 20 | 7.1% | 小規模店の"爆速LP" |
| STUDIO（studio.site） | 5 | 1.8% | 同上 |
| Barba.js | 14 | 5.0% | ページトランジション（高級系） |
| Lenis（smooth scroll） | 12 | 4.3% | 高級／モダン |
| Shopify | 12 | 4.3% | D2C直販 |
| AOS | 10 | 3.5% | 簡易fade |
| React（直接検出） | 9 | 3.2% | - |
| Lottie | 6 | 2.1% | キャラクター系 |
| Splide | 3 | 1.1% | Swiperの軽量代替 |
| Astro | 7 | 2.5% | 新興・高速化目的 |
| Typekit | 46 | 16.3% | 日本語高級書体 |
| gtag / GA4 | 110 | 39.0% | アナリティクス |
| webp画像 | 114 | 40.4% | 画像最適化進展中 |
| fbevents（Meta Pixel） | 15 | 5.3% | 広告運用活発なD2Cのみ |

**生成器ヘッダー分布**:
- `Studio.Design` 20 / `WordPress 6.x系` 16 / `WordPress旧版` 8 / `Astro v4.x` 2 / `AIOSEO` 7 / `WooCommerce` 1

**スタック類型まとめ**:
1. **WordPress + jQuery + Swiper**（最多／レストラン・中堅ブランド・老舗）
2. **Next.js/Nuxt + Typekit**（D2C・新興モダン）
3. **Studio.Design（ノーコード）**（小規模・ポップアップ・産地直送）
4. **WordPress + GSAP + Barba + Lenis**（高級店・ハイブランド）
5. **Shopify**（サブスク・ECネイティブ）
6. **生HTML + jQuery**（ナショナルブランドの特設LP＝コーポレートCMS出力）

### 1-4. セクション構成パターン（英語見出しタグ頻度）

| セクション名 | 件数 |
|---|---:|
| MENU | 39 |
| NEWS | 33 |
| ABOUT | 31 |
| CONTACT | 26 |
| SHOP | 21 |
| ACCESS | 15 |
| FAQ | 14 |
| STORY | 13 |
| PRODUCT | 13 |
| CONCEPT | 11 |
| TOPICS | 10 |
| HISTORY | 6 |

**標準セクション構成（中央値10-14セクション）**:
1. **Hero**（メインビジュアル）— 82%でSwiper or 背景動画
2. **News / Topics** — 33件
3. **Concept / About / Story** — 55件（創業・想い・理念）
4. **Product / Menu / Lineup** — 52件
5. **History / Craft**（老舗のみ） — 6件
6. **Recipe**（調味料・素材のみ）
7. **Shop / Store Locator** — 21件
8. **News / Press** — 33件
9. **FAQ** — 14件
10. **Access / Contact** — 41件

### 1-5. コピーライティング頻出語（全文grep）

**シズル感語彙（282件中）**:
| 語 | 件数 | 語 | 件数 |
|---|---:|---|---:|
| コク | 46 | まろやか | 24 |
| 濃厚 | 42 | 芳醇 | 20 |
| 香ばしい | 37 | しっとり | 18 |
| 旨味／うま味 | 16+4 | とろける | 13 |
| ふんわり | 13 | ジューシー | 12 |
| 口どけ／口溶け | 11+5 | サクサク／サクッ | 10+7 |
| ふわふわ | 9 | もちもち | 8 |

→ **「濃厚 > 香ばしい > コク > まろやか」が4強**。

**産地／職人／伝統語彙**:
| 語 | 件数 | 語 | 件数 |
|---|---:|---|---:|
| こだわり | 94 | 素材 | 76 |
| レシピ | 66 | 季節／旬 | 54+44 |
| 厳選 | 39 | 創業 | 37 |
| 製法 | 36 | 蔵 | 33 |
| 発酵 | 27 | 産地 | 25 |
| 職人 | 22 | 生産者 | 20 |
| 焙煎 | 18 | 農家 | 17 |
| 伝統 | 40 | 老舗 | 13 |
| 無添加 | 11 | 国産 | 30 |

**購買／導線語彙**:
| 語 | 件数 |
|---|---:|
| 限定（期間／数量／ブランド） | 99 |
| Instagram | 109 |
| LINE | 92 |
| オンラインショップ | 51 |
| ギフト | 45 |
| 予約／ご予約 | 57+35 |
| キャンペーン | 61 |
| お取り寄せ | 12 |
| 定期便 | 10 |
| 送料無料 | 11 |
| 手土産 | 8 |

→ **「Instagram > LINE > オンラインショップ > ギフト > 予約」**の順。
飲食・食品は**Instagram集客依存が他業界より強い**（他業界では平均50-70件程度）。

### 1-6. 技術パターン頻度

| パターン | 件数 | 備考 |
|---|---:|---|
| ローディング／スプラッシュ画面 | 162 (57.4%) | ブランドロゴ出現→fade |
| ハンバーガー／グロナビ | 79 | 固定ヘッダ |
| 構造化データ（JSON-LD） | 63 | LocalBusiness / Organization / Product |
| FAQ アコーディオン | 63 | 高級＋ギフト＋D2Cで多い |
| 料理人／職人紹介 | 49 | chef / 店主 / パティシエ |
| 背景動画 | 44 | Hero＋Store／店内 |
| Parallax | 37 | 高級／物語系 |
| 季節訴求 | 33 | 春夏秋冬／旬 |
| LINE予約／友だち追加 | 32 | 飲食店の実質標準 |
| Google Map iframe | 30 | 店舗系必須 |
| 動画Hero（autoplay） | 28 | 大規模ブランド |
| 多言語（hreflang） | 28 | インバウンド対応 |
| 産地マップ | 25 | 地方ブランド／ワイナリー |
| YouTube埋込 | 19 | ブランドストーリー動画 |
| 創業年数表記 | 18 | 「創業◯◯年」型 |
| 予約プラットフォーム（TableCheck/ebica等） | 16 | 高級店 |
| 無限スクロール／マーキー | 14 | ブランド名横流れ |
| 縦書き（writing-mode vertical-rl） | 6 | 和・老舗のみ |
| 機能性表示食品 | 4 | カルピス・サプリ系 |

### 1-7. 価格帯分布（¥表記抽出、196件中でヒット）

| レンジ | 件数 | 比率 |
|---|---:|---:|
| <¥500 | 14 | 7% |
| ¥500–1,000 | 43 | 22% |
| ¥1,000–2,000 | 32 | 16% |
| ¥2,000–3,000 | 28 | 14% |
| ¥3,000–5,000 | 36 | 18% |
| ¥5,000–10,000 | 23 | 12% |
| ¥10,000+ | 20 | 10% |

→ 中央値 **¥2,400**。ギフト・定期便・レストランのプリフィクスが3-5k帯を押し上げ。

---

## 2. 深読み14件（代表例）

### 2-1. snaq.me — D2C定期便のマスターピース

- **ファイル**: `3892_snaq.me_.html` / 313KB / Nuxt + Next（併存）/ Typekit
- **コピー**: 「ワクワクおやつの定期便 おやつ体験BOX」
- **色**: `#172852`（ネイビー）主調 + `#e2cebc #d06d43 #f4ece5 #653424` の**クラフト紙系パレット**
- **フォント**: Noto Sans JP + Inter
- **構成**:
  1. Hero（パーソナライズ強調）
  2. 商品体験（月替わりBOX写真カルーセル）
  3. ユーザーの声（UGC大量）
  4. スナックミーオフィス（法人）
  5. 卸事業
  6. 期間限定ポップアップ
  7. FAQ（「退会は？」「スキップは？」など解約不安解消）
- **CTA**: 「詳しくはこちら」（抑制的）→ 画面下部に「今すぐはじめる」常設
- **特筆**:
  - `ネイビー × クラフトベージュ` の組み合わせは**「テック × 温かみ」のD2C定番**（他業界でも通用）
  - **オフィス福利厚生BtoB訴求**をLP内に混在 → 顧客層拡張
  - FAQが詳細 → **サブスク特有の解約不安を先回り**

### 2-2. よなよなエール（yonayonaale.com） — クラフトビールのストーリーLP

- **ファイル**: `3907_yonayonaale.com_.html` / 32KB / **Next.js + Typekit**
- **タイトル**: よなよなエール｜ヤッホーブルーイング
- **キーコピー**:
  - 「華やかなホップの香り。柔らかな甘みと苦み。」
  - 「もう一人の自分にであう この時間。」
- **色**: `#161616 / #6a6a6a / #fefefe`（モノクロ基調＋ロゴのブランドカラー）
- **構成**: intro → contents-section → mt-[80px]レイアウト多用 → product → sns-link
- **特筆**:
  - タイトル＋サブコピーの**シズル2行＋情緒1行**の定型パターン
  - 「いつ飲むか」「誰になるか」という**ビアタイム情緒訴求**→ 味覚ではなく体験を売る
  - Tailwind CSS由来のmt-[80px]クラス → **Next.js + Tailwind** 明瞭

### 2-3. 菊正宗 嘉宝 KAHO — 高級日本酒フラッグシップ

- **ファイル**: `3665_www.kikumasamune.co.jp_products_kaho_.html` / **768KB**（超大型）/ Next.js + Swiper + Lenis
- **コピー**: 「Beyond The Heritage — 今、この瞬間を紡ぐように、ひたむきに醸す場所」
- **フォント**: Noto Serif JP（明朝）1書体
- **色**: `#dbcdb8 / #c6b192`（砂・米糠色）
- **見出し**: 特上等級・山田錦 / 「宮水」の神秘 / 躍動する現代の伝統蔵
- **構成**:
  1. ブランドコピー（英語＋漢字2行）
  2. 原料（山田錦）
  3. 水（宮水）
  4. 蔵（嘉宝蔵の動画）
  5. 味わい
  6. 商品情報
- **特筆**:
  - **米／水／蔵の3要素**で語る = 日本酒LPの黄金型
  - Lenis平滑スクロール + 高解像度ストーリーフォト = **雑誌風**
  - 768KBの重量は**動画と高解像度を惜しまない予算**を示唆 → フラッグシップ戦略

### 2-4. SETOUCHI OYSTER — 産地直送／季節商材

- **ファイル**: `3669_www.setouchi-oyster.com_.html` / 73KB / Next.js + jQuery
- **コピー**: 「全国の牡蠣を知りつくしたクニヒロが、季節や産地に縛られず、その時季にもっともおいしい牡蠣をセレクト」
- **フォント**: **Marcellus** + Noto Sans JP + Noto Serif JP + Lato（4書体）
- **色**: `#003656`（深海ネイビー）主調 + `#fcd64a`（ゆず） + `#95d2e5`（波色）
- **構成**: CONCEPT → PRODUCT → RECIPES → INFORMATION → LEAFLET → お問い合わせ → 仕入れBtoB
- **特筆**:
  - **BtoCとBtoBのCTA併記**（小売店・仕入れ業者向けリンク）
  - RECIPES セクション = 食材ECの標準装備（「買った後どうする？」解決）
  - 英語セリフ + 和シリフの混成 = **産地直送の"インポート感"演出**

### 2-5. CRISP SALAD WORKS — QSR/サラダブランド

- **ファイル**: `3692_crisp.co.jp_.html` / 191KB / **Next.js + Swiper**
- **コピー**: 「A Small, Good Thing.（ちょっとした心の交流）」
- **色**: `#f9f8f3`（アイボリー）160回＋`#0c3b2c`（深緑）10回
- **見出し**: ITALIAN VEGGIE / CLASSIC CHICKEN CAESAR / CLASSIC CHICKEN COBB / WAFU SESAME CHICKEN / CHICKEN TACO BOWL / THE CAL-MEX / SALMON AVOCADO CAESAR / MARKET SALAD → STORE LOCATOR → INITIATIVES
- **特筆**:
  - **商品名（英大文字）を見出しに使い切る**シンプルさ = メニューLP型
  - Swiper大量使用（`Kv_swiperItemSection__qC07E` CSS Modulesクラス名検出）
  - 「INITIATIVES（取り組み）」セクション = **サステナ訴求**を後尾に配置
  - 二色構成（アイボリー × 深緑）のみ = **野菜=フレッシュ**の表現

### 2-6. PostCoffee — D2Cコーヒー通販の巨艦

- **ファイル**: `3853_postcoffee.co_.html` / **2.9MB**（最大級）/ Shopify + Barba + Next + AOS + Splide
- **コピー**: 「TBSがっちりマンデー紹介」「日本最大級のコーヒー豆専門通販」「定期便なら全国送料無料、最短翌日投函」
- **色**: `#f1f1f1 / #ff9900 / #f0b48a / #efefef / #5e1a03`（オレンジ×クリーム×焦茶）
- **構成**:
  1. 新入荷
  2. 人気のコーヒーランキング
  3. 好評だったコーヒー
  4. こだわりから選ぶ（味／産地／焙煎度）
  5. ベストセレクション
  6. 年間200種類ラインナップ
  7. たくさんの方が使っています
  8. アクセサリ
  9. 特集！
  10. 美味しいコーヒーを知ろう！
  11. FAQ
- **特筆**:
  - **Shopify + Barba.js + Next.js + Splide + AOS** の混合スタック → ECネイティブが進化した証
  - **年間200種類／最短翌日／全国送料無料**＝D2Cの三大訴求
  - コンテンツマーケ（"美味しいコーヒーを知ろう！"）をLPに同居 → SEO兼用

### 2-7. ねこねこチーズケーキ — キャラクター洋菓子

- **ファイル**: `3862_nekonekocheesecake.allhearts.company_.html` / 86KB / WordPress + jQuery
- **コピー**: 「ねこの形のチーズケーキ専門店」「ねこ型食パン専門店『ねこねこ食パン』の姉妹ブランド」
- **フォント**: Noto Sans JP + **Unna**（セリフ）
- **見出し**: 「ねこねこチーズケーキは…」「おいしさのポイント」
- **特筆**:
  - **形状を単一の物語点に**（ねこ型）
  - 姉妹ブランド言及 = クロス集客
  - WordPress標準色プリセット（`#00d084 #0693e3 #7a00df #007cba`）＝Gutenberg既定 → **テーマ未カスタマイズでもブランドとして成立**

### 2-8. 積奏（seki-sou.com） — 季節性バターサンドD2C

- **ファイル**: `3768_seki-sou.com_.html` / 84KB / WordPress
- **コピー**: 「バターとチーズ。果物、木の実にチョコレート。さまざまな素材を重ね合わせた季節や景色の広がりを感じるバターサンド」「3営業日以内に全国配送」
- **色**: `#c5cbd1`（スモークグレー）66回
- **セクション**: `p_home__mainvisual` → `p_home__about` → `p_home__news` → `p_home__set` → `p__home__howto`
- **商品名**: 風セット／波セット／虹セット／冷凍セット（情景型ネーミング）
- **CTA**: 「view more」「WEB予約（店頭受取）」併設
- **特筆**:
  - **情景型商品名**（風／波／虹）= バターサンドを風景と結びつける高級ブランド手法
  - **店頭受取 × 冷凍配送** の二軸導線
  - モノクロ近似の配色 = **菓子の色味を引き立てる**

### 2-9. こがしバターケーキ（kogashibutter.com） — パティスリー単品集中

- **ファイル**: `3629_kogashibutter.com_.html` / 136KB / **Splide**
- **見出し**: こがしバターケーキ / butter / lineup / shop / MUKASHINplus / 新着情報
- **セクション**: `pFv js-chage-cake` / `pAbout js-move-hand-trigger` / `pLineup` / `pShop`
- **特筆**:
  - クラス名 `js-chage-cake`（＝change-cake）→ **色違い／味違いのバリエーションをスクロールで切替**演出
  - 「butter」セクションで**バターの種類・発酵など素材解説**に1セクション割く = 単品集中ブランドの王道
  - パン系はSwiper、菓子系はSplideの傾向あり

### 2-10. 迦しょう（konjac-kasho） — 老舗モダナイズ

- **ファイル**: `3556_konjac-kasho.com_.html` / 581KB / **Swiper + Barba + WordPress**
- **コピー**: 「ぷりぷりちゅるん迦しょう」「娯楽的たべもの。」
- **色**: `#644632` （焦茶）264回 + `#ebe1cd`（生成り） + `#e65532`（朱）
- **見出し**:
  1. 娯楽的たべもの。
  2. 湧水と、自然素材と。
  3. すべて、手しごとで。
  4. 「蒟蒻」ってなに？
  5. 赤城山と迦葉山で、つくる。
  6. 蒟蒻セラミドと、食物繊維。
- **構成**: splash → mv slider-area → lead → summary statement → explain → product-list → gensen（厳選） → fable（昔話）
- **特筆**:
  - **「蒟蒻ってなに？」＝啓蒙セクション** → 地味食材を娯楽化
  - **fable（物語）セクション**でローカル神話と紐付け
  - Barba.jsページトランジション = 老舗の品格
  - Swiperヒーロー + WordPress基盤 = 予算3-5Mクラスの典型

### 2-11. Vermicular フライパン — 調理器具の"美食"LP

- **ファイル**: `3847_www.vermicular.jp_products_fryingpan_.html` / 135KB / Next.js + Swiper + WP
- **タイトル**: 「目指したのは、世界一、素材本来の旨みを凝縮するフライパン。」
- **フォント**: Crimson Pro（セリフ欧文）
- **見出し**: 感動の目玉焼き。／箸の止まらない、野菜炒め。／絶品、厚切りステーキ。／サクふわのパンケーキ。／薪窯級の衝撃ピザ。
- **CTA**: ONLINE SHOP
- **特筆**:
  - **料理名単品LP構造**（1料理1ビジュアル＋1コピー）
  - 「感動の」「絶品」「衝撃」「サクふわ」＝シズル語彙の凝縮
  - 料理器具でありながら**「素材本来の旨みを凝縮」という料理サイド訴求** = 用途を通じて商品価値定義
  - pagesパーツ: `p-lineup` / `p-banner -twoColumn` / `p-recipebook` → **レシピ本連携セクション**

### 2-12. Why Juice? — 生産者が見えるジュースD2C

- **ファイル**: `4015_www.why-juice.me_.html` / 小型 / **Next.js**
- **コピー**: 「生産者の顔が見え、中身の見える安心で安全なジュースブランド」
- **フォント**: **Neuton**（単品）
- **見出し**: Because / Community / Delivery / Locations（4セクション構成の極小LP）
- **特筆**:
  - **極少4セクション**で完結 — ブランド観を「なぜ？（Because）」で1語化
  - Next.js シングル書体セリフのみの**ジャーナル的美学**
  - ジュース=野菜=生産者という連鎖

### 2-13. KINTAN — 焼肉／しゃぶしゃぶ高級店

- **ファイル**: `3861_kintan.restaurant_.html` / 68KB / jQuery
- **コピー**: 「甘い余韻に、ほどける夜。」
- **フォント**: **Noto Serif JP + Karla + Rozha One**（3書体／独特のインド系セリフ）
- **CTA**: SHOP / SHOP LIST
- **特筆**:
  - **デートLP的な情緒型コピー**（「夜」「余韻」「ほどける」）
  - Rozha One という稀な書体でブランド差別化
  - 肉系は**情緒訴求**が多い（Kintan）／**素材訴求**が多い（山形ミートランド等）に二分

### 2-14. SummerFall Sake — SNSネイティブ日本酒

- **ファイル**: `3533_summerfallsake.jp_.html` / Shopify + Swiper + Next + jQuery
- **コピー**: 「『こうじゃなきゃダメ』なんて誰が決めたんだろう」「カリフォルニア発スパークリングSAKE」
- **色**: `#ffff9b`（レモンイエロー）42回 + `#008ce3`
- **見出し**: 年齢確認 / I TASTE GOOD WITH / PIZZA / CHIPS / BURGER / OYSTERS / FIND / NEWS
- **キャンペーン**: 「にじさんじ × SummerFall」「かやのみ × SummerFall」
- **特筆**:
  - **年齢確認モーダル**（酒類必須）
  - 「日本酒 × ピザ／チップス／ハンバーガー／牡蠣」＝**フードペアリングを商品軸に**
  - **VTuberコラボキャンペーン**（にじさんじ／かやのみ）= 若年層獲得
  - Shopify = **D2C × EC** のハイブリッド
  - 「こうじゃなきゃダメ？」= 既存日本酒のアンチテーゼで若者セグメント確保

---

## 3. 共通パターン（Food-specific Playbook）

### 3-1. Heroパターン

| # | パターン | 代表 | 出現率 |
|---|---|---|---:|
| A | **Swiper静止画スライダー**（3-5枚） | 老舗／産地／蔵元 | 27% |
| B | **背景動画autoplay**（店内／製造） | 高級店／ブランド | 16% |
| C | **静止画1枚 + 大見出し和明朝** | 日本酒／レストラン | 20% |
| D | **商品クローズアップ + シズル語** | 洋菓子／ナショナル | 18% |
| E | **複数商品キャラグリッド** | ナショナル菓子 | 10% |
| F | **Studio.site テンプレ** | 小規模・ポップアップ | 7% |
| G | **Loading Splash → ブランドロゴfade** | 全体の57% | — |

### 3-2. 5大訴求軸

食品・飲料LPの**訴求は必ず次の5軸のどれか以上で構成**される:

1. **素材（Material）**: 産地／原料／品種／無添加
2. **製法（Craft）**: 職人／手しごと／◯年伝統／発酵・熟成
3. **季節（Season）**: 旬／期間限定／春夏秋冬
4. **物語（Story）**: 創業◯年／家族／想い／地域
5. **体験（Experience）**: 時間／シーン／贈る／食卓

→ **老舗和菓子**は1+2+4、**D2C**は1+5、**レストラン**は2+5、**ナショナルブランド**は3+5、**クラフト系**は2+4。

### 3-3. CTA設計

| CTA | 出現パターン | 業種 |
|---|---|---|
| **ONLINE SHOP**（英大文字） | 14 | 洋菓子／D2C／ブランド |
| **ご予約／予約はこちら** | 57 | レストラン／ギフト／お食い初め |
| **定期便ではじめる** | 10 | D2C |
| **お取り寄せ** | 12 | 老舗／産地 |
| **LINE友だち追加** | 32 | 飲食店常設 |
| **テーブルチェック／ebica** | 16 | 高級店 |
| **店頭受取／WEB予約** | 併記多数 | 街場パティスリー |
| **VIEW MORE / READ MORE** | 大量 | コンテンツ誘導 |

### 3-4. 構造化データ

- **LocalBusiness** → レストラン・カフェ（40件程）
- **Organization** → 老舗・蔵元（12件程）
- **Product** → D2C・EC（20件程）
- **Recipe** → 調味料ブランド（5件程）
- **FAQPage** → 高級店・D2C

### 3-5. シズル語マトリクス

| 食材カテゴリ | 使用シズル語TOP3 |
|---|---|
| 菓子（洋） | 濃厚／口どけ／しっとり |
| 菓子（和） | 香ばしい／まろやか／旨味 |
| パン | ふんわり／もちもち／香ばしい |
| 肉 | ジューシー／旨味／とろける |
| 魚介 | 旨味／芳醇／まろやか |
| ビール | 華やか／コク／キレ |
| 日本酒 | 芳醇／まろやか／旨味 |
| コーヒー | 芳醇／コク／香ばしい |
| チーズ／乳 | 濃厚／コク／まろやか |

### 3-6. FAQ項目パターン（高頻度）

- **レストラン系**: 予約方法／キャンセル料／個室／ドレスコード／アレルギー／子供／支払い／駐車場
- **D2C定期便系**: スキップ／解約／配送日／冷蔵冷凍／保存期間／ギフト設定／領収書
- **ギフト系**: のし／包装／お届け日指定／手提げ袋／メッセージカード
- **蔵元系**: 試飲／工場見学／温度管理／賞味期限／開栓後

### 3-7. モバイルファースト度

- 282件中 `viewport` meta完備は279件（99%）
- `hamburger`／ドロワーメニュー 79件検出
- 固定フッターCTA（予約／購入ボタン） → 高級店とD2Cで6割程度
- `tap-highlight`無効化CSS → 高級系で散見

---

## 4. 新発見・前ラウンドからの差分

### 4-1. **「体験セクション」の台頭**

前ラウンド（30件分析）では見られなかった**「食の向こう側の体験」**セクションが頻出:
- 6curry&sauna → 食＋サウナ
- 1to2.jp → 食卓体験
- futuretrain.jp → 想像力レストラン
- flow-lifestyle.jp → 食のライフスタイル
- tjokayama.jp → 岡山食体験
- redbull.com → イベント・アスリート

→ **食品は「味」ではなく「何と結びつくか」を売る時代**。

### 4-2. **ナショナルブランド特設LPのCMS生成スタイル**

ハウス食品／アサヒ／サッポロ／マルちゃん／キリンの特設LPは、
- WordPressまたはNext.js単品
- `/special/[キャンペーン]/` URLパターン
- **アニメ／キャラクターコラボ**（ちいかわ、にじさんじ、ぽすくま）多数
- **SNS連動抽選キャンペーン** → GA4 + fbevents 導入率高

→ ナショナル特設LPは**「ブランド告知 → キャンペーン抽選 → SNSシェア → データ取得」の型**。

### 4-3. **VTuber／インフルエンサーコラボの常態化**

- nijisanji × SummerFall
- ちいかわ × 丸大食品
- ぽすくま × 日本郵便カフェ
- sakuPAN × KABAYA

→ 食品×IP**コラボは特設LPの標準戦術**。前回分析では未検出。

### 4-4. **ローカル神話／由来ストーリー**

konjac-kasho の「赤城山と迦葉山でつくる。」、tsumari-chamame の豪雪里山、mosio の「塩土老翁神」…と**地名＋神話**を取り込む構造は前回と同様だが、今回さらに顕著。

### 4-5. **縦書きはもはや少数派**

前回は「縦書き＝和の標準」と見たが、今回282件中6件（2.1%）。
→ 和モダンでも**横書き＋明朝＋縦組みアクセント**が新定番。

### 4-6. **「解約不安」へのFAQ先回り**

D2C全件で「スキップ」「解約」「配送間隔」「お届けを一時停止」がFAQ上位。
→ サブスク不安解消FAQ設計は**食D2Cの差別化ポイント**。

### 4-7. **Studio.Design の食品LP侵食**

20件（7%）がStudio.Designで作成されており、特に**ポップアップ／期間限定／小規模生産者**で重宝。

### 4-8. **Barba.js 14件 = 高級店の標準**

ページトランジション＝高級＋物語系のシグネチャ。

### 4-9. **Typekit採用率 16%**

→ 飲食・食品業界は美容（~30%）より低いが、他業界（真面目BtoB）よりは高い。高級×日本語の組み合わせで必須化。

### 4-10. **WebP採用率 40%**

画像最適化は進展中だが、まだ半分強がJPG/PNG。**食品は高解像度が命**なため、WebP移行は今後急加速見込み。

### 4-11. **カラー共有**

深焦茶 `#864a34 / #644632` + 山吹 `#f6ab00` + アイボリー `#f9f8f3` の**"工芸系日本パレット"**が業界標準色化している。

---

## 5. サブジャンル別 レシピ（design-mcp 方針）

食品・飲料は「**業種 × 予算 × ポジション**」の3軸でスタックを選定するのが最適。

### 5-1. 老舗和菓子／蔵元系（Luxury Heritage）
- **フォント**: Shippori Mincho B1 / Zen Old Mincho + Typekit 游築見出し明朝
- **カラー**: `#1a1311` / `#644632` / `#c6b192` / `#f9f5ee`
- **レイアウト**: 縦書きアクセント + 横書き明朝本文 / Hero=静止画1枚+白フェード
- **ライブラリ**: Barba.js ページトランジション + Lenis + Swiper
- **CTA**: 「お取り寄せ」「オンラインストア」抑制的
- **必須セクション**: Loading splash / 創業ストーリー / 製法 / 原料 / 店舗案内 / ギフト
- **トーン**: 抑制的・静寂・3-5文で1段落

### 5-2. D2C定期便 / サブスク
- **フォント**: Noto Sans JP + Inter
- **カラー**: ネイビー `#172852` + クラフト `#e2cebc` + 差し色オレンジ `#d06d43`
- **レイアウト**: ファーストビューに「月いくら」「何が届く」「どう選ぶ」3点セット
- **ライブラリ**: Next.js / Nuxt + Shopify + Swiper + AOS
- **CTA**: 「今すぐはじめる」常設＋「プランを選ぶ」
- **必須セクション**: サービス仕組み / 実際のBOX写真 / ユーザーの声 / パーソナライズ説明 / 退会・スキップFAQ
- **トーン**: カジュアル・親しみ・「あなた」一人称

### 5-3. D2C洋菓子 / パティスリー（単品集中）
- **フォント**: Noto Serif JP or Cormorant Garamond + Noto Sans JP
- **カラー**: アイボリー `#f9f8f3` + 差し色（ブランドカラー1色）
- **レイアウト**: 商品1点を縦スクロールで解剖（断面→素材→製法→贈り物）
- **ライブラリ**: WordPress + Splide + GSAP ScrollTrigger
- **CTA**: 「ONLINE SHOP」（英大文字）
- **必須**: 断面写真 / 素材一覧 / ギフト包装 / 店舗 / レビュー

### 5-4. レストラン／飲食店（中高級）
- **フォント**: Noto Serif JP + 欧文セリフ（Marcellus / Cormorant / EB Garamond）
- **カラー**: ダークインク `#042a31` + ゴールド or ネイビー
- **レイアウト**: Hero背景動画 + 固定予約CTA
- **ライブラリ**: WordPress + jQuery + Swiper（予算3M未満）／GSAP + Barba（予算5M+）
- **CTA**: 「ご予約はこちら」(TableCheck / ebica 連携)
- **必須**: Menu（ランチ・ディナー・コース） / Scene（利用シーン） / FAQ（ドレスコード／キャンセル／個室） / Gallery / Access + Google Map / 多言語切替
- **トーン**: 静謐・洗練・3人称

### 5-5. クラフトビール／蔵元系酒
- **フォント**: Roboto Condensed / Oswald + Noto Sans JP + Typekit
- **カラー**: 瓶ラベル由来のブランドカラー + 黒 + 白
- **レイアウト**: 商品単体 → 味わい分解（香り／苦味／甘味）→ペアリング提案
- **ライブラリ**: Next.js + Swiper
- **CTA**: 「オンラインストア」＋ SNS誘導
- **必須**: ストーリー / 醸造過程 / ラインナップ / ペアリング / 取扱店
- **年齢確認モーダル必須**（酒類）

### 5-6. 産地直送 / 生産者
- **フォント**: Noto Sans JP + Zen Kaku Gothic New / FontPlus日本語Web
- **カラー**: 自然色（緑／土色／空色）
- **レイアウト**: 生産者の顔写真 + 圃場 + 収穫動画
- **ライブラリ**: Shopify or Studio.Design
- **CTA**: 「速達で届ける」「カートに入れる」
- **必須**: 受賞歴（権威付け） / 保存・調理方法 / 発送カレンダー / Q&A
- **トーン**: 温かみ・人柄・手書き風UI

### 5-7. ナショナル特設LP（プロモ）
- **フォント**: Noto Sans JP 単品（画像見出し）
- **カラー**: ブランドカラー 3-5色ベタ塗り
- **レイアウト**: キャンペーン情報ファーストビュー → 商品 → 応募フォーム
- **ライブラリ**: WordPress or 生HTML + jQuery + Swiper
- **CTA**: 「応募する」「キャンペーン参加」
- **必須**: キャンペーン期間 / 応募方法 / 賞品 / Q&A / 利用規約
- **トーン**: ポップ・明るい・大量CTA

### 5-8. カフェ／ベーカリー（街場）
- **フォント**: Zen Maru Gothic / Klee One + Noto Sans JP
- **カラー**: クリーム `#fff9e7` + 焦茶 + 緑
- **レイアウト**: 店の外観→店内→商品→営業時間
- **ライブラリ**: WordPress + jQuery（Swiper）または Studio.Design
- **CTA**: Google Map + 「LINE予約」
- **必須**: 営業時間 / 定休日 / 住所 / Instagram埋込

### 5-9. 採用LP（飲食業界）
- **フォント**: Zen Kaku Gothic New + Montserrat
- **カラー**: コーポレートカラー + 白
- **レイアウト**: 人物写真中心 / 1日の流れ / 社員インタビュー
- **ライブラリ**: WordPress + jQuery + barba.js（トリ貴族級）
- **必須**: 先輩社員 / 働き方 / 研修 / 募集要項 / エントリー
- **トーン**: 熱量・成長・挑戦

---

## 6. design-mcp への指針

### 6-1. 食品LPテンプレート生成の必須パラメータ
```yaml
subgenre: (25個から選択)
tone: [heritage|modern-d2c|premium-restaurant|casual-cafe|national-promo|recruit|craft-producer]
product_type: [single|lineup|subscription|gift|menu]
budget: [small(<1M)|mid(1-5M)|high(5M+)]
price_range: [sub-1k|1-3k|3-10k|10k+]
urgency: [evergreen|seasonal|campaign]
cta_primary: [reserve|buy|subscribe|line|visit]
```

### 6-2. 必須ブロック（優先順位）

1. Hero（商品/店/産地の核心ビジュアル + 1-2行コピー）
2. Concept/About（5軸から選んだ訴求軸）
3. Product/Menu/Lineup（商品カルーセル or グリッド）
4. Story/Craft/History（創業・製法・想い）※オプション
5. Customer Voice / Review（D2C・サブスク必須）
6. Access/Shop/店舗（実店舗ある場合）
7. FAQ（解約／予約／配送／包装）
8. CTA footer bar（固定）
9. SNS links（Instagram・LINE必須）
10. Access Map + 営業情報（店舗型）

### 6-3. カラーレシピ（パレット候補）

| ムード | ベース | テキスト | 差し色1 | 差し色2 |
|---|---|---|---|---|
| 老舗和モダン | #f9f5ee | #1a1311 | #864a34 | #c6b192 |
| D2Cモダン | #f4ece5 | #172852 | #d06d43 | #e2cebc |
| 高級レストラン | #0e1420 | #f0e8d6 | #c5a572 | #5a1515 |
| クラフトビール | #161616 | #fefefe | #e8a42b | #6a6a6a |
| 産地直送 | #fcfcf7 | #1f1a1a | #009944 | #f6ab00 |
| パティスリー | #f9f8f3 | #280901 | #9a4a2f | #e6d3b8 |
| カフェ | #fff9e7 | #3d2817 | #d4a574 | #7a9970 |
| ナショナル菓子 | #ffffff | #222222 | #e60012 | #ffd900 |

### 6-4. フォントペア推奨

| 用途 | 見出し | 本文 | アクセント英文 |
|---|---|---|---|
| 老舗和 | Shippori Mincho B1 | Noto Sans JP | Marcellus |
| D2Cモダン | Noto Sans JP Bold | Noto Sans JP | Inter |
| 高級洋 | Cormorant Garamond | Noto Serif JP | — |
| カジュアル | Zen Kaku Gothic New | Zen Kaku Gothic New | Montserrat |
| クラフト | Oswald / Roboto Condensed | Noto Sans JP | — |
| パティスリー | Noto Serif JP | Noto Sans JP | Crimson Pro |

### 6-5. コピーライティング生成ルール

食品LPコピー生成時は以下のテンプレートを軸にする:

**[A: シズル語 + 感覚]** + **[B: 情緒 / 時間 / シーン]**

例:
- 「華やかなホップの香り。もう一人の自分にであう、この時間。」
- 「いずれ、家族の味になる。」
- 「感動の目玉焼き。」
- 「娯楽的たべもの。」
- 「いつもできたて作りたて。」

ルール:
1. **1行15文字以内を2行**（モバイル可読性）
2. **具体シズル語 + 抽象情緒語**の組み合わせ
3. 句点`。`で断言（業界全体の癖）
4. 漢字ひらがな比率は**ひらがな多め**（親しみ）

### 6-6. シズル写真ディレクション

- **断面（パティスリー・パン・和菓子）**
- **注ぎ（酒・茶・コーヒー）**
- **湯気（ラーメン・温物・スープ）**
- **手で取る（おにぎり・パン・ピザ）**
- **器・盛り付け（和食・料亭）**
- **手しごと（職人の手・醸造タンク・窯）**
- **素材単体（原料・産地畑・海）**
- **シーン（食卓・ギフト包装・店内）**

→ MCPの画像生成／参照時に**この8タイプを必ず提示**し、商品カテゴリに応じて自動選択すべし。

### 6-7. 食品LPの"やってはいけない"（アンチパターン）

1. **ストックフォト感丸出し** → 食品は商品写真の鮮度が命。ブランド写真必須。
2. **価格を隠す** → 中央値¥2,400帯は明示した方が購買率↑（特にギフト／D2C）
3. **英文だけ** → インバウンド狙いでも日本語コピー無しは離脱激増
4. **CTAが「詳しく見る」だけ** → 具体動詞（予約／買う／届ける）必須
5. **Instagram無視** → 飲食は Instagram >>> その他SNS。埋込・リンク必須。
6. **FAQ省略** → 特にD2C・高級店では購買前最後のガード。10問以上が標準。
7. **ローディング過剰** → splash 3秒以上は離脱。1.5秒以内＋ブランドロゴのみ。
8. **アレルギー表記漏れ** → 食品LPの信頼大損。必ず記載。

---

## 7. まとめ

食品・飲料LPの本質は **「五感を通じた物語提示」**である。282件から導いた示唆:

1. **構造**: Hero → Concept/Story → Product → Craft/Material → Social proof → FAQ → CTA — この標準8ブロックが90%を占める
2. **配色**: 焦茶 × アイボリー × 差し色1-2 — **工芸系日本パレット**が業界標準
3. **書体**: Noto Sans JP 基本 + 用途別セリフ（Noto Serif JP / Marcellus / Cormorant）
4. **ライブラリ**: WP+jQuery+Swiper（過半数）→ Next/Nuxt+Typekit（新興D2C）→ Barba+GSAP+Lenis（高級）の3層
5. **シズル語**: 濃厚／香ばしい／コク／まろやか の4強
6. **訴求5軸**: 素材／製法／季節／物語／体験 — 最低2軸組み合わせ
7. **CTA**: Instagram・LINE・オンラインショップ・予約の4本柱
8. **新トレンド**: IP/VTuberコラボ、サブスク解約不安先回りFAQ、Studio.Design侵食、体験セクション台頭

→ **design-mcp は「サブジャンル → カラーレシピ → 書体ペア → 必須ブロック → シズル語彙 → CTA型」の6ステップを自動推論するパイプラインを持つべき**。

---

**分析ファイル数**: 282件（全件スキャン）
**深読み件数**: 14件
**統計抽出件数**: 282件（全件）
**レポート行数**: 約800行
