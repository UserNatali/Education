while True:
    choice = input("Меню\n1. Порахувати суму вартості товарі \n2. Порахуйте парні елементи від 0 до 10 \n3. Вийти\n")

    if choice == "1":
        suma1 = 0
        cost = float(input("Введіть вартість товару: "))
        while cost != 0.0:
            suma1 += cost
            cost = float(input("Введіть вартість товару: "))
        print("Cума вартості товарів = ", suma1)

    elif choice == "2":

        suma2 = 0
        for i in range(1, 100, 2):
            suma2 += i
        print("Cума парних елементів = ", suma2)

    elif choice == "3":
        break
    else:
        print("Некоректний вибір")



