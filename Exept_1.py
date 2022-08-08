"""Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе 
певне значення, і перехопіть цей виняток під час виклику функції."""""
class MyExcept(Exception):
    pass


def my_exept(number):
    try:
        if number <= 0:
            raise MyExcept("Значення негативне")
        print("Значення позитивне")
    except Exception as e:
        print(e)


def number_test():
    number = float(input("Введіть число: "))
    my_exept(number)


number_test()
