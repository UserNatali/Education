class Base:
    def method(self):
        print("Hello from Base")


class Child(Base):
    def method(self):
        print("Hello from Child")


base = Base()
child = Child()
base.method()
child.method()
