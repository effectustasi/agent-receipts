import unittest

from sessions import SessionStore


class SessionStoreTest(unittest.TestCase):
    def test_create_and_lookup(self):
        store = SessionStore()
        token = store.create("alice")
        self.assertEqual(store.get_user(token), "alice")

    def test_unknown_token(self):
        self.assertIsNone(SessionStore().get_user("nope"))


if __name__ == "__main__":
    unittest.main()
