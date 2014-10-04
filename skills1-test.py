import unittest


from skillsmapreducefilter import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
        self.word_list = ["What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

    ### Tests - 11 total

    def test_all_odd(self):
        self.assertEqual(all_odd(self.number_list), [-5, 15, 23, 7])

    def test_all_even(self):
        self.assertEqual(all_even(self.number_list), [6,4,8,16,42,2])

    def test_long_words(self):
        self.assertEqual(long_words(self.word_list), ["What", "about", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "spam"])

    def test_smallest(self):
        self.assertEqual(smallest(self.number_list), -5)

    def test_largest(self):
        self.assertEqual(largest(self.number_list), 42)

    def test_halvsies(self):
        self.assertEqual(halvesies(self.number_list), [-2.5, 3.0, 2.0, 4.0, 7.5, 8.0, 11.5, 21.0, 1.0, 3.5])

    def test_word_lengths(self):
        self.assertEqual(word_lengths(self.word_list),[4, 5, 3, 4, 7, 4, 4, 5, 4, 6, 3, 4])

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(self.number_list), 118)

    def test_mult_numbers(self):
        self.assertEqual(mult_numbers(self.number_list), -3115929600)

    def test_join_strings(self):
        self.assertEqual(join_strings(self.word_list), "What about the Spam sausage spam spam bacon spam tomato and spam")

    def test_average(self):
        self.assertEqual(average(self.number_list), 11.8)


if __name__ == '__main__':
    unittest.main()