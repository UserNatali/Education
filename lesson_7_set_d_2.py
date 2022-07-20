'''Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою:
автор: твір. Передбачте можливість виведення на екран сортування за автором та твором.'''

library = {"Stephen King": "Just After Sunset", "Mark Twain": "The Adventures of Tom Sawyer", "Jack London": "Martin Eden"}


valua = library["Jack London"]

print(valua)

# library["Jack London"] = "Hearts of Three"

print(library)

sorted_key = sorted(library.keys())
print(sorted_key)

sorted_valua = sorted(library.values())
print(sorted_valua)
sorted_dict_key, sorted_dict_value = {}, {}
# sorted by value
for i in sorted_valua:
    for k in library.keys():
        if library[k] == i:
            sorted_dict_value[k] = library[k]
            break

print(sorted_dict_value)
# sorted by value
for key in sorted_key:
    for el in library.values():
        if library[key] == el:
            sorted_dict_key[key] = library[key]
            break

print(sorted_dict_key)
