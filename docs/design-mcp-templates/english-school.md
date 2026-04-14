# English School / 英会話・語学スクール専用LP Template

## When to Use
英会話スクール、オンライン英会話、語学コーチング、TOEIC対策、留学準備、ビジネス英語、コーチング型英語学習のランディングページ。個人系スクール（Masa English型）から大手（レアジョBODY、DMM英会話、ENGLISH COMPANY、PROGRIT）まで共通する「話せるようになる」型。

**判別基準**:
- 売っているのは「英語を話せるようになる体験」
- 受講生の「変化ストーリー」が購買の核
- 先生・コーチ・AIなど「誰が教えるか」が差別化要素
- 体験レッスンや無料カウンセリングへの導線がCTA

**使わないケース**:
- 汎用オンラインスクール（語学以外） → `tiered-program`
- 単純な資料請求LP → `landing-page`
- 単発セミナー募集 → `sales-letter`

---

## Core Principle: Transformation-First Flow（変化先行型）

英会話LPの王道は「話せない現実 → 話せる未来」の変化を最速で見せること。**テスティモニアル動画を最前面に置き、問題提起を省略する。**

```
Minimal Hero → Student Voices → Before/After → Method → Teachers → Plans → Guarantee → FAQ → CTA
(静かな入口)  (声・動画)        (変化証拠)     (手法)   (人)       (価格)  (安心)     (疑問) (予約)
```

### なぜこの順序か
英会話スクールを検索している人は既に:
1. 「話せるようになりたい」と決めている
2. 過去に挫折経験がある（だから慎重）
3. 「本当に話せるようになるのか？」を疑っている

だから最初に「自分と似た人が話せるようになった証拠」を見せ、次に「なぜ話せるようになるのか」のメソッドで論理を補強する。

---

## Rule of 3 vs Rule of 5（認知数の使い分け — MANDATORY）

| 要素 | 数 | 理由 |
|---|---|---|
| メソッドの柱 | **3つ** | インプット/アウトプット/継続 の認知フレーム |
| 差別化（他社との違い） | **5つ** | 他英会話との比較防御ライン |
| 料金プラン | **2〜3** | 体験＋本コース or ライト/スタンダード/プレミアム |
| 講師紹介 | **4〜8人** | 選択肢の豊富さを見せる |
| FAQ | **6〜10** | 「本当に話せる？」系の深い異議処理が必要 |
| 受講生動画 | **9以上** | 数自体が「多くの成功者」の証明 |

**これらの数字は推奨ではなく規則。**

---

## Section Architecture（全11セクション）

### 1. Minimal Hero（静かな入口）
**[MANDATORY SKELETON]**
- **感情**: calm | **背景**: base（白 or ソフト背景）
- ブランドロゴ + サービス名
- 1行キャッチ（12-20字）「話せる自分に、半年で。」型
- サブコピー1行（ターゲット明示）
- **大型CTA禁止** — 目的は下へスクロールさせること
- ヒーロー背景動画 or ネイティブ・受講生の笑顔写真

```html
<header class="min-h-[60vh] flex items-center justify-center relative overflow-hidden">
  <div class="absolute inset-0 bg-gradient-to-b from-white to-[#fff8f0]"></div>
  <div class="relative text-center z-10">
    <img src="logo.svg" class="h-14 mx-auto mb-6" alt="">
    <h1 class="font-display text-4xl md:text-6xl font-black leading-tight">
      話せる自分に、<br>半年で。
    </h1>
    <p class="text-muted mt-4 text-lg">社会人のための、本気の英会話コーチング</p>
    <i class="ph ph-caret-down text-3xl text-accent mt-12 animate-bounce"></i>
  </div>
</header>
```

### 2. Student Voice Video Carousel（受講生の声 — 最前面）
**[MANDATORY SKELETON — このテンプレートの核]**
- **感情**: HIGH | **背景**: base
- 自動スクロールカルーセル、**9件以上**のYouTube/動画サムネイル
- 各サムネに「受講期間」「変化の一言」を重ねる
- クリックでYouTube外部遷移（外部検証 = 信頼）
- ホバーで一時停止

