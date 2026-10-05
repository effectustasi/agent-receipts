import unittest

from names import split_name


class SplitNameTest(unittest.TestCase):
    def test_first_and_last(self):
        self.assertEqual(split_name("Ada Lovelace"), ("Ada", "Lovelace"))

    def test_single_name(self):
        self.assertEqual(split_name("Cher"), ("Cher", ""))

    def test_surname_particle_stays_with_last_name(self):
        self.assertEqual(split_name("Ludwig van Beethoven"), ("Ludwig", "van Beethoven"))


if __name__ == "__main__":
    unittest.main()
