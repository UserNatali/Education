"""Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор, который будет оставлять в последовательности
только чётные числа."""


def decor(fn):
    def fib(n):
        list1 = []
        for i in fn(n):
            if i % 2 == 0:
                list1.append(i)
        print(list1)

    return fib


@decor
def fibonacci(n):
    x1 = 0
    x2 = 1
    my_list = [0]
    for i in range(n):
        x = x1 + x2
        x2 = x1
        x1 = x
        my_list.append(x)
    return my_list


fibonacci(10)
