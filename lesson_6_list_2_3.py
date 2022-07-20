'''Простим називається число, яке ділиться націло лише на одиницю і на саме себе. Число 1 не
вважається простим. Напишіть програму, яка знаходить усі прості числа в заданому проміжку,
виводить їх на екран, а потім на вимогу користувача виводить їхню суму або добуток.'''

a = int(input("Input start of range: "))
b = int(input("Input end of range: "))

my_list = []
list_prime_number = []

for i in range(a, b):
    for n in range(2, i + 1):
        if i % n == 0:
            my_list.append(n)
    if len(my_list) == 1:
        list_prime_number.append(i)
    my_list.clear()

print(list_prime_number)

choice = input("1. Find the sum of primes in the range\n2. Find the product of primes in the range\n")

sum, product = 0, 1

for element in list_prime_number:
    sum += element
    product *= element

if choice == "1":
    print("Sum of primes in the range: ", sum)
elif choice == "2":
    print("Product of primes in the range: ", product)
else:
    print(" The choice is wrong " )

