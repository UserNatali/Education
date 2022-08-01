class A:
    def __init__(self, b):
        self.b = b

    def method_a(self):
        print('A clas', self.b)


class B(A):
    def method_b(self):
        print('B clas', self.b)


class C(B):
    def method_c(self):
        print('C clas', self.b)


class D(C):
    def method(self):
        print('D clas', self.b)


obj = D(5)
obj.method()
obj.method_c()
obj.method_b()
obj.method_a()
