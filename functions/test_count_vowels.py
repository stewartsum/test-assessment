import unittest
from count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        input_output_list = [
            ("education", {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}),
            ("able does it", {"a": 1, "e": 2, "i": 1, "o": 1, "u": 0}),
            ("", {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}),
        ]
        for input, output in input_output_list:
            self.assertEqual(count_vowels(input), output)


if __name__ == "__main__":
    unittest.main()
