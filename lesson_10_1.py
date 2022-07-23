def add_stationery(list):
    stationery = tuple(input("Введіть канцтовари: "))
    return list.insert(0, stationery)


list_stationery = ["олівець", "ручка", "ластик", "пенал"]
add_stationery(list_stationery)


