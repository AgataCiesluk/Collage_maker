import unittest


def sum(a, b):
    return a + b


# pure Python
class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3, "Should be 3")

# assert sum(1, 2) == 4, "Should be 3"
