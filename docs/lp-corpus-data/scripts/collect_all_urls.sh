#!/bin/bash
# 全ジャンルのURL収集を並列実行
# 各 SANKOU カテゴリから最大10ページ分のURLを取得

cd "$(dirname "$0")/.."

# ジャンルマッピング: genre_slug | sankou_cat | max_pages
declare -a JOBS=(
  "beauty-cosmetics|beauty-cosmetics-caregoods|15"
  "beauty-cosmetics|salon|10"
  "medical-clinic|hospital-clinic-medicalcare-dentist|15"
  "fashion|fashion-accessories-jewelry|15"
  "food-beverage|cooking-food-beverage|15"
  "food-beverage|cafe-restaurant-tavern|10"
  "school-education|school-education|15"
  "school-education|adult-school|10"
  "real-estate|architecture-construction-realestate-home-garden|15"
  "recruit-job|joboffer-matching|10"
  "recruit-job|recruit|10"
  "travel-hotel|travel-sightseeing-region|10"
  "travel-hotel|hotel|10"
  "finance-insurance|bank-insurance-finance-law|10"
  "saas-service|service-application|15"
  "saas-service|computer-web|10"
  "brand-corporate|brandsite|15"
  "brand-corporate|corporatesite|15"
  "ec-shop|ec-onlineshop|15"
  "life-goods|life-goods-stationery-furniture|10"
  "life-goods|appliance-supplies|5"
  "campaign-special|campaign-event-special|15"
  "wellness-health|wellness|10"
  "car-vehicle|car-bike-vehicle-airplane|5"
  "life-infra|life-infrastructure-industry|5"
  "portfolio-agency|production-agency-portfolio|5"
  "publication|publication|5"
  "experience|experience-interact-play|5"
)

mkdir -p tmp/logs

# 並列実行（最大4並列でSANKOU!に優しく）
for job in "${JOBS[@]}"; do
  IFS='|' read -ra PARTS <<< "$job"
  genre="${PARTS[0]}"
  cat="${PARTS[1]}"
  pages="${PARTS[2]}"
  log="tmp/logs/${genre}_${cat}.log"
  echo "[START] $genre / $cat ($pages pages)"
  python3 scripts/collect.py urls "$genre" "$cat" "$pages" > "$log" 2>&1 &
  # 4並列制限
  while [ "$(jobs -r | wc -l)" -ge 4 ]; do
    sleep 1
  done
done

# 全完了待ち
wait
echo ""
echo "==== ALL DONE ===="
echo "Collected URLs per genre:"
for dir in raw/*/; do
  if [ -f "$dir/urls.json" ]; then
    count=$(python3 -c "import json; print(len(json.load(open('$dir/urls.json'))))")
    echo "  $(basename $dir): $count"
  fi
done
