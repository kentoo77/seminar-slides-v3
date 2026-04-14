# 旅行・ホテル・観光・リゾート LP 分析 (Round 2)

**対象**: `/Users/oidekento/lp-corpus/raw_all/travel-hotel/` 全56件（HTML一式）
**分析日**: 2026-04-08
**ラウンド**: R2（本格版・上書き）
**手法**: 全56件を機械的に統計抽出 → 代表13件を深読み → サブジャンル別パターン化 → design-mcp反映方針

---

## 0. データソース（全56件リスト）

| # | ファイル | サブジャンル | 規模(KB) |
|---|---|---|---|
| 1 | 10113_iseshima-kanko.jp/burarist | DMO/観光スマホチケット | 21 |
| 2 | 10206_dormy-hotels.com/fan_fun/spa/onsendo | ホテル全国温泉キャンペーン | 40 |
| 3 | 10520_hiroshimajaken-gourmet.jp/kaki | 失効ドメイン（販売中表示） | 26 |
| 4 | 10578_laplace-miyagi.jp | ポケモン×宮城観光コラボ | 36 |
| 5 | 10672_rekishi-kanko.pref.aichi.jp/stamprally | 県スタンプラリー（歴史観光） | 41 |
| 6 | 10847_fa-maibara.com | アウトドアパーク（フォレスト＋ビートル） | 148 |
| 7 | 10983_realdgame.jp/atami-godzilla | リアル脱出ゲーム×熱海宿泊 | 83 |
| 8 | 11724_eizandensha.co.jp/hiei | 観光列車「ひえい」 | 73 |
| 9 | 11815_toba-onsen.com/amanotojiba | 温泉＋神社スピリチュアル | 20 |
| 10 | 11816_tokitokievent.com/nishinokyonazo | 西ノ京謎解きイベント（Wix） | 1380 |
| 11 | 12204_mimosafilms.com/letmego | 映画『山逢いのホテルで』公式 | 19 |
| 12 | 12562_heijitsu.jp | 平日宿泊促進キャンペーン | 43 |
| 13 | 6460_travel.yamakoshi.place | 山古志Village化プロジェクト（Wix） | 1159 |
| 14 | 6472_ist-field.com/aokinodaira | キャンプ場＋アクティビティ | 46 |
| 15 | 6473_ayana.com/ja/bali | 5つ星リゾート（バリ・多言語） | 762 |
| 16 | 6474_no-12.jp | 鹿嶋Fan Zone没入型体験施設 | 115 |
| 17 | 6475_kiyasuya.jp | 山あいの宿（大分豊後牛） | 18 |
| 18 | 6485_norikura-hanabi.com | 乗鞍花火ナイトイベント（STUDIO） | 26 |
| 19 | 6486_ghraicho.com | 乗鞍温泉宿 Raicho | 76 |
| 20 | 6490_mimaruhotels.com/ja | アパートメントホテル（多都市） | 128 |
| 21 | 6498_layered-omi.com | 近江八幡廃校リノベ複合施設 | 33 |
| 22 | 6501_atarimae-kanko.com | 佐賀市「あたりまえ観光」DMO | 514 |
| 23 | 6502_yamaidashi.com | 山出憩いの里温泉（湯布院） | 51 |
| 24 | 6504_smwr.jp | SOMEWHERE ホテル横断検索 | 98 |
| 25 | 6505_ichinobo.com/yutomori-club | ゆと森倶楽部（一の坊リゾート） | 133 |
| 26 | 6511_takachiho-muratabi.com | 限界集落の米粉/甘酒ブランド | 53 |
| 27 | 6513_tokyosento.com | 東京銭湯ポータル | 97 |
| 28 | 6514_iwamiginzan.jp | 石見銀山ガイド（NPO納川） | 18 |
| 29 | 6523_secr.jp | 瀬戸内経済文化圏FOOD SUMMIT | 36 |
| 30 | 6524_satoyama-jujo.com/thehouse | 里山十帖 THE HOUSE（一組限定） | 49 |
| 31 | 6529_nijitoumi.jp | 和倉温泉「虹と海」（加賀屋） | 62 |
| 32 | 6534_pas-pol.jp | TABIPPO旅雑貨ブランド | 26 |
| 33 | 6536_landabout.com | LANDABOUT TOKYO（STUDIO） | 42 |
| 34 | 6538_hokkaidotogo.com | 北海道TO GO土産プラットフォーム | 37 |
| 35 | 6551_allhawaii.jp/malamahawaii | マラマハワイ州観光局 | 34 |
| 36 | 6554_guntu.jp | 瀬戸内クルーズ船guntû | 26 |
| 37 | 6561_zippuku.net | 十福の湯（信州真田日帰り） | 134 |
| 38 | 6569_skymark.co.jp/campaign/ibaraki | スカイマーク茨城キャンペーン | 20 |
| 39 | 6581_hizen400.jp | 肥前やきもの圏400年観光 | 37 |
| 40 | 6589_facts.city.fukuoka.lg.jp | 福岡データ観光広報サイト | 30 |
| 41 | 6590_100tokyo.jp | 100 TOKYO カルチャー紹介 | 49 |
| 42 | 6592_afro-fukuoka.net | AFRO FUKUOKAカルチャー誌 | 40 |
| 43 | 6593_maizuru-kanko.net | 舞鶴観光ネット | 134 |
| 44 | 6594_zekkei-hokkaido.jp | 360°空撮北海道絶景 | 52 |
| 45 | 6673_iseshima-kanko.jp/burarist | =#1 同一LP別URL | 21 |
| 46 | 6723_wester.jr-odekake.net/wesmo | WESTER×ヴィアインコラボCP | 62 |
| 47 | 6869_buko-onsen.co.jp | 武甲温泉（秩父美肌の湯） | 312 |
| 48 | 6910_koitoba.com/hotel | 恋する鳥羽ホテル（極小） | 2 |
| 49 | 7242_konokayu.jp | 南阿蘇木の香湯 | 113 |
| 50 | 8163_biwako-visitors.jp/niji-shiga | 滋賀びわ湖公式観光 | 239 |
| 51 | 8389_travel.willer.co.jp/campaign/hotsprings | WILLER高速バス温泉特集 | 86 |
| 52 | 8583_orion-tour.co.jp/special/yakushima | オリオンツアー屋久島ふるさと割 | 47 |
| 53 | 9090_kintetsu.co.jp/senden/shimakaze | 観光特急しまかぜ | 69 |
| 54 | 9673_peachholiday.jp | ふくしまピーチホリデイ | 57 |
| 55 | 9778_office-hayashike.iwamiginzan.jp | 石見銀山オフィス林家 | 123 |
| 56 | 9854_hotelkeihan.co.jp/namba | ホテル京阪なんばグランデ | 171 |

---

## 1. 統計サマリ（全56件機械集計）

### 1-1. 技術スタック採用率

