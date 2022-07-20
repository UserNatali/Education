'''Створіть прототип програми «Бібліотека», в якій є можливість перегляду та внесення змін до структури:
прізвище:
посада: ...
досвід роботи: …
портфоліо: …
коефіцієнт ефективності: …
стек технологій: …
зарплата: …
Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим
співробітником'''

catalog = {"Петренко":{"посада": "керівник", "досвід роботи": 15, "портфоліо": 25, "коефіцієнт ефективності": 78,
         "стек технологій": "PHP 7, MySQL, Git", "зарплата": 5000}, "Веклюк":{"посада": "розробник", "досвід роботи": 7,
        "портфоліо": 15, "коефіцієнт ефективності": 75, "стек технологій": "Python, MySQL, Git", "зарплата": 3000}, "Артинцев":{"посада": "тестувальник",
        "досвід роботи": 4, "портфоліо": 10, "коефіцієнт ефективності": 90, "стек технологій": "Python, MySQL, Git", "зарплата": 2000}}

sorted_katalog_key = sorted(catalog.keys())
new_katalog, sorted_efficiency = {}, {}

for key in sorted_katalog_key:
    for el in catalog.values():
        if catalog[key] == el:
            new_katalog[key] = el
            break

print(new_katalog)
my_list_coefficient, new_katalog2 = [], {}

for value_catalog in catalog.values():
    coefficient = value_catalog['коефіцієнт ефективності']
    my_list_coefficient.append(coefficient)

my_list_coefficient.sort()
print(my_list_coefficient)

for i in my_list_coefficient:
    for z in catalog.values():
        for k in catalog:
            if catalog[k] == z and i == z['коефіцієнт ефективності']:
                new_katalog2[k] = z
                break



print(new_katalog2)

