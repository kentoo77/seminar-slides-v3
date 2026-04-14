# Sales Letter / セールスレター Template

## Aesthetic Direction
Long-form persuasion page that builds emotional momentum toward conversion. The design must feel premium, trustworthy, and urgent — like a private invitation, not a billboard. Think high-end coaching program or exclusive software launch.

---

## Core Design Principles

### 1. Emotional Rhythm
Alternate between **emotional hooks** (stories, pain points, transformations) and **evidence blocks** (stats, testimonials, features). Never stack more than 2 evidence blocks without an emotional break.

### 2. Visual Hierarchy of Persuasion
The reader's eye follows this path on every screen:
1. Headline (emotional hook) — largest text
2. Supporting visual or proof point
3. Body copy (builds the case)
4. CTA or bridge to next section

### 3. Color Strategy
- **Premium dark**: `#0F0F14` to `#1A1A2E` base, or warm dark `#1a1510` for luxury
- **Gold accent `#D4AF37`**: for premium/luxury products (coaching, high-ticket services)
- **Green accent**: for SaaS, productivity, health products
- **Red/urgency accent**: for limited-time offers, scarcity elements only
- Never more than 1 accent + gold for price anchoring

---

## Emotional Arc Map (セクション設計の羅針盤)

以下の波形に従ってセクションを配置する。各セクションの感情ポジションを厳守すること。

```
感情レベル
  HIGH ████ Hero    ████ Testi#1    ████ Testi#2    ████ Guarantee    ████ Final CTA
       │            │               │                │                 │
  MID  │    ████ B/A│  ████Features │  ████Method    │  ████Urgency    │
       │         │  │         │     │         │      │         │       │
  LOW  │████Pain │  │         │████Stats     │ ████Price     │       │
       └──────────────────────────────────────────────────────────────────→
       1  2   3  4  5   6   7  8   9  10  11  12  13  14  15  16
```

ルール:
- HIGH→LOWの直接落下は禁止（必ず中間MIDセクションを挟む）
- 実績(Testimonial)は序盤(4)・中盤(7)・終盤(12)の3箇所に分散
- Pricing(緊張)の直後にBonus→Guarantee→FAQで不安を段階的に解消
- 各セクションのbody copyは**150-300字**に収める

---

## Section Architecture (12-16 sections, long-form)

### 1. Hero — Emotional Hook (min-h-[100svh])
**[MANDATORY SKELETON — この構造を維持し、テキストのみ差し替え]**
- **感情**: HIGH | **背景**: dark | **6段構造**: 希少性バッジ
- Full-viewport, centered text layout (NOT 2-column for sales letters)
- Headline: 痛み→解決の対比構造。「〜で悩んでいませんか？」は禁止。断言形
- Badge above headline: "期間限定" / "先着100名" with live-dot indicator
- Subcopy: 3行の感情→機能→断言構造
- Primary CTA button with glow shadow
- Social proof immediately below: avatar stack + 「3,000人が体験」

```html
<section class="relative min-h-[100svh] flex items-center justify-center text-center">
  <div class="max-w-4xl mx-auto px-6">
    <div class="inline-flex items-center gap-2 bg-accent/10 text-accent text-sm font-bold px-4 py-2 rounded-full mb-8">
      <span class="relative flex h-2 w-2">
        <span class="animate-ping absolute h-full w-full rounded-full bg-accent opacity-75"></span>
        <span class="relative rounded-full h-2 w-2 bg-accent"></span>
      </span>
      期間限定公開
    </div>
    <h1 class="font-display text-4xl md:text-6xl font-black leading-[1.1] mb-6">
      Headline with <span class="marker-highlight">key phrase</span> highlighted
    </h1>
    <p class="text-lg md:text-xl text-muted max-w-2xl mx-auto mb-10 leading-relaxed">subcopy</p>
    <button class="cta-primary bg-accent text-dark font-bold px-8 py-4 rounded-lg text-lg">
      今すぐ申し込む <i class="ph ph-arrow-right ml-2"></i>
    </button>
    <!-- Social proof -->
    <div class="flex items-center justify-center gap-3 mt-8">
      <div class="flex -space-x-2">
        <img src="https://i.pravatar.cc/150?u=s1@x.com" class="w-8 h-8 rounded-full border-2 border-bg" alt="">
        <img src="https://i.pravatar.cc/150?u=s2@x.com" class="w-8 h-8 rounded-full border-2 border-bg" alt="">
        <img src="https://i.pravatar.cc/150?u=s3@x.com" class="w-8 h-8 rounded-full border-2 border-bg" alt="">
      </div>
      <span class="text-sm text-muted"><strong class="text-white">3,000人</strong>が体験済み</span>
    </div>
  </div>
</section>
```

