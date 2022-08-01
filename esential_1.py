class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def voice(self, voice_animal):
        self.voice_animal = voice_animal
        print(f'{self.color} {self.name}, age {self.age}, say {voice_animal}')


class Cat(Animal):
    def voice(self, voice_animal):
        print(f'{self.color} {self.name}, age {self.age}, meows {voice_animal}')

    def climbs_trees(self):
        print(f'{self.color} {self.name}, age {self.age}, climbs_trees')


class Dog(Animal):
    def voice(self, voice_animal):
       print(f'{self.color} {self.name}, age {self.age}, barks {voice_animal}')

    def runs(self):
        print(f'{self.color} {self.name}, age {self.age}, runs')


class Cow(Animal):
    def voice(self, voice_animal):
       print(f'{self.color} {self.name}, age {self.age}, is mooing {voice_animal}')

    def milk_it(self):
        print(f'{self.color} {self.name}, age {self.age}, milk it')


cat = Cat("Mesik", 5, "Blaсk")
cat.voice("meow-meow")
cat.climbs_trees()
dog = Dog("Rex", 3, "White")
dog.voice("gav-gav")
dog.runs()
cow = Cow("Rose", 2, "Brown")
cow.voice("mu - mu")
cow.milk_it()
