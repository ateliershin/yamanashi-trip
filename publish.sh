#!/bin/zsh
# しおりを組み立てて GitHub に反映する。使い方: ./publish.sh "変更の説明"
set -e
cd "$(dirname "$0")"
python3 src/build.py
git add -A
if git diff --cached --quiet; then echo "変更なし"; exit 0; fi
git commit -q -m "${1:-しおりを更新}"
git push -q origin main
echo "GitHub に反映しました"
