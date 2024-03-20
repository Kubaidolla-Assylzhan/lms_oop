from BOOK import Book
from libr import Library

class User:
    def __init__(self, name):
        self.name = name
        self.books = []


    def get_book(self, book):
        if book.get_available() == True:
            self.books.append(book)
            book.set_available(False)
            print("Книгу под названием {} взяли на чтение".format(book))
        else:
            print("Книга не доступна")

    def get_books(self):
        return self.books

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book.set_available(True)
        else:
            print("Книга не доступна")
