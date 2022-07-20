'''Створіть програму, яка перевіряє, чи є паліндромом введена фраза.'''


def my_palindrom(text):
    my_list = list(text)
    my_list_new = []
    for i in list(reversed(my_list)):
        my_list_new.append(i)
    if my_list_new == my_list:
        print("Введена фраза є паліндром")
    else:
        print("Введена фраза не паліндром")


my_text = input("Введіть фразу")
my_palindrom(my_text)
