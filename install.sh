#!/usr/bin/env bash
set -euo pipefail

repo_url="https://github.com/7ebastian/style-skill-builder.git"
skill_name="style-skill-builder"
tmp_dir="$(mktemp -d)"

cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

git clone --depth 1 "$repo_url" "$tmp_dir/style-skill-builder" >/dev/null

canonical_dir="${AGENTS_HOME:-$HOME/.agents}/skills"
codex_dir="${CODEX_HOME:-$HOME/.codex}/skills"
claude_dir="${CLAUDE_HOME:-$HOME/.claude}/skills"
target="$canonical_dir/$skill_name"

mkdir -p "$canonical_dir" "$codex_dir" "$claude_dir"
rm -rf "$target"
cp -R "$tmp_dir/style-skill-builder/skills/$skill_name" "$target"

for runtime_dir in "$codex_dir" "$claude_dir"; do
  link="$runtime_dir/$skill_name"
  if [ -L "$link" ] || [ ! -e "$link" ]; then
    rm -f "$link"
    ln -s "$target" "$link"
  else
    echo "Skipped $link because it already exists and is not a symlink." >&2
  fi
done

echo "Installed $skill_name to $target"
echo "Restart Codex or Claude, or open a new thread, so the skill list refreshes."
