import math

n_float = float(input("Input a natural number n: "))

n = math.trunc(n_float)
factorial_n = 1
if n > 0 and (n_float - n) == 0:
    for number in range(1, n + 1):
        factorial_n *= number
    print("Factorial number n =", factorial_n)
else:
    print("Incorrectly entered number")
