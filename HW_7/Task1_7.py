"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for key, lasting in self.__color.items():
            print(key)
            sleep(lasting)


colors_t = TrafficLight(color={("\033[31m{}\033[0m".format("красный")): 7,
                               ("\033[33m{}\033[0m".format("Желтый")): 2,
                               ("\033[32m{}\033[0m".format("Зеленый")): 7})
colors_t.running()
