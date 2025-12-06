import json
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self, filepath="catalog.json"):
        self.filepath = Path(filepath)
        self.books = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        return self.books

    def save_data(self):
        try:
            data = [book.to_dict() for book in self.books]
            with self.filepath.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Error saving data:", e)

    def load_data(self):
        try:
            if not self.filepath.exists():
                self.filepath.write_text("[]", encoding="utf-8")
                return

            content = self.filepath.read_text(encoding="utf-8")
            data = json.loads(content)

            self.books = []
            for item in data:
                book = Book(
                    item["title"],
                    item["author"],
                    item["isbn"],
                    item.get("status", "available")
                )
                self.books.append(book)

        except json.JSONDecodeError:
            print("Corrupted JSON. Resetting file.")
            self.filepath.write_text("[]", encoding="utf-8")
            self.books = []
