---
name: design-mcp AIDesigner蒸留プロジェクト
description: AIDesigner MCPの出力50本からパターン抽出→自作MCPに移植する進行中プロジェクト
type: project
---

## 現状（2026-04-08更新）
- AIDesigner MCPの出力50本を自動生成・保存完了
- 全50本のCSS/HTML/レイアウトパターンを5エージェントで並列分析完了
- **system.ts反映完了**: AIDesigner DNAパターン + **GENERATE_SALES_LETTER_SYSTEM_PROMPT新設**（16セクション、6段セールスコピー構造、感情波形設計、コード効率ルール）
- **sales-letter.mdテンプレート改善完了**: 感情波形マップ、MANDATORY/REFERENCEラベル、セクション品質制約（コピー量・背景色・感情レベル）追加
- **IOアニメーションバグ修正完了**: prefers-reduced-motion fallback + 3秒フォールバックタイマー + LLM独自IO時の二重防御（FALLBACK_REVEAL_JS常時注入）
- **generate.ts分岐完了**: sales-letter検出時に専用システムプロンプトを使用
- コミット: c375b12 (main, pushed)

## 次のステップ
1. ~~50本分析結果の統合~~ ✅
2. ~~system.ts + テンプレート反映~~ ✅
3. ~~sales-letter.md テンプレート新設~~ ✅
4. ~~セールスレターで再テスト → AIDesignerと比較~~ ✅ 追いついた
5. ~~auto_refine 実装~~ ✅ generate→critique→refine自動ループ完成
6. ~~コード効率改善~~ ✅ LLM style 336行→31行、inline style 347→3
7. ~~品質ブレ検証~~ ✅ 3バリアント生成で安定確認
8. ~~IOフォールバック根本修正~~ ✅ FALLBACK_REVEAL_JS確実注入+window.loadフック
9. Champion サンプル保存機能（高スコアHTML自動蓄積+次回注入）
10. 他テンプレート（LP、ダッシュボード等）にも専用プロンプト展開

## AIDesignerの設計DNA（統計的に確定した「癖」）
- Phosphor Icons限定: 50/50 (100%)
- カスタムスクロールバー: 49/50 (98%)
- ::selection ブランドカラー: 47/50 (94%)
- tracking-widest + uppercase ラベル: 47/50 (94%)
- group/group-hover 多段アニメ: 50/50 (100%)
- transition-all duration-200~500: 50/50 (100%)
- glassmorphism (backdrop-blur): 40/50 (80%)
- animate-float: 35/50 (70%)
- feTurbulence SVGノイズ: 35/50 (70%)
- text-gradient (-webkit-background-clip): 30/50 (60%)
- marker-highlight (linear-gradient 50%): セールスレター5/5 (100%)
- Gold #D4AF37: 高単価商品で3/5 (60%)

## 比較テスト結果
- LP: 36 vs 36（同点）→ 改修後は自作MCP改善
- スライド: 29 vs 44（自作MCP圧勝）
- セールスレター(4/7): AIDesigner勝ち — IOバグでコンテンツ不可視 + 汎用LPプロンプト競合
- **セールスレター(4/8再テスト): 追いついた** — 16セクション全描画、6段構造+感情波形注入、IOバグ修正
- **セールスレター(4/9 auto_refine): AIDesigner超え** — CSS効率91%改善(style 336→31行, inline 347→3)、auto_refineで5項目自動改善、IOフォールバック完全動作

**Why:** AIDesignerの「ビジュアル品質」と「情報設計力」を自作MCPに移植し、指示再現性の強みを維持しながら品質で上回ることが目標。
**How to apply:** セールスレターは完成水準。次は他テンプレート（LP、ダッシュボード）への専用プロンプト展開。
