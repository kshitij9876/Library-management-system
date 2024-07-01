from models import Book
import storage


class BookManager:
    #Class for managing books in the library.
    def __init__(self):
        self._books = []
        self._storage = storage.load_books()

    def add_book(self, title, author, isbn):
        #Adds a new book to the library.
        if not any(book.isbn == isbn for book in self._books):
            book = Book(title, author, isbn)
            self._books.append(book)
            storage.save_books(self._books)
            print("Book added successfully.")
        else:
            print("Book with this ISBN already exists.")

    def list_books(self):
        #Lists all books in the library.
        if self._books:
            for book in self._books:
                print(book)
        else:
            print("No books available.")

    def find_books(self, **kwargs):
        #Finds books by given attributes.
        results = self._books
        for attr, value in kwargs.items():
            results = [book for book in results if getattr(book, attr, '').lower() == value.lower()]
        return results

    def update_book(self, isbn, **kwargs):
        #Updates the details of a book by ISBN.
        for book in self._books:
            if book.isbn == isbn:
                for key, value in kwargs.items():
                    if value is not None:
                        setattr(book, key, value)
                storage.save_books(self._books)
                print("Book updated successfully.")
                return
        print("Book not found.")

    def delete_book(self, isbn):
        #Deletes a book by ISBN.
        found = False
        for book in self._books:
            if book.isbn == isbn:
                self._books.remove(book)
                found = True
                break
        if found:
            storage.save_books(self._books)
            print("Book deleted successfully.")
        else:print("Book not Found.")
        return found
