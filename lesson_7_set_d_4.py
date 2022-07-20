'''Дано два рядки. Виведіть на екран символи, які є в обох рядках.'''

a = "fhknll;dnddjmb;"
b = "ljhgfjvhfhfv"
a_set = set(a)
b_set = set(b)
print(a_set)
print(b_set)
print(a_set|b_set)
