---
name: Lisaセミナー スライドデザイン検証
description: 3つのスライド生成手法（frontend-slides/Marp/Canva AI Connector）の比較テスト状況
type: project
---

## 概要
Lisa×Masaセミナー（4/19）「脱・通じない英語｜発音を身につけ、"話せる自分へ"」のスライド制作。

## デプロイURL
- 本番: https://deploy-masaenglish.vercel.app
- ローカル最新（本番より新しい）: `/Users/oidekento/Projects/frontend-slides-test/deploy/index.html`

## テスト用スライド（3枚共通）
1. タイトル「Lisa×Masa 英語脳覚醒セミナー」/ 発音から始める本当の英語力 / 4/19(日) 20:00~
2. インパクト「脳は自分が出せる音しか聞き取れない」
3. 受講生実績「Kaoriさん」Before: 10社コーチング全部ダメ → After: 英語で仕事するレベルまで復活

## テスト結果

### 1. frontend-slides（HTML/CSS）— 完了 ★最高品質
- 場所: `/Users/oidekento/Projects/frontend-slides-test/test-lisa-seminar.html`
- 865行の単一HTML。CSS/JSインライン。ゼロ依存
- パーティクルアニメーション、スクロールトリガー、キーボード/スワイプ対応
- けんとさん評価: 「レイアウトめっちゃいい。PPTXより全然きれい。画像入れたら完璧」
- 配色は改善余地あり

### 2. Marp + CSSテーマ — 完了
- 場所: `/Users/oidekento/Projects/marp-test/test-lisa-seminar.html` / `.pdf`
- Markdown 1ファイルで管理。1コマンドでPDF/HTML出力
- デザイン品質: 高いがfrontend-slidesには劣る
- 大量スライド管理には最適

### 3. Canva AI Connector — 未テスト（次セッションで実行）
- Claude.ai → Settings → Connectors → Canva: **接続済み**
- claude.aiのWebチャットでCanva ONにしてテストプロンプトを投げる
- テストプロンプト:
```
セミナーのプレゼンテーションスライドを3枚作成してください。
テーマ: 英語セミナー
配色: ネイビー(#2A274E)とゴールド(#EBCC58)
スライド1: タイトル「Lisa×Masa 英語脳覚醒セミナー」サブタイトル「発音から始める本当の英語力」日付「4/19(日) 20:00~」
スライド2: インパクトスライド「脳は自分が出せる音しか聞き取れない」
スライド3: 受講生実績「Kaoriさん」Before: 10社もコーチングを受けて全部ダメ → After: 英語で仕事するレベルまで復活
```

## 現行スライド（pptxgenjs）の状況
- 場所: `/Users/oidekento/Projects/seminar-slides/output/lisa_seminar.pptx`（144枚）
- 構成: 全8Phase、感情→論理サイクル設計、実績6人分を序盤/中盤/終盤に分散
- QA結果: 総合6.4/10。CRITICAL修正済み（CTA不可視バグ）
- 実績データ: Instagramから取得した実データ + Canvaから確認した実名6人

## Canva MCP 調査結果
- 3種類ある: AI Connector（本命）/ Dev MCP（開発者向け）/ Connect API
- AI Connector: Pro以上でBrand Kit自動適用。素材は生成時にAIが選択
- 要素レベル編集はAPI経由では不可。生成→Canvaで微調整のワークフロー
- テンプレートベースの自動入力はEnterprise限定

**Why:** pptxgenjsのデザイン品質（6.4/10）を上げるための手法比較。frontend-slidesが現時点で最有力。
**How to apply:** 次セッションでCanvaテスト完了後、最終的な手法を決定してフル生成に移行。
