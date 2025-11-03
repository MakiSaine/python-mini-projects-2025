class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.checked_out = False

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.num_pages} pages ({'Checked Out' if self.checked_out else 'Not Checked Out'})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        duplicate = next((b for b in self.books if b.title == book.title), None)
        if duplicate:
            print(f"The book '{book.title}' is already in the library.")
        else:
            self.books.append(book)
            print(f"Successfully added '{book.title}' to the library.")

    def remove_book(self, title):
        for index, book in enumerate(self.books):
            if book.title == title:
                if book.checked_out:
                    print(f"Cannot delete '{title}' while it is checked out.")
                    return
                del self.books[index]
                print(f"'{title}' has been removed from the library.")
                return
        print(f"No book found with the title '{title}'.")

    def check_out(self, title):
        book = next((b for b in self.books if b.title == title), None)
        if book:
            if book.checked_out:
                print(f"The book '{title}' is already checked out.")
            else:
                book.checked_out = True
                print(f"You have successfully checked out '{title}'.")
        else:
            print(f"'{title}' is not available in the library.")

    def check_in(self, title):
        book = next((b for b in self.books if b.title == title), None)
        if book:
            if not book.checked_out:
                print(f"The book '{title}' is already in the library.")
            else:
                book.checked_out = False
                print(f"'{title}' has been returned successfully.")
        else:
            print(f"No record of the book titled '{title}'.")

    def list_books(self):
        if not self.books:
            print("There are no books currently in the library.")
        else:
            print("Current library inventory:")
            for book in self.books:
                print(book)
