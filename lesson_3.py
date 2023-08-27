class MusicPlaybleMixin:
    @staticmethod
    def play_music(song):
        print(f"Играет музыка - {song}")


class Car(MusicPlaybleMixin):
    def __init__(self, model, year) -> None:
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    def drive(self):
        print("I can drive!")

    def __str__(self) -> str:
        return f"\nModel: {self.model}\nYear: {self.year}"


class ElectricCar(Car):
    def __init__(self, model, year, battery) -> None:
        Car.__init__(self, model, year)
        self.battery = battery

    def drive(self):
        print("I can drive using electric engine!")

    def __str__(self) -> str:
        return super(ElectricCar, self).__str__() + f"\nBattery: {self.battery}"


class FuelCar(Car):
    __total_fuel = 500

    def __init__(self, model, year, fuel_bank) -> None:
        Car.__init__(self, model, year)
        self.fuel_bank = fuel_bank

    @staticmethod
    def print_fuel_type():  # Метод который сам по себе
        print("AI 98")

    @classmethod
    def put_fuel(cls, car, amount):  # Метод который работает с классом
        cls.__total_fuel -= amount
        car.fuel_bank += amount
        print(f"Осталось топлива: {cls.__total_fuel}")

    def drive(self):  # Метод который работает с объектом
        print(f"{self.model} can drive using fuel engine!")

    def __str__(self) -> str:
        return super(FuelCar, self).__str__() + f"\nFuel bank: {self.fuel_bank}"

    def __add__(self, other):
        return self.fuel_bank + other.fuel_bank

    def __sub__(self, other):
        return self.year - other.year

    def __mul__(self, other):
        return self.fuel_bank * other.fuel_bank

    def __lt__(self, other):
        return self.fuel_bank < other.fuel_bank

    def __gt__(self, other):
        return self.fuel_bank > other.fuel_bank

    def __eq__(self, other):
        return self.fuel_bank == other.fuel_bank

    def __ne__(self, other):
        return self.fuel_bank != other.fuel_bank

    def __ge__(self, other):
        return self.fuel_bank >= other.fuel_bank

    def __le__(self, other):
        return self.fuel_bank <= other.fuel_bank


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, fuel_bank, battery) -> None:
        ElectricCar.__init__(self, model, year, battery)
        FuelCar.__init__(self, model, year, fuel_bank)


# class SmartPhone(MusicPlaybleMixin):
#     def __str__(self) -> str:
#         return "Hello"


# s = SmartPhone()
# print(s)

# DRY - Don't Repeat Yourself

tesla = ElectricCar("Tesla S", 2023, battery=1000)
supra = FuelCar("Toyota Supra", 2003, fuel_bank=40)
prius = HybridCar("Toyota Prius", 2015, fuel_bank=20, battery=800)

# +, -, *, /, **, %
# >, >=, ==, <=, <

# print(supra + prius)
# print(prius >= supra)
# print(prius < supra)
# if prius < supra:
#     print("SUPRAAAAAAAAAAAAA!")
# print(tesla)
# print(prius)

# samsung = SmartPhone()

# SmartPhone.play_music("Take on me")
# samsung.play_music("What is love?")
# prius.play_music("Where is my")

# supra.print_fuel_type()
# FuelCar.print_fuel_type()

# print(supra.fuel_bank)
# FuelCar.put_fuel(supra, 10)
# print(supra.fuel_bank)

# tesla.drive()
# supra.drive()
# prius.drive()

# print(HybridCar.__mro__)
# print(HybridCar.mro())

