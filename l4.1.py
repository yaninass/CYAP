class Calculator:
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b

    def input_numbers(self):
        try:
            a = float(input("введите первое число: "))
            b = float(input("введите второе число: "))
            return a, b
        except ValueError:
            return "Ошибка: числа введены некорректно"


calc = Calculator()
a,b=calc.input_numbers();
while(True):
    print("\nМеню:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. До свидания")
    choice = input("Выберите пункт меню (1-5): ")

    if choice == "1":
       result= calc.add(a,b)
       print(f"результат сложения {result}")
    elif choice == "2":
        result=calc.substract(a,b)
        print(f"результат вычитания {result}")
    elif choice == "3":
        result=calc.multiply(a,b)
        print(f"результат умножения {result}")
    elif choice == "4":
        result=calc.divide(a,b)
        print(f"результат деления {result}")
    elif choice == "5":
        print("До свидания!")
        break
    else:
        print("Некорректный ввод")