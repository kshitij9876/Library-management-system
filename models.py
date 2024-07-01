class Item:
    #Base class for library items.
    def __init__(self, title, author):
        self._title = title  # Private attribute to store the title of the item
        self._author = author  # Private attribute to store the author of the item

    @property  #decorator - used to define a getter method for an attribute
    def title(self):
        return self._title  # Getter method to access the title attribute

    @property
    def author(self):
        return self._author  # Getter method to access the author attribute

    def __repr__(self):
        return f"Item(title='{self.title}', author='{self.author}')"  # String representation of the item

class Book(Item):
    #Class representing a book, inheriting from Item.
    def __init__(self, title, author, isbn):
        super().__init__(title, author)  # Call the constructor of the base class Item
        self._isbn = isbn  # Private attribute to store the ISBN of the book
        self._is_checked_out = False  # Private attribute to store the checkout status of the book

    @property
    def isbn(self):
        return self._isbn  # Getter method to access the ISBN attribute

    @property
    def is_checked_out(self):
        return self._is_checked_out  # Getter method to access the checkout status attribute

    @is_checked_out.setter
    def is_checked_out(self, value):
        self._is_checked_out = value  # Setter method to update the checkout status attribute

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', checked_out={self.is_checked_out})"  # String representation of the book

class User:
    #Class representing a library user.
    def __init__(self, name, user_id):
        self._name = name  # Private attribute to store the user's name
        self._user_id = user_id  # Private attribute to store the user's ID

    @property
    def name(self):
        return self._name  # Getter method to access the name attribute

    @property
    def user_id(self):
        return self._user_id  # Getter method to access the user ID attribute

    def __repr__(self):
        return f"User(name='{self.name}', user_id='{self.user_id}')"  # String representation of the user