### 2. Problem Agitation — 痛みの深掘り
**[REFERENCE PATTERN — 構造を参考にカスタマイズ可]**
- **感情**: LOW | **背景**: dark (dot-grid) | **6段構造**: 敵を作る | **コピー量**: 150-250字
- 3-4 pain points as icon + short text cards (grid-cols-2)
- Each card: red-tinted left border (`border-l-4 border-red-400`)
- Copy: 読者の現実を具体的に描写。「9割の人は〜」で分断し1割側に自己投影させる

### 3. BEFORE / AFTER — 変化の可視化
**[MANDATORY SKELETON — このグリッド構造を維持]**
- **感情**: MID→HIGH | **背景**: base | **コピー量**: 200-300字
- 2-column layout: left=BEFORE (muted, red accent), right=AFTER (bright, green/gold accent)
- Each column: 4-5 bullet points with check/x icons
- Center divider: vertical line with arrow or "→" icon

```html
<div class="grid md:grid-cols-2 gap-0 rounded-2xl overflow-hidden">
  <div class="bg-red-950/30 p-8 border-r border-white/10">
    <div class="text-xs font-bold tracking-widest uppercase text-red-400 mb-6">BEFORE</div>
    <ul class="space-y-4">
      <li class="flex items-start gap-3">
        <i class="ph ph-x-circle text-red-400 text-xl mt-0.5"></i>
        <span class="text-muted">Pain point description</span>
      </li>
    </ul>
  </div>
  <div class="bg-emerald-950/30 p-8">
    <div class="text-xs font-bold tracking-widest uppercase text-emerald-400 mb-6">AFTER</div>
    <ul class="space-y-4">
      <li class="flex items-start gap-3">
        <i class="ph ph-check-circle text-emerald-400 text-xl mt-0.5"></i>
        <span>Positive outcome description</span>
      </li>
    </ul>
  </div>
</div>
```

### 4. Testimonial #1 — 実績証明（序盤）
**[REFERENCE PATTERN]**
- **感情**: HIGH | **背景**: base | **6段構造**: 実績(序盤) | **コピー量**: 150-200字
- Single large testimonial card with photo, name, role
- Quote in larger text (1.25rem) with accent left border
- Result metric highlighted: 「売上3倍」「月100万円達成」
- Background: subtle glass card on dark

### 5. Feature Showcase — 3つの柱
**[REFERENCE PATTERN]**
- **感情**: MID | **背景**: dark | **6段構造**: 3分類で自己投影 | **コピー量**: 200-300字
- 3 feature cards (grid-cols-1 md:grid-cols-2 — bento禁止、sales letterは縦読み)
- Each card: icon + title + 2-line description
- group-hover with top color bar animation
- Section headline: カテゴリ再定義（「単なる〇〇ではありません」）

### 6. Social Proof Band — 数字で証明
**[REFERENCE PATTERN]**
- **感情**: LOW→MID | **背景**: alt-bg | **コピー量**: 最小限（数字+ラベルのみ）
- Full-width accent/dark background
- 4 stat cards with counter animation (data-target)
- Stats: 受講者数, 満足度%, 成果達成率, 継続率
- Each stat has a label below in muted small text

### 7. Testimonial Grid — 実績の厚み（中盤）
**[REFERENCE PATTERN]**
- **感情**: HIGH | **背景**: base | **6段構造**: 実績(中盤) | **コピー量**: 200-250字
- 2-column testimonial cards (3-column禁止 — sales letterは縦読み)
- Each: avatar + name + role + 2-3 line quote + result metric
- Staggered data-animate delays for scroll reveal

### 8. Method / Timeline — ステップ解説
**[MANDATORY SKELETON — タイムライン構造を維持]**
- **感情**: MID | **背景**: dark | **コピー量**: 200-300字
- Vertical timeline with left border
- 3-5 steps: numbered circles + title + description
- Active/completed steps: accent dot with glow
- Future steps: gray dot