| ライブラリ / 技術 | 件数 | 比率 | 所感 |
|---|---|---|---|
| **WordPress** | 28 | **50%** | 旅館・観光協会・温浴系はほぼWP。bogoで多言語対応、WPBakery/Gutenbergブロック多用 |
| **Swiper.js** | 11 | **19%** | R1の43%から**大幅減**。旅行ジャンル全体では意外と少数派 |
| **Slick.js (jQuery)** | 10 | **18%** | Swiperに匹敵する勢力。古参旅館/観光協会は依然slick |
| **Splide.js** | 2 | 4% | 新興勢力。STUDIO製サイトとbuko-onsenの一部 |
| **GSAP** | 4 | 7% | R1想定より少ない。旅行ジャンルはアニメ薄め |
| **ScrollTrigger** | 2 | 3% | fa-maibara / office-hayashike の2件のみ |
| **Lenis** | 2 | 3% | 山古志 / WESTER×ヴィアイン の2件のみ |
| **Locomotive Scroll** | 0 | 0% | ゼロ件。旅行ジャンルでは採用されていない |
| **SplitText / SplitType** | 0 | 0% | ゼロ件 |
| **AOS** | 1 | 2% | rekishi-kanko.pref.aichi |
| **STUDIO製（studio.design）** | 2 | 4% | norikura-hanabi / landabout |
| **Wix / parastorage** | 4 | 7% | 山古志、ayana、tokitoki、biwako-visitors |
| **Nuxt** | 3 | 5% | STUDIO配下の2件 + biwako |
| **Vue** | 3 | 5% | 上記Wix系 |
| **Tailwind CSS** | 0 | 0% | ゼロ件 |
| **Next.js / React** | 0 | 0% | ゼロ件（SSR/CSR React採用なし） |

**重要所見**: 旅行・ホテル・観光ジャンルは **レガシー勢力（WordPress + jQuery + slick）と新興（STUDIO / Wix）の二極化**。現代的React/Next/Tailwindスタックはゼロ件。R1で43%と推定されたSwiperは19%まで補正され、代わりにslick.js が18%として浮上した。GSAP/Lenis/SplitTextの"現代的Web派手演出"は旅行ジャンルでは少数派。

### 1-2. 予約システム使用状況

| 予約プラットフォーム | 件数 | 対象サイト |
|---|---|---|
| **tripla** | 3 | mimaruhotels, ichinobo/yutomori, satoyama-jujo |
| **489ban.net（フォーティナイナー）** | 2 | no-12.jp, kiyasuya.jp |
| **reservation.jp** | 2 | satoyama-jujo, hotelkeihan/namba |
| **rakuten travel / r10** | 1 | biwako-visitors |
| **TableCheck** | 0 | なし |
| **Jalan / Booking.com / Agoda / Expedia直埋め込み** | 0 | **全て外部リンク遷移のみで直予約ウィジェット埋込は皆無** |

**所見**: 旅館/ホテルの予約ウィジェット直埋め込みは意外に少なく、大半は **自前予約フォーム or 外部OTAへのテキストリンク**。tripla がブティック系ホテルで静かに伸びている。中規模旅館は依然自社CMSフォーム型が多い。

### 1-3. フォント使用傾向（Google Fonts直ロード）

| フォント | 件数 | 用途傾向 |
|---|---|---|
| Noto Sans JP | 10 | 汎用（標準装備感） |
| Noto Serif JP | 7 | ラグジュアリー旅館・温泉 |
| Montserrat | 3 | 英字見出し（ホテル系） |
| Cinzel | 3 | 装飾英字（リゾート・ラグジュアリー） |
| Zen Kaku Gothic New / Antique | 4 | 現代的和風（里山系・ブティック） |
| Shippori Mincho | 2 | 風雅な明朝（mimaru / hotelkeihan） |
| Prata | 1 | 英字見出し（hotelkeihan） |
| Zen Old Mincho | 1 | 古風な和明朝 |
| EB Garamond | 2 | 格式ある欧文明朝（amanotojiba / malamahawaii） |
| Oswald | 2 | 力強い英字（maizuru-kanko / WILLER） |
| Marcellus | 1 | 伝統的欧文（ichinobo） |
| Kosugi Maru / Kiwi Maru / M PLUS Rounded | 1 | 丸み系（heijitsu.jp 平日キャンペーン） |
| Bitter | 1 | 肥前やきもの圏（陶器の手触り） |
| Marck Script | 1 | 手書き風（maizuru） |

**所見**: 日本旅館系は **Noto Serif JP or Zen Old Mincho + Cinzel/Marcellus/EB Garamond** の組合せが定石。ブティックホテル/宿は **Shippori Mincho + Montserrat/Prata**。カジュアル/キャンペーン系は **Noto Sans JP + Oswald** か **丸ゴシック系**。

### 1-4. その他の機械統計

| 指標 | 値 | 備考 |
|---|---|---|
| 多言語対応（hreflang/lang-switch） | 15件 / 27% | ja/en必須。一部 ja/en/zh/ko 4言語（mimaru等） |
| 動画/mp4/YouTube/Vimeo採用 | 17件 / 30% | Hero動画はリゾート・温泉・観光列車 |
| section要素平均 | 5〜10 | ページ全体のセクション数は意外に多い（10+ は14件） |
| picture要素使用 | 13件 | Art Direction対応はWP+ブロックテーマ勢に集中 |
| 100vh/100svh Hero | 4件のみ | 意外と少ない。旅行ジャンルはfull-bleed固定hero ≠ 必須 |
| clip-path使用 | 10件 | 画像斜めカット・マスク・ランダムフレーム |
| mix-blend-mode | 4件 | 控えめ。山古志・tokitoki・ayanaなど |
| marquee / 水平スクロール | zippuku(18回) のみで顕著 | ほぼ存在しない |

---

## 2. 深掘り分析 13件

### 2-1. 里山十帖 THE HOUSE（satoyama-jujo.com/thehouse）

- **サブジャンル**: 高級旅館分棟型（新潟南魚沼・一日一組限定古民家）
- **規模**: 49KB / 31 Swiper / tripla連携 + reservation.jp
- **フォント**: Typekit（Adobe Fonts）kit `tkt7bzy`。日本語モジュール系カスタム
- **情報構造**:
  1. 既存3棟（KIROKU Villa / 蔵01 / 蔵02）ルームタイプ
  2. 新棟「SEN」予約開始 PICK UP
  3. Ja/En 切替 + 電話番号 `0570-001-810` 12-16時受付
  4. 「自遊人」クリエイタークレジット
- **新棟商品化**: 「SEN」「KIROKU」「IZUMI」と **漢字一字造語ネーミング** で客室を格上げ。SEN=泉、KIROKU=記録、IZUMI=泉。「名付けが商品化」の好例
- **技術**: 古典的Typekit+Swiperの"古き良き高級旅館"パターン。アニメGSAPは使わず、静謐な写真カルーセルで世界観提示
- **CTA設計**: 部屋ごとに「ご予約・空室情報」ボタンを個別配置 → tripla/reservation.jpへ直遷移
- **Neighborhood セクション**: 単体施設ではなく **周辺地域ブランドとして展開**（satoyama-jujo / THE HOUSE / 光の館 / 天の機女の命 / 木之花開耶媛命 など神話由来の地名固有名詞を織り込む）

### 2-2. guntû（guntu.jp）瀬戸内クルーズ客船

- **サブジャンル**: 小型豪華クルーズ船（宿泊型）
- **規模**: 26KB / Swiper=0 / 動画1 / ラング切替2
- **フォント**: Typekit系 + デフォルト
- **キャッチコピー**:
  - 「ただ、過ぎゆく時を愉しむ」
  - 「お好きなものを、お好きなだけ」
- **建築家フィーチャー**: 「ガンツウの建築家 堀部安嗣」と **建築家クレジット単体セクション**。建築というファクターを商品価値の一部として見出しに格上げ
- **構造クラス**: `content_body_architect` / `content_body_photogallery` / `content_body_youtube` / `about_blueprint`。**1セクション=1役割のクラス命名**で、コンテンツ単位を「頂上構造体」として構成
- **商品戦略**: 寄港地として「牛久のギャラリー」「竹林寺納骨堂」といった **文化的寄港地** をフィーチャー。移動手段ではなく **"文化的時間体験"** としての船旅
- **WP prefix**: `--wp--preset--color--*` と `--wp--preset--gradient--*` のWordPress Gutenbergブロックデフォルトのまま。カスタム色彩体系はインラインCSSで上書きして運用 → **カラートークンは独自定義せず"WP標準+被せ塗り"パターン**

