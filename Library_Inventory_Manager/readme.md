# Library Inventory Manager

A lightweight command-line application to help campus libraries manage their book inventory.  
It allows staff to add books, issue and return them, search the catalog, and store all records in a JSON file for persistence.

---

## 1. Project Overview

This project is built using Python and follows Object-Oriented Programming (OOP) principles.

Key design points:

- `Book` class represents individual books with attributes like title, author, ISBN, and status.
- `LibraryInventory` class manages a collection of books and handles file persistence using JSON.
- A menu-driven CLI in `cli/main.py` provides a simple interface for staff to interact with the system.
- Data is stored in `catalog.json` so that the catalog is preserved between program runs.

---

## 2. Features

- Add new books to the catalog
- Issue a book (mark as "issued")
- Return a book (mark as "available")
- View all books in the inventory
- Search books by title
- Persistent storage of books in `catalog.json`
- Basic error handling for missing or corrupted JSON file

---

## 3. Folder Structure

```text
library_inventory_manager/
│
├── catalog.json              # JSON file storing the current book catalog
│
├── library_manager/          # Core package
│   ├── __init__.py           # Package initializer
│   ├── book.py               # Book class
│   ├── inventory.py          # LibraryInventory class
│
├── cli/
│   ├── main.py               # Command-line interface (CLI)
│
├── tests/                    # (Optional) Unit tests
│   ├── test_inventory.py
│
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies (standard library)
└── .gitignore                # Files to ignore in Git
