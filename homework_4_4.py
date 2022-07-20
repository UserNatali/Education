length = int(input("Input length: "))
width = int(input("Input width: "))

for i in range(1, width + 1):
    for j in range(1, length + 1):
        print('*', end='')
    print()