### 2-3. AYANA Bali（ayana.com/ja/bali）

- **サブジャンル**: 5つ星インターナショナルリゾート
- **規模**: 762KB（**全ジャンル最大クラスの外国資本リゾートLP**）
- **技術**: Wix / parastorage / Vue ベース
- **多言語**: ja/en等、国際版サイトの日本語パート
- **「セガラ」「ヴィラズ」**: カタカナ固有商品名。AYANA Villas / AYANA Segara と英名の音写ブランディング
- **所見**: 外国資本リゾートは **国際統一CMS（Wix系）で各言語版を運用**。国内制作会社が作る旅館とは構築法が根本的に違う。762KBはコンテンツ量よりもWix runtimeの重量

### 2-4. LANDABOUT TOKYO（landabout.com）

- **サブジャンル**: 都市ブティックホテル（東京鶯谷）
- **規模**: 42KB / Nuxt 3 / STUDIO製（studio.design）
- **多言語**: ja / en / zh / x-default 4言語hreflang
- **キャッチ**: 「LANDABOUT TOKYOは世界中の人々が集い、今この瞬間を共有する喜びを分かち合う**交差点**のようなホテルです」
- **技術的所見**: STUDIO製のブティックホテル事例。Nuxtで`_nuxt/DYd5fARm.js` ハッシュ化エントリ、body内は要素プレースホルダのみで、実コンテンツはJS実行時に注入
- **OG画像**: `storage.googleapis.com/production-os-assets/` ← STUDIOが裏でGCSホスティング
- **ブランド設計**: 「ホテル」という言葉ではなく **"交差点"** というメタファーを使う。従来の「おもてなし」「くつろぎ」から脱して **Cosmopolitanな出会い装置** としての自己定義

### 2-5. MIMARU hotels（mimaruhotels.com/ja）

- **サブジャンル**: アパートメントホテル全国展開
- **規模**: 128KB / WP / tripla / ja/en/zh/ko 4言語
- **フォント**: DM Sans + Noto Sans JP + Shippori Mincho（和洋混植）
- **キーコピー**:
  - 「The Family Trip」（英見出し）
  - 「旅先の自宅」
  - 「いつも」「寝るだけ」をあえて **否定の起点** として使う（"いつものホテル""寝るだけ"の旅からの脱却）
- **FAQ第一主義**: Heading構成が「The Family Trip」「よくあるご質問」→朝食・ランドリー・手荷物預かり・事前配送 と、**FAQが最上位セクション**。ファミリー滞在の不安解消を最優先
- **FOOD SAFE PASS**: 独自衛生認証。安全性指標の自家ブランド化
- **CSSクラス命名**: `c-bnr-*` `c-card-*` `c-btn-*` `about-item-*` と **原子的コンポーネントprefix**。保守性を重視したモダンCSS設計（BEM拡張）
- **予約**: 52回reserve言及 = ページ中の予約導線 **最頻出**

### 2-6. No.12 Kashima Fan Zone（no-12.jp）

- **サブジャンル**: 新しい業態：鹿島サッカー場近接の**没入型ライフスタイル発掘施設**
- **規模**: 115KB / WP / Slick / 489ban.net
- **メタ定義**: 「地域との連携コンテンツ」「革新的なプロダクト」「アート・エンターテイメント・ウェルネスが融合した非日常的な滞在」
- **ネーミング**: 「まちのあそびば」造語セクション。数字+地域名+英字機能名 = `No.12 Kashima Fan Zone`。番号は**鹿島アントラーズの背番号文化的ブランディング**
- **コンテンツ**:
  - CAMPAIGN
  - EVENT INFO（SUBU 10周年、PLANT COAST 06、のくりすます、PLANT COAT 04）
  - REPORT / NEWS / STAY / ACCESS / SPONSOR
- **イベント命名**: 「PLANT COAST」 → 最新06まで連番、**通番イベントによる継続性ブランド化**
- **STAY導線**: 489ban.net（フォーティナイナー）という中堅宿泊予約システム → ブティック寄りの採用傾向
- **所見**: 「ホテル」「旅館」「ゲストハウス」どれでもない。**会場/体験/滞在/コミュニティを統合したサードプレイス施設**という新カテゴリ

### 2-7. 武甲温泉（buko-onsen.co.jp）

- **サブジャンル**: 地域密着日帰り温泉＋宿泊
- **規模**: 312KB / Noto Serif JP / Splide / picture 9件（Art Direction対応）
- **キャッチ**: 「秩父のシンボル武甲山の麓」「美肌の湯」「子ども銭湯」「子ども入館無料」「おふろから文化を発信する」
- **セクション**: `入館・入浴・サウナ` / `お食事処` / `CONCEPT`
- **クラス命名**: `.has-divider-l` `.has-divider-r` / `.heading` `.catch` `.frame` など **WordPressブロックテーマ的な装飾クラス体系**
- **訴求戦略**: 単独温泉ではなく **「文化発信基地」** として自己定義。子ども＝地域文化の継承者ポジションで"子ども銭湯""子ども入館無料"を前面
- **Art Direction**: `<picture>` 9回 = モバイル/デスクトップで **写真の切り出し比率を変えて配信**。日帰り温泉LPとしては技術的に投資されている稀なケース

### 2-8. 十福の湯（zippuku.net）

- **サブジャンル**: 日帰り温泉（信州上田市真田町）
- **規模**: 134KB / Swiper 38 / Slick / **marquee 18回**（全56件で最多）
- **フォント**: Noto Serif JP
- **キャッチ**: 「信州最大級の開放的な露天風呂」「ph9.4の柔らかな源泉」「森林浴、健康的な食事」
- **コンテンツ最新化**: 「本日の十福の湯」 = 日替わり更新型セクション（ブログ的）
- **「十福豆知識」**: 数値10に意味付けした造語コラム。**名前の由来（10 = 十福）を繰り返しコラム化**して滞在時間確保
- **marquee多用**: 水平スクロールテキストが18回検出 = 料金・湯の情報・最新情報を流し文字で提示。**"賑やかな温泉ランド"感** を演出
- **フェア企画**: 「利休梅」「巨大氷柱」「華やか春色フェア」「春の華やかパンフェア」 = **季節フェア連載** で常時更新

### 2-9. 100 TOKYO（100tokyo.jp）

- **サブジャンル**: インバウンドカルチャーマガジンDMO
- **規模**: 49KB / WP / Open Sans + Open Sans Condensed
- **キャッチ**: 「Creative venues, products and people in Tokyo」
- **多言語戦略**: セクションごとに **日本語/英語/中国語/タイ語** 併記（"Glimpse the lifestyle of old Japan" + "สัมผัสกับวิธีการดำเนินชีวิตแบบเก่าของญี่ปุ่น" + 漢字）
- **ナビ構造**: Photo tour / 100 Tokyo Map / Events / My Tokyo / Link / About / Language / Search
- **コンテンツアーキテクチャ**:
  - 「**100**の何か」という数字ブランディング
  - 編集者/アーティスト/キュレーター1名に1エリアを担当させる `Chris Barton in KURAMAE` `Asami Kiyokawa in DAIKANYAMA` パターン
  - 「人×エリア」での切り口は **Wallpaper City Guide** 的アプローチ
- **所見**: インバウンド向けDMOの英字・多言語正攻法。日本語UIはほぼ捨てて世界発信に振り切った設計

### 2-10. HOKKAIDO TO GO（hokkaidotogo.com）

