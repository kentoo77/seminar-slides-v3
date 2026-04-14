# Presentation / Slide Deck Template

## Aesthetic Direction
Investor-grade pitch deck with cinematic slide transitions. Each slide is a full-viewport canvas. Think Apple keynote meets Bloomberg data density.

---

## Slide System Architecture

### Core Structure
```css
.slide {
  position: absolute; top: 0; left: 0;
  width: 100vw; height: 100vh;
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  padding: 4rem 8rem;
  opacity: 0; visibility: hidden;
  transition: opacity 0.4s ease-in-out, visibility 0.4s ease-in-out,
              transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  transform: scale(0.98) translateY(10px);
  z-index: 1;
}
.slide.active {
  opacity: 1; visibility: visible;
  transform: scale(1) translateY(0);
  z-index: 10;
}
```
Key: `opacity + visibility` dual control. `scale(0.98) + translateY(10px)` creates a subtle "float up" entrance.

### Navigation JavaScript
```javascript
let current = 0, isAnimating = false;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
  if (isAnimating || index < 0 || index >= slides.length) return;
  isAnimating = true;
  slides[current].classList.remove('active');
  current = index;
  slides[current].classList.add('active');
  // Update counter, dots, nav colors
  updateUI();
  setTimeout(() => { isAnimating = false; }, 600);
}

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight') showSlide(current + 1);
  if (e.key === 'ArrowLeft') showSlide(current - 1);
});

// Click anywhere to advance (except interactive elements)
document.addEventListener('click', e => {
  if (!e.target.closest('button, a, input, details')) showSlide(current + 1);
});
```

### Adaptive Nav Color (light/dark slide mix)
```javascript
function updateUI() {
  const nav = document.getElementById('global-nav');
  const slide = slides[current];
  if (slide.classList.contains('bg-light')) {
    nav.classList.remove('text-muted'); nav.classList.add('text-gray-500');
  } else {
    nav.classList.remove('text-gray-500'); nav.classList.add('text-muted');
  }
  document.getElementById('slide-counter').textContent = `${current + 1} / ${slides.length}`;
}
```

### Global Nav (fixed bottom, pointer-events: none)
```html
<div id="global-nav" class="fixed bottom-0 left-0 w-full px-10 py-8
     flex justify-between items-center z-50 pointer-events-none">
  <!-- Left: brand logo -->
  <div class="flex items-center gap-3">
    <span class="text-sm font-semibold" style="color:var(--accent)">BrandName</span>
  </div>
  <!-- Right: confidential + counter -->
  <div class="flex items-center gap-4">
    <div class="text-xs uppercase tracking-widest opacity-50">Confidential</div>
    <div id="slide-counter" class="text-sm font-medium tracking-wide">1 / 10</div>
  </div>
</div>
```
`pointer-events: none` is MANDATORY — prevents nav from blocking slide interactions.

### Keyboard Hint (title slide only)
```html
<div class="absolute bottom-12 text-sm text-muted flex items-center gap-2">
  Use
  <kbd class="px-2 py-1 bg-white/10 rounded text-xs border border-white/20">←</kbd>
  <kbd class="px-2 py-1 bg-white/10 rounded text-xs border border-white/20">→</kbd>
  to navigate
</div>
```

---

## Slide Layout Patterns

### Title Slide (slide 1)
- Center-aligned, generous whitespace
- Brand logo with gradient text (48px, weight 900)
- Tagline below (24px, muted)
- Separator line + metadata (Series A, Confidential, date)
- Background: radial accent glow (opacity 0.08) from center

### Stat Cards (3-4 across)
```html
<div class="grid grid-cols-3 gap-6">
  <div class="rounded-xl p-7 relative overflow-hidden"
       style="background:var(--surface);border:1px solid rgba(255,255,255,0.06)">
    <!-- Ghost icon (decorative, top-right) -->
    <div class="absolute top-0 right-0 p-4 opacity-10 text-7xl">ICON</div>
    <div class="text-xs text-accent uppercase tracking-widest mb-3">LABEL</div>
    <div class="text-4xl font-bold">67%</div>
    <p class="text-sm text-muted mt-2">Description text</p>
  </div>
</div>
```
Ghost icon pattern: large Phosphor icon at `opacity-10` in top-right corner.

