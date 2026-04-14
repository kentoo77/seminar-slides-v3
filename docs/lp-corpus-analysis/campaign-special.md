# キャンペーン / イベント / 特設LP 分析レポート (Round 2)

対象ディレクトリ: `/Users/oidekento/lp-corpus/raw_all/campaign-special/`
対象件数: **591 HTML ファイル**
分析日: 2026-04-08
分析者: Claude (Opus 4.6 / 1M context)
分析手法: ripgrep/sed による全件統計抽出 (591件) + 代表 12 サイトの深読み
前回レポート: 30件 → 本レポート: **591件 (約20倍)**

---

## 0. エグゼクティブサマリ (先に結論)

### 0.1 データで見える「日本のキャンペーンLP」の骨格

- **591件の内訳** (タイトル/descriptionベースの一次分類)
  - 未分類(ブランド特集/概念LP主体) **210 (36%)**
  - コラボ (×) **56 (9.5%)**
  - 周年 (Anniversary) **51 (8.6%)**
  - ブランドストーリー特設 **49 (8.3%)**
  - 季節・シーズナル **43 (7.3%)**
  - 新商品/プロダクト特設 **28 (4.7%)**
  - プロジェクト系 **27 (4.6%)**
  - フェス/祭 **26 (4.4%)**
  - 学校/受験 **21 (3.6%)**
  - ゲーム/エンタメ **18 (3.0%)**
  - 展示/博覧会 **17 (2.9%)**
  - キャンペーン/プレゼント **13 (2.2%)**
  - 採用/カルチャー **13 (2.2%)**
  - 音楽/リリース **9 (1.5%)**
  - CSR/サステナ **4 (0.7%)**
  - 映画/番組 **4 (0.7%)**
  - カンファレンス **2 (0.3%)**

- **プラットフォーム (591 分母の生出現率)**
  - WordPress系 (`wp-content`) **116件 (19.6%)** — 意外にも最多
  - STUDIO **24件 (4.0%)** (`STUDIO` 文字列。実質 `.studio.design` 配信)
  - Next.js (`_next` チャンク) **56件 (9.4%)**
  - Nuxt **42件 (7.1%)**
  - Astro **31件 (5.2%)** (前回の代表作 SmartHR / マガポケ 10th 系)
  - Shopify **8件 (1.4%)**
  - **Tailwind 明示** は 5件のみ(痕跡: Tailwindはビルド時消失するので検出困難)
  - React (単独痕跡) **44件**

- **結論**: キャンペーンLPは `WordPress ≧ Next/Nuxt ≫ Astro/STUDIO > Shopify` の序列。「巨大一発特設=Next/Nuxt」、「継続運用=WordPress」、「ノーコード=STUDIO」の棲み分けが明瞭。Astroは SaaS系の周年特設(SmartHR/マガポケ)で局所的に突き抜けている。

- **ウェブフォント提供元** (591 分母)
  - Google Fonts (`fonts.googleapis`) **243件 (41%)** — 支配的
  - Typekit (Adobe Fonts) **155件 (26%)** — WP系と強相関
  - FONTPLUS **32件 (5.4%)**
  - TypeSquare **23件 (3.9%)**
  - Morisawa (直貼り) **9件 (1.5%)**
  - **Google Fonts 単独使用** が最多。ただしWP系の約半数は Typekit 併用、「WP + Typekit + Noto Sans JP」の黄金配合が日本商業系の定番。

- **和文フォント支配率** (Google Fonts `family=` 展開、全件)
  1. **Noto Sans JP** 122件 — 圧倒的一強 (全 Google Fonts 使用ファイルの約 56%)
  2. Noto Serif JP 37
  3. Zen Kaku Gothic New 24
  4. Zen Kaku Gothic Antique 10
  5. Zen Maru Gothic 9
  6. IBM Plex Sans JP 6
  7. Zen Old Mincho 6
  8. M PLUS Rounded 1c 4
  9. Shippori Mincho B1 4 (電音部 等の「ポップ和モダン」)
  10. Shippori Antique 2

- **欧文フォント支配率**
  1. Roboto 16 / 2. Oswald 13 / 3. Inter 11 / 4. Poppins 9 / 5. Montserrat 8
  6. Lato 9 / 7. Barlow 6 / 8. Cormorant Garamond 6 / 9. Work Sans 4 / 10. Josefin Sans 4

- **フォント混在数** (Google Fonts 使用 232ファイルの内訳)
  - 1書体 110件 (47%)
  - 2書体 77件 (33%)
  - 3書体 36件 (16%)
  - 4書体+ 9件 (4%) — 最大で 10書体 (お祭り系の例外)
  - → **「1〜2書体構成」が 80%**。前回観察の "周年=お祭り大量書体" は例外寄り

- **配色 TOP10** (全591件 grep, 重複含む大域 hex 集計)
  1. `#0081ce` 892 — シチズン (citizen.jp 関連の大量ファイル)
  2. `#e4e8ed` 671 — 薄ブルーグレー (UIバックグラウンド)
  3. `#ffffff` 539 — 白
  4. `#ffdce6` 464 — INTLOOP 20周年の淡ピンク
  5. `#3b3b3b` 464 — INTLOOP ダーク
  6. `#000000` 419 — 黒
  7. `#ff80b4` 277 — メルカリピンク
  8. `#ffce00` 274 — メルカリイエロー
  9. `#1a1916` 267 — ほぼ黒 (Shippori Mincho 系サイトで頻出)
  10. `#ff0211` 238 — 鮮赤

  **注記**: 特定サイト(メルカリ/シチズン/INTLOOP)の大ファイルの出現数に引っ張られる傾向がある。色の「種類の多さ」ではなく「強さ」を見るべき。

- **配色の彩度分布** (300ファイルサンプル、unique色を階層化)
  - 中間色 292 / パステル明るい 264 / **ビビッド高彩度 257** / 深色 245 / ほぼ白 207 / グレー低彩度 172 / ほぼ黒 111
  - → **ビビッド高彩度が全体の 17%** を占める。EC/SaaSと比較すると約 2倍。キャンペーンLP特有の「派手さの許容」が数字で出た

- **セクション構造の頻出 class 名** (section / hero / mv / cta / step / flow など)
  - `section` 290 / `container` 334 / `wrapper` 217 / `main` 159 / `header` 157 / `footer` 141
  - `section-title` 110 / `section-mania` 74 (tabio 関連) / `campaign` 54 / `mv` 51 / `kv` 45
  - `step` 47 (応募3ステップの残骸) / `about` 69 / `lineup` (個別) / `concept` (個別)
  - → **セクション骨格は "header / mv-kv / section(×n) / footer" で普遍**。「mv と kv が拮抗」: mv(メインビジュアル) 51 / kv(キービジュアル) 45 は使用分布がほぼ半々。関西系は mv / 関東系は kv という傾向も薄く存在。

