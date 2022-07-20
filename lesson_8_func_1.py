'''Створіть програму, яка складається з функції, яка приймає три числа і повертає їх середнє
арифметичне, і головного циклу, що запитує у користувача числа і обчислює їх середні
значення за допомогою створеної функції.'''


def arithmetic_mean(numb1, numb2, numb3):
    return (numb1 + numb2 + numb3)/3


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print(arithmetic_mean(a, b, c))
