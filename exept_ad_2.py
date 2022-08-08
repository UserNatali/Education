"""Створіть програму спортивного комплексу, у якій передбачене меню: 1 - перелік видів спорту, 2 -
команда тренерів, 3 - розклад тренувань, 4 - вартість тренування. Дані зберігати у словниках. Також
передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню. Якщо
ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику
виключень."""


class SportComplex:
    def __init__(self, kind_sport, trainer, timetable, cost):
        self.kind_sport = kind_sport
        self.trainer = trainer
        self.timetable = timetable
        self.cost = cost


class TrainerEror(Exception):
    pass


kind_sport1 = SportComplex("football", "Ivan", "18.30", 10000)
kind_sport2 = SportComplex("tennis", "Ira", "19.30", 12000)
kind_sport3 = SportComplex("dance", "Alex", "15.00", 8000)
list_sport = [kind_sport1, kind_sport2, kind_sport3]


def get_trainer():

    list_trainer = []
    trainer_filtr = input("Input trainer")
    for i in list_sport:
        list_trainer.append(i.trainer)
    print(list_trainer)
    try:
        if trainer_filtr not in list_trainer:
            raise TrainerEror("Error")
        for i in list_sport:
            if i.trainer == trainer_filtr:
                print(i.__dict__)

    except TrainerEror:
        print("There is no such trainer")


get_trainer()