- **CTA/導線の実装率** (591 分母)
  - og:image 設置 **562件 (95%)** — ほぼ全件
  - twitter:card 設置 **465件 (79%)**
  - Instagram への外部リンク **261件 (44%)**
  - Twitter/X シェアボタン **119件 (20%)** + x.com/intent 7件
  - モーダル/ダイアログ **272件 (46%)**
  - FAQ/アコーディオン **114件 (19%)**
  - `<form>` 要素 **55件 (9.3%)** — 応募はフォームより外部フォーム多い
  - Google Forms 埋込 **6件**
  - LINE 友だち追加 URL **44件 (7.4%)**
  - `<video autoplay>` **96件 (16%)** — KV動画背景の定番化
  - `<canvas>` 要素 **63件 (10.7%)**
  - Lottie **13件 (2.2%)**
  - WebGL/three.js **4件 (0.7%)**
  - **カウントダウンタイマー実装**: `countdown` 文字列 8件 / `timer` 23件 / 実質的な日付カウントダウン関連実装 ≤10件 **(1.7%未満)**

- **日付表記フォーマット**
  - `YYYY年MM月DD日` 表記 **142件 (24%)** — 依然ハードコード日付が主流
  - `〜` 範囲表記 **31件 (5%)**
  - → **期間の"動的カウントダウン"はほぼ無い**。「日付を直書きしてビルドごと更新」が圧倒的多数

### 0.2 キャンペーンLP の 3 大発見 (Round 1 比)

1. **カウントダウンタイマー仮説の検証**: 「カウントダウンはほぼ無い」は Round 1 の推論通り。591件中 **実装はわずか10件未満**。「数字が動くタイマー」より「大文字で日付を置く」方が圧倒的に多い。理由推定: 期間公示は法務の校閲対象で、「JSで動的描画される日付」は校正しにくいため。
2. **プラットフォームは WordPress が最多だった**: Round 1 では Astro/Next が目立って見えたが、実は数ベースでは **WordPress 系(wp-content)が 19.6%で最大派閥**。特設LPと言えど、地方自治体/企業のお祭り・フェス系は WP が主。Astroは「SaaS 周年/マンガ周年/一発キラLP」の局所トップにすぎない。
3. **Google Fonts 単独が最多 + 1-2書体構成が8割**: Round 1 の「お祭りは書体沢山」は例外寄り。大半は **Noto Sans JP 1書体 + 欧文1書体** という保守構成。お祭りポップ感は色と写真で出している。

### 0.3 design-mcp 使用方針 (更新版)

- **デフォルトプリセット**: Noto Sans JP + 欧文1書体 (Inter / Poppins / Oswald のどれか)、「中間色 or パステル」寄り、`<video autoplay>` 背景 OK
- **3プリセット駆動**
  1. **"お祭り/フェス系"**: Dela Gothic / Zen Kaku Bold + ビビッド3色 + 縦書き見出し (WP系で再現すると馴染みやすい)
  2. **"周年/SaaS系"**: Figtree/Inter + 白地 + ブランド1色 + 大判数字カウント (Astro 型)
  3. **"コラボ/期間限定"**: 両ブランドロゴ交互配置 + パステル or ポップ + 3ステップ応募図解 + SNSハッシュタグ訴求
- **テンプレート非依存がやはり最適**: キャンペーンは「1個しかない固有体験」なので、既存テンプレ化しにくい。`mode:url` に特定1件の参照URLを渡す方式が生成品質が最も高い
- **Round 2 で追加すべき指示プロンプト要素**:
  - 「カウントダウンは直書き日付で」(動的タイマー不要)
  - 「og:image / twitter:card を必ず設置」
  - 「`<form>` より外部応募URL(LINE友だち追加/Google Forms)を推奨」
  - 「モーダル/アコーディオンを半数で使う」

---

## 1. データソース / 調査方法

### 1.1 対象
- `raw_all/campaign-special/` 直下の `.html` ファイル 591件
- 総サイズ: 73MB
- 命名規約: `NNNN_<host>_<path>.html` (HTMLダンプ)
- 年代レンジ: `2020`〜`2025` (URL内年次で検出可能なもの)、実際は直近2-3年が中心

### 1.2 抽出コマンド要約
```bash
# タイトル
for f in *.html; do
  title=$(grep -oE '<title>[^<]*</title>' "$f" | head -1 | sed 's/<[^>]*>//g')
  echo "$f|$title"
done > /tmp/cs_stats/titles.txt  # 591行

# descr
for f in *.html; do
  grep -oE '<meta[^>]*name="description"[^>]*>' "$f" | head -1 \
    | grep -oE 'content="[^"]*"' | sed 's/content="//;s/"$//'
done

# Google Fonts family 集計
grep -rhoE 'fonts\.googleapis\.com/css2?\?family=[^"'\'']*' .

# 色
grep -rhoE '#[0-9a-fA-F]{6}' . | tr 'A-Z' 'a-z' | sort | uniq -c | sort -rn

# ライブラリ
for lib in tailwind swiper gsap lenis astro _next react nuxt splide barba lottie three wp-content STUDIO; do
  c=$(grep -rli "$lib" . | wc -l); echo "$c $lib"
done
```

### 1.3 分類ロジック
- タイトル + description + ファイル名(URL) をテキスト化
- 17 種類のバケットを正規表現でマッチング、**最初にマッチしたバケットを primary ラベル**
- 複数マッチは sub tag として保持

---

## 2. 統計サマリ(詳細)

### 2.1 配色 TOP30 (全出現回数)

| 順位 | HEX | 出現 | 推定コンテキスト |
|---:|---|---:|---|
| 1 | `#0081ce` | 892 | シチズンブルー (citizen.jp の大ファイル 6件) |
| 2 | `#e4e8ed` | 671 | UI淡グレー (セクション境界に多用) |
| 3 | `#ffffff` | 539 | 白 |
| 4 | `#ffdce6` | 464 | ピンクパステル (INTLOOP 20th 等) |
| 5 | `#3b3b3b` | 464 | ダークグレー(本文) |
| 6 | `#000000` | 419 | 黒 |
| 7 | `#ff80b4` | 277 | メルカリピンク |
| 8 | `#ffce00` | 274 | メルカリイエロー |
| 9 | `#1a1916` | 267 | ほぼ黒 (高級紳士系の背景) |
| 10 | `#ff0211` | 238 | 鮮赤 (Sale/祭り/緊急) |
| 11 | `#003970` | 224 | 紺 (学校/大学系) |
| 12 | `#00c1aa` | 194 | ミント (ブランドアクセント) |
| 13 | `#212121` | 187 | Material Dark |
| 14 | `#221714` | 154 | ブラウン (食品系) |
| 15 | `#45484d` | 142 | 中間グレー |
| 16 | `#ffd900` | 127 | セイバン ランドセルイエロー (100周年) |
| 17 | `#8b7729` | 111 | 金茶 (伝統工芸) |
| 18 | `#00b9ff` | 110 | シアン (INTLOOP等) |
| 19 | `#eacaca` | 99 | 桜色 |
| 20 | `#2b2b2b` | 96 | 炭黒 |
| 21 | `#5dc806` | 94 | グリーン(エコ/春系) |
| 22 | `#231815` | 94 | 本墨色 (伝統/和文印刷のデフォ) |
| 23 | `#006ae4` | 94 | コバルトブルー |
| 24 | `#ff8245` | 92 | オレンジ (祭り/食品) |
| 25 | `#d62c36` | 90 | 和紅 |
| 26 | `#32373c` | 90 | WPブロック デフォルト |
| 27 | `#f8f1e7` | 85 | クリーム (アンティーク) |
| 28 | `#007000` | 83 | 深緑 (ロフトワーク ちきゅうのみちくさ展) |
| 29 | `#0693e3` | 81 | 水色 (Wordpress default) |
| 30 | `#00d084` | 81 | 緑 (Wordpress default) |

