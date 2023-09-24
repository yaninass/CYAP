def divide_numbers():
    try:
        numerator = float(input("Введите числитель: "))
        denominator = float(input("Введите знаменатель: "))

        result = numerator / denominator
        print(f"Результат деления: {result}")

    except ZeroDivisionError:
        print("Деление на ноль!")

    except ValueError:
        print("Введено не число!")

    finally:
        print("Завершение работы функции.")

divide_numbers()
