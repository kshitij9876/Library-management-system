from book_management import BookManager
from user_management import UserManager
from checkout_management import CheckoutManager


def main_menu():
    # Displays the main menu and returns the user's choice.
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Checkout Book")
    print("4. Check-in Book")
    print("5. Exit")
    return input("Enter choice: ")


def book_menu(book_manager):
    #Displays the book management menu and handles user input.
    print("\nBook Management")
    print("1. Add Book")
    print("2. List Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Return to Main Menu")
    choice = input("Enter choice: ")
    if choice == '1':
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        book_manager.add_book(title, author, isbn)
    elif choice == '2':
        book_manager.list_books()
    elif choice == '3':
        isbn = input("Enter ISBN of book to update: ")
        title = input("Enter new title (or press Enter to skip): ")
        author = input("Enter new author (or press Enter to skip): ")
        book_manager.update_book(isbn, title=title if title else None, author=author if author else None)
    elif choice == '4':
        isbn = input("Enter ISBN to delete: ")
        book_manager.delete_book(isbn)
    elif choice == '5':
        search_attr = input("Search by (title/author/isbn): ").lower()
        search_value = input(f"Enter {search_attr}: ")
        results = book_manager.find_books(**{search_attr: search_value})
        if results:
            for book in results:
                print(book)
        else:
            print("No books found.")
    elif choice == '6':
        return
    else:
        print("Invalid choice, please try again.")
    book_menu(book_manager)


def user_menu(user_manager):
    #Displays the user management menu and handles user input.
    print("\nUser Management")
    print("1. Add User")
    print("2. List Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Return to Main Menu")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        user_manager.add_user(name, user_id)
    elif choice == '2':
        user_manager.list_users()
    elif choice == '3':
        user_id = input("Enter user ID to update: ")
        name = input("Enter new name (or press Enter to skip): ")
        user_manager.update_user(user_id, name=name if name else None)
    elif choice == '4':
        user_id = input("Enter user ID to delete: ")
        user_manager.delete_user(user_id)
    elif choice == '5':
        return
    else:
        print("Invalid choice, please try again.")
    user_menu(user_manager)


def main():
    # function to initialize managers and display the main menu.
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager(book_manager)

    while True:
        choice = main_menu()
        if choice == '1':
            book_menu(book_manager)
        elif choice == '2':
            user_menu(user_manager)
        elif choice == '3':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_manager.checkout_book(user_id, isbn)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to check-in: ")
            checkout_manager.checkin_book(isbn)
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