**なぜ最前面か**: 訪問者は「本当に話せるようになるの？」だけを知りたい。その答えは「あなたと似た人が話しているこの動画」でしか返せない。

```html
<section class="py-20 overflow-hidden bg-white">
  <div class="text-center mb-12">
    <p class="text-accent font-bold text-sm tracking-widest">STUDENT VOICES</p>
    <h2 class="font-display text-3xl md:text-4xl font-black mt-2">
      受講生が、英語で話している動画
    </h2>
    <p class="text-muted mt-3">ぜんぶ、本物です。</p>
  </div>
  <div class="marquee-track gap-5">
    <!-- 9+ video thumbs -->
    <a href="https://youtube.com/watch?v=..." class="shrink-0 w-80 group">
      <div class="relative aspect-video rounded-xl overflow-hidden shadow-lg">
        <img src="thumb1.webp" class="w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
        <div class="absolute top-3 left-3 bg-accent text-white text-xs font-bold px-2 py-1 rounded">6ヶ月受講</div>
        <div class="absolute bottom-3 left-3 right-3 text-white">
          <p class="text-sm font-bold">「海外出張で堂々と話せるように」</p>
          <p class="text-xs opacity-80">田中さん・32歳・営業職</p>
        </div>
        <i class="ph-fill ph-play-circle absolute inset-0 m-auto text-6xl text-white opacity-90"></i>
      </div>
    </a>
    <!-- ... 8+ more ... -->
  </div>
</section>
```

### 3. Before / After Transformation（話せない → 話せる）
**[MANDATORY SKELETON]**
- **感情**: MID→HIGH | **背景**: alt-bg
- 2カラム左右比較（Before=グレー、After=アクセントカラー）
- 具体指標: スピーキング時間、語彙数、発話頻度、TOEICスコア等
- 受講生の言葉（吹き出し or 引用スタイル）
- 「◯ヶ月でこの変化」のタイムライン

```html
<section class="py-24 bg-[var(--alt-bg)]">
  <div class="max-w-5xl mx-auto px-6">
    <h2 class="text-center font-display text-3xl md:text-4xl font-black mb-16">
      6ヶ月で、ここまで変わる
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="bg-gray-100 p-8 rounded-2xl">
        <p class="text-gray-500 text-sm font-bold tracking-widest mb-4">BEFORE</p>
        <h3 class="font-display text-2xl font-bold text-gray-700 mb-6">話せなかった</h3>
        <ul class="space-y-3 text-gray-600">
          <li class="flex gap-2"><i class="ph ph-x-circle text-gray-400"></i>Yes/Noしか言えない</li>
          <li class="flex gap-2"><i class="ph ph-x-circle text-gray-400"></i>会議で黙ってしまう</li>
          <li class="flex gap-2"><i class="ph ph-x-circle text-gray-400"></i>単語が出てこない</li>
        </ul>
      </div>
      <div class="bg-accent/10 border-2 border-accent p-8 rounded-2xl">
        <p class="text-accent text-sm font-bold tracking-widest mb-4">AFTER</p>
        <h3 class="font-display text-2xl font-bold mb-6">話せる自分に</h3>
        <ul class="space-y-3">
          <li class="flex gap-2"><i class="ph-fill ph-check-circle text-accent"></i>自分の意見を英語で伝えられる</li>
          <li class="flex gap-2"><i class="ph-fill ph-check-circle text-accent"></i>海外MTGで発言できる</li>
          <li class="flex gap-2"><i class="ph-fill ph-check-circle text-accent"></i>言いたいことがスッと出る</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

### 4. Method — 3つのメソッド（Rule of 3）
**[MANDATORY SKELETON]**
- **感情**: MID | **背景**: base
- **厳密に3カード**（認知のスイートスポット）
- 各カード: 番号バッジ + 見出し + 2-3行の説明 + 手法の根拠
- 定番の「言語学ベース」「第二言語習得論（SLA）」「AI/独自教材」を軸に
- 見出しパターン: 「○○だから話せる」

```html
<section class="py-24">
  <div class="max-w-6xl mx-auto px-6">
    <div class="text-center mb-16">
      <p class="text-accent font-bold text-sm tracking-widest">METHOD</p>
      <h2 class="font-display text-3xl md:text-4xl font-black mt-2">
        なぜ、話せるようになるのか
      </h2>
    </div>
    <ul class="grid grid-cols-1 md:grid-cols-3 gap-10">
      <li class="relative pt-16">
        <span class="absolute top-0 left-0 text-7xl font-black text-accent opacity-15">01</span>
        <h3 class="font-display text-xl font-bold mb-4">
          第二言語習得論に基づく<br><span class="text-accent">科学的カリキュラム</span>
        </h3>
        <p class="text-muted leading-relaxed">
          「なんとなく」ではなく、言語学・認知科学の研究成果に基づいた順序で学ぶ。最短で話せるようになる経路を設計しています。
        </p>
      </li>
      <!-- 02: アウトプット量、03: 継続の仕組み -->
    </ul>
  </div>
