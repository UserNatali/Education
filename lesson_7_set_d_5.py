'''Створіть програму, яка емулює роботу сервісу зі скорочення посилань. Повинна бути реалізована можливість
введення початкового посилання та короткої назви і отримання початкового посилання за її назвою'''

'''http://zernovita.com/calculator/imt  =>   https://tinyurl.com/hmd72kk6'''
'''https://www.tablycjakalorijnosti.com.ua/tablytsya-yizhyi  =>  https://tinyurl.com/mrypsua7'''


initial_reference = input("Введіть посилання: ")
short_name = input("Введіть коротку назву: ")

my_dict = {short_name: initial_reference}

print(my_dict[short_name])