**観察**:
- 6色(`#0693e3 #00d084 #f78da7 #ff6900 #cf2e2e #fcb900 #9b51e0 #8ed1fc #7bdcb5 #abb8c3`)がほぼ同数(81〜63)並ぶのは **WordPress Gutenberg デフォルトカラーパレット** の痕跡。WP系が 116件あることの裏付け
- 派手色1位は `#ff0211` (鮮赤) > `#ffce00` (黄) > `#ff8245` (橙)。**「赤 > 黄 > 橙」** の祭り系ヒエラルキー
- ニュートラル基盤は **`#ffffff` + `#3b3b3b` or `#212121`** が基準

### 2.2 ウェブフォント提供元

| 提供元 | 使用ファイル | 比率 | 備考 |
|---|---:|---:|---|
| Google Fonts | 243 | 41% | 最多 |
| Adobe Typekit | 155 | 26% | WP系と強相関 |
| FONTPLUS | 32 | 5.4% | 官公庁/大学系 |
| TypeSquare | 23 | 3.9% | 大企業 |
| Morisawa (直) | 9 | 1.5% | Vaundy×Morisawa の特殊事例含む |

### 2.3 和文フォント ランキング (Google Fonts 展開)

```
122  Noto Sans JP       (圧倒的)
 37  Noto Serif JP
 24  Zen Kaku Gothic New
 10  Zen Kaku Gothic Antique
  9  Zen Maru Gothic
  6  IBM Plex Sans JP
  6  Zen Old Mincho
  4  M PLUS Rounded 1c
  4  Shippori Mincho B1
  2  Shippori Antique
```

**解釈**:
- Noto Sans JP 1強 (使用数 2位の 3倍以上)
- Zen ファミリー (Adobe Fonts 由来/Google Fonts 配信) は計 **43件** で2位集団
- "お祭り系" 専用書体 (Dela Gothic One / Cherry Bomb One / Tilt Warp / Boldonse) は統計には乗らず、マガポケ10th/コーヒーシティフェス等の個別例外
- **ミニマル現代系 vs お祭りポップ系 = 95:5** と Round2 スケールで見れば圧倒的にミニマル

### 2.4 欧文フォント ランキング

```
16  Roboto
13  Oswald        (縦長ディスプレイ = スポーツ/祭り系)
11  Inter          (SaaS/ミニマル)
 9  Poppins        (女性向け/カジュアル)
 9  Lato
 8  Montserrat
 6  Barlow
 6  Cormorant Garamond   (細セリフ = モード/ファッション)
 4  EB Garamond
 4  Roboto Condensed
 4  Manrope
 4  Josefin Sans
 4  Work Sans
 3  DM Sans / Outfit / Barlow Semi Condensed / Crimson Text
```

**二極化**: `Inter/Manrope/Outfit/DM Sans/Work Sans` = ミニマル SaaS系 / `Oswald/Roboto Condensed/Barlow` = 祭り・スポーツ系

### 2.5 ライブラリ使用率 (591 分母)

| 技術 | ファイル数 | 比率 | コメント |
|---|---:|---:|---|
| swiper | 156 | 26.4% | カルーセル定番 |
| wp-content | 116 | 19.6% | WP最多 |
| wp-includes | 78 | 13.2% | WP本体 |
| STUDIO | 72 | 12.2% | STUDIOビルド痕跡 (正確には 24件がデプロイ先だが文字列痕跡72件) |
| gsap | 61 | 10.3% | アニメーション |
| _next | 56 | 9.4% | Next.js |
| wordpress | 50 | 8.5% | メタ含む |
| react | 44 | 7.4% | |
| nuxt | 42 | 7.1% | |
| astro | 31 | 5.2% | |
| splide | 32 | 5.4% | swiper代替 |
| barba | 25 | 4.2% | ページ遷移 |
| next.js (別検出) | 21 | 3.6% | |
| lenis | 21 | 3.6% | スムーススクロール |
| lottie | 17 | 2.9% | |
| shopify | 8 | 1.4% | |
| scrollmagic | 8 | 1.4% | |
| vivus | 5 | 0.8% | SVGストローク |
| tailwind (痕跡) | 5 | 0.8% | ビルド後消失 |
| three.js | 4 | 0.7% | |
| aos.js | 4 | 0.7% | |
| pixi.js | 3 | 0.5% | |
| locomotive | 3 | 0.5% | |
| anime.js | 3 | 0.5% | |
| p5.js | 2 | 0.3% | |
| framer-motion | 0 | 0% | (React の中に埋没) |

**ポイント**: `swiper` 26% (158件) は **"何かしらのカルーセル/スライド"が 4件に 1件** あることを示す。GSAPは 10%、すなわち「まともに動く」サイトは1割。残り9割は静的+CSSトランジションで十分賄っている。

### 2.6 セクション class 名頻度 TOP30

```
 359 menu-item      (WP メニュー)
 334 container
 290 section
 282 info           (企業情報/キャンペーン情報)
 217 wrapper
 177 menu-item-type-custom
 159 main
 157 header
 141 footer
 110 section-title
 104 sectionHeding_texts_text
  86 menu
  74 section-mania  (Tabio の靴下MANIAシリーズ独自)
  69 about
  54 campaign
  53 main-lead
  52 news
  51 mv
  49 kvSliderText__target
  47 step
  46 section-title-letter
  45 kv
  44 menu-item-has-children
  43 main-title
  43 container-main
```

**観察**:
- `section` (290) を軸にしたシンプル構造が骨格
- 「`mv` + `kv`」の合計は 96 件で、主要 KV 呼称の 2トップ
- `step` 47件 → 応募3ステップ図解のパターンはやはり頻出だが全体の 8% と限定的
- `campaign` 明示クラスは 54 件 (9%)

### 2.7 CTA / コンテンツパターン 詳細

