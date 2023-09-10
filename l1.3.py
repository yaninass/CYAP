my_list = input("Введите ваш список ")
true_list = list(map(int, my_list.split()))  # делаем каждый элемент интом деля по пробелам
pr = 1
for i in range(len(true_list)):
    if i % 2 != 0:
        pr *= true_list[i]
print("Произведение элементов с нечётными номерами:",pr)
max_value=max(true_list)
true_list.remove(max_value)
print("Список без максимального элемента: ",true_list)
sorted_list=sorted(true_list,reverse=True)
three_big=sorted_list[:3]
print("Три наибольших элемента: ",three_big)