</section>
```

### 5. Differentiators — 5つの差別化（Rule of 5）
**[MANDATORY SKELETON]**
- **感情**: MID | **背景**: alt-bg
- **厳密に5カード**（3+2 レイアウト）
- 各カード: アイコン + 見出し + 1-2行説明
- 英会話業界特有の差別化ポイント:
  - 「講師の質（選抜率◯%）」
  - 「アウトプット時間が◯倍」
  - 「日本人バイリンガルコーチ付き」
  - 「専用アプリ・独自教材」
  - 「週◯回の個別セッション」

### 6. Teachers / Coaches — 講師・コーチ紹介
**[MANDATORY SKELETON]**
- **感情**: HIGH（親近感） | **背景**: base
- 4-8人のグリッド（写真・名前・経歴・専門分野）
- ネイティブ講師＋日本人バイリンガルコーチの組み合わせを見せる
- 各講師の「メッセージ一言」を吹き出しで

```html
<section class="py-24">
  <div class="max-w-6xl mx-auto px-6">
    <div class="text-center mb-16">
      <p class="text-accent font-bold text-sm tracking-widest">TEACHERS</p>
      <h2 class="font-display text-3xl md:text-4xl font-black mt-2">
        あなたを支える、プロフェッショナル
      </h2>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
      <div class="text-center">
        <div class="aspect-square rounded-full overflow-hidden mb-4 bg-gray-100">
          <img src="teacher1.webp" class="w-full h-full object-cover">
        </div>
        <h3 class="font-display font-bold">Sarah Johnson</h3>
        <p class="text-xs text-muted mt-1">TESOL認定 / 12年指導</p>
        <p class="text-xs text-accent mt-1">ビジネス英語</p>
      </div>
      <!-- more... -->
    </div>
  </div>
