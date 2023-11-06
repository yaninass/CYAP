class Animal:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def move(self):
        return "Способ передвижения - не указан"


class Fish(Animal):
    def move(self):
        return "Cпособ передвижения - плавание"


class Bird(Animal):
    def move(self):
        return "Cпособ передвижения - полёт"


class ZooShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            print("не верный тип данных")

    def find_most_expensive(self):
        if not self.animals:
            return "нет данных"
        most_expensive_animal = max(self.animals, key=lambda animal: animal.cost)
        return f"самая дорогая порода: {most_expensive_animal.brand}, стоимость : {most_expensive_animal.cost}"

    def write_to_file(self, filename):
        with open(filename, "w") as file:
            for animal in self.animals:
                file.write(f"Порода: {animal.brand}, Стоимость {animal.cost}\n")


zoo_shop = ZooShop()
fish1 = Fish("золотая рыбка", 15)
fish2 = Fish("рыба-клоун", 25)
bird1 = Bird("сова", 120)
bird2 = Bird("попугай", 70)
zoo_shop.add_animal(fish1)
zoo_shop.add_animal(fish2)
zoo_shop.add_animal(bird1)
zoo_shop.add_animal(bird2)
print(zoo_shop.find_most_expensive())
zoo_shop.write_to_file("animal.txt")
