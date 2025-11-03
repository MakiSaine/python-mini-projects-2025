from library import Book, Library

def library_script():
    my_library = Library()

    book_a = Book("Brave New World", "Aldous Huxley", 311)
    my_library.add_book(book_a)
    book_b = Book("The Catcher in the Rye", "J.D. Salinger", 277)
    my_library.add_book(book_b)
    book_c = Book("Moby Dick", "Herman Melville", 635)
    my_library.add_book(book_c)
    book_d = Book("Pride and Prejudice", "Jane Austen", 279)
    my_library.add_book(book_d)
    book_e = Book("Fahrenheit 451", "Ray Bradbury", 194)
    my_library.add_book(book_e)

    print("\nLibrary Collection:")
    my_library.list_books()

    print("\nChecking out 'Moby Dick'")
    my_library.check_out("Moby Dick")

    print("\nTrying to check out 'Moby Dick' again")
    my_library.check_out("Moby Dick")

    print("\nBooks After Checkout:")
    my_library.list_books()

    print("\nTrying to remove 'Moby Dick' while checked out")
    my_library.remove_book("Moby Dick")

    print("\nReturning 'Moby Dick'")
    my_library.check_in("Moby Dick")

    print("\nRemoving 'Moby Dick' after return")
    my_library.remove_book("Moby Dick")

    print("\nRemoving a book that doesn't exist")
    my_library.remove_book("The Invisible Man")

    print("\nFinal Library Listing:")
    my_library.list_books()

if __name__ == "__main__":
    library_script()
