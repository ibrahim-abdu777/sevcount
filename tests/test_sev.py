import unittest
from src.sevcount import count_severe


class TestSev(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(count_severe(["all good", "ERROR bad", "fatal: x"]), 2)


if __name__ == "__main__":
    unittest.main()
