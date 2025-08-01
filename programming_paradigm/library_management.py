class Book:

    def __init__(self, title, author, is_checked_out=False) -> None:
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self) -> None:
        self._books = []

    def add_book(self, book):
        return self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if title == book.title:
                return self._books.remove(book)

    def return_book(self, title):
        for book in self._books:
            if title == book.title:
                return self._books.append(book)

    def list_available_books(self):
        for book in self._books:
            print(book)
