'''Створіть список та введіть його значення. Знайдіть найбільший та найменший елемент списку,
а також суму та середнє арифметичне його значень.'''
number = int(input("Введіть кількість елементів: "))

my_list = []
for i in range(number):
    valua = float(input("Введіть {} число: ".format(i + 1)))
    my_list.append(valua)

my_list.sort()
max_el = my_list[-1]
min_el = my_list[0]
print("Maximum  and minimym element : ", max_el, min_el)


sum = 0

for element in my_list:
    sum += element

valua = sum / number

print("Sum = ", sum)
print("Average value = ", valua)
