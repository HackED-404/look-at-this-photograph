import unittest
import cv2

# filepath: /Users/ryanbott/Projects/look-at-this-photograph/ocr/tests/test_imageTextExtraction.py
from src.imageTextExtraction import removeSpecialCharacters, getText


class TestImageTextExtraction(unittest.TestCase):

    def test_extract_text_from_image_bottom_to_top(self):
        # Example test case
        # paths need to be from package root
        test_image_path = "tests/images/book-bottom-to-top.png"
        expected_contained_text = "bewilderment"

        # need a numpy image array to pass to getText
        numpy_image_array = cv2.imread(test_image_path)

        result = getText(numpy_image_array)
        self.assertIn(expected_contained_text.lower(), result.lower())

    def test_extract_text_from_image_top_to_bottom(self):
        test_image_path = "tests/images/book-top-to-bottom.png"
        expected_contained_text = "bewilderment"

        numpy_image_array = cv2.imread(test_image_path)

        result = getText(numpy_image_array)
        self.assertIn(expected_contained_text.lower(), result.lower())

    def test_extract_text_from_image_right_to_left(self):
        test_image_path = "tests/images/book-right-to-left.png"
        expected_contained_text = "bewilderment"

        numpy_image_array = cv2.imread(test_image_path)

        result = getText(numpy_image_array)
        self.assertIn(expected_contained_text.lower(), result.lower())

    def test_extract_text_from_image_left_to_right(self):
        test_image_path = "tests/images/book-left-to-right.png"
        expected_contained_text = "bewilderment"

        numpy_image_array = cv2.imread(test_image_path)

        result = getText(numpy_image_array)
        self.assertIn(expected_contained_text.lower(), result.lower())

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
