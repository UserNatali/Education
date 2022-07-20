'''Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового
списку new_list. Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть
дублювання списку new_list, repeat кількість разів. Очистіть список int_list.'''
int_list = [3, 5, 56, 18, 7, 15, 5, 25, 64, 11, 50, 19]
new_list = []
for element in int_list:
    if element % 2 != 0:
        new_list.append(element)
print(new_list)

repeat = int(input("Input repeat: "))
for i in range(repeat):
    new_list_copy = new_list.copy()
    print(new_list_copy)

int_list.clear()
print(int_list)

'''Для цього завдання вихідний список значень беремо з підсумкового списку new_list додаткового 
завдання 2. Користувач вводить з клавіатури значення; якщо таке є у списку — вивести кількість 
його повторів та його позицію у цьому списку.'''
number = int(input("Input natural number: "))
print(new_list)

list_index = []
if new_list.count(number) != 0:
    k = 0
    el = 0
    print("Count of number: ", new_list.count(number))
    print("Index number: ", end=" ")

    while el < len(new_list):
        if new_list[el:len(new_list)].count(number) != 0:
            k = new_list.index(number, el, len(new_list))
            list_index.append(k)
            el = k + 1
        else:
            break
    print(list_index)
else:
    print("Number is not list")

'''Попереднє завдання, перероблене з рекурсією'''

number = int(input("Input natural number: "))
new_list = [3, 5, 56, 18, 7, 15, 5, 25, 56, 11, 50, 56]
print(new_list)

if new_list.count(number) == 0:
    print("Number is not list")
else:
    print("Count of number: ", new_list.count(number))
    print("Index number: ", end=" ")


def index_number(first_index):
    if new_list[first_index:len(new_list)].count(number) != 0:
        index = new_list.index(number, first_index, len(new_list))
        print(index, end=" ")
        return index_number(index + 1)


index_number(0)




