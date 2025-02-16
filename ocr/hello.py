from ocr.src.imageTextExtraction import removeSpecialCharacters, getText

# If you don't have tesseract executable in your PATH, include the following:

# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

single_img_path = "single-book-spine.png"
multiple_books_path = "book-spine.png"
single_img_90_path = "book-spine-rotate-side.png"

print("fixed rotated image")
print(removeSpecialCharacters(getText(single_img_90_path)))
print(removeSpecialCharacters(getText(single_img_path)))
