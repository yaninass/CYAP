number = int(input("Введите натуральное число: "))
max_digit = 0
for digit in str(number):
    if int(digit) > max_digit:
        max_digit = int(digit)
print(max_digit)
