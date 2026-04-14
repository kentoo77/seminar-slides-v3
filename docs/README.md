# セミナースライド v3 — デザインナレッジ

## なぜ高品質なスライドが生成できたのか

### 1. 日本LP 45,000件のコーパス分析 (`lp-corpus-analysis/`)
- sankoudesign.com + rdlp.jp から45,105件のLPを収集
- 21ジャンルに分類し、各ジャンルの配色・レイアウト・CTA・技術スタックを統計分析
- **特に `school-education.md`** が本プロジェクトの配色決定に直接影響
  - 教育LP 120件の深層分析（大学43, 幼稚園35, 専門学校25, プログラミング19, 英語15）
  - 4つの配色プリセットを抽出: Traditional Academic / Modern Vocational / Nursery Soft / **Online School Clean（採用）**

### 2. デザイン方針・フィードバック (`design-knowledge/`)
- `feedback_slide_design_direction.md` — CSS v2プロトタイプへの詳細批評。海外風NG、日本LP参照必須
- `feedback_slide_design_sense.md` — 具体的なNG配色（紫+金、ジオメトリックパターン）とOKパターン
- `feedback_seminar_emotion_logic_cycle.md` — 感情→論理サイクル設計、実績の分散配置
- `feedback_sales_copy_structure.md` — 6段階セールスコピー構造
- `feedback_seminar_slide_design_principles.md` — 聴衆の99%は「脳死」で見ている前提の設計原則
- `reference_slide_structure_template.md` — 16段構造テンプレート（Apple Keynote風）
- `seminar_design.md` — セミナー設計の原則（信頼ゼロからのスタート）

### 3. design-MCPテンプレート (`design-mcp-templates/`)
- `presentation.md` — プレゼンテーション生成テンプレート
- `sales-letter.md` — 感情ウェーブマップ付きセールスレター構造
- `english-school.md` — 英会話スクール特化テンプレート

### 4. CSS Design System v3 の決定プロセス
1. v2（Navy-Gold）をプロトタイプ → ケントから「海外っぽい」とNG
2. lp-corpusの教育LP分析から4つの配色プリセットを提示
3. **Online School Clean** を選択: White + Black + Orange (#e74f00)
4. 日本の教育LP（Discovering Sounds, RareJob, DMM英会話）を実地リサーチ
5. v3として `prototype.html` を作成 → レイアウト承認 → `index.html` 163枚に適用

## コーパスDB本体
SQLite DB（48MB）: `/Users/oidekento/lp-corpus/db/lp_corpus.db`
生HTML（3.2GB）: `/Users/oidekento/lp-corpus/raw_all/`
※ サイズが大きいためリポジトリには含めず。分析レポートのみ収録。

## design-MCP サーバー
ソース: `/Users/oidekento/design-mcp/`
corpus_lookupツールがlp_corpus.dbを参照し、ジャンル別のLP例と分析レポートを返す。
50社以上のデザインシステム（Apple, Stripe, Linear, Notion等）を参照データとして保持。
