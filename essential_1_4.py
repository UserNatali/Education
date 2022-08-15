class Response:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return f"{self.response}"


class Book:
    def __init__(self, name, response):
        self.name = name
        self.response = response

    def __repr__(self):
        return f"{self.name}  \n Відгуки до книги\n {self.response}"


response1 = Response(["Чудова книга", "Варто прочитати", "Захоплюючий сюжет", "Читаючи книгу"])
book1 = Book("Захар Беркут", response1)
print(book1)


