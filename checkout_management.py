import storage


class CheckoutManager:
    #Class for managing book checkouts and check-ins.
    def __init__(self, book_manager):
        self._book_manager = book_manager
        self._checkouts = storage.load_checkouts()

    def checkout_book(self, user_id, isbn):
        #Checks out a book to a user.
        book = next((b for b in self._book_manager._books if b.isbn == isbn), None)
        if book and not book.is_checked_out:
            book.is_checked_out = True
            self._checkouts.append({"user_id": user_id, "isbn": isbn})
            storage.save_checkouts(self._checkouts)
            print("Book checked out successfully.")
        else:
            print("Book is either unavailable or already checked out.")

    def checkin_book(self, isbn):
        #Checks in a book to the library.
        for checkout in self._checkouts:
            if checkout['isbn'] == isbn:
                self._checkouts.remove(checkout)
                book = next((b for b in self._book_manager._books if b.isbn == isbn), None)
                if book:
                    book.is_checked_out = False
                    storage.save_checkouts(self._checkouts)
                    print("Book checked in successfully.")
                return
        print("Checkout record not found.")
