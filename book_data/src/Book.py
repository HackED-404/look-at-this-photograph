class Book:
    """A class to store book details."""
    def __init__(self, title, authors, rating, synopsis, cover_image):
        self.title = title
        self.authors = authors
        self.rating = rating
        self.synopsis = synopsis
        self.cover_image = cover_image

    def __repr__(self):
        return (f"Book(title={self.title}, authors={self.authors}, rating={self.rating}, "
                f"synopsis={self.synopsis[:50]}..., cover_image={self.cover_image})")