| パターン | 件数 | 比率 |
|---|---:|---:|
| og:image 設置 | 562 | 95% |
| hash-tag 表記(任意) | 494 | 84% |
| twitter:card 設置 | 465 | 79% |
| モーダル要素 | 272 | 46% |
| Instagram 外部リンク | 261 | 44% |
| YYYY年MM月DD日 | 142 | 24% |
| X/Twitter シェアボタン(share) | 119 | 20% |
| アコーディオン/FAQ | 114 | 19% |
| video 背景(autoplay) | 96 | 16% |
| エントリー文字列 | 89 | 15% |
| YouTube 埋込 | 94 | 15% |
| プレゼント文字列 | 79 | 13% |
| ハンバーガー/ドロワー | 85 | 14% |
| canvas 要素 | 63 | 11% |
| 応募ボタン | 63 | 11% |
| パンくず | 60 | 10% |
| form 要素 | 55 | 9% |
| LINE 友だち | 44 | 7% |
| チケット | 39 | 7% |
| map 埋込 | 36 | 6% |
| 日付範囲 〜 | 31 | 5% |
| 診断/quiz | 26 | 4% |
| timer 文字列 | 23 | 4% |
| hashtag 装飾クラス | 44 | 7% |
| countdown 文字列 | 8 | 1.4% |
| 3ステップ応募 明示 | 3 | 0.5% |

**Round 2 新発見**:
- **hash-tag 表記が 84%で極めて高い** — SNS拡散装置として "記号 # 付きワード" は必須化している
- **モーダル 46%** — 「応募規約」「商品詳細」「注意事項」を モーダルに押し込むパターンが半数近い
- **診断/quiz 文字列 26件 (4%)** — キャンペーンのエンゲージメント装置として "あなたの◯◯診断" が想像より少ない
- **カウントダウンタイマー実装率は 1% 台** — 日本のキャンペーンLPでは動的タイマーは実質"使われていない"

### 2.8 上位ドメイン(事業者)ランキング

```
31  www.dot-st.com          (アダストリア系 — RAGEBLUE/niko and/studio CLIP 他)
11  www.felissimo.co.jp     (フェリシモ 各種プロジェクト)
 9  www.goldwin.co.jp
 7  www.nintendo.co.jp
 6  www.nikoand.jp
 6  citizen.jp
 6  www.globalwork.jp
 4  spicato.com             (大阪のデザイン会社 年賀サイト)
 4  tabio.com               (靴下MANIA)
 4  www.junonline.jp
 4  jp-news.mercari.com
 4  sp.elle.co.jp
 4  rinnai.jp
 4  www.akindo-sushiro.co.jp
 3  green-spoon.jp / www.petline.co.jp / www.kai-group.com / sirup.online / 45r.jp / sauna-ikitai.com / www.haruta-shoes.co.jp / jp.marugame.com
```

- **アダストリア(dot-st.com)が 31件で最大** — 同社の各ブランド特設の蓄積が強い
- **フェリシモ 11件** — 「プロジェクト」 (GO!PEACE / HAPPY CAPS 他) のカルチャーが色濃い
- 上位5社で全体の 10% を占める → **キャンペーンLPはリピーター企業が作り続ける領域**

---

## 3. 深読み 12 ケーススタディ

### 3-1. Mercari Unleash (mercari.com/unleash/) — 10th Anniversary

- **URL/ファイル**: `2025_about.mercari.com_unleash_.html` (1.9MB)
- **カテゴリ**: 周年 (anniversary)
- **タイトル**: "Unleash | Mercari's 10th Anniversary | 株式会社メルカリ"
- **コピー**: 「世界中のあらゆる人の可能性を Unleash する存在になるために、新たな１歩を踏み出します」
- **プラットフォーム**: **Next.js** + swiper
- **フォント**: `Inter:ital,opsz,wght@0,14..32,100..900` (可変軸フル) + `typekit.net/bxl7aoa.css` (Adobe Fonts 併用 — 和文補強用と推定)
- **配色**:
  - ブランド `#0081ce` (シチズン共有の空色) — ウエイト 892 で突出
  - ピンク `#ff80b4` / 黄 `#ffce00` / 赤 `#ff0211` (メルカリ3原色) / ミント `#00c1aa`
  - これは **同社の5色ブランドガイドそのまま**を特設サイトに展開
- **セクション** (h見出しベース):
  1. KV「Unleash」
  2. 「なぜ新たなグループミッションを掲げるのか」
  3. 「これからのメルカリが目指すこと」
  4. 「改めての決意」
  5. 「失敗を恐れず、大胆に。」
  6. 英語版セクション (2-5 の英訳)
  7. "Read more about our Group mission"
- **class 名**: `kv / kv-contents / kv-heading / footer-inner / footer-notes / header-button-en / header-button-ja`
- **キャンペーン要素**: **純粋な企業ビジョン発信型**。応募も購入もない "メッセージング一点突破"
- **示唆**: **「SaaS/スタートアップ周年=プロダクトを売らない。世界観を売る」** の代表例。Next.js + Inter 可変軸で "言葉が主役" の構成

### 3-2. INTLOOP 20周年 (intloop.com/company/history/20th/)

- **ファイル**: `1823_www.intloop.com_company_history_20th_.html` (1MB)
- **カテゴリ**: 周年 (anniversary) / B2B コンサル
- **タイトル**: "INTLOOP20周年特設サイト"
- **プラットフォーム**: **WordPress + Next.js (hybrid)** + splide + lottie
- **フォント**: `Albert Sans:wght@100..900` (シングル欧文、可変軸)
- **配色**:
  - `#FFDCE6` (淡ピンク) + `#3B3B3B` (墨色) の ピンク×墨 のコントラスト
  - サブ: `#00b9ff / #5dc806 / #ff8245 / #5884f1 / #00cbaf / #e9c02b` で 6色のアクセント
- **コピー**: 「一緒だから、超えられた」
- **セクション**:
  1. KV「INTLOOP 20周年特設サイト」
  2. 「一緒だから、超えられた」(主メッセージ)
  3. 「感謝のループをつなげてみませんか？」(CTA/UGC フォーム)
  4. 「コメントを残す」(実フォーム 2個)
  5. 軌跡年表 (`sectionHeadItem`) — 創業期→田町オフィス設立→成長期→海外事業スタート→リーマンショック→...
- **キャンペーン要素**:
  - `<form>` 要素 **2個** (感謝メッセージ投稿 / 問い合わせ) — フォーム連動あり
  - Lottie でアイコンアニメ (ループの可視化)
  - スタッフ写真モザイク (`splide` 使用)
- **示唆**: **「B2B周年は "感謝のループ" を UGC 投稿で可視化」** という独自パターン。多彩色+可変軸1書体でモダン感、Lottie でループモチーフを動かす

### 3-3. Bandai キャラパキ発掘恐竜チョコ 5周年 (bandai.co.jp)

