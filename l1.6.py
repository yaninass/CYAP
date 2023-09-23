input_str = input("Введите кортеж целых чисел : ")
list_of_numbers = [int(item) for item in input_str.split()]
tuple_of_numbers = tuple(list_of_numbers)
maximum_value = max(tuple_of_numbers)
minimum_value = min(tuple_of_numbers)
print(f"Максимальное значение: {maximum_value}")
print(f"Минимальное значение: {minimum_value}")
