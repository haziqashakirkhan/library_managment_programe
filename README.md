# Library Management System

A simple, command-line based Library Management System built in Python. This program allows users to manage library inventory, issue and return books, and generate basic library reports. It stores data in memory using Python lists and dictionaries during execution.

## Features

- **Add Book**: Add a new book to the library inventory by specifying the Book ID, Name, Author, and Quantity.
- **Display Books**: View a list of all books currently available in the library along with their details.
- **Issue Book**: Issue a book to a student by providing the Student Name and Book ID. Updates the available quantity automatically.
- **Return Book**: Return an issued book back to the library using the Book ID, incrementing the available stock.
- **Search Book**: Quickly find a book by searching for its exact title.
- **Report**: View a high-level summary of the library, including:
  - Total number of unique books
  - Total number of issued books
  - Total quantity of books available across the inventory

## Prerequisites

- Python 3.x installed on your system.

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the following command:

```bash
python task.py
```

4. Follow the on-screen prompts from the Main Menu to interact with the system.

## Usage

When you run the script, you will be presented with a main menu:

```
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. Display Books
3. Issue Book
4. Return Book
5. Search Book
6. Report
7. Exit
```

Type the number corresponding to the action you want to perform and press Enter.

## Note

This application stores data in memory. Any books added, issued, or returned will be lost when the program is closed. For persistent storage, you would need to integrate a database or file-handling system (like JSON or CSV).