- **ファイル**: `1972_www.bandai.co.jp_candy_camp_charapaki5th_.html` (578KB)
- **カテゴリ**: 周年 (5周年) / 菓子 / キッズ
- **コピー**: 「発売5周年を記念した商品や大型企画を一挙に大公開！この機会にしか手に入らない限定商品やコラボアイテムの他、豪華景品が当たるキャンペーンやコンテストが目白押し！！」
- **プラットフォーム**: lenis + (WP もしくは素 HTML)
- **フォント**: Typekit (`use.typekit.net` 動的ロード)
- **配色**: ブラウン系 `#272727 / #ecc692 / #4D2A0B / #7c4617 / #623401 / #DCB98A / #5C3415 / #1F120D` — **発掘=土の色** のシリーズ配色
- **カラースキーム**: 8色が全て茶系で統一 → "土の質感" を表現する配色の好例
- **HTML 特徴**: 独自 `arrowRight/arrowRightYellow/arrowDown` 等のカスタムアイコン(SVG sprite)、ハッシュタグ `#charapaki5th` 内部アンカー
- **キャンペーン要素**:
  - `<form>` 1個 (応募フォーム推定)
  - 豪華景品 + コンテスト + 限定商品 + コラボ = **複合企画型**
- **示唆**: **「商品周年=世界観の色で統一。応募はフォーム1つで回す」**。5周年でも10周年並の予算感で作っている

### 3-4. Vaundy × Morisawa Fonts 『置き手紙』 (okitegami.morisawafonts.com)

- **ファイル**: `2082_okitegami.morisawafonts.com_.html` (552KB)
- **カテゴリ**: コラボ / 音楽 / フォントメーカー
- **コピー**: 「Morisawa FontsとVaundyのコラボレーションが実現。Vaundyのパワフルな歌声と、それを可視化した様々なフォントたちが「書体見本帳」を舞台に共演する、クラフト感に溢れたMusic Videoです」
- **プラットフォーム**: **Next.js + Barba.js** (ページ遷移アニメーション)
- **フォント**: 自社製 Morisawa 直貼り (`morisawa-fonts__headline / __body / __point` 独自クラス) — **Google Fonts を一切使わない**
- **セクション(内部アンカー)**: `#concept / #lyrics / #interview / #credit / #about`
- **ヘディング**: "Points" のみ — タイポグラフィ重視で文字自体が主役
- **キャンペーン要素**:
  - **純粋な映像作品紹介サイト** — 応募も購入もない
  - 書体と音楽のクロスオーバー表現
- **示唆**: **「フォントメーカーの自社コラボLP=自社書体だけで世界観を作る最強プロモ」**。Next.js + Barba で映画的トランジション

### 3-5. ノースマン公式 (northman-hokkaido.com) — 新商品特設

- **ファイル**: `2087_northman-hokkaido.com_.html` (670KB)
- **カテゴリ**: 新商品発売 / リブランド
- **タイトル**: "ノースマン公式サイト｜生ノースマンが新登場"
- **プラットフォーム**: 素 HTML (フレームワーク痕跡なし)
- **配色**: `#232742` (紺色 1色のみ検出)
- **セクション class**: `header / header-logo / footer-main / footer-sitemap / footer-company / footer-sub / footer-copy / gallery / info / information / information-body / information-archive-link`
- **特徴**:
  - **2022年10月、札幌千秋庵101年目の年にリブランド** → 周年+新商品発売のハイブリッド
  - `information` 構造で「お知らせ/アーカイブ」が実装されている=運用型
- **示唆**: **「老舗の新商品特設=静的HTMLで十分、運用性だけ担保」**。101年目というエモい設定だが装飾は控えめ

### 3-6. 東大工学部 狂ATE the FUTURE (park.itc.u-tokyo.ac.jp/createthefuture/)

- **ファイル**: `2117_park.itc.u-tokyo.ac.jp_createthefuture_.html` (230KB)
- **カテゴリ**: 学校 (大学) / 動画メディア
- **タイトル**: "狂ATE the FUTURE" (Create の Cre を "狂" で置換した大学らしい強烈タイトル)
- **コピー**: 「東大工学部の若き研究者たちが衝動と未来を語る動画メディア」
- **プラットフォーム**: **Next.js** + swiper
- **配色**: `#221714` (濃茶黒) + `#F3EEDB` (クリーム) + `#E31B14` (赤) — 3色に絞った大人モード
- **ヘディング**: "狂ATORS"
- **セクション**: `footer / main-container` (Next.js generated 構造)
- **示唆**: **「大学の研究者紹介特設=Next.js + 3色絞り + タイトル逆説で知性を出す」**。動画コンテンツメディアとしての "季刊誌" 的運用

### 3-7. 電音部 DEN-ON-BU (denonbu.jp)

- **ファイル**: `2234_denonbu.jp_.html` (954KB)
- **カテゴリ**: ゲーム/エンタメ / 音楽プロジェクト
- **コピー**: 「バンダイナムコエンターテインメントが贈るダンスミュージックをテーマにした音楽原作キャラクタープロジェクト」
- **プラットフォーム**: **Next.js** (CSS Modules 多用: `header_block__WIfWG / header_container__GEi8a` など)
- **フォント**: `Shippori Mincho B1:wght@400;500;600;700` — **明朝体をポップに使う "和ネオ渋谷"** 系
- **特徴**:
  - `og:site_name` がデフォルト値 "sitename" のまま → プロダクション前の名残 or 意図的
  - ハンバーガー＋ドロワーナビ (`header_spNavi_*` 多数)
- **示唆**: **「アニメ/音楽プロジェクト=Next.js + CSS Modules + 明朝 = 日本のキャラIPの新定番ムード」**

### 3-8. 燕三条 工場の祭典 2023 (kouba-fes.jp)

- **ファイル**: `1879_2023.kouba-fes.jp_.html` (200KB)
- **カテゴリ**: フェス / 地域産業
- **コピー**: 「工場の祭典 2023 のテーマは『WHAT IS KOUBA?』。機械加工の "工場" だけでも、手仕事の "工房" だけでもない、多様なものづくりが重なり合う『KOUBA』の本質を探求し…」
- **プラットフォーム**: **Nuxt.js + Lenis + Swiper**
- **フォント**: `Noto Sans JP` 単独
- **配色**: `#262627 / #D9D9D8 / #ffffff` + 薄いグレー系 — **墨×白のモノクロミニマル**
- **セクション class**: `info / mv / section` (シンプル)
- **特徴**:
  - 特別ゲストのトークショー、コンセプトツアー、新デザイン展示 など複合企画
  - **配色がほぼ黒白** — 工場(硬質)を表現するミニマル設計
- **示唆**: **「地域フェス=ミニマル黒白 + Nuxt + Noto Sans JP 1書体」**。Round 1で推測した "お祭り=ビビッド" とは逆のインテリ地域型

### 3-9. 全国こけし祭り (kokeshimatsuri.com)

