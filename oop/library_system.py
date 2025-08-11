class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {super().__str__()}, File Size: {self.file_size} KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"Print Book: {super().__str__()}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only Book instances can be added to the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

# Example usage in library_system.py (optional)
if __name__ == "__main__":
    library = Library()
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    ebook1 = EBook("1984", "George Orwell", 500)
    print_book1 = PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 180)

    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(print_book1)

    library.list_books()