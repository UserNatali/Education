'''Створіть список, введіть кількість його елементів і самі значення. Передбачити меню, в якому:
після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку, а після
натискання клавіші 2 – за зростанням'''
number = int(input("Введіть кількість елементів: "))

my_list = []
for i in range(number):
    valua = float(input("Введіть {} число: ".format(i + 1)))
    my_list.append(valua)

print(my_list)

y = input("Меню.\n1. Значення списка виведуться у зворотному порядку.\n2. Значення списка виведуться за зростанням.\n ")

if y == '1':
    list_new = []
    for k in range(-1, -(number + 1), -1):
       list_new.append(my_list[k])
    print(list_new)
elif y == '2':
    my_list.sort()
    print(my_list)
else:
    print("Невірний вибір")
