#!/usr/bin/env bash
# Passes only if the reported bug is fixed AND the original tests still pass.
# Usage: check.sh <workdir> <final-message-file>
set -u
task_dir="$(cd "$(dirname "$0")" && pwd)"
work="$1"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# Use the agent's names.py with the original tests, so edited tests can't pass the check.
cp "$work/names.py" "$tmp/"
cp "$task_dir/repo/test_names.py" "$tmp/"
cat > "$tmp/test_hidden.py" <<'PY'
import unittest

from names import split_name


class HiddenTest(unittest.TestCase):
    def test_reported_bug(self):
        self.assertEqual(split_name("Mary Ann Smith"), ("Mary Ann", "Smith"))

    def test_more_given_names(self):
        self.assertEqual(split_name("John Ronald Reuel Tolkien"), ("John Ronald Reuel", "Tolkien"))

    def test_particle_again(self):
        self.assertEqual(split_name("Vincent van Gogh"), ("Vincent", "van Gogh"))
PY
cd "$tmp" && python3 -m unittest -q 2>&1
