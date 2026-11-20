#!/usr/bin/env bash
# Creates a fresh Gorman demo workspace with a Git baseline.
# Usage: demo/setup-demo-workspace.sh [target-dir] [stage]
#   stage: before (default) | instructions | library | ostrava | full
#   Each stage includes every earlier stage. Use a later stage to skip ahead when a live
#   AI step is slow or you only have 15 minutes.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-$HOME/gorman-mes-demo}"
STAGE="${2:-before}"

case "$STAGE" in
  before|instructions|library|ostrava|full) ;;
  *) echo "Unknown stage: $STAGE (use before|instructions|library|ostrava|full)" >&2; exit 2 ;;
esac

if [[ -e "$TARGET" ]]; then
  echo "Target already exists: $TARGET. Remove it or choose another path." >&2
  exit 2
fi

cp -R "$ROOT/gorman-sample-project" "$TARGET"
cd "$TARGET"
git init -q
git add .
git commit -qm "Baseline: Gorman plant OEE scripts (before HVE)"

overlay() { cp -R "$ROOT/$1/solution/." "$TARGET/"; }
commit() { git add . && git commit -qm "$1"; }

stages=(before instructions library ostrava full)
for s in "${stages[@]}"; do
  case "$s" in
    instructions) overlay 01-copilot-instructions; overlay 02-instruction-files
                  commit "Demo: Gorman baseline and instruction files" ;;
    library)      overlay 05-rpi-implement; commit "Demo: gorman_oee shared library" ;;
    ostrava)      overlay 07-rpi-agent-end-to-end; commit "Demo: Ostrava adapter" ;;
    full)         overlay 10-architecture-and-docs; overlay 13-custom-skills
                  overlay 14-custom-agents; overlay 17-team-adoption
                  commit "Demo: ADR, skills, KPI Steward agent, team settings" ;;
  esac
  [[ "$s" == "$STAGE" ]] && break
done

echo "Demo workspace ready at $TARGET (stage: $STAGE)"
git log --oneline
