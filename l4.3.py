import time


class TrafficLight:
    def __init__(self):
        self.__color = "red"  # ������� color ������ ���������
        self.__valid_sequence = ["red", "yellow", "green"]  # ������������������ ������

    def change_color(self, color):
        if color in self.__valid_sequence:
            self.__color = color
        else:
            print("������: ������������ ����")

    def running(self):
        while True:
            if self.__color == "red":
                print("��������: �������")
                time.sleep(7)
                self.change_color("yellow")
            elif self.__color == "yellow":
                print("��������: ������")
                time.sleep(2)
                self.change_color("green")
            elif self.__color == "green":
                print("��������: �������")
                time.sleep(5)
                break  # ����� �� �����


# ������� ��������� ������ � ��������� ��������
traffic_light = TrafficLight()
traffic_light.running()
while True:
    user_input = input("������� ������ ���� ������� (red/yellow/green) ��� (exit) ��� ������: ")
    if user_input == "red":
        traffic_light.change_color(user_input)
        traffic_light.running()
    elif user_input == "exit":
        break
    else:
        print("������ ������� ������")
