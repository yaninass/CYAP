import math

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d<0:
        return "нет корней"
    x_1 = (b * (-1) - math.sqrt(d)) / 2 * a
    x_2 = (b * (-1) + math.sqrt(d)) / 2 * a
    if d==0:
        return f"Один корень = {x_1}"
    if x_2 > x_1:
        return f"Первый корень = {x_2}, второй корень {x_1}"
    else:
        return f"Первый корень = {x_1}, второй корень = {x_2}"
print(solve(a, b, c))