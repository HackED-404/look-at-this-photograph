import requests
from book_data.Book import Book

API_KEY = None

def get_book_details(book_name, max_results=1):
    """
    Fetches book details from Google Books API.

    :param book_name: The title of the book to search for.
    :param max_results: Number of results to return (default is 1).
    :return: A list of Book objects.
    """

    if API_KEY is None:
        raise ValueError("API key not set. Please set the API key before calling this function.")

    url = (f"https://www.googleapis.com/books/v1/volumes?q={book_name}"
           f"&maxResults={max_results}&printType=books&projection=full&key={API_KEY}")
    response = requests.get(url)
    data = response.json()

    if "items" not in data:
        return [Book(book_name, "Unknown Author", "Not found", "Not found", "No image available")]

    books = []
    for item in data["items"]:
        volume_info = item.get("volumeInfo", {})

        title = volume_info.get("title", "Unknown Title")
        authors = ", ".join(volume_info.get("authors", ["Unknown Author"]))
        rating = volume_info.get("averageRating", "No rating available")
        synopsis = volume_info.get("description", "No synopsis available")
        cover_image = volume_info.get("imageLinks", {}).get("thumbnail", "No image available")

        books.append(Book(title, authors, rating, synopsis, cover_image))

    return books