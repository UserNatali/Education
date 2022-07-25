"Створіть магазин канцтоварів використовуючи списки для зберігання елементів. Для додавання\
елементів створіть функцію, яка буде запитувати дані в користувача і зібрані дані у вигляді\
кортежу додавати у створений список на початку. Результат вивести на екран. Під час створення\
дотримуйтесь правил специфікації PEP 8"


def add_stationery(list_x):
    stationery = input("Введіть канцтовари: ")
    stationery_tuple = tuple(stationery.split())
    return list_x.insert(0, stationery_tuple)


list_stationery = ["олівець", "ручка", "ластик", "пенал"]
add_stationery(list_stationery)
print(list_stationery)
