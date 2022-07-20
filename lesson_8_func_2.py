'''Створіть програму, яка приймає як формальні параметри зріст і вагу користувача, обчислює
індекс маси тіла і в залежності від результату повертає інформаційне повідомлення (маса тіла в
нормі, недостатня вага або слідкуйте за фігурою). Користувач з клавіатури вводить значення
росту та маси тіла та передає ці дані у вигляді фактичних параметрів під час виклику функції.
Програма працює доти, доки користувач не зупинить її комбінацією символів «off»'''


def body_mass_index(m, h):
    return round(((m / h / h) * 10000), 2)


while True:

    my_height = float(input("Input your height: "))
    my_weight = float(input("Input your weight: "))
    bmi = body_mass_index(my_weight, my_height)
    if bmi < 18.5:
        print("Insufficient weight.")

    elif 18.5 <= bmi < 24.9:
        print("Weight is normal.")

    elif bmi >= 24.9:
        print("Follow the figure.")

    else:
        print("Invalid value")

    off_choice = input("For exit enter off ")

    if off_choice == "off":
        break