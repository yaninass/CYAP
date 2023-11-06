import time


class TrafficLight:
    def __init__(self):
        self.__color = "red"  # Атрибут color сделан приватным
        self.__valid_sequence = ["red", "yellow", "green"]  # Последовательность цветов

    def change_color(self, color):
        if color in self.__valid_sequence:
            self.__color = color
        else:
            print("Ошибка: Недопустимый цвет")

    def running(self):
        while True:
            if self.__color == "red":
                print("Светофор: Красный")
                time.sleep(7)
                self.change_color("yellow")
            elif self.__color == "yellow":
                print("Светофор: Желтый")
                time.sleep(2)
                self.change_color("green")
            elif self.__color == "green":
                print("Светофор: Зеленый")
                time.sleep(5)
                break  # Выход из цикла


# Создаем экземпляр класса и запускаем светофор
traffic_light = TrafficLight()
traffic_light.running()
while True:
    user_input = input("Введите первый цвет сигнала (red/yellow/green) или (exit) для выхода: ")
    if user_input == "red":
        traffic_light.change_color(user_input)
        traffic_light.running()
    elif user_input == "exit":
        break
    else:
        print("ошибка порядка режима")
