from Book import book
from Fiction import fiction
from Nonfiction import nonfiction

books = {}


def add_book():
    title = input("Enter the title of the book you would like to add: ")
    author = input("Enter the author of the book: ")
    ISBN = input("Enter the ISBN: ")
    pub_date = input("Enter the publication date of the book: ")
    book = book(title, author, ISBN, pub_date)
    books.append(book)
    print(f"Book, {book}, added successfully.")

def borrow_book():
    book_to_borrow = input("Enter the title of the book you would like to borrow: ")
    if book_to_borrow in books and book_to_borrow.availability: # add in books?
        books.remove(book_to_borrow)
    else:
        print("This book is not available to be borrowed at this time.")


def return_book():
    book_to_return = input("Enter the title of the book you would like to return: ")
    if book_to_return in books:
        book = books[book_to_return]
        if not book.is_avilable(): # Come back to fix this, need to fix availability method
            book.set_availability(True)
            print(f"Book '{book.get_title()}' returned successfully.")
        else: 
            print("You did not borrow this book from the library.")

def search_book():
    title = input("Enter the title of the book you would like to search for: ")
    found = False
    for book in books.values():
        if book.get_title().lower == title.lower():
            found = True
            print(f"Book found: Title {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_ISBN}")
            break
        if not found:
            print("Book was not found in the database.")


def display_books():
    if books:
        for book in books.values():
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_isbn()}, Genre: {book.get_genre()}, Available: {'Yes' if book.is_available() else 'No'}")
    else:
        print("No books available at this time.")
