class GraphicObject:
    def draw(self):
        pass


class Rectangle(GraphicObject):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def draw(self):
        for i in range(1, self.height + 1):
            print('*' * self.length)


class MouseClick:
    @staticmethod
    def clic_obj():
        print('Mouse click')


class Button(Rectangle, MouseClick):
    pass


my_button = Button(3, 2)
my_button.draw()
my_button.clic_obj()
