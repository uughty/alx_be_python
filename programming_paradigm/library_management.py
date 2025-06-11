class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books and allows basic library operations."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds and checks out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"Sorry, '{title}' is not available or doesn't exist.")

    def return_book(self, title):
        """Finds and returns a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out or doesn't exist.")

    def list_available_books(self):
        """Prints all available books in the library."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books are currently available.")
        else:
            for book in available:
                print(f"{book.title} by {book.author}")
