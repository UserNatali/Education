print("Solve the equation ax2 + bx + c = 0")
a = float(input("Input the coefficient a: "))
b = float(input("Input the coefficient b: "))
c = float(input("Input the coefficient c: "))

x_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a
x_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 / a
print(x_1)
print(x_2)
