import math

input("\n\t1. Площа трикутника \n\t2. Об'єм кулі \n\t3. Об'єм конуса")
x = int(input("Введіть 1, 2 або 3 "))

if x == 1:
    a = float(input("Введіть довжину основи трикутника: "))
    h = float(input("Введіть довжину висоти трикутника: "))
    if a > 0 and h > 0:
        s = round(1/2 * a * h)
        print(s)
    else:
        print("Неправильно введене значення")
elif x == 2:
    r = float(input("Введіть радіус кулі: "))
    if r>0:
        v = round(4/3 * math.pi * r ** 3)
        print(v)
    else:
        print("Неправильно введене значення")
elif x == 3:
    r = float(input("Введіть радіус основи конуса: "))
    h = float(input("Введіть висоту  конуса: "))
    if r > 0 and h > 0:
        v = round(1/3 * math.pi * h * r ** 2)
        print(v)
    else:
        print("Неправильно введене значення")
else:
    print("Введене значення не вірне")
