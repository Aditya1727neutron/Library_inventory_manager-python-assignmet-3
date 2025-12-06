from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    inventory = LibraryInventory()

    while True:
        print("\n=== Library Inventory System ===")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search by Title")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book added successfully.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                book.issue()
                inventory.save_data()
                print("Book issued.")
            else:
                print("Book not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                book.return_book()
                inventory.save_data()
                print("Book returned.")
            else:
                print("Book not found.")

        elif choice == "4":
            books = inventory.display_all()
            for b in books:
                print(b)

        elif choice == "5":
            keyword = input("Enter title: ")
            results = inventory.search_by_title(keyword)
            for b in results:
                print(b)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
