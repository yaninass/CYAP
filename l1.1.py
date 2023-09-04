number = int(input("Введите натуральное число: "))
max_digit = 0
for digit in str(number):
    if int(digit) > max_digit:
        max_digit = int(digit)
print(max_digit)
reverse_number = str(number)[::-1]
print(reverse_number)
