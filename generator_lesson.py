list_x = (x for x in range(0, 30, 5))
#print(list(list_x))
while True:
    try:
        print(next(list_x))
    except StopIteration:
        break
