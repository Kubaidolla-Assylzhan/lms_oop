from BOOK import Book
from libr import Library
from user import User

library = Library()

User1 = User(name="Alex")

book1 = Book(title="Harry Potter", author="Rowling", genre="fantastic")
book2 = Book(title="1972", author="Oruell", genre="kriminal")
book3 = Book(title="Queen's move", author="Uolter Tevis", genre="Drama")
book4 = Book(title="Almaty", author="Kanat", genre="bio")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

count = True

while count:
    print("Укажите команду \n")
    print("1. Список книг в библиотеке\n")
    print("2. Взять книгу\n")
    print("3. Показать список книг которые имеются у пользователя\n")
    print("4. Показать доступные книги {}\n")
    print("Если хотите остановить процесc введите OOP project library\n\n")
    otvet = int(input(""))
    if otvet == 9:
        count = False

    if otvet == 1:
        print(library.get_books())

    elif otvet == 2:
        print(library.get_available_books())
        q = library.get_books()
        w = User1.get_books()
        for i in range(len(q)):
            print(i,q[i])
        number = int(input("Выберите по индексу: "))
        if q[number] in w:
            print("Вы уже забрали эту книгу: ")
        else:
            print("Ползователь взял книгу под названием {}".format(q[number]))
        User1.get_book(q[number])

    elif otvet == 3:
        print(User1.get_books())

    elif otvet == 4:
        print(library.get_available_books())

