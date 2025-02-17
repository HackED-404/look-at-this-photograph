class Book:
    """A class to store book details."""

    def __init__(self, title, authors, rating, synopsis, coverImage):
        self.title = title
        self.authors = authors
        self.rating = rating
        self.synopsis = synopsis
        self.coverImage = coverImage

    def __repr__(self):
        return (
            f"Book(title={self.title}, authors={self.authors}, rating={self.rating}, "
            f"synopsis={self.synopsis[:50]}..., coverImage={self.coverImage})"
        )