</section>
```

### 7. Curriculum — カリキュラム詳細
**[REFERENCE PATTERN]**
- **感情**: MID | **背景**: alt-bg
- タイムライン or ステップ形式（1ヶ月目〜6ヶ月目）
- 各月の学習内容・到達目標・課題
- アコーディオンで詳細展開可

### 8. Plans — 料金プラン比較表
**[MANDATORY SKELETON]**
- **感情**: LOW→MID→HIGH | **背景**: base
- 2-3プラン横並び（ライト / スタンダード / プレミアム）
- **必須の行（順序も守る）:**
  1. プラン名（色付きヘッダー）
  2. 受講期間
  3. 週あたりのセッション回数
  4. 専属コーチの有無
  5. アウトプット時間（週◯時間）
  6. 独自教材/アプリアクセス
  7. グループレッスン回数
  8. **料金（税込・分割可能額併記）**
  9. **他社料金目安**（アンカリング）
  10. CTA行（体験申込 or カウンセリング予約）

```html
<section class="py-24">
  <div class="max-w-6xl mx-auto px-6">
    <h2 class="text-center font-display text-3xl md:text-4xl font-black mb-4">料金プラン</h2>
    <p class="text-center text-muted mb-16">最初は無料カウンセリングから。</p>
    <div class="overflow-x-auto">
      <table class="w-full border-collapse">
        <thead>
          <tr>
            <th class="p-4 border border-black/10"></th>
            <th class="p-4 border border-black/10 bg-[#f7b12b] text-white font-display">ライト</th>
            <th class="p-4 border border-black/10 bg-[#44b5a1] text-white font-display">スタンダード</th>
            <th class="p-4 border border-black/10 bg-[#66badc] text-white font-display">プレミアム</th>
          </tr>
        </thead>
        <tbody>
          <!-- 全行 -->
          <tr>
            <th class="p-4 border border-black/10 bg-alt-bg text-left">料金（税込）</th>
            <td class="p-4 border border-black/10 text-center">
              <span class="stat-numeral text-2xl font-black">29.8</span>万円<br>
              <span class="text-xs text-muted">月々4,980円〜</span>
            </td>
            <td class="p-4 border border-black/10 text-center">
              <span class="stat-numeral text-2xl font-black">49.8</span>万円<br>
              <span class="text-xs text-muted">月々8,300円〜</span>
            </td>
            <td class="p-4 border border-black/10 text-center">
              <span class="stat-numeral text-2xl font-black">79.8</span>万円<br>
              <span class="text-xs text-muted">月々13,300円〜</span>
            </td>
          </tr>
          <tr>
            <th class="p-4 border border-black/10"></th>
            <td class="p-4 border border-black/10 text-center"><a href="#cta" class="inline-block bg-[#f7b12b] text-white font-bold px-6 py-3 rounded-lg">無料体験</a></td>
            <td class="p-4 border border-black/10 text-center"><a href="#cta" class="inline-block bg-[#44b5a1] text-white font-bold px-6 py-3 rounded-lg">無料体験</a></td>
            <td class="p-4 border border-black/10 text-center"><a href="#cta" class="inline-block bg-[#66badc] text-white font-bold px-6 py-3 rounded-lg">無料体験</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```

### 9. Guarantee — 保証制度（安心の構造化）
**[MANDATORY SKELETON]**
- **感情**: HIGH（安堵） | **背景**: alt-bg
- **最低2つの保証**を見せる:
  - **全額返金保証**（例: 30日間、レッスン未満足時）
  - **達成保証**（例: TOEIC◯点未達時は無料延長）
- バッジ/印章デザイン（円形アイコン + 太字）
- 「リスクはこちらが引き受けます」のメッセージ

```html
<section class="py-20 bg-[var(--alt-bg)]">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h2 class="font-display text-3xl md:text-4xl font-black mb-12">
      安心の、2つの保証
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="bg-white p-10 rounded-2xl shadow-lg">
        <div class="w-24 h-24 mx-auto rounded-full bg-accent/10 flex items-center justify-center mb-6">
          <i class="ph-fill ph-shield-check text-5xl text-accent"></i>
        </div>
        <h3 class="font-display text-xl font-bold mb-3">30日間<br>全額返金保証</h3>
        <p class="text-sm text-muted">受講開始から30日以内にご満足いただけなかった場合、全額返金いたします。</p>
      </div>
      <div class="bg-white p-10 rounded-2xl shadow-lg">
        <div class="w-24 h-24 mx-auto rounded-full bg-accent/10 flex items-center justify-center mb-6">
          <i class="ph-fill ph-trophy text-5xl text-accent"></i>
        </div>
        <h3 class="font-display text-xl font-bold mb-3">スコア<br>達成保証</h3>
        <p class="text-sm text-muted">TOEIC目標スコア未達成の場合、達成まで無料で学習期間を延長します。</p>
      </div>
    </div>
  </div>