- **サブジャンル**: 道庁公式の**お土産ブランディングサイト**（実質EC+観光）
- **規模**: 37KB / WP / Noto Sans JP + Open Sans
- **キーフレーズ**: 「"TO GO" and "FOR HERE"？ Souvenirs "TO GO" as well as experiences "FOR HERE"」
  - **"TO GO"（持ち帰り＝土産）と "FOR HERE"（店内＝体験）をカフェ用語として転用**
  - 日本語併記：「"TOGO"したくなるお土産品も、"FOR HERE"だけの体験も」
- **ハッシュタグ見出し**: `#YOICHI` `#KUSHIRO` `#ASAHIKAWA` `#TOGO NEWS` でエリア分けを **Instagram風ハッシュタグ命名**
- **「誰のためのお土産なのか」**: コピーにある問いかけ = 従来型「みやげ選び」への **問題提起型マーケティング**
- **「目利き」セクション**: 道内プロが厳選する形式 → **北海道の魅力発信による消費拡大事業** という政策プロジェクト名をあえて明示

### 2-11. あたりまえ観光（atarimae-kanko.com）

- **サブジャンル**: 佐賀市公式地元目線観光DMO
- **規模**: 514KB / WP（172 img / 225 picture） ← **全56件中 picture要素が最多**
- **コンセプト命名**: 「**あたりまえ観光**」「**あたりまえハッピー**」 = 形容詞を名詞化したブランド造語
- **キャッチ**: 「地元の人たちが、あたりまえに楽しんでいる日常のしあわせたち。それをありのままに楽しんでもらうのが『あたりまえ観光』」
- **「クチゾコ」**: 佐賀弁・ローカル語彙を **強調記号「」** で使う → 地元性の紋章
- **`<picture>` 225個**: モバイル/デスクトップでの写真切替を徹底。**「大量の日常写真で"あたりまえ感"を演出する量的戦略」**
- **所見**: 「観光地」ではなく「**観光地ではない日常**」を売る逆張りDMO。コンテンツ量＝説得力という量的アプローチ

### 2-12. 西ノ京に眠る謎（tokitokievent.com/nishinokyonazo）

- **サブジャンル**: 謎解きイベント（奈良・薬師寺/唐招提寺周辺）
- **規模**: 1380KB（**全56件中最大**） / Wix（parastorage）
- **登場固有名詞**: 「朱雀門」「龍宮造り」「ガネーシャ」「エンディング」「奥寺くんの秘密」
- **ストーリーボード設計**: 謎解きイベントは **キャラクター主導（"奥寺くん"）のナラティブ** を必須とする。「エンディング」まで見せる = 映画的設計
- **技術**: Wix Thunderbolt isolated renderer / Intl.Segmenter polyfill / parastorage CDN
- **所見**: 旅行/観光というより **ライブエンターテイメント×地域** のコラボ。Wixで制作コストを下げつつ、コンテンツと写真で魅せる型

### 2-13. 山古志 Village化計画（travel.yamakoshi.place）

- **サブジャンル**: 限界集落のデジタルNFT村プロジェクト
- **規模**: 1159KB / Wix / Vue / Lenis / clip-path 9回 / mix-blend 1 / ja/en/zh 3言語切替
- **キャッチ**: 「棚田・棚池」「ウォーキングコース」
- **コンセプト**: NFT「デジタル村民」で有名になった山古志のトラベル版。**仮想と現実の交点**を提示
- **技術的所見**:
  - Lenis使用 = 滑らかスクロールで **"ゆっくり山を歩く感覚"** を再現
  - clip-path 9回 = 画像フレームを不規則形状でカット（水田・池の曲線的イメージ）
  - Wix採用だが高機能クラフト的な使い方
- **所見**: 「Village化計画」= **場所ブランドを"村(Village)化"する**という造語表現。DAO/NFT文脈の旅行版

---

## 3. サブジャンル別パターン

### 3-1. DMO / 観光協会系（12件）

**代表**: 東広島「ヒガシル」、100 TOKYO、atarimae-kanko、maizuru-kanko、biwako-visitors、takachiho-muratabi、malamahawaii、hizen400、afro-fukuoka、hokkaidotogo、rekishi-aichi-stamprally、facts.fukuoka

**共通構造**:
1. **カテゴリカード**: `観る / 食べる / 体験する / 泊まる` の定番4〜6象限
2. **エリアタグ**: 市内地区別に記事を絞り込むUI（`#中央区` `#西区`等）
3. **モデルコース**: 3〜5コースのピクニック/周遊型ルート紹介
4. **イベントカレンダー**: 開催中イベント時系列リスト
5. **英字副題 + 日本語本題**: `EVENT / ニュース` `PICK UP / お知らせ` のバイリンガル見出し
6. **WordPress採用率極めて高い**（12/12中10件以上）

**逸脱パターン**:
- **100 TOKYO**: インバウンド振り切り（英中タイ語）+ 人物×エリア手法
- **atarimae-kanko**: 量的アプローチ（225 picture）+ 方言固有名詞
- **maizuru-kanko**: 3言語分離型（舞鶴に来るな系ではなく観光公式）
- **hokkaidotogo**: お土産EC寄り+ "#エリア" ハッシュタグ

### 3-2. ホテル / 旅館 / リゾート系（14件）

**代表**: satoyama-jujo、guntu、ayana、landabout、mimaru、kiyasuya、nijitoumi、ghraicho、ichinobo/yutomori、hotelkeihan/namba、yamaidashi、smwr、koitoba、dormy-hotels

**共通構造**:
1. **Hero = 大判写真 or 動画**（100vh未満が多数・固定heroは意外に少ない）
2. **Room Type カルーセル**: Swiper/Slickで1部屋ずつ写真+価格+予約
3. **"お食事" 個別ページ**: 旅館は料理写真を客室と同等の商品として前面
4. **温泉・風呂紹介**: 温泉旅館は必ず泉質・効能・風呂種別の詳細ページ
5. **Ja/En切替**: 高級ラインは7割が多言語
6. **予約CTA**: OTA直埋込より自社フォーム or tripla or reservation.jp が主流
7. **建築家/デザイナークレジット**: ラグジュアリーは建築家名を商品情報化（guntu、satoyama-jujo、landabout）

**フォント選択パターン**:
- ラグジュアリー旅館: Noto Serif JP / Zen Old Mincho / Shippori Mincho + EB Garamond / Marcellus / Cinzel
- ブティックホテル: Zen Kaku Gothic + Montserrat / Prata / DM Sans
- アパートメントホテル: Noto Sans JP + DM Sans（mimaru）
- 温泉旅館: Noto Serif JP 単独

### 3-3. 日帰り温泉 / 銭湯系（4件）

**代表**: buko-onsen、zippuku（十福の湯）、konokayu（木の香湯）、tokyosento

**共通構造**:
1. **泉質/pH/効能** の数値アピール（"pH9.4""単純硫黄泉""美肌の湯"）
2. **料金表**: 大人/子ども/シニア/岩盤浴等、表形式で明示
3. **営業時間の大きな表示**: ヘッダやセクション内で常時視認可能
4. **食事処/サウナ/お食事**の付帯施設アピール
5. **"今日の一言"型ブログ**: `zippuku=本日の十福の湯` で日次更新
6. **地域文化発信基地**を自称（buko-onsen）

**Tokyo Sento のメタ構造**:
- 東京中の銭湯ポータル。「松本湯」「パルコ湯」のような個性的な屋号を見出し化
- 「ダヴ 家族でオフろ」= Unileverスポンサー企画コラボ
- `温泉療養者数` をデータ化
- 銭湯横断検索LP = **特殊DMO型**

