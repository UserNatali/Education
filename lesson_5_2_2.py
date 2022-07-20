'''Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел (в діапазоні має бути не менше 5
чисел). Вивести на екран суму другого, передостаннього, а також середнього арифметичного значення даної
послідовності.'''
number_1 = int(input("Input start of range: "))
number_2 = int(input("Input end of range: "))

my_tuple = tuple(range(number_1, number_2))
sum_1 = my_tuple[1] + my_tuple[-2]
print(sum_1)
sum_2 = sum(my_tuple)
print(sum_2)
