input("Solve the equation ax2 + bx + c = 0")

a = float(input("Input the coefficient a, except zero: "))
b = float(input("Input the coefficient b: "))
c = float(input("Input the coefficient c: "))

d = b ** 2 - 4 * a * c

if d < 0:
    print("The equation has no solutions")
elif d == 0:
    if a != 0:
        x = -b / 2 / a
        print("x = ", x)
    else:
        print("Сannot be divided by zero, the entered coefficient is incorrect")
else:
    if a != 0:
        print("The equation has two solution")
        x_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a
        x_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 / a
        print("x_1 = ", x_1)
        print("x_2 = ", x_2)
    else:
        print("Сannot be divided by zero, the entered coefficient is incorrect")

