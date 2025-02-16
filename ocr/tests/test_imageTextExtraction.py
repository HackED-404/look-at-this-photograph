import unittest

# filepath: /Users/ryanbott/Projects/look-at-this-photograph/ocr/tests/test_imageTextExtraction.py
from src.imageTextExtraction import removeSpecialCharacters, getText


class TestImageTextExtraction(unittest.TestCase):

    # def test_extract_text_from_image(self):
    #     # Example test case
    #     test_image_path = "path/to/test/image.png"
    #     expected_text = "Expected text from image"
    #     result = extract_text_from_image(test_image_path)
    #     self.assertEqual(result, expected_text)

    def test_removeSpecialCharacters_with_special_characters(self):
        input_text = "Hello, World!"
        expected_output = "Hello World"
        self.assertEqual(removeSpecialCharacters(input_text), expected_output)

    def test_removeSpecialCharacters_with_numbers_and_special_characters(self):
        input_text = "123@#Hello$%^456"
        expected_output = "123Hello456"
        self.assertEqual(removeSpecialCharacters(input_text), expected_output)

    def test_removeSpecialCharacters_with_only_special_characters(self):
        input_text = "@#$%^&*()"
        expected_output = ""
        self.assertEqual(removeSpecialCharacters(input_text), expected_output)

    def test_removeSpecialCharacters_with_no_special_characters(self):
        input_text = "Hello World"
        expected_output = "Hello World"
        self.assertEqual(removeSpecialCharacters(input_text), expected_output)

    def test_removeSpecialCharacters_with_empty_string(self):
        input_text = ""
        expected_output = ""
        self.assertEqual(removeSpecialCharacters(input_text), expected_output)

    def test_removeNewLineCharacter(self):
        input_text = "\n"
        expected_output = " "
        self.assertEqual(removeSpecialCharacters(input_text), expected_output)


if __name__ == "__main__":
    unittest.main()
