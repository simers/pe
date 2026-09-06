#!/usr/bin/env bash
#
# build.sh — rebuild the LBO model and the course handbook.
#
#   ./build.sh              rebuild model + handbook
#   ./build.sh --install    install deps first (pip + playwright chromium), then build
#   ./build.sh model        rebuild only the model
#   ./build.sh handbook     rebuild only the handbook
#
set -euo pipefail
cd "$(dirname "$0")"

if [[ "${1:-}" == "--install" ]]; then
  echo "==> Installing dependencies..."
  pip install -r requirements.txt
  playwright install chromium
  shift || true
fi

build_model()    { echo "==> Building LBO model...";      python3 build_model.py; }
build_handbook() { echo "==> Building handbook (PDF)..."; python3 build_handbook.py; }

case "${1:-all}" in
  model)    build_model ;;
  handbook) build_handbook ;;
  all)      build_model; build_handbook ;;
  *) echo "usage: ./build.sh [--install] [all|model|handbook]"; exit 1 ;;
esac

echo "==> Done."
echo "    Model:    Cascade_Components_LBO_Model.xlsx"
echo "    Handbook: pe_course_handbook.pdf"