```html
<div class="relative border-l-2 border-accent/30 ml-6 space-y-12 py-4">
  <div class="relative pl-10" data-animate data-animate-delay="1">
    <div class="absolute -left-[13px] top-1 w-6 h-6 rounded-full bg-accent flex items-center justify-center text-xs font-bold text-dark"
         style="box-shadow: 0 0 12px rgba(var(--accent-rgb),0.5)">1</div>
    <h3 class="text-xl font-bold mb-2">Step Title</h3>
    <p class="text-muted">Step description</p>
  </div>
</div>
```

### 9. Pricing — 価格提示
**[MANDATORY SKELETON — 価格構造を維持]**
- **感情**: LOW→MID | **背景**: dark | **6段構造**: 期限+希少性 | **コピー量**: 150-250字
- Single pricing card (NOT comparison grid — sales letters sell ONE offer)
- Anchor price with strikethrough: `<span class="line-through text-muted text-lg">¥49,800</span>`
- Actual price large and bold: `<span class="stat-numeral text-5xl font-black text-accent">¥29,800</span>`
- Bonus list below price with checkmarks
- CTA button with glow at bottom of card

```css
/* Marker highlight for key phrases */
.marker-highlight {
  background: linear-gradient(transparent 50%, rgba(var(--accent-rgb), 0.3) 50%);
  padding: 0 4px;
}
/* Gold marker for premium */
.marker-gold {
  background: linear-gradient(transparent 50%, rgba(212, 175, 55, 0.3) 50%);
  padding: 0 4px;
}
```

### 10. Bonus Stack — 特典の積み上げ
**[REFERENCE PATTERN]**
- **感情**: MID→HIGH | **背景**: base | **コピー量**: 200-300字
- List of 3-5 bonuses, each in a card with:
  - "特典 1" label (accent, uppercase, tracking-widest)
  - Bonus title (font-bold, 1.25rem)
  - Value display: `通常価格 ¥XX,XXX → 無料`
  - Thumbnail image or icon
- Running total at bottom: 「総額 ¥XXX,XXX 相当 → 今だけ ¥XX,XXX」

### 11. Guarantee — 安心の保証
**[MANDATORY SKELETON — 保証カード構造を維持]**
- **感情**: HIGH | **背景**: base | **コピー量**: 100-200字
- Centered card with shield icon
- Border: dashed accent or gold
- Guarantee text in clear, confident language
- Duration badge: 「30日間全額返金保証」

```html
<div class="max-w-2xl mx-auto text-center p-8 rounded-2xl border-2 border-dashed border-accent/50"
     style="background: rgba(var(--accent-rgb), 0.05)">
  <i class="ph ph-shield-check text-5xl text-accent mb-4"></i>
  <h3 class="text-2xl font-bold mb-3">30日間全額返金保証</h3>
  <p class="text-muted leading-relaxed">Guarantee copy here</p>
</div>
```

### 12. Testimonial #3 — 実績証明（終盤）
**[REFERENCE PATTERN]**
- **感情**: HIGH | **背景**: alt-bg | **6段構造**: 実績(終盤) | **コピー量**: 200-300字
- 1-2 more testimonials focused on transformation stories
- Longer format: 3-4 sentences with before/after narrative

### 13. Urgency / Scarcity — 限定性
**[REFERENCE PATTERN]**
- **感情**: MID | **背景**: dark | **6段構造**: 期限を切る | **コピー量**: 100-200字
- Counter or deadline display: 「毎月○社限定」「残り○枠」
- Subtle pulse animation on urgency badge
- Do NOT fake urgency — present real constraints. 「毎月3社限定」のような現実的な制約

### 14. Final CTA — クロージング
**[REFERENCE PATTERN]**
- **感情**: HIGH | **背景**: dark | **コピー量**: 100-150字
- Full-width section with gradient background
- Large headline: 断言形の行動喚起
- Price reminder (smaller, below headline)
- Primary CTA button (largest on page)
- Trust badges below: payment icons, SSL, guarantee reminder

### 15. FAQ — よくある質問
**[MANDATORY SKELETON — details/summary構造を維持]**
- **感情**: MID | **背景**: base | **コピー量**: 300-500字（5-8問の合計）
- `<details><summary>` elements with smooth animation
- 5-8 questions covering objections (price, time, skill level, refund)
- Chevron rotation on open

```html
<details class="group border-b border-white/10">
  <summary class="flex items-center justify-between py-5 cursor-pointer text-lg font-semibold hover:text-accent transition-colors">
    よくある質問テキスト
    <i class="ph ph-caret-down text-xl transition-transform duration-300 group-open:rotate-180"></i>
  </summary>
  <div class="pb-5 text-muted leading-relaxed">
    Answer text here
  </div>
</details>
```

