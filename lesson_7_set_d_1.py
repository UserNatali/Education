'''Створіть словник із ключами-рядками та значеннями-числами. Створіть функцію, яка приймає довільну
кількість іменованих параметрів. Викличте її зі створеним словником і явно вказуючи параметри.'''

my_dict = {"Elen": 15, "Maxim": 19, "Roman": 22, "Iren": 16, "Liza": 20}


def my_dict_print(**args):
    print(args)
    return


my_dict_print(**my_dict)

my_dict_print(Elen=15, Maxim=19)

my_dict_print(Anna=15, Oled=19)

my_dict_print(**{"Elen": 10, "Maxim": 20, "Roman": 14, "Iren": 25})