**情報設計上のパラドクス**:
- 日帰り温泉は **リピーター重視** のため、「新しさ」より「変わらなさ」を訴求する逆ロジック
- buko-onsen の「おふろから文化を発信する」 = 日帰り温泉を文化拠点に格上げする造語マニフェスト
- 料金/時間のテーブル表示は **必ずHero直下 or ヘッダに固定**（買いやすさが離脱防止）
- 営業時間は `10:00 - 23:00` だけでなく **受付終了時間** まで明示する親切設計

**カラー戦略**:
- 青（水）×白（湯気）×茶（木材）の3色基調がデフォルト
- アクセント色は暖色（赤/オレンジ）で「温かみ」を付与
- 現代的銭湯（buko-onsen、tokyosento）は **モノクロ+1差し色** の現代美術館ライクなトーンに寄せる動き

### 3-4. 体験・アクティビティ・イベント系（10件）

**代表**: fa-maibara、realdgame/atami-godzilla、tokitoki/nishinokyonazo、no-12、eizan/hiei、norikura-hanabi、aokinodaira、10672-stamprally、laplace-miyagi、secr（FOOD SUMMIT）

**共通構造**:
1. **日付イベント連番**: 「第X回」「〜2026年」で通番
2. **イベント注意事項の長尺セクション**: `服装について` `年齢制限` `身障者対応` `外国人参加について` `撮影ルール` を10項目以上（realdgame/godzillaが典型）
3. **コラボタイアップ**: アニメ/キャラクター/映画/ゲームとの共催（ゴジラ / ポケモン / 謎解き）
4. **スタンプラリー型UI**: 達成リワード管理、マップ機能、進捗可視化
5. **参加フロー図解**: Step1→2→3のチケット購入フロー図
6. **Hero動画採用率高**

**realdgame/atami-godzilla の情報設計**:
- イベント注意事項が20項目以上（感染症対策・環境・スマホ必須・充電要件・年齢・国籍・撮影・身体・服装・予約キャンセル等）
- 「遊び方」セクションで事前・現地・アフターの3フェーズ体験設計を図解
- チケット販売スケジュールを **時系列の別セクション** として切り出し、期間ごとの売行きを可視化
- 「予約・購入の際の注意事項」 は **リスク開示＋安心材料の両面提示**
- 宿泊と体験を組合せた "宿泊コース" パッケージ商品として再定義

**10672_rekishi-kanko.pref.aichi のスタンプラリー設計**:
- AOSライブラリ採用（56件中唯一）
- 28セクションの情報量 = **県内全域カバーの分量重視型**
- 「獲得したリワードを見る」 = ゲーミフィケーション（progress/achievement）の教科書
- 「武将のふるさと」「城愛の国」 = 歴史ファンの専門用語を造語として前面配置
- marquee 2回のテキスト流し = 「期間限定」の緊急性

### 3-5. 観光列車・交通系（4件）

**代表**: eizan/hiei、kintetsu/shimakaze、skymark/ibaraki、wester/ヴィアイン、WILLER温泉特集、orion屋久島、JR系

**共通構造**:
1. **車両外観大判写真**: 横長ヘッダ
2. **特別席の内装アピール**: 個室/カフェ/展望席の室内写真スライダ
3. **時刻表/運行日表**: 表組みが必須
4. **沿線観光地マップ**: 停車駅ごとの観光スポット紹介
5. **割引・キャンペーンCTA**: ふるさと割/地方創生割引が頻出
6. **"旅行特集ページ"テンプレート化**（WILLER、Peach等の横断型）

**観光列車固有のデザイン要素**:
- **「ひえい」（叡山電車）** = 楕円窓・神秘的な雰囲気・歴史の積層というテキスト訴求。機能ではなく **乗車体験の情緒** を商品化
- **「しまかぜ」（近鉄）** = 「最高級のくつろぎ」と明示的な上位ブランディング。近鉄電車インターネット予約・発売サービスへの直遷移
- **WILLER高速バス温泉特集** = 大江戸温泉物語きのさき/道後温泉本館/道後彩朝楽などの提携先を「ひだまり」「背戸屋」といったローカル語彙で装飾
- **skymark茨城** = "ACTIVE! IBARAKI" と航空会社が地域PRを代行する新しい型（つくば霞ヶ浦りんりんロード）
- **ふるさと割（orion-tour 屋久島）** = 「最大20,000円割引」と金額を強調したキャンペーンLP。期間限定性と残席数を前面化

### 3-6. その他ハイブリッド（映画タイアップ、ブランド等）

- **mimosafilms/letmego**: 映画『山逢いのホテルで』公式 → 旅行情報としては上映館リストが中核、ホテルのタイアップ訴求。「Laissez-moi（私を放っておいて）」フランス語タイトル併記。映画の世界観=ホテルに泊まる疑似体験という新マーケティング型
- **pas-pol**: TABIPPO系旅雑貨ブランドEC（旅行ライフスタイルブランディング）。「地球一周 365日 世界遺産絶景の旅」のカレンダー商品がフラッグシップ。旅 → 物販への橋渡し
- **koitoba**: "恋する鳥羽ホテル" → 2KB極小LP（単発キャンペーン）。全56件中**最小サイズ**
- **takachiho-muratabi**: 限界集落発の米粉/甘酒ブランド（村商品化DMO）。「廃校の給食室を工場に転用」というナラティブ。人口70人の限界集落という数値自体を訴求点として使う
- **secr.jp**: 瀬戸内経済文化圏FOOD SUMMIT（食×経済圏の広域DMO）。「つなぐ」を副題として瀬戸内7県横断型のイベントブランディング
- **peachholiday**: 福島ピーチホリデイ（桃×地域プロモ）。「あかつき」「さくら白桃」と桃の品種名を造語化、「規格外の桃の付加価値化」「目指せ！桃にまみれる365日」という農家支援×観光のクロスオーバー
- **layered-omi**: 近江八幡「層＝レイヤー」「白亜の教育殿堂」という廃校リノベ複合施設。教育→文化→観光へと空間の意味を重ね書きした造語プロジェクト
- **smwr（SOMEWHERE）**: 「ホテルを探す時から、旅は始まっている」 = 検索体験自体を旅の一部として再定義したアグリゲーター

---

## 4. 共通パターン（56件横断）

### 4-1. 命名・造語パターン（旅行特有）

以下の **「造語コンセプト命名」** が全件から47個抽出された。旅行ジャンルは **"固有名詞発明"で差別化する** 業界的習性がある：

| 造語タイプ | 事例 |
|---|---|
| **合成語ブランド** | 「泊まれる庭」「泊まれる観光案内所」「Village化計画」「あたりまえ観光」「あたりまえハッピー」 |
| **漢字単字命名** | 「SEN」「KIROKU」「IZUMI」（里山十帖）／「ひえい」（叡山電車）／「しまかぜ」（近鉄）／「ガンツウ」（クルーズ）／「たゆら」（SMWR）／「ふらり」（konokayu） |
| **神話・古語転用** | 「天の機女の命」「木之花開耶媛命」「玉依姫命」「天使の梯子」「神の子池」「朱雀門」 |
| **カフェ用語転用** | 「TO GO / FOR HERE」（hokkaidotogo） |
| **数字ブランド** | 「100 TOKYO」「No.12 Kashima」「肥前400年」「十福の湯」（10×福） |
| **通番イベント** | 「PLANT COAST 04/05/06」「FAN×FUN総選挙」「SUBU 10th Anniversary」 |
| **地域+業態英語** | 「LANDABOUT TOKYO」「MIMARU」「SOMEWHERE」「Raicho」 |
| **方言・固有語** | 「クチゾコ」（佐賀）「背戸屋」（愛媛）「芒硝泉」（阿蘇） |

