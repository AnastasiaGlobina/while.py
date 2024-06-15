# Создайте класс «Книга», который имеет атрибуты название, автор и количество страниц.
# Добавьте методы для чтения и записи книги.

import pickle

class Book:
    def __init__(self, title, author, pages, content=""):
        self.title = title
        self.author = author
        if isinstance(pages, int) and pages > 0:
            self.pages = pages
        else:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.content = content

    def read_book(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Количество страниц: {self.pages}")
        if self.content:
            print("Содержание:\n", self.content)
        else:
            print("Содержание не добавлено.")

    def update_book(self, title=None, author=None, pages=None, content=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if pages is not None:
            if isinstance(pages, int) and pages > 0:
                self.pages = pages
            else:
                raise ValueError("Количество страниц должно быть положительным целым числом")
        if content is not None:
            self.content = content

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def books_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def books_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def display_books(self):
        if not self.books:
            print("В библиотеке нет книг.")
        else:
            for book in self.books:
                print(book)

    def save_library(self, filename="library.pkl"):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)


    def load_library(filename="library.pkl"):
        with open(filename, 'rb') as f:
            return pickle.load(f)


if __name__ == "__main__":
    my_library = Library()
    my_library.add_book(
        Book("Мастер и Маргарита", "Михаил Булгаков", 448, "Давным-давно, в древнем городе Ершалаиме..."))
    my_library.add_book(Book("Война и мир", "Лев Толстой", 1225))
    my_library.add_book(Book("Преступление и наказание", "Фёдор Достоевский", 671))

    print("Все книги в библиотеке:")
    my_library.display_books()

    user_input = input("\nВведите название книги или фамилию автора для поиска: ")

    books_found = my_library.books_title(user_input)
    if not books_found:
        books_found = my_library.books_author(user_input)

    if books_found:
        print("\nНайденные книги:")
        for book in books_found:
            print(book)
            book.read_book()
    else:
        print("\nКниг не найдено по вашему запросу.")

    my_library.save_library()