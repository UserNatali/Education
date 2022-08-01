class Transport:
    def __init__(self, model, color, weight):
        self.model = model
        self.color = color
        self.weight = weight


class Car(Transport):
    def __init__(self, model, color, weight, characteristic_car):
        super().__init__(model, color, weight)
        self.characteristic_car = characteristic_car

    def __str__(self):
        return print(f"Car model {self.model}, color {self.color}, weight {self.weight},"
                     f" characteristic_car {self.characteristic_car}")


class AirPlane(Transport):
    def __init__(self, model, color, weight, fuselage_size):
        super().__init__(model, color, weight)
        self.fuselage_size = fuselage_size

    def __str__(self):
        return print(f"AirPlane model {self.model}, color {self.color}, weight {self.weight}, "
                     f"fuselage_size {self.fuselage_size}")


car1 = Car("Ford", "black", "500 kg", 15)
car1.__str__()

airPlane1 = AirPlane("Aн-170", "white", "3000 kg", 130)
airPlane1.__str__()