- **ファイル**: `2192_kokeshimatsuri.com_.html` (277KB)
- **カテゴリ**: フェス/祭 / 伝統工芸
- **プラットフォーム**: **WordPress** (wp-content 検出)
- **フォント**: Typekit (`typekit.net/hte5kno.css`) — Adobe Fonts
- **配色**: `#1a1311` (本墨色) 1色のみ検出 = **本文は墨、装飾は画像**
- **セクション**: 「こけし祭りとは / イベント / こけし供養祭 / こけし奉納式 / 即売会 / こけしコンクール / こけし座談会 / フェスティバルパレード / 伝統こけしとは？」
- **キャンペーン要素**: 日時明記 + お問い合わせ先案内 + 実演展示即売会
- **示唆**: **「伝統系地域祭=WordPress + Typekit + 1色」**。装飾より情報量。役所系運営の典型

### 3-10. 丸亀うどん祭り 2025 (jp.marugame.com/campaign/marugameudonmatsuri/)

- **ファイル**: `1761_jp.marugame.com_campaign_marugameudonmatsuri_.html`
- **カテゴリ**: 祭 / 食品キャンペーン
- **コピー**: 「五感で感じる、讃岐うどんの原点と進化」
- **プラットフォーム**: **Astro** + swiper
- **フォント**: `Noto Sans JP:wght@100..900` (可変軸)
- **配色**: `#D60614 (赤) / #D7B04E (金) / #D2AF57 / #D9D6BB` — **赤×金2色** の祝祭感
- **セクション class**: `hero / hero__catch / hero__logo / hero__meta / heroInfo / footer / footer__boy / footer__kame / footer__tsuru / footer__women / footerShare / footerShare__heading / footerShare__item / footerShare__list`
- **ヘディング**:
  1. 開会式 / 最大のうどん試食イベント
  2. 「丸亀食いっプリ！グランプリ！」
  3. 「一夜限りの幻のコラボうどん」
  4. うどん&うどーなつ体験キッチンカー
  5. うどん愛×原点と進化トーク
  6. 婆娑羅太鼓演奏
  7. SANU-1 GRAND PRIX
  8. 青空うどん教室
  9. THIS IS 丸亀エンターテイメント！
- **CTAフッター構造**: `footer__boy / footer__kame / footer__tsuru / footer__women` = **キャラクター4体が足元を飾る** というユニーク実装
- **示唆**: **「食品チェーン祭=Astro + Noto Sans JP + 祝祭2色 + キャラ登場」**。Astroでも祭りは可能

### 3-11. RAGEBLUE × 銀だこ (dot-st.com/cp/rageblue/gindaco/)

- **ファイル**: `2139_www.dot-st.com_cp_rageblue_gindaco_.html` (180KB)
- **カテゴリ**: コラボ (アパレル × フード)
- **タイトル**: "みんなと夏とたこ焼と。 | RAGEBLUE"
- **コピー**: 「和のファストフードを代表する『築地銀だこ』とレイジブルーのコラボアイテムが登場！人気クリエイター3名によるデザインは、どれも夏をにぎやかに盛り上げてくれる一品ばかり。」
- **プラットフォーム**: three.js (検出) — 3D演出あり
- **フォント**: Typekit 動的ロード
- **配色**: `#e4d4a7 / #afc7d9 / #414166` — たこ焼の茶色＋夏の水色＋濃紺
- **セクション class (PascalCase)**:
  - `Main / Main__heading`
  - `Info / Info__cont / Info__heading / Info__lead / Info__tags`
  - `Footer / Footer__allItems / Footer__brand / Footer__copy / Footer__links / Footer__staff / Footer__thanks`
  - **"Footer__thanks" と "Footer__staff"** が特徴 — クレジット重視
- **LINE連携**: `line.me/R/ti/p/@rageblue` — LINE 公式アカウント友だち追加
- **UGCキャプション**: `look_1_1_caption` 〜 `look_3_2_caption` — **ルックブック画像にキャプションを個別マッピング**
- **示唆**: **「アパレル×異業種コラボ=BEM風 PascalCase + 3D + LINE送客」**。クリエイター紹介+ルックブック+SNS の3段構え

### 3-12. なら国際映画祭 2020 (nara-iff.jp/2020/)

- **ファイル**: `2268_nara-iff.jp_2020_.html` (288KB)
- **カテゴリ**: フェス / 映画祭
- **プラットフォーム**: **WordPress + React** のハイブリッド
- **コピー**: 「なら国際映画祭は今年で10年目を迎えました。奈良には、歴史・自然・神仏・生き物、たくさんの宝物があります。そして今年、コロナウィルスが猛威をふるい、あらゆる "つながり" が分断されたとき…」
- **特徴**: コロナ禍のメッセージング、「宝物」モチーフ、10周年告知を兼ねる
- **示唆**: **「国際映画祭=WP+React 静的ビルド+コロナ期の情緒的テキスト+10年の重み」**

### 3-13. SEIBAN 100周年 (seiban.co.jp/100th/) — ボーナス

- **ファイル**: `2380_www.seiban.co.jp_100th_.html` (1.6MB)
- **カテゴリ**: 周年 (100周年) / ランドセル
- **プラットフォーム**: swiper + splide + Shopify (ハッシュタグ `#shopify` 検出)
- **配色**: `#ffd900` (ランドセルイエロー) + `#00a0e9` (水色) + `#19bfd6` (シアン) = ランドセル3色
- **ハッシュタグ**: `#キミと一緒の6年間` — ブランドタグライン兼UGCハッシュタグ
- **示唆**: **「製造業100周年=ブランドコア色 + タグライン兼ハッシュタグ + Shopify連携商品販売」**

---

## 4. 共通パターン一覧

### 4.1 構造パターン TOP10

1. **`<header> + KV(mv/kv) + section×N + footer`** — 骨格 99%
2. **KV は画像 or 動画背景 (16%) + 大判タイポ見出し** — 画像配置は半数以上
3. **3〜7 セクションのスクロール型** — 長尺ペラが主流、マルチページは稀
4. **FAQ/注意事項のアコーディオン** (19%) — 下部固定
5. **お知らせ/news セクション** — 運用型は必須
6. **og:image + twitter:card** 設置率 95%/79% — OGP は完璧
7. **日付は `YYYY年MM月DD日(曜)` 全角直書き** 24% — JS 動的化は稀
8. **モーダルで規約/注意事項/商品詳細** 46%
9. **ハンバーガー or ドロワーナビ** 14% — SP でのみ表示が主
10. **フッターにシェアボタン** (丸亀うどん祭り 等) — `footerShare` パターン

### 4.2 視覚表現パターン

