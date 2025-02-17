import json
import requests
from dotenv import load_dotenv
import os
from Book import Book

load_dotenv()


def getApiKey():
    api_key_from_env = os.getenv("LATP_API_KEY")
    return api_key_from_env


def get_book_details(book_name, max_results=1):
    """
    Fetches book details from Google Books API.

    :param book_name: The title of the book to search for.
    :param max_results: Number of results to return (default is 1).
    :return: A list of Book objects.
    """

    if getApiKey() is None:
        raise ValueError(
            "API key not set. Please set the API key before calling this function."
        )

    url = (
        f"https://www.googleapis.com/books/v1/volumes?q={book_name}"
        f"&maxResults={max_results}&printType=books&projection=full&key={getApiKey()}"
    )
    response = requests.get(url)
    data = response.json()

    if "items" not in data:
        return []

    books = []
    for item in data["items"]:
        volume_info = item.get("volumeInfo", {})

        title = volume_info.get("title", "Unknown Title")
        authors = ", ".join(volume_info.get("authors", ["Unknown Author"]))
        rating = volume_info.get("averageRating", "No rating available")
        synopsis = volume_info.get("description", "No synopsis available")
        coverImage = volume_info.get("imageLinks", {}).get(
            "thumbnail", "No image available"
        )

        book = {
            "title": title,
            "authors": authors,
            "rating": rating,
            "synopsis": synopsis,
            "coverImage": coverImage,
        }
        books.append(book)

    return books
