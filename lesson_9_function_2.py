'''Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c. Усередині цієї
функції створити змінні x1, x2 зі значенням None (спочатку приймаємо, що рівняння не має
коренів) та функцію calc_rezult з формальними параметрами зовнішньої функції
quadratic_equation. Всередині функції calc_rezult здійснити пошук дискримінанта, згідно з
результатом якого зробити розрахунок коренів рівняння. Зовнішня функція quadratic_equation
має повернути перелік значень коренів квадратного рівняння. Надати можливість користувачеві
ввести з клавіатури формальні параметри для передачі їх у створену функцію
quadratic_equation, результати роботи функції відобразити на екрані'''
import math


def quadratic_equation(a, b, c):
    x1 = None
    x2 = None

    def calc_rezult(a, b, c):
        return b ** 2 - 4 * a * c

    if calc_rezult(a, b, c) < 0:
        return x1, x2
    elif calc_rezult(a, b, c) > 0 and a != 0:
        return round((-b + abs(math.sqrt(calc_rezult(a, b, c)))/ 2 / a), 2), round((-b - abs(math.sqrt(calc_rezult(a, b, c)))/ 2 / a), 2)
    elif calc_rezult(a, b, c) == 0 and a != 0:
        return round((-b / 2 / a), 2)
    else:
        print("На нуль ділити не можна")


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    quadratic_equation(a, b, c)
else:
    print(quadratic_equation(a, b, c))
