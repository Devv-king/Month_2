# class - Чертеж
# __init__ - Конструктор
# self - Сам обьект / адрес на объект
# self.model - Атрибут объекта
# wheel - Атрибут класса
# model, color, year - Входящие параметры
# def drive(self): - Методы


class Transport:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def change_color(self, new_color):
        self.color = new_color


class Car(Transport):
    wheel = 4

    def __init__(self, model, color, year, penalties=[]):
        Transport.__init__(self, model, color, year)
        self.penalties = penalties

    def drive(self, city):
        print(f"Машина {self.model} едет в {city}")

    def info(self):
        print(f"{self.model} {self.color} {self.year} Penalties: {self.penalties}")


class Truck(Car):
    wheel = 8

    def __init__(self, model, color, year, load_capacity, penalties=[]):
        super().__init__(model, color, year, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight):
        if weight > self.load_capacity:
            print(f"Ты не можешь загрузить, максимальная грузоподьемность {self.load_capacity} кг")
        else:
            print(f"Груз загружен {weight} кг")



mers = Car("Mersedes Benz", "Black", 2023, [20000])
mers.info()

zil = Truck("Zil", "Green", 1980, 2000)

zil.change_color("ewef")
zil.load_cargo(1000)




# mers.color = "White" # меняем атрибут объекта
# mers.info()

# mers.change_color(new_color="Blue")
# mers.info()


# print(f"{mers.model} {mers.color} {mers.year}")
# mers.drive("Ош")

bmw = Car(color="Red", model="BMW M5", year=2022, penalties=[10, 39, 23])
bmw.info()
# bmw.drive("Бишкек")

# Car.wheel = 8
# bmw.wheel = 6
# print(bmw.wheel)
# print(Car.wheel)


def create_car():
    bmw1 = Car(color="few", model="333", year=3, penalties=[10, 39, 23])
    bmw2 = Car(color="f", model="BMW f", year=2022, penalties=[10, 39, 23])
    bmw3 = Car(color="Red", model="BMW M5", year=2022, penalties=[10, 39, 23])
    return [bmw1, bmw2, bmw3]


cars = create_car()
for car in cars:
    car.info()