### 16. P.S. + Footer — シンプル
**[REFERENCE PATTERN]**
- **感情**: MID | **背景**: base
- P.S.: 感情的なワンライン。セールスレターで最も読まれるパート。最後の一押し
- Footer: Minimal — brand name + legal links + copyright only
- No complex multi-column layout (this is a sales letter, not a corporate site)

---

## Sticky Bottom CTA Bar
Appears after scrolling past the hero. Fixed at bottom with slide-up animation.

```html
<div id="sticky-cta" class="fixed bottom-0 left-0 w-full z-50 transform translate-y-full transition-transform duration-500">
  <div class="bg-surface/95 backdrop-blur-md border-t border-white/10 px-6 py-3 flex items-center justify-between max-w-5xl mx-auto">
    <div>
      <span class="text-sm text-muted">期間限定価格</span>
      <span class="stat-numeral text-xl font-bold ml-2">¥29,800</span>
    </div>
    <button class="cta-primary bg-accent text-dark font-bold px-6 py-3 rounded-lg">今すぐ申し込む</button>
  </div>
</div>
```

```javascript
// Show sticky CTA after scrolling past hero
const hero = document.querySelector('section');
const stickyCta = document.getElementById('sticky-cta');
const obs = new IntersectionObserver(([e]) => {
  stickyCta.classList.toggle('translate-y-full', e.isIntersecting);
  stickyCta.classList.toggle('translate-y-0', !e.isIntersecting);
}, { threshold: 0 });
obs.observe(hero);
```

---

## Typography Scale (Sales Letter specific)

- Hero headline: `clamp(2.5rem, 6vw, 4rem)`, weight 900, tight tracking
- Section headlines: `clamp(1.8rem, 4vw, 2.5rem)`, weight 800
- Body: 1.05-1.125rem, weight 400, line-height 1.8 (more generous for long-form reading)
- Price display: stat-numeral class, 3-4rem, weight 900
- Labels/badges: 0.75rem, uppercase, tracking-widest, accent color
- Testimonial quotes: 1.125rem, italic or normal, line-height 1.7

---

## Mandatory CSS Classes

```css
/* Marker highlight — for key selling phrases */
.marker-highlight {
  background: linear-gradient(transparent 50%, rgba(var(--accent-rgb), 0.3) 50%);
  padding: 0 4px;
}

/* Gold marker — for premium/price anchoring */
.marker-gold {
  background: linear-gradient(transparent 50%, rgba(212, 175, 55, 0.3) 50%);
  padding: 0 4px;
}

/* Strikethrough price */
.price-anchor {
  text-decoration: line-through;
  color: var(--text-muted);
  font-size: 1.125rem;
}
.price-actual {
  font-family: var(--font-body);
  font-variant-numeric: tabular-nums;
  font-size: clamp(2.5rem, 5vw, 3.5rem);
  font-weight: 900;
  color: var(--accent);
}

/* Guarantee card */
.guarantee-card {
  border: 2px dashed rgba(var(--accent-rgb), 0.5);
  background: rgba(var(--accent-rgb), 0.05);
  border-radius: 1rem;
  padding: 2rem;
  text-align: center;
}

/* FAQ details animation */
details summary { list-style: none; }
details summary::-webkit-details-marker { display: none; }
details[open] summary ~ * {
  animation: slide-down 300ms ease-out;
}
@keyframes slide-down {
  0% { opacity: 0; transform: translateY(-8px); }
  100% { opacity: 1; transform: translateY(0); }
}
```

---

## Copy Rules (Sales Letter specific)

### 6段構造（セールスコピー）
1. **敵の設定**: 読者の現状の「本当の原因」を名指しする
2. **禁断の真実**: 業界が言わない不都合な真実を暴く
3. **3分類**: 解決策を3つのカテゴリに分け、自分のポジションを明確にする
4. **期限**: なぜ「今」行動すべきかの理由
5. **実績**: 具体的な数字と変化のストーリー
6. **希少性**: 数量限定、期間限定、条件限定のいずれか

### リズム規則
- 見出し: 20-30字。対比構造（否定→肯定）
- 本文: 1段落3文まで。短文連打→長文→短文のリズム
- CTA: 断言形。「〜してみませんか？」「〜はいかがですか？」は禁止
- 数字は具体的に: 「多くの」→「3,247人の」、「すぐに」→「30秒で」