</section>
```

### 10. FAQ — よくある質問
**[MANDATORY SKELETON]**
- **感情**: MID | **背景**: base
- 6-10問、details/summary形式
- **必須質問パターン**:
  - 「本当に話せるようになりますか？」
  - 「初心者でも大丈夫ですか？」
  - 「忙しくて続けられるか不安です」
  - 「TOEIC◯点ですが受講できますか？」
  - 「返金制度はありますか？」
  - 「他の英会話スクールと何が違いますか？」
  - 「一日どれくらいの学習時間が必要？」
  - 「オンラインだけで完結できますか？」

### 11. Final CTA — 無料体験 / 無料カウンセリング予約
**[MANDATORY SKELETON]**
- **感情**: PEAK | **背景**: accent or dark
- 大型フォーム or 予約ボタン
- 「まずは無料カウンセリング」or「無料体験レッスン」
- **価格を繰り返さない** — 体験への敷居を低く
- 所要時間明記（「30分の無料カウンセリング」等）
- LINE予約 / Googleカレンダー連携の選択肢

```html
<section class="py-24 bg-accent text-white">
  <div class="max-w-3xl mx-auto px-6 text-center">
    <h2 class="font-display text-3xl md:text-5xl font-black mb-6">
      まずは、話してみませんか？
    </h2>
    <p class="text-lg opacity-90 mb-10">
      30分の無料カウンセリング。勧誘は一切ありません。
    </p>
    <a href="#" class="inline-block bg-white text-accent font-bold text-lg px-12 py-5 rounded-full hover:-translate-y-1 transition-transform shadow-2xl">
      無料カウンセリングを予約する
    </a>
    <div class="flex gap-4 justify-center mt-6 text-sm opacity-80">
      <span><i class="ph ph-check"></i> 所要30分</span>
      <span><i class="ph ph-check"></i> オンライン対応</span>
      <span><i class="ph ph-check"></i> 完全無料</span>
    </div>
  </div>
</section>
```

### 12. Footer — LEGAL COMPLIANCE MANDATORY
- **特定商取引法に基づく表記** (REQUIRED by Japanese law) ← **MANDATORY**
- プライバシーポリシー
- 利用規約
- 運営会社情報
- Copyright

日本の有料サービスでは特商法表記が必須。リンクだけでも絶対に含めること。

---

## Banned Patterns

- **Problem agitation in hero** — 「英語で悩んでいませんか？」系のいきなり悩み煽りは逆効果。訪問者は既に悩んでいる
- **「ペラペラになる」系の誇大表現** — 根拠のない断定は信頼を破壊する。必ず具体指標（時間・回数・スコア）で語る
- **Countdown timers** — 英会話は長期コミット商品。偽の緊急性は信頼を破壊する
- **講師紹介なし** — 「誰が教えるか」を隠してはいけない。最低4人は見せる
- **受講生の声がテキストのみ** — 動画なしのテスティモニアルは弱い。**必ず9+の動画**を最前面に
- **Before/After なし** — 「話せない→話せる」の変化証拠は英会話LPの核。省略不可
- **料金だけの比較表** — プラン表は「アウトプット量・セッション回数・コーチ有無」を行に含めること
- **保証制度なし** — 高単価プログラムで保証なしは売れない。最低1つの保証を見せる
- **CTA が価格ページ直行** — 英会話は体験 → 本契約の2段階。必ず「無料体験/無料カウンセリング」を挟む
- **特商法表記なし** — 法令違反

---

## Typography
- Headlines: `font-display` (Noto Serif JP or Noto Sans JP 900)
- 英語キャッチ: `font-english` (Inter, Playfair Display等)
- Plan names in table: `font-display font-bold text-lg`
- Prices: `stat-numeral` class (tabular-nums, body font)
- Body: `font-body`, line-height 1.8

## Color Recommendations
- **親しみ系**（個人スクール、Masa English型）: warm coral `#ff7b54` + cream `#fff8f0`
- **信頼系**（大手、ENGLISH COMPANY型）: navy `#1e3a5f` + gold `#c9a961`
- **ポップ系**（DMM英会話型）: orange `#ff6b35` + sky `#4fc3f7`
- **学術系**（PROGRIT型）: deep green `#2d5f3f` + ivory `#faf9f5`

## Responsive Rules
- Table: `overflow-x-auto` wrapper for mobile scroll
- Video carousel: 動画サムネ幅は mobile でも縮小せず横スクロール
- Method pillars: `grid-cols-1 md:grid-cols-3`
- Differentiators: `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` (5 items = 3+2)
- Teachers: `grid-cols-2 md:grid-cols-4`
- Hero: `min-h-[60vh]` on desktop, `min-h-[50vh]` on mobile
