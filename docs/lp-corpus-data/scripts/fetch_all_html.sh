#!/bin/bash
# 全ジャンルのHTML取得を並列実行
# 各ジャンル30件ずつ取得（計約600件を実体取得）

cd "$(dirname "$0")/.."

LIMIT_PER_GENRE="${1:-30}"

mkdir -p tmp/fetch_logs

for dir in raw/*/; do
  genre=$(basename "$dir")
  if [ ! -f "$dir/urls.json" ]; then
    continue
  fi
  log="tmp/fetch_logs/${genre}.log"
  echo "[START] fetch $genre (limit=$LIMIT_PER_GENRE)"
  python3 scripts/collect.py fetch "$genre" "$LIMIT_PER_GENRE" > "$log" 2>&1 &
  # 6並列制限（外部サイトへのアクセスなので少し多めOK）
  while [ "$(jobs -r | wc -l)" -ge 6 ]; do
    sleep 2
  done
done

wait
echo ""
echo "==== FETCH DONE ===="
for dir in raw/*/html/; do
  if [ -d "$dir" ]; then
    count=$(ls "$dir"/*.html 2>/dev/null | wc -l | tr -d ' ')
    genre=$(basename $(dirname "$dir"))
    echo "  $genre: $count"
  fi
done
