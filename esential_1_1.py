class Carnew:
    def __init__(self, name):
        self.name = name

    def sale_cars(self, price):
        self.price = price
        print(f"A car {self.name} is for sale at a price of {price} $")



class Salon:
    def __init__(self, cars):
        self.cars = cars

    def sale_salon(self):
        cars_i = ""
        for i in cars:
           cars_i += i
        print(f"Sale {cars_i}")




car1 = Carnew("Audi ")
car2 = Carnew(" Skoda ")
car3 = Carnew("Nissan")
cars = [car1.name, car2.name, car3.name]

my_carDealership0 = Salon(cars)
my_carDealership0.sale_salon()

car1.sale_cars("200 000")

car2.sale_cars("100 000")
car3.sale_cars("250 000")