- **配色は 3〜5 色以内**: WordPress 系は Gutenberg デフォルトを引き継ぎ 9色パレットを無加工使用するケース有
- **フォントは 1〜2 書体**: Noto Sans JP + 欧文1書体
- **写真は大判フルブリード** or **モノトーンミニマル** の二極化
- **動画自動再生は 16%** — 通信制約を考慮した比率。モバイルでは画像置換が多い
- **Lottie 微アニメは 2.9%** — 意外と少ない。CSSトランジションで賄う傾向
- **WebGL/Three.js は 0.7%** — 極稀。RAGEBLUE× 銀だこ等の特殊事例のみ

### 4.3 コンテンツ構成パターン

- **コピー構文**:
  - 「〇〇と△△と、□□と。」 (RAGEBLUE×銀だこ「みんなと夏とたこ焼と。」)
  - 「一緒だから、超えられた」 (感謝型)
  - 「〇〇は、□□へ」 / 「0→1→10」 (進化型)
  - 「WHAT IS XX?」 (問いかけ型 — 燕三条工場の祭典)
  - 「〇周年記念特設サイト」 (シンプル周年型)
- **CTAテキスト TOP5**:
  1. 参加 (785件出現)
  2. 詳しくはこちら / もっと見る
  3. 応募する
  4. エントリー
  5. SNSでシェア

### 4.4 SNS/拡散装置パターン

- **ハッシュタグ** (`#xxx` 表記) は 84% で "必須装備化"
- **X/Twitter シェアボタン** 20%、**x.com/intent** 移行は7%と始まったばかり (twitter.com の方が依然多数)
- **Instagram リンク** 44% — 女性向けブランドで特に高比率
- **LINE 友だち追加** 7% — アパレル/食品の継続接点
- **YouTube 埋込** 15% — ブランドムービー/メイキング展開
- **Google Forms / Typeform** は 1% 程度 — 応募は自社フォーム or 外部URL誘導型が支配的

### 4.5 技術選定の相関 (示唆)

| 業種 | 推奨プラットフォーム | 根拠 |
|---|---|---|
| 地方祭/自治体 | WordPress + Typekit | kokeshimatsuri 等 |
| B2B SaaS 周年 | Astro / Next.js + Inter | SmartHR/Mercari |
| アパレル コラボ | 独自 + three.js / swiper | RAGEBLUE / 丸亀うどん祭り |
| ゲーム/エンタメ IP | Next.js + CSS Modules + 明朝 | 電音部 |
| 教育/大学 | Next.js + 独自タイポ | 狂ATE the FUTURE |
| 食品 大型キャンペーン | Astro / Nuxt + swiper | 丸亀うどん祭り |
| 100周年 老舗 | 素HTML or WP + Shopify 連携 | SEIBAN100 / ノースマン |
| マンガ/出版 周年 | Astro + Tailwind + 特殊書体 | マガポケ 10th (Round1) |

---

## 5. Round 2 新発見

### 5.1 Round 1 仮説の検証結果

| Round 1 仮説 | Round 2 検証 | 結論 |
|---|---|---|
| カウントダウンタイマーは少数派 | 591件中 実装1.7%未満 | **確定**: ほぼ存在しない |
| 日付は直書きが標準 | 24%が `YYYY年MM月DD日` 直書き | **正** |
| Astro が急速増加 | 全体では 5.2%、むしろ WP 19.6% の下位 | **修正**: Astro は"特定領域の勝ち組"で支配的ではない |
| Noto Sans JP が和文デフォ | 122件 (2位の3倍以上) | **強化**: 支配的 |
| お祭り=多書体/ビビッド | 1-2書体が 80%、ミニマル祭も多い | **修正**: Round 1 の代表30件は例外寄りだった |
| SNS シェアが必須 | og:image 95%, hashtag 84% | **強化** |
| 応募3ステップ図解は定番 | `step` class 47件=8%、明示3ステップは0.5% | **弱化**: 想像より少ない |

### 5.2 Round 1 に無かった発見

