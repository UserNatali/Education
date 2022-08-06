class English:
    def greeting(self):
        print("Hello friend")


class Spanish:
    def greeting(self):
        print("Hola amigo")


def hello_friend():
    english = English()
    spanish = Spanish()
    english.greeting()
    spanish.greeting()


hello_friend()
