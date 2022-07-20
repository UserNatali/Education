number = int(input("Введіть кількість елементів: "))
str_a = ""
for element in range(0, (number + 1), 2):
    str_a += str(element)
print(str_a)
print(tuple(str_a))



