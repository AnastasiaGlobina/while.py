# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять
# информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно. Использовать модуль pickle
# для сериализации и десериализации объектов Python в бинарном формате.
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

    def save_def(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_def(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

# Создаем экземпляры класса Book
book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 448, "Давным-давно, в древнем городе Ершалаиме...")
book2 = Book("Война и мир", "Лев Толстой", 1225)
book3 = Book("Преступление и наказание", "Фёдор Достоевский", 671)

book1.save_def("book1.pkl")
book2.save_def("book2.pkl")
book3.save_def("book3.pkl")

loaded_book1 = Book.load_def("book1.pkl")
loaded_book2 = Book.load_def("book2.pkl")
loaded_book3 = Book.load_def("book3.pkl")

print("Загруженные книги:")
loaded_book1.read_book()
loaded_book2.read_book()
loaded_book3.read_book()