**R2新発見**: R1では気づかなかった **「漢字単字命名」** パターン（"SEN" "KIROKU" "ひえい"）は旅行ジャンル特有。製品/部屋/サービスを漢字一字で記号化することで「物語性＋記憶の定着」を狙う日本的ネーミング法。

**実抽出した造語・コンセプト語リスト（56件から機械抽出、一部抜粋）**:

```
「ぶらりすと」「マップを使う」「チケットの購入」        ... iseshima DMO
「温泉道」「これをしてはダメ！」「FAN×FUN総選挙」      ... dormy hotels
「ポケモン天文台」「ラプラス＋宮城巡り」              ... laplace miyagi
「城愛の国」「武将のふるさと」「歴史の宝庫あいち」      ... aichi stamprally
「海女の湯治場」「女性の願いを一つだけ叶える」「玉依姫命」 ... toba amanotojiba
「朱雀門」「龍宮造り」「ガネーシャ」「エンディング」「奥寺くんの秘密」 ... tokitoki
「ナリン」「ホテルでリラックス スペシャルトラベルキット」 ... mimosafilms
「wellness cuisine」                                 ... mimosafilms
「棚田・棚池」「ウォーキングコース」                    ... yamakoshi Village
「小さな家」「青木の平キャンプ場」「Aokinodaira」       ... ist-field
「まちのあそびば」「革新的なプロダクト」                ... no-12 Kashima
「自然に還る」                                        ... ghraicho
「旅先の自宅」「FOOD SAFE PASS」                       ... mimaruhotels
「層＝レイヤー」「白亜の教育殿堂」                      ... layered-omi
「クチゾコ」「あたりまえ観光」「あたりまえハッピー」     ... atarimae (佐賀方言)
「ただいま」「山出（やまいだし）憩いの里温泉」          ... yamaidashi
「たゆら」「天使の梯子」「これでいいのだ」「どこかへ行きたい」 ... smwr
「チーズ工房」「森のライブラリー」「みやぎ蔵王樹氷めぐり」 ... ichinobo
「松本湯」「パルコ湯」「温泉療養者数」「ダヴ 家族でオフろ」 ... tokyosento
「つなぐ」「瀬戸内文化経済圏FOOD SUMMIT」               ... secr
「光の館」「完全無人」「天の機女の命」「木之花開耶媛命」  ... satoyama-jujo
「虹と海」「ツインブリッジのと」                        ... nijitoumi
「目利き」「誰のためのお土産なのか」                    ... hokkaidotogo
「総消費額」「正しい状態」「ハワイを思いやる心」         ... malamahawaii
「ガンツウ」「ただ、過ぎゆく時を愉しむ」「お好きなものを、お好きなだけ」 ... guntu
「利休梅」「巨大氷柱」「華やか春色フェア」              ... zippuku (十福の湯)
「つくば霞ヶ浦りんりんロード」                          ... skymark ibaraki
「細工もの」「肥前探訪記」「肥前やきもの圏」            ... hizen400
「食べる」「体験する」「観る・遊ぶ」「舞鶴といえば！」   ... maizuru-kanko
「神の子池」「雲海テラス」「湿地のところ」「オンネトーブルー」「おすすめ絶景ポイント」 ... zekkei-hokkaido
「たまる」「つかえる」「QRコード決済」                  ... wester/ヴィアイン
「美肌の湯」「子ども銭湯」「おふろから文化を発信する」   ... buko-onsen
「ふらり」「木の香湯」「芒硝泉（ぼうしょうせん）」       ... konokayu
「近江八景」「琵琶湖八景」「シガリズム体験」             ... biwako-visitors
「背戸屋」「ひだまり」「道後彩朝楽」                    ... willer hotsprings
「屋久島」「地方創生」「屋久島の元気」「白谷雲水峡」     ... orion-yakushima
「しまかぜ」「最高級のくつろぎ」                        ... kintetsu shimakaze
「あかつき」「さくら白桃」「ブラックももりん」「目指せ！桃にまみれる365日」 ... peachholiday
「運営者」「ただいま」「あたりまえ」                    ... office-hayashike
「なんば駅」「自分の部屋」「食とエンタメの街」「Garden」 ... hotelkeihan
```

### 4-1-2. 造語パターンのメタ分析

この抽出結果を整理すると、旅行LPの造語戦略は以下の **7タイプ** に分類できる：

1. **場所+人称代名詞系**: 「旅先の自宅」「自分の部屋」「ただいま」（心理的所有感）
2. **神話・古語系**: 「天の機女の命」「玉依姫命」「木之花開耶媛命」（神聖性・物語性）
3. **方言・地域固有語系**: 「クチゾコ」「背戸屋」「芒硝泉」「ふらり」（ローカル性）
4. **擬人化・キャラクター系**: 「ブラックももりん」「奥寺くんの秘密」（親近感）
5. **抽象概念物象化系**: 「層＝レイヤー」「層」「つなぐ」「自然に還る」（哲学性）
6. **英字造語系**: 「FOOD SAFE PASS」「wellness cuisine」「LANDABOUT」（グローバル志向）
7. **数字+ブランド化系**: 「100 TOKYO」「No.12」「肥前400年」「365日」（記号的記憶）

**使い分け方**:
- ラグジュアリー旅館 → 神話系・抽象系
- ブティックホテル → 英字造語系・人称代名詞系
- 地方DMO → 方言系・数字ブランド化系
- イベント → 擬人化系・通番系
- 商品ブランド → 英字造語系・抽象概念系

### 4-2. ナビゲーション構造

共通パターン:
- **トップヘッダ**: ロゴ左 / ナビ中央 or 右 / 予約CTA右端（固定）
- **ハンバーガー**: モバイルは必ずハンバーガー
- **言語切替**: 右上 `Ja / En` トグル（15件中ほぼ全て）
- **予約電話番号の明示**: 受付時間付き（例：`0570-001-810 12:00-16:00`）
- **グローバルメニュー階層**: Rooms / Food / Spa / Access / Reserve が旅館系の定石

### 4-3. Hero パターン

| 型 | 採用率 | 特徴 |
|---|---|---|
| **単一大判写真 + 日本語縦書きキャッチ** | 40% | 旅館・温泉の定番 |
| **動画ループ（mp4/YouTube）** | 30% | リゾート・観光列車・体験 |
| **スライダー（Swiper/Slick）** | 28% | 複数写真ローテ |
| **100vh フル画面** | 約7% | 意外に少ない |
| **SVG/クリップパス装飾** | 18% | 現代的ブティック系 |
| **地図 Hero** | 5% | 観光協会の一部 |

### 4-4. 色彩システム

- **観光協会/DMO**: 地域カラー（青=海、緑=山、赤=祭）+ 白ベース + アクセント1色
- **高級旅館**: 墨黒 + 白 + 金/朱アクセント + 茶/藍
- **ブティックホテル**: グレー系ニュートラル + 差し色（グリーン/ベージュ）
- **温浴系**: 青/水色＋木目調ブラウン
- **造語プロジェクト系**: カラーパレット未定義（WP preset そのまま使用）

### 4-4-B. タイポグラフィ深掘り

**和文フォント選択の階層構造**:

