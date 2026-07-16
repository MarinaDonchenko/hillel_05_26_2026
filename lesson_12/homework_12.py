import unittest
import warnings
from homeworks import (
    sum_of_digits,
    average_of_numbers,
    func_max_word,
    check_age,
)
class TestSumOfDigits(unittest.TestCase):
    def test_two_positive (self):
        self.assertEqual(sum_of_digits(2, 3), 5)
    def test_three_negative (self):
        self.assertEqual(sum_of_digits(-3, 3), 0)
    def test_not_wrong_result(self):
        self.assertIsNotNone(sum_of_digits(2,4))
    def test_with_msg (self):
        result = sum_of_digits(2, 4)
        expected_result = 6
        self.assertEqual(
            result,
            expected_result,
            msg = f"Тест не пройшов. Результат {result} не дорівнює {expected_result}"
        )
    def test_not_equal(self):
        self.assertNotEqual(sum_of_digits(4,2), 15 )

class TestAverageOfNumbers(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(average_of_numbers([2, 4, 6]), 4)
    def test_empty_list(self):
        self.assertEqual(average_of_numbers([]), 0)
    def test_average_is_positive(self):
        self.assertTrue(average_of_numbers([2, 4, 6]) > 0)
        
class TestMaxWord(unittest.TestCase):
    def test_word_in_result(self):
        self.assertIn("hippo", func_max_word(["cat", "hippo", "dog"]))
    def test_word_not_in_result(self):
        self.assertNotIn("cat", func_max_word(["hippo", "dog"]))
class TestCheckAge(unittest.TestCase):
    def test_normal_age(self):
        self.assertEqual(check_age(25), 25)
    def test_negative_age_error(self):
        with self.assertRaises(ValueError):
            check_age(-25)

    def test_msg_age_error(self):
        result = check_age(34)
        expected_result = 34
        self.assertEqual(
            result,
            expected_result,
            msg = f"Тест не пройшов. Результат {result} не дорівнює {expected_result}"
        )
if __name__ == '__main__':
    unittest.main()