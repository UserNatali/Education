
import math


def sum_numb(a, b):
    return (a + b)


def diff_numb(a, b):
    return (a - b)


def product_numb(a, b):
    return a * b


def fraction_numb(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ZeroDivisionError")


def exp_numb(a, b):
    try:
        return math.pow(a, b)
    except ValueError:
        print("ValueError")


while True:
    operation = input("1. +\n2. -\n3. *\n4. /\n5. Піднесення до степеня\n6. Вихід\n")
    if operation in "1, 2, 3, 4, 5":
        try:
            a = float(input("Input first number: "))
            b = float(input("Input second number: "))
        except ValueError:
            print("ValueError")
        if operation == "1":
            print(sum_numb(a, b))
        elif operation == "2":
            print(diff_numb(a, b))
        elif operation == "3":
            print(product_numb(a, b))
        elif operation == "4":
            print(fraction_numb(a, b))
        elif operation == "5":
            print(exp_numb(a, b))
        elif operation == "6":
            break
    else:
        print("Wrong choice")
