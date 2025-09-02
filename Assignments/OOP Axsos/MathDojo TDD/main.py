import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        """Add one or more numbers"""
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        """Subtract one or more numbers"""
        self.result -= num
        for n in nums:
            self.result -= n
        return self



class TestMathDojo(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()

    # --- Tests for add ---
    def test_add_single_number(self):
        self.md.add(5)
        self.assertEqual(self.md.result, 5)

    def test_add_multiple_numbers(self):
        self.md.add(1, 2, 3)
        self.assertEqual(self.md.result, 6)

    def test_add_chaining(self):
        self.md.add(2).add(3, 4)
        self.assertEqual(self.md.result, 9)

    # --- Tests for subtract ---
    def test_subtract_single_number(self):
        self.md.subtract(5)
        self.assertEqual(self.md.result, -5)

    def test_subtract_multiple_numbers(self):
        self.md.subtract(2, 3, 5)
        self.assertEqual(self.md.result, -10)

    def test_subtract_chaining(self):
        self.md.subtract(1).subtract(2, 3)
        self.assertEqual(self.md.result, -6)

    # --- Combined tests ---
    def test_add_and_subtract_chain(self):
        x = self.md.add(2).add(2, 5, 1).subtract(3, 2).result
        self.assertEqual(x, 5)



if __name__ == "__main__":
    unittest.main()