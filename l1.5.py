products = {
    "Кольцо": ["золото", 1500, 5],
    "Серьги": ["серебро", 500, 7],
    "Браслет": ["золото", 1200, 3]
}
def display_description():
    for product, details in products.items():
        print(f"{product} - состав: {details[0]}")

def display_price():
    for product, details in products.items():
        print(f"{product} - цена: {details[1]} руб.")

def display_quantity():
    for product, details in products.items():
        print(f"{product} - количество: {details[2]} шт.")
def display_all_info():
    for product, details in products.items():
        print(f"{product} - состав: {details[0]}, цена: {details[1]} руб., количество: {details[2]} шт.")
def purchase():
    item = input("Введите название изделия, которое вы хотите купить: ")
    quantity = int(input(f"Сколько штук {item} вы хотите купить? "))

    if item not in products:
        print("Такого изделия нет в магазине.")
        return

    if products[item][2] < quantity:
        print("К сожалению, у нас нет такого количества данного изделия.")
        return

    cost = products[item][1] * quantity
    products[item][2] -= quantity
    print(f"Стоимость вашей покупки: {cost} руб.")
    print(f"Осталось в магазине: {products[item][2]} шт. {item}")
def main():
    while True:
        print("\nМеню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Всю информацию")
        print("5. Покупка")
        print("6. До свидания")
        choice = input("Выберите пункт меню (1-6): ")

        if choice == "1":
            display_description()
        elif choice == "2":
            display_price()
        elif choice == "3":
            display_quantity()
        elif choice == "4":
            display_all_info()
        elif choice == "5":
            purchase()
        elif choice == "6" or choice.lower() == 'n':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
