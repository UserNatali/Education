'''Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого
проміжку'''


def sum_recurtion(a, b):
    if a == b:
        return b
    else:
        return b + sum_recurtion(a, b - 1)


a = int(input("Введіть початок числового діапазону:"))
b = int(input("Введіть кінець числового діапазону:"))

print(sum_recurtion(a, b))
