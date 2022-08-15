class Book:
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.name}, {self.author}, {self.year}, {self.genre}"

    def __repr__(self):
        return f"[{self.name}, {self.author}, {self.year}, {self.genre}]"

    def __eq__(self, other):
        return self.author == other.author


book1 = Book("Захар Беркут", "Іван Франко", 1991, "Історична повість")
book2 = Book("Таємничий острів", "Жюль Верн", 2005, "Фантастика")
book3 = Book("Собака Баскервілів", "Артур Конан Дойль", 2007, "Детектив")
book4 = Book("Людина", "Ольга Кобилянська", 1998, "Повість")

print(book1.__str__())
books = [book1, book2, book3, book4]
print(books)

print(book1 == book2)
