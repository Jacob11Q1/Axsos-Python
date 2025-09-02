import unittest

# 1) reverseList
def reverseList(arr):
    # reverse in place (no extra array)
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# 2) isPalindrome
def isPalindrome(word):
    return word == word[::-1]

# 3) coins
def coins(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    return [quarters, dimes, nickels, pennies]

# BONUS 4) factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# BONUS 5) fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# ============================
# TEST CASES
# ============================

class TestAlgorithms(unittest.TestCase):
    # reverseList
    def test_reverseList_basic(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])
    def test_reverseList_even(self):
        self.assertEqual(reverseList([1, 2, 3, 4]), [4, 3, 2, 1])
    def test_reverseList_single(self):
        self.assertEqual(reverseList([7]), [7])
    def test_reverseList_empty(self):
        self.assertEqual(reverseList([]), [])

    # isPalindrome
    def test_isPalindrome_racecar(self):
        self.assertTrue(isPalindrome("racecar"))
    def test_isPalindrome_level(self):
        self.assertTrue(isPalindrome("level"))
    def test_isPalindrome_single(self):
        self.assertTrue(isPalindrome("a"))
    def test_isPalindrome_false(self):
        self.assertFalse(isPalindrome("hello"))
    def test_isPalindrome_madam(self):
        self.assertTrue(isPalindrome("madam"))

    # coins 
    def test_coins_87(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])
    def test_coins_41(self):
        self.assertEqual(coins(41), [1, 1, 1, 1])
    def test_coins_99(self):
        self.assertEqual(coins(99), [3, 2, 0, 4])
    def test_coins_0(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])
    def test_coins_5(self):
        self.assertEqual(coins(5), [0, 0, 1, 0])

    # factorial
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

    # fibonacci
    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5)
    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(4), 3)
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)


if __name__ == "__main__":
    unittest.main()