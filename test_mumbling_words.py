import unittest
import mumbling_words

class TestMumblingWords(unittest.TestCase):

    def setUp(self):
        self.mumbling_words = mumbling_words.MumblingWords()

    def test_return_string(self):
        self.assertEqual("",self.mumbling_words.mumble_letters(""))

    def test_return_capital(self):
        self.assertEqual("A",self.mumbling_words.mumble_letters("a"))

    def test_return_repeated_for_position_two(self):
        self.assertEqual("A-Bb",self.mumbling_words.mumble_letters("ab"))
    
    def test_letters_separated_non_capital_repeat(self):
        self.assertEqual("A-Bb-Ccc",self.mumbling_words.mumble_letters("abC"))

    def test_return_three_repeated_letters(self):
        self.assertEqual("A-Bb-Ccc-Dddd",self.mumbling_words.mumble_letters("aBCd"))

    def test_return_formatted_when_input_is_capitalised(self):
        self.assertEqual("Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy",self.mumbling_words.mumble_letters("QWERTY"))

    