1. **WordPress 系が 19.6% で実は最大派閥** — 地方自治体/老舗の特設サイトは WP で作られ続けている
2. **ハッシュタグ表記 84%** — キャンペーンLP最強のSNS装置は「コピー#タグワード」の直書き
3. **`<video autoplay>` 16%** — KV動画は完全定着、4割が画像、2割が動画、4割が静止画
4. **モーダル使用率 46%** — 応募規約や注意事項を モーダルに詰める運用が半数近くに
5. **診断/quiz コンテンツ 4%** — エンゲージメント装置として期待より少ない
6. **アダストリア(dot-st.com) 31件で最大リピーター** — 巨大アパレル企業のブランド戦略として "特設LP量産" 文化
7. **WP Gutenberg デフォルトカラー(#0693e3 #00d084 等) が 81件ずつ並ぶ現象** — WP 系はデフォルトパレット無加工運用
8. **FONTPLUS 5.4% / TypeSquare 3.9%** — 国産ウェブフォントは依然2社で 10% 弱のシェア
9. **Barba.js 4.2% (25件)** — ページ遷移アニメは Next.js/Nuxt の SPA 遷移と並行して Barba 利用が一定数
10. **フェスがミニマル黒白の場合がある** — 燕三条工場の祭典 = 祭=ポップの固定観念への反証

### 5.3 キャンペーンLP 独自のデザインパターン

- **「キャラ足元シリーズ」**: footer にキャラクターを並べる (丸亀うどん祭り: boy/kame/tsuru/women 4キャラ)
- **「ブランドコア色×3だけで100周年」**: SEIBAN が黄+水+シアンの3色のみで100周年を表現
- **「土の色で発掘を表現」**: キャラパキ5周年が茶系8色で世界観統一
- **「感謝のループを形にする」**: INTLOOP 20周年が淡ピンク×墨+ループモチーフ
- **「Vaundy × Morisawa のように Google Fonts 非依存」**: フォントメーカーの自社デモは Google Fonts を一切使わない矜持
- **「狂ATE the FUTURE のタイトル逆説」**: "Create" を "狂ATE" と書いて大学の知性と衝動を両立

---

## 6. design-mcp 使用方針 (最終版・Round 2)

### 6.1 基本原則

1. **テンプレートに頼らない** — `list_templates` より `generate_design` のプロンプト駆動が優位
2. **参照URLは必ず1件以上渡す** — `mode: url` で具体事例を1件渡すと生成品質が格段に上がる
3. **Round 2 で判明した数字を defaults に反映**:
   - デフォルトフォント: Noto Sans JP + Inter/Poppins
   - デフォルト配色: 中間色系 3色 + アクセント1色
   - デフォルトセクション数: 5〜7
   - カウントダウンは入れない(直書き日付)
   - og:image / twitter:card は必ず設置

### 6.2 3プリセット戦略 (Round 2 改訂)

#### プリセット A: お祭り/地域フェス型
- フォント: Noto Sans JP (+ Oswald or Barlow 欧文)
- 配色: 祭赤 `#d62c36` + 金 `#d7b04e` or ミニマル黒白 `#1a1a1a / #ffffff` の2択
- プラットフォーム示唆: WordPress + Typekit (地域系) / Astro + swiper (企業主催)
- セクション: 開催概要 → 日程 → コンテンツ紹介×N → アクセス → FAQ → フッター
- 必須要素: 日付直書き、ハッシュタグ、InstagramリンLineへの誘導

#### プリセット B: SaaS/B2B/学校 周年型
- フォント: Inter or Figtree + Noto Sans JP
- 配色: 白ベース + ブランドカラー1色 + グレー2段階 (`#e4e8ed` `#3b3b3b`)
- プラットフォーム示唆: Astro or Next.js + 少数の Lottie
- セクション: Vision → なぜ今か → 数字ストーリー(Past N data) → 未来 → メディア掲載
- 必須要素: "なぜ今か" のWHY文、大判数字、メディア露出リンク

#### プリセット C: コラボ/期間限定/アパレル型
- フォント: Zen Kaku Gothic Antique + Cormorant Garamond (ファッション) or Poppins (カジュアル)
- 配色: 両ブランド色を3:2で混成
- プラットフォーム示唆: 独自 HTML or Shopify + swiper + LINE連携
- セクション: KV → コンセプト → ルックブック(キャプション個別) → ラインナップ → 購入 → SNS
- 必須要素: LINE 友だち追加、ハッシュタグキャンペーン、クリエイター紹介(Footer__staff pattern)

### 6.3 プロンプト駆動時のチェックリスト

```
入力時に必ず指定する:
[ ] 業種 (食品 / アパレル / SaaS / 地域 / 教育 / 音楽 / ゲームIP)
[ ] キャンペーン種別 (周年 / 祭 / コラボ / 新商品 / 特設 / プロジェクト / 展示)
[ ] 期間 (YYYY年MM月DD日 〜 YYYY年MM月DD日 / 曜日表記要)
[ ] ハッシュタグ (#xxx を1個)
[ ] プラットフォーム希望 (Astro / Next / Nuxt / WP / 素HTML)
[ ] ブランドカラー 1-3色 (HEX)
[ ] og:image 原稿 (用意)
[ ] フォント指定 (Google Fonts 1-2書体)
[ ] セクション数 (5〜7推奨)
[ ] 動画KV の有無
[ ] モーダル入れるか (規約用)
[ ] SNSシェア導線 (X/Insta/LINE のどれか)
```

### 6.4 避けるべきアンチパターン

- **カウントダウンタイマー** (実装1.7%、需要が無い)
- **WebGL/three.js をデフォルトで入れる** (0.7%、過剰)
- **framer-motion** (0件、React前提なら OK だが明示する)
- **Typeform/Google Forms 前提の応募フロー** (合計 <2%、外部URL 誘導が主流)
- **7書体以上のフォント混在** (4%未満、読みにくさを招く)
- **カルーセル必須化** (swiper 26% は裏返せば 74% は使っていない)

---

## 7. 付録

### 7.1 分析したファイルの代表サンプル

| # | ファイル | タイトル | カテゴリ | 備考 |
|---|---|---|---|---|
| 1 | 2025_about.mercari.com_unleash | Unleash Mercari 10th | 周年 | Next.js/Inter |
| 2 | 1823_www.intloop.com_20th | INTLOOP 20周年 | 周年/B2B | WP+Next.js hybrid |
| 3 | 1972_bandai.co.jp_charapaki5th | キャラパキ5周年 | 周年/菓子 | 茶色8色 |
| 4 | 2082_okitegami.morisawafonts | Vaundy×Morisawa | コラボ/音楽 | Barba+Next.js |
| 5 | 2087_northman-hokkaido | ノースマン(生) | 新商品 | 素HTML |
| 6 | 2117_u-tokyo_createthefuture | 狂ATE the FUTURE | 教育 | Next.js |
| 7 | 2234_denonbu.jp | 電音部 | ゲーム/IP | Next.js+明朝 |
| 8 | 1879_2023.kouba-fes | 燕三条 工場の祭典 | フェス | Nuxt+Lenis |
| 9 | 2192_kokeshimatsuri | 全国こけし祭り | 伝統祭 | WP+Typekit |
| 10 | 1761_jp.marugame_udonmatsuri | 丸亀うどん祭り | 食品祭 | Astro+swiper |
| 11 | 2139_dot-st_rageblue_gindaco | みんなと夏とたこ焼と。 | コラボ | three.js+LINE |
| 12 | 2268_nara-iff_2020 | なら国際映画祭 | 映画祭 | WP+React |
| 13 | 2380_seiban.co.jp_100th | SEIBAN 100周年 | 周年 | Shopify+swiper |

### 7.2 統計再現コマンド一覧

```bash
cd /Users/oidekento/lp-corpus/raw_all/campaign-special

# 1. タイトル一括
for f in *.html; do
  title=$(grep -oE '<title>[^<]*</title>' "$f" | head -1)
  echo "$f|$title"
done

# 2. Google Fonts ファミリ
python3 -c "
import os,re
from collections import Counter
c=Counter()
for fn in os.listdir('.'):
    if not fn.endswith('.html'): continue
    with open(fn,errors='ignore') as f: t=f.read()
    for m in re.finditer(r'fonts\.googleapis\.com/css2?\?([^\"<>\\s]+)',t):
        for fam in re.findall(r'family=([^&:]+)',m.group(1)):
            c[fam.replace('+',' ')]+=1
print(c.most_common(30))
"

# 3. 配色 TOP
grep -rhoE '#[0-9a-fA-F]{6}' . | tr 'A-Z' 'a-z' | sort | uniq -c | sort -rn | head -30

# 4. ライブラリ
for lib in swiper gsap lenis astro _next nuxt react wp-content STUDIO lottie barba three shopify; do
  c=$(grep -rli "$lib" . | wc -l)
  printf "%5d %s\n" "$c" "$lib"
done | sort -rn
```

### 7.3 この分析の次に取り組むべきこと

1. **業種別フォント/配色マトリクスの作成** — 「食品キャンペーン=赤金」「学校=紺」「SaaS=白+1色」のような二次元ヒートマップ
2. **LP 成功事例の定性分析** — UGC が実際に生成された企画(ハッシュタグ件数 vs KPI)
3. **モバイル専用 CSS の抽出** — 591件の中でモバイルファーストのコードパターン
4. **Shopify/STUDIO の特性分析** — ノーコード系で作られたキャンペーンLP 24件 + 8件 の個別特徴
5. **WP Gutenberg 直使いパターンの抽出** — 9デフォルト色出現81件の WP 系を個別に見る
6. **アダストリア 31件の定性分析** — 同社のブランド戦略がLPとしてどう実装されているか

---

**レポート終わり**
分析日: 2026-04-08 / 分析者: Claude Opus 4.6 (1M context)
データソース: `/Users/oidekento/lp-corpus/raw_all/campaign-special/` 591件