### 2-Column (text + mockup, 5:7 ratio)
```html
<div class="flex gap-16 items-center w-full max-w-[1200px]">
  <div class="w-5/12"><!-- text content --></div>
  <div class="w-7/12"><!-- mockup / visual --></div>
</div>
```

### Competitor Table (border-spacing rows)
```css
.competitor-table { border-collapse: separate; border-spacing: 0 12px; width: 100%; }
.competitor-table td { background: rgba(31,41,55,0.3); padding: 20px 16px; }
.competitor-table td:first-child { border-radius: 12px 0 0 12px; }
.competitor-table td:last-child { border-radius: 0 12px 12px 0; }
.highlight-col { background: rgba(ACCENT_R,ACCENT_G,ACCENT_B,0.1); position: relative; }
.highlight-col::before {
  content: ''; position: absolute; inset: 0; border-radius: 12px;
  border: 1px solid rgba(ACCENT_R,ACCENT_G,ACCENT_B,0.5); pointer-events: none;
}
```

### Timeline (vertical, left-border)
```html
<div class="relative border-l-2 border-white/15 ml-4 space-y-10 py-2">
  <div class="relative pl-8">
    <!-- Done dot: accent bg + glow -->
    <div class="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-accent"
         style="box-shadow:0 0 10px var(--accent)"></div>
    <p class="font-bold">Milestone text</p>
  </div>
  <div class="relative pl-8">
    <!-- Future dot: gray, no glow -->
    <div class="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-gray-700"></div>
    <p class="text-muted">Future milestone</p>
  </div>
</div>
```

### Concentric Circles (TAM/SAM/SOM)
Use absolute-positioned rounded-full divs with decreasing size and increasing opacity.
Outer (TAM): border only, bg transparent. Middle (SAM): accent/10 bg + accent border.
Inner (SOM): accent gradient fill.

### SVG Line Chart with Stroke Animation
```html
<svg viewBox="0 0 1000 200">
  <defs>
    <linearGradient id="lineGrad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="ACCENT" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="ACCENT"/>
    </linearGradient>
    <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="ACCENT" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="ACCENT" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="3"/></filter>
  </defs>
  <path d="..." fill="url(#areaGrad)" class="animate-rise-up"/>
  <path d="..." fill="none" stroke="url(#lineGrad)" stroke-width="3"
        filter="url(#glow)" class="animate-draw-line"/>
</svg>
```
Reset animation on slide revisit: `path.style.animation='none'; void path.offsetWidth; path.style.animation='...'`

### Fund Allocation Bar (segmented horizontal)
```html
<div class="w-full h-6 rounded-full flex overflow-hidden">
  <div class="bg-accent h-full" style="width:45%">45%</div>
  <div class="bg-blue-500 h-full" style="width:30%">30%</div>
  <div class="bg-teal-500 h-full" style="width:15%">15%</div>
  <div class="bg-amber-500 h-full" style="width:10%">10%</div>
</div>
```

---

## Visual Depth (same as LP, applied per-slide)

- Ambient glow: 1-2 radial-gradient orbs per dark slide, different positions
- Glass panels: `backdrop-filter: blur(16px)` for card overlays
- Left-border hierarchy: `border-l-4 border-accent` for emphasis cards
- Border-top accent: `border-t-2 border-accent` for KPI cards

---

## Typography Scale (Presentation-specific)
- Slide title: `clamp(2.5rem, 5vw, 4.5rem)`, weight 700-800, tracking -0.03em
- Section label: 12px, accent color, uppercase, tracking 0.2em, weight 700
- Body: 14-16px, muted color, line-height 1.6
- Stat numbers: 36-60px, weight 700-800, white
- Use body font for all numbers (tabular-nums), never display font

---

## Color Strategy
- 8 dark slides + 2 light slides (How It Works, Business Model)
- Consistent accent across all slides
- Ambient glow intensity varies: title=subtle, CTA=bold
- Light slides: same accent color, dark text (#0F0F14)
