'''Нехай на кожну сходинку можна стати з попередньої або переступивши через одну. Визначте,
скількома способами можна піднятися на задану сходинку.'''


def stairs(number):
    k = 0
    for x in range(number + 1):
        for y in range(number + 1):
            if 2 * x + y == number:
                k += 1
    return k


n = int(input("Введіть кількість сходів: "))
print(stairs(n))
