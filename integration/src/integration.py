import sys
from imageTextExtraction import getText, removeSpecialCharacters
from get_boxes import extract_books
from get_book_data import get_book_details


def getBookTitles(pictures):
    # pictures is a file path

    _, book_pictures = extract_books(pictures)

    results_words = []
    for book_picture in book_pictures:
        results_words.append(removeSpecialCharacters(getText(book_picture)))

    results_words = [result for result in results_words if len(result) > 2]

    print("extracted this book info: ")
    print(results_words)

    results_api = []
    for words in results_words:
        results_api.append(get_book_details(words))

    return results_api
