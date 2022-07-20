input("\n\t1. y = x2\n\t2. y = 2*|x| - 1\n\t3. y = 2x")

choice = input("Make a choice ")

if choice == "1":
    x = float(input("Input x in the range from -5 and to 5 "))
    if -5 <= x <= 5:
        y = x ** 2
        print("y = ", y)
    else:
        print("The value is not in the specified range")
elif choice == "2":
    x = float(input("Input x  is less than -5 "))
    if x < -5:
        y = 2 * abs(x) - 1
        print("y = ", y)
    else:
        print("The value is not in the specified range")
elif choice == "3":
    x = float(input("Input x  is more than more 5 "))
    if x > 5:
        y = x ** 2
        print("y = ", y)
    else:
        print("The value is not in the specified range")
else:
    print("The choice was made incorrectly")

'''Можна виконати простіше, з меншою кількістю рядків
x = int(input("Введите число X:"))

if -10 <= x <= 10:
    if -5 <= x <= 5:
        y = x ** 2
    elif x < -5:
        y = 2 * abs(x) - 1
    else:
        y = 2 * x

print("y =", y)
'''