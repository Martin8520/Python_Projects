class Book:
    def __init__(self, b_title, b_author, b_isbn, b_available_copies, b_total_copies):
        self.title = b_title
        self.author = b_author
        self.isbn = b_isbn
        self.available_copies = int(b_available_copies)
        self.total_copies = int(b_total_copies)

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available Copies: {self.available_copies}/{self.total_copies}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print("Book not found.")

    def checkout_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available_copies > 0:
                    book.available_copies -= 1
                    print(f"Book '{book.title}' checked out successfully.")
                    return
                else:
                    print("All copies of this book are currently checked out.")
                    return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available_copies < book.total_copies:
                    book.available_copies += 1
                    print(f"Book '{book.title}' returned successfully.")
                    return
                else:
                    print("All copies of this book are already available.")
                    return
        print("Book not found.")

    def display_books(self):
        if self.books:
            print("Books in the Library:")
            for book in self.books:
                book.display_details()
                print("---------------------")
        else:
            print("No books available in the library.")
