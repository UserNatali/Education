'''Створіть програму, яка зчитує рядок, в якому знаходиться ПІБ користувача і перевіряє, чи складається рядок з
літер, при чому кожне слово має бути записане з великої літери. Вивести результат на екран.'''

full_name = "Петренко Леся Іванівна"
breakdown = full_name.split()

result_1 = []
result_2 = []
for i in range(3):
    name_letters = breakdown[i].isalpha()
    element = breakdown[i]
    leters_first = element[0].isupper()
    result_1.append(name_letters)
    result_2.append(leters_first)

if False in result_1:
    print("ПІБ складається лише з літер", False)
else:
    print("ПІБ складається лише з літер", True)

if False in result_2:
    print("Всі слова з великої літери", False)
else:
    print("Всі слова з великої літери", True)
