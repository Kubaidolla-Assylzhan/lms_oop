from BOOK import Book

class Library:
    def __init__(self):
        self.book_storage = []

    def add_book(self, new_book):
        self.book_storage.append(new_book)
        new_book.set_available(True)

    def remove_book(self, book):
        self.book_storage.remove(book)
        book.set_available(False)

    def get_books(self):
        return self.book_storage

    def get_available_books(self):
        result = []
        for i in range(len(self.book_storage)):
            if self.book_storage[i].get_available() is True:
                result.append(self.book_storage[i])
        return result


    def search_of_genre(self, genre):
        result = []
        for i in range(len(self.book_storage)):
            if self.book_storage[i].genre == genre:
                result.append(self.book_storage[i])
        return result
