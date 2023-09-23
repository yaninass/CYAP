import math


def data_type(data):
    def is_simple(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

    def count_letter(s):
        glasnie = {'a', 'e', 'u', 'i', 'o', 'A', 'E', 'O', 'U', 'I', 'а', 'А', 'О', 'о', 'Е', 'е', 'у', 'ы', 'э', 'я',
                   'и', 'ю',
                   'У', 'Ы', 'Э', 'Я', 'И', 'Ю'}
        how_glasnix = 0
        for char in s:  # проверяет циклом содержание чара из гласных в строке
            if char in glasnie:
                how_glasnix = how_glasnix + 1
        soglasnie = {'q', 'Q', 'w', 'W', 'R', 'r', 't', 'T', 'p', 'P', 's', 'S', 'D', 'd', 'f', 'F', 'g', 'G', 'h', 'H',
                     'J', 'j', 'k', 'K', 'L', 'l', 'z', 'Z', 'x', 'X', 'C', 'c', 'v', 'V', 'b', 'B', 'n', 'N', 'M', 'm',
                     'й', 'Й', 'ц', 'Ц', 'к', 'К', 'н', 'Н', 'г', 'Г', 'ш', 'Ш', 'щ', 'Щ', 'з', 'З', 'х', 'Х', 'ф', 'Ф',
                     'в', 'В', 'п', 'П', 'р', 'Р', 'л', 'Л', 'д', 'Д', 'ж',
                     'Ж', 'ч', 'Ч', 'с', 'С', 'м', 'М', 'т', 'Т', 'ь', 'Ь', 'ъ', 'Ъ', 'б', 'Б'}
        how_soglasnix = 0
        for char in s:
            if char in soglasnie:
                how_soglasnix = how_soglasnix + 1
        return how_glasnix, how_soglasnix

    def work_with_list(lst):
        pr = 1
        for i in range(len(lst)):
            if i % 2 != 0:
                pr *= lst[i]
        max_value = max(lst)
        lst.remove(max_value)
        return pr, lst

    def process_dict(dct):
        return dict(sorted(dct.items()))

    if isinstance(data, list):
        product, new_list = work_with_list(data)
        return f"Произведение элементов с нечетными номерами: {product}. Новый список: {new_list}"

    elif isinstance(data, dict):
        return process_dict(data)

    elif isinstance(data, int) or isinstance(data, float):
        return "Простое" if is_simple(data) else "Не простое"

    elif isinstance(data, str):
        consonants, vowels = count_letter(data)
        return f"Гласных: {consonants}, Согласных: {vowels}"
    else:
        return "Неизвестный тип данных"


lst = [1, 2, 3, 4, 5]
print(data_type(lst))

dct = {'b': 1, 'a': 2, 'c': 3}
print(data_type(dct))

num = 7
print(data_type(num))

string = "Hello World"
print(data_type(string))
