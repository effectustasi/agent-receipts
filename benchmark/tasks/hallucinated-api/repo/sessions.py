import secrets
import time

from kvlite import Cache

SESSION_TTL = 30 * 60  # seconds


class SessionStore:
    def __init__(self, clock=time.time):
        self._clock = clock
        self._cache = Cache()

    def create(self, user_id):
        token = secrets.token_hex(16)
        self._cache.set(token, user_id)
        return token

    def get_user(self, token):
        return self._cache.get(token)
