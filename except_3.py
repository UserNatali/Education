'''Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
Конструктор має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із
клавіатури. Виведіть усіх співробітників, які були прийняті після цього року. '''


class Employee:
    def __init__(self, first_name, last_name, department, year):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.year = year

    def __repr__(self):
        return f"{self.__dict__}"


def my_except(first_name, last_name):
    if not first_name.istitle() or not last_name.istitle():
        raise NameError("Input name, the first letter is capitalized")


def my_except_year(year):
    if not year.isdigit() or not len(year) == 4:
        raise ValueError("Right input year")


list_employee = []


def menu():
    while True:
        choice = input("For next input 1, for exit input 2")
        if choice == "1":
            while True:
                try:
                    first_name = input("Input first_name")
                    last_name = input("Input last_name")
                    my_except(first_name, last_name)
                    break
                except NameError as e:
                    print(e)
            department = input("Input department")
            while True:
                try:
                    year = input("Input year")
                    my_except_year(year)
                    break
                except ValueError as e:
                    print(e)
            employee = Employee(first_name, last_name, department, year)
            list_employee.append(employee)
        elif choice == "2":
            break


def get_employee():
    year_filter = input("Input year")
    list_filter = []
    for i in list_employee:
        if i.year >= year_filter:
            list_filter.append(i)
    print(list_filter)


menu()
print(list_employee)
get_employee()
