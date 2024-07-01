# Library Management System

A simple Library Management System implemented in Python, utilizing Object-Oriented Programming principles. This system allows you to manage books and users, track book availability, and perform check-in and check-out operations.

## Features

#### 1. Manage Books: 
Add, update, delete, list, and search books by title, author, or ISBN.

#### 2. Manage Users: 
Add, update, delete, list, and search users by name or user ID.

#### 3. Check Out and Check-In Books: 
Track book availability and perform check-in and check-out operations.

#### 4. Logging: 
Simple logging of operations.

#### 5. File-Based Storage: 
Storage using JSON files.

#### 6. Modular and Scalable: 
Designed to be easily extendable.

## Code Overview

#### 1. models.py
Defines the class: Item, Book, and User.

Item: Base class for library items.

Book: Represents a book, inherits from Item.

User: Represents a library user.


#### 2. storage.py
Handles file-based storage for books and users using JSON.

Storage: Provides methods to load and save data.

#### 3. book_management.py
Manages book-related operations.

BookManager: Provides methods to add, update, delete, list, and search books.

#### 4. user_management.py

Manages user-related operations.

UserManager: Provides methods to add, update, delete, and list users.

#### 5. checkout_management.py
Manages check-out and check-in operations.

CheckoutManager: Provides methods to check out and check in books.

#### 6. main.py
The entry point of the application, provides the CLI.

Main Menu: Allows navigation between book management, user management, and check-out/check-in operations.
