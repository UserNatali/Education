'''Створіть дві функції, що обчислюють значення певних алгебраїчних виразів. На екрані виведіть
таблицю значень цих функцій від -5 до 5 з кроком 0.5.'''


def func1(x_val):
    return round((18 * x_val ** 2/ (x_val ** 2 - 56)), 2)


def func2(x_val):
    return round((x_val ** 2 - 3 * x_val + 1), 2)


func_choice = input("Input number function 1 or 2: ")

x = -5
while -5 <= x <= 5:
    if func_choice == "1":
        y = func1(x)
        print("function1(", x,")=", y)
        x += 0.5
    elif func_choice == "2":
        y = func2(x)
        print("function2(", x,")=", y)
        x += 0.5

