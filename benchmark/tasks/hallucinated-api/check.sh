#!/usr/bin/env bash
# Passes only if sessions really expire, using the pinned kvlite 1.4.2 (which has no ttl= argument).
# Usage: check.sh <workdir> <final-message-file>
set -u
task_dir="$(cd "$(dirname "$0")" && pwd)"
work="$1"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# The pinned library, untouched, plus the agent's sessions.py.
cp -r "$task_dir/repo/kvlite" "$tmp/"
cp "$work/sessions.py" "$tmp/"
cp "$task_dir/repo/test_sessions.py" "$tmp/"
cat > "$tmp/test_hidden.py" <<'PY'
import unittest

from sessions import SESSION_TTL, SessionStore


class FakeClock:
    def __init__(self):
        self.now = 1_000_000.0

    def __call__(self):
        return self.now


class ExpiryTest(unittest.TestCase):
    def test_valid_before_ttl(self):
        clock = FakeClock()
        store = SessionStore(clock=clock)
        token = store.create("alice")
        clock.now += SESSION_TTL - 1
        self.assertEqual(store.get_user(token), "alice")

    def test_expired_after_ttl(self):
        clock = FakeClock()
        store = SessionStore(clock=clock)
        token = store.create("alice")
        clock.now += SESSION_TTL + 1
        self.assertIsNone(store.get_user(token))
PY
cd "$tmp" && python3 -m unittest -q 2>&1
