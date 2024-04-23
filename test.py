import unittest
from main import get_prime_number
from main import sum_of_digits


class TestGetPrimeNumber(unittest.TestCase):
    def test_get_prime_number(self):
        self.assertEqual(get_prime_number(1), 2)
        self.assertEqual(get_prime_number(2), 3)
        self.assertEqual(get_prime_number(5), 11)
        self.assertEqual(get_prime_number(10), 29)
        self.assertEqual(get_prime_number(99), 523)
        self.assertEqual(get_prime_number(10001), 104743)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_prime_number(0)
        with self.assertRaises(ValueError):
            get_prime_number(-5)
        with self.assertRaises(ValueError):
            get_prime_number(3.5)
        with self.assertRaises(ValueError):
            get_prime_number("abc")
        with self.assertRaises(ValueError):
            get_prime_number(None)


class TestSumOfDigitsOfPowerOfTwo(unittest.TestCase):
    def test_sum_of_digits_of_power_of_two(self):
        self.assertEqual(sum_of_digits(15), 26)
        self.assertEqual(sum_of_digits(4), 7)
        self.assertEqual(sum_of_digits(3), 8)
        self.assertEqual(sum_of_digits(1000), 1366)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sum_of_digits(-5)
        with self.assertRaises(ValueError):
            sum_of_digits(3.5)
        with self.assertRaises(ValueError):
            sum_of_digits("abc")
        with self.assertRaises(ValueError):
            sum_of_digits(None)
# Отлично, есть проверка типов, возвратов. Очень круто, что используются методы класса тестов

if __name__ == '__main__':
    unittest.main()
