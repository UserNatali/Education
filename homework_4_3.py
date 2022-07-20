side_1 = int(input("Input one side of a triangle: "))

len = 1
for i in range(1, side_1 + 1):
    for j in range(1, (len + 1)):
        print('*', end='')
    len += 1
    print()

