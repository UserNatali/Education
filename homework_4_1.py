import math

a_first = float(input("Input a: "))
b_first = float(input("Input b (b > a): "))

a = math.trunc(a_first)
b = math.trunc(b_first)

if a < b and (a_first - a) == 0 and (b_first - b) == 0:
    sum = 0
    for number in range(a, b + 1):
        if number > 0:
            sum += number
    print("sum = ", sum)
else:
    print("The entered numbers are incorrect")



