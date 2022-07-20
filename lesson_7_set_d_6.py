'''Створіть функцію, яка на вхід отримує 2 списки цілочисельних значень, і повертає список унікальних значень без
повтору, які є в 1 списку (немає в другому) і навпаки.'''

def difference_list(x, y):
    my_set1 = set(x)
    my_set2 = set(y)
    my_difference1 = my_set1.difference(my_set2)
    my_difference2 = my_set2.difference(my_set1)
    return my_difference1, my_difference2


my_list1 = list(input("Input a first list of integers: "))
my_list2 = list(input("Input a second list of integers: "))

print(difference_list(my_list1, my_list2))
