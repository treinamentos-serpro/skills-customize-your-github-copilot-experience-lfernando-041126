import unittest


def calculate_discount(price, percentage):
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= percentage <= 100:
        raise ValueError("percentage must be between 0 and 100")
    return round(price * (1 - percentage / 100), 2)


class TestCalculateDiscount(unittest.TestCase):
    def test_applies_discount(self):
        self.assertEqual(calculate_discount(100, 20), 80)


if __name__ == "__main__":
    unittest.main()