import json
from models import Book, User

# Filenames for storing data
BOOKS_FILE = 'books.json'
USERS_FILE = 'users.json'
CHECKOUTS_FILE = 'checkouts.json'


def load_books():
    #Loads books from the JSON file.
    try:
        with open(BOOKS_FILE, 'r') as file:
            data = json.load(file)
            k=[Book(**book) for book in data]
            
    except FileNotFoundError:
        return []


def save_books(books):
    #Saves books to the JSON file.
    with open(BOOKS_FILE, 'w') as file:
        json.dump([book.__dict__ for book in books], file, indent=4)


def load_users():
    #Loads users from the JSON file.
    try:
        with open(USERS_FILE, 'r') as file:
            data = json.load(file)
            k= [User(**user) for user in data]
            return k
    except FileNotFoundError:
        return []

def save_users(users):
    #Saves users to the JSON file.
    with open(USERS_FILE, 'w') as file:
        json.dump([user.__dict__ for user in users], file, indent=4)


def load_checkouts():
    #Loads checkouts from the JSON file.
    try:
        with open(CHECKOUTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_checkouts(checkouts):
    #Saves checkouts to the JSON file.
    with open(CHECKOUTS_FILE, 'w') as file:
        json.dump(checkouts, file, indent=4)
