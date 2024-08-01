from Book import book
from Fiction import fiction
from Nonfiction import nonfiction

books = {}


def add_book():
    title = input("Enter the title of the book you would like to add: ")
    author = input("Enter the author of the book: ")
    ISBN = input("Enter the ISBN: ")
    pub_date = input("Enter the publication date of the book: ")
    genre = input("Enter the genre of the book: ")
    
    new_book = book(title, author, ISBN, pub_date, genre)
    books[ISBN] = new_book
    print(f"Book, {title}, added successfully.")

def borrow_book():
    ISBN = input("Enter the ISBN of the book you would like to borrow: ")
    if ISBN in books:
        book = books[ISBN]
        if book.is_available():
            book.set_availability(False)
            print(f"Book {book.get_title()}' borrowed successfully.")
        else:
            print("This book is not available to be borrowed at this time.")
    else:
        print("Book is not in the database.")


def return_book():
    ISBN = input("Enter the ISBN of the book you would like to return: ")
    if ISBN in books:
        book = books[ISBN]
        if not book.is_available():
            book.set_availability(True)
            print(f"Book '{book.get_title()}' returned successfully.")
        else: 
            print("You did not borrow this book from the library.")
    else: 
        print("Book was not found in the database.")

def search_book():
    isbn = input("Enter the isbn of the book you would like to search for: ")
    found = False
    for book in books.values():
        if book.get_ISBN() == isbn:
            found = True
            print(f"Book found: Title {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_ISBN()}")
            break
        if not found:
            print("Book was not found in the database.")


def display_books():
    if books:
        for book in books.values():
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_ISBN()}, Genre: {book.get_genre()}, Available: {'Yes' if book.is_available() else 'No'}")
    else:
        print("No books available at this time.")
