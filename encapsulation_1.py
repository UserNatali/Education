class Car:
    def __init__(self, model, color, weigth, body_type):
        self.model = model
        self.color = color
        self.weigth = weigth
        self.body_type = body_type

    def get_model(self):
        return print(self.model)

    def get_color(self):
        return print(self.color)

    def get_weigth(self):
        return print(self.weigth)

    def body_type(self):
        return print(self.body_type)

    def set_model(self, model_new):
        self.model = model_new
        return print(self.model)

    def set_color(self, color_new):
        self.color = color_new
        return print(self.color)

    def set_weigth(self, weigth_new):
        self.weigth = weigth_new
        return print(self.weigth)

    def set_body_type(self, body_type_new):
        self.body_type = body_type_new
        return print(self.body_type)




car1 = Car("Ford", "white", 500, "minivan")
car1.get_model()
car1.set_model("Volvo")
