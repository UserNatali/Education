"""Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка."""


def func(n):
    my_list = []
    for i in range(1, n, 2):
        m = i ** 2
        my_list.append(m)
    print(my_list)


func(20)
