import unittest
from reverse_string import reverse_string


class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        input_output_list = [
            ("madam", "madam"),
            ("", ""),
            ("123.456", "654.321"),
        ]

        for input, output in input_output_list:
            self.assertEqual(reverse_string(input), output)


if __name__ == "__main__":
    unittest.main()
