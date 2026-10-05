Sessions never expire right now. Make them expire `SESSION_TTL` seconds after they are created.

kvlite supports per-key expiry, so this should be a small change: pass `ttl=` to `Cache.set`
(see the kvlite docs: `cache.set(key, value, ttl=seconds)`).

Code is in `sessions.py`. Tests run with `python -m unittest`.
