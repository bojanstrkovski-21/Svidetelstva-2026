#!/bin/bash
set -euo pipefail

DEFAULTS_DIR="$HOME/Projects/session-defaults"

if [[ ! -d "$DEFAULTS_DIR" ]]; then
    echo "session-defaults not found at $DEFAULTS_DIR"
    exit 1
fi

echo "Syncing memory back to session-defaults..."

cp -r ./memory/. "$DEFAULTS_DIR/memory/"

cd "$DEFAULTS_DIR"
git add memory/
git diff --cached --quiet && echo "Nothing new to sync." && exit 0
git commit -m "sync: updates from $(basename $OLDPWD)"
git push

echo "Done. session-defaults is up to date."