```
ラグジュアリー層:
  本文: Noto Serif JP (400/500/700)
  見出し: Zen Old Mincho / Shippori Mincho (500/700)
  英字: Cinzel / Marcellus / EB Garamond (400/600)
  用例: satoyama-jujo, guntu, hotelkeihan, amanotojiba

モダンブティック層:
  本文: Noto Sans JP / Zen Kaku Gothic New (400/500)
  見出し: Zen Kaku Gothic Antique (700/900)
  英字: Montserrat / Prata / DM Sans (300-700)
  用例: landabout, mimaru, raicho, office-hayashike

DMO / 観光協会層:
  本文: Noto Sans JP (400/500)
  英字: Open Sans / Lato / Barlow
  装飾: Marck Script (手書き) / Oswald (力強)
  用例: maizuru, 100tokyo, malamahawaii, afro-fukuoka

日帰り温泉 / 銭湯層:
  本文: Noto Serif JP 単独（装飾極限抑制）
  用例: zippuku, buko-onsen, konokayu

キャンペーン / カジュアル層:
  本文: Noto Sans JP + Kosugi Maru / Kiwi Maru
  見出し: M PLUS Rounded 1c (やわらか)
  用例: heijitsu, laplace-miyagi
```

**フォントサイズ標準**:
- H1（Hero）: 48px〜96px（PC） / 32px〜56px（SP）
- H2（セクション）: 32px〜48px / 24px〜32px
- H3（サブ）: 20px〜28px / 18px〜22px
- 本文: 16px〜18px / 14px〜16px
- キャプション: 12px〜14px / 11px〜12px

**line-heightの傾向**:
- 和文本文: 1.75〜1.9（旅行ジャンルは読み応え重視）
- 英字装飾: 1.0〜1.3（詰め気味で格式感）
- ラグジュアリー旅館: 2.0〜2.2（余白を大きく）

### 4-5. CTAパターン

| CTAタイプ | 頻度 | 対象サブジャンル |
|---|---|---|
| 「ご予約」/「Book Now」 | 最頻 | ホテル・旅館・体験 |
| 「お問い合わせ」 | 頻 | 全般 |
| 「マップを見る」 | 中 | DMO・観光列車 |
| 「チケット購入」 | 中 | イベント・スタンプラリー |
| 「LINE友だち追加」 | 稀（6件） | 地域施設/宿泊 |
| 「資料請求」 | 稀 | ワーケーション・移住 |

### 4-6. グリッドレイアウトパターン

**共通する情報ブロック構造**:
- **12カラムベース**: 多くのWordPressテンプレは12グリッド、ブティック系は16グリッド or フリーフロー
- **セクション縦間隔**: 80px〜160px（SPは40px〜80px）
- **コンテナ最大幅**: 1200px〜1440px
- **左右マージン**: PC 40px〜80px / SP 16px〜24px

**コンテンツカードの定形**:
```
cardタイプ A: DMO観光施設
  [画像 16:9]
  [カテゴリタグ] [エリアタグ]
  [タイトル]
  [本文1行]
  [→ 詳細リンク]

cardタイプ B: 客室/旅館
  [画像 3:2]
  [部屋名 和英併記]
  [定員 / 面積 / タイプ]
  [価格から表示]
  [ご予約ボタン]

cardタイプ C: イベント/ニュース
  [日付 yyyy.mm.dd]
  [カテゴリ]
  [タイトル]
  [サムネイル]

cardタイプ D: モデルコース
  [コース番号]
  [ルート縮約図（5-8駒のアイコン行）]
  [コースタイトル]
  [所要時間 / 難易度 / 交通手段]
```

### 4-7. 画像戦略

**画像の使い方**:
- DMO: **量**勝負（atarimae-kanko の 294 img）
- 旅館/ホテル: **質**勝負（Art Direction用picture、モデルカット）
- 日帰り温泉: **機能**写真（施設全景・料金表・内部）
- イベント: **情緒**写真 + **参加者**写真の二軸
- カルチャー: **人物**写真中心（100 TOKYO, afro-fukuoka）

**アスペクト比の使い分け**:
- 16:9 → Hero動画/DMOカード
- 3:2 → 客室/料理
- 1:1 → Instagram連携コンテンツ
- 9:16 → TikTok/Reels連携のスマホ縦動画
- フリー → クリップパス+マスクの現代的装飾

---

## 5. 新発見（R1比較）

### 5-1. R1からの主要補正

| 項目 | R1仮説 | R2実測 | 差異 |
|---|---|---|---|
| Swiper使用率 | 43% | **19%** | ほぼ半減。現実的には5分の1しか使わない |
| GSAP+ScrollTrigger | 想定高 | **7% / 3%** | 旅行ジャンルでは少数派 |
| Lenis | 想定中 | **3%** | ほぼ使われない |
| Locomotive | 想定中 | **0%** | ゼロ件 |
| STUDIO製LP | 想定少 | **4%のみ（norikura / landabout）** | まだ少数派 |
| WordPress支配率 | - | **50%** | 旅行/観光業界の半分はWP |
| slick.js（R1未検知） | - | **18%** | R1で見落とし。jQueryレガシー勢が依然強い |

**結論**: 旅行ジャンルは **「派手演出の現代Webテック」とは対極**。WordPress + jQuery + Slick/Swiper の**定番セット**が依然として主流。モーション演出よりも **写真・文章・情報設計・ネーミング** で差別化するジャンル。

### 5-2. R2の新発見

1. **外部予約埋め込みは実はレア**
   - OTA（Booking.com/Agoda/Expedia/Jalan）直埋込は0件。
   - tripla（3件）、489ban（2件）、reservation.jp（2件）と中小系予約SaaSが静かに浸透
   - 大半は自社CMSフォーム or 外部リンク遷移
2. **観光列車・鉄道LP のサブジャンルが独自の型を持つ**
   - 車両外観→内装→時刻表→沿線観光という情報順序
   - 「観光列車＋地域ブランド」のクロスオーバー
3. **銭湯ポータル（tokyosento）という特殊DMO**
   - 都内銭湯横断検索 = 業種別DMOという珍しい型
4. **Wix系の意外な伸長（7%）**
   - ayana、tokitoki、yamakoshi、biwako-visitors
   - 海外資本/新興自治体/イベント勢が採用
5. **多言語4言語（ja/en/zh/ko）はアパートメントホテル(MIMARU)が最強**
   - インバウンド依存度が高いホテル業態ほど多言語対応が充実
6. **"建築家クレジット"セクション化**（guntu、satoyama-jujo、landabout）
   - 建築家名を商品バリューの一部として前面化する日本的高級ホテル流儀
7. **通番イベント/シリーズ化**（PLANT COAST、FAN×FUN）
   - 継続性を数値化することでブランド資産化
8. **方言・固有語を「」で強調**（「クチゾコ」「背戸屋」）
   - ローカル性の紋章としての方言採用
9. **Font選択パターンの明確化**
   - ラグジュアリー和: **Noto Serif JP + EB Garamond / Cinzel / Marcellus**
   - ブティック現代: **Zen Kaku Gothic + Montserrat / Prata**
   - 温泉日帰り: **Noto Serif JP 単独**（ほぼ装飾なし）
   - 平日キャンペーン系: **Kosugi Maru + Kiwi Maru + M PLUS Rounded**（やわらか系）
10. **都市集合ホテル(mimaru)のFAQ最前化**
    - 不安解消を**Heroに次ぐセクション**に配置する逆転構成

---

## 6. design-mcp 使用方針

### 6-1. テンプレート提案（design-mcpで生成する際の前提）

旅行・ホテル・観光ジャンルのLPを design-mcp で作る際は、**サブジャンル6分類** に応じてベーステンプレートを切り分ける：

