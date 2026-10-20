import unittest
from src.sevcount import count_severe


class TestNone(unittest.TestCase):
    def test_none(self):
        self.assertEqual(count_severe(["fine line"]), 0)


if __name__ == "__main__":
    unittest.main()
