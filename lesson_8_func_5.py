'''Створіть програму-калькулятор, яка підтримує наступні операції: додавання, віднімання,
множення, ділення, зведення в ступінь, зведення до квадратного та кубічного коренів. Всі дані
повинні вводитися в циклі, доки користувач не вкаже, що хоче завершити виконання програми.
Кожна операція має бути реалізована у вигляді окремої функції. Функція ділення повинна
перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на
нуль.'''
import math


def sum_numb(a, b):
    return (a + b)


def diff_numb(a, b):
    return (a - b)


def product_numb(a, b):
    return a * b


def fraction_numb(a, b):
    if b != 0:
        return a / b



def exp_numb(a, b):
    return math.pow(a, b)


def square_root(a):
    return math.sqrt(a)


def cube_root(a):
    return a ** (1/3)


while True:
    operation = input("1. +\n2. -\n3. *\n4. /\n5. Піднесення до степеня\n6. Квадратний корінь\n7. Кубічний корінь\n8. Вихід\n")
    if operation in "1, 2, 3, 4, 5":
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        if operation == "1":
            print(sum_numb(a, b))
        elif operation == "2":
            print(diff_numb(a, b))
        elif operation == "3":
            print(product_numb(a, b))
        elif operation == "4":
            if b == 0:
                print("Cannot be divided by zero")
            else:
                print(fraction_numb(a, b))
        elif operation == "5":
            print(exp_numb(a, b))
    elif operation in "6, 7":
        a = float(input("Input number: "))
        if operation == "6":
            print(square_root(a))
        elif operation == "7":
            print(cube_root(a))
    elif operation == "8":
        break
    else:
        print("Wrong choice")