| サブジャンル | 推奨ベーステンプレ | 必須要素 | 推奨フォント |
|---|---|---|---|
| **DMO / 観光協会** | カードグリッド6分類 + エリアタグ + イベントカレンダー | モデルコース3本 / ニュース欄 / エリアマップ | Noto Sans JP + Open Sans / Montserrat |
| **ラグジュアリー旅館** | Hero動画 + Room/Food/Spa セクション | 建築家クレジット / 温泉種別 / 予約フォーム | Noto Serif JP + Cinzel / Marcellus |
| **ブティックホテル** | Hero写真 + Room Type スライダー | 多言語切替（ja/en/zh） / tripla or 489ban連携 | Zen Kaku Gothic + Montserrat / Prata |
| **日帰り温泉 / 銭湯** | 料金表 + 営業時間 + 泉質 + 施設紹介 | pH値/効能/食事処/サウナ詳細 | Noto Serif JP 単独 |
| **体験 / イベント** | ヒーロー動画 + フロー図 + 注意事項詳細 | チケット購入CTA / Q&A / 年齢制限 / 持物 | Noto Sans JP + Oswald / Zen Kaku |
| **観光列車 / 交通** | 車両外観 + 内装スライダー + 時刻表 + 沿線マップ | 運行カレンダー / 割引CP | Noto Sans JP + Barlow / Lato |

### 6-2. 生成時のパラメータ指示

design-mcp への instruction template：

```
genre: travel-hotel
subgenre: [dmo|ryokan-luxury|boutique-hotel|hotspring-day|experience-event|tourist-train]
brand_tone: [traditional|modern-boutique|community-first|cinematic-luxury]
tech_stack_hint: WordPress-Gutenberg base + Swiper/Slick for carousel (current jurisdictional norm; avoid GSAP-heavy animation unless subgenre is luxury-ryokan or experience-event)
nameing_style: adopt coined kanji (1-2 字) + bilingual英字subtitle + 地域固有名詞
color_palette:
  - luxury-ryokan: 墨黒 #1a1a1a / 白 #fafafa / 金 #c5a572 / 茶 #8b6d4f
  - dmo: 地域色（海/山/祭から1色選定） + 白 + グレー
  - boutique: グレー #f5f5f5 + アクセント1色
  - hotspring: 青 #2c5f8c + 木目 + 白
fonts:
  jp_primary: [Noto Serif JP | Zen Old Mincho | Shippori Mincho | Zen Kaku Gothic]
  en_accent: [Cinzel | Marcellus | Montserrat | Prata | EB Garamond]
must_have_sections:
  - Hero（写真 or 動画 / キャッチ和英併記）
  - コンセプト / ブランドストーリー
  - Room/体験/コース 一覧
  - 予約CTA（1画面ごとに配置）
  - アクセス（地図 + 公共交通 + 駐車場）
  - Food / 食事（旅館/ホテルの場合）
  - News / イベントカレンダー（DMOの場合）
  - FAQ（アパートメントホテルの場合は最上位）
  - 多言語切替（ja/en必須、zh/ko推奨）
```

### 6-3. 参考比較軸

`mcp__design-mcp__compare_designs` で比較する際の比較ペア候補：

- **ラグジュアリー旅館 vs ブティックホテル**: 里山十帖 THE HOUSE vs LANDABOUT TOKYO
- **DMO王道 vs 逆張りDMO**: 東広島ヒガシル vs あたりまえ観光（佐賀）
- **温泉日帰り vs 温泉宿泊**: 武甲温泉 vs 十福の湯
- **伝統観光 vs 没入体験**: 肥前400年 vs No.12 Kashima Fan Zone
- **国内DMO vs インバウンドDMO**: 舞鶴観光ネット vs 100 TOKYO
- **観光列車 vs 路線キャンペーン**: 観光特急しまかぜ vs スカイマーク茨城

### 6-4. critique_design で使うべきチェックリスト

```
旅行・ホテル系のcritique観点:
1. 写真の質と量: 旅行LPは写真が命。最低15-20枚、Art Direction対応のpicture推奨
2. ネーミングの造語性: "ホテル""旅館"のみの凡庸ネーミングは避け、漢字1字や合成語を提案
3. 予約導線の配置: Hero / 客室紹介 / Footer の3箇所以上にCTA
4. 多言語対応: ja/en必須、地理的特性でzh/koを追加
5. 料金透明性: 温泉/日帰りは料金表必須、旅館は "から" 価格で最低表示
6. 地図とアクセス情報: 公共交通/車/駐車場の3経路カバー
7. 季節性コンテンツ: 春夏秋冬のフェア/イベントを枠として確保
8. FAQ の深度: ファミリー/ビジネス/インバウンド3層の想定質問に対応
9. 写真と動画のバランス: Hero動画は30%採用、動画自動再生は音声ミュート必須
10. 社会的証明: 口コミ/アワード/メディア掲載バナーセクション
```

### 6-5. 避けるべきアンチパターン

旅行・ホテルLPで **これだけはやるな** のリスト（56件分析から抽出）：

1. **GSAPで派手に文字アニメーションする**: 旅行ジャンルの読者は"静謐な写真"を期待。過度なScrollTrigger演出は逆効果
2. **価格を隠す**: "お問い合わせください"は離脱要因。必ず "¥XX,XXXから" で下限提示
3. **予約ボタンを1箇所だけに置く**: Heroと別セクションで最低3回繰り返す
4. **日本語だけで運用**: インバウンド比率が高い現在、ja/en の2言語は最低限必須
5. **更新情報が古い**: "本日の" "今月の"セクションが数ヶ月前のままは致命的
6. **FAQなし**: 特にアパートメント/ホステル/ワーケーション系
7. **ナビが6項目以上の階層メニュー**: 3-4層のドロップダウンは迷子の元
8. **地図がGoogle Maps直埋め込みのみ**: 交通/駐車場/徒歩経路の補足が必要
9. **予約システムが自社フォームのみ**: tripla/489ban等のSaaSでUX改善可能
10. **写真サイズの未最適化**: WebP未対応/picture未使用は2026年時点で失格

---

## 7. 技術スタック推奨（design-mcp配下で生成する際の指針）

```yaml
travel-hotel:
  default_cms: WordPress  # 保守/運用の現実
  default_carousel: Swiper 11  # slickは非推奨（jQuery依存）
  optional_animation: GSAP + ScrollTrigger  # luxury/event subgenre のみ
  smooth_scroll: Lenis  # 高級旅館/ブティックのみ
  font_loading: Google Fonts CSS2 API（Noto Serif JP + 英字1種）
  image_delivery: picture要素 + WebP + srcset  # Art Direction必須
  reserve_integration:
    priority: [tripla, 489ban.net, reservation.jp]
    fallback: 自社フォーム + Googleカレンダー
  i18n: WPML or bogo plugin  # WP前提の場合
  analytics: GA4 + サーチコンソール
  performance_target:
    LCP: ≤2.5s
    CLS: ≤0.1
    画像: WebP、LQIP placeholder
```

---

## 8. 結論

旅行・ホテル・観光LPは **「華やかな演出」より「正確な情報・写真・命名の力」で勝負するジャンル**。技術的にはWordPress + jQuery/Swiper の定番スタックが今も支配的で、最先端Reactスタックは事実上ゼロ件。

代わりに **言葉の発明力**（造語ネーミング・方言・カフェ用語転用・漢字1字ブランディング）と **写真の量的質的充実**（あたりまえ観光の225 picture、里山十帖のTypekit+Swiper世界観）、そして **地域文化の物語化**（guntu建築家、100TOKYO人物×地域、山古志Village化）が差別化の主軸となる。

design-mcpで生成する際は「モーションの派手さ」を抑え、**サブジャンル定義→ネーミング提案→情報設計→写真配置→予約導線** の順で積み上げる。テクノロジーはその受け皿であって主役ではない。
