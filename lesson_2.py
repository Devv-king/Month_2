# public - self.city
# private - self.__city
# protected - self._city

class Address:
    def __init__(self, city, street, number):
        self._city = city
        self.__street = street
        self.__number = number

    # @property
    # def city(self):
    #     return self._city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number


class Animal:
    def __init__(self, name, age, address):
        self.__name = name
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("age must be int and age must be > 0")
        if isinstance(address, Address):
            self.address = address
        else:
            raise ValueError("address must be Address instance")

    def get_name(self):  # Геттер 1
        return self.__name

    def set_name(self, new_name):  # Cеттер 1
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("new_name must be str")

    @property
    def age(self):  # Геттер 2
        return self.__age

    @age.setter
    def age(self, value):  # Cеттер 2
        if isinstance(value, int):
            self.__age = value
        else:
            raise ValueError("value must be int")

    def info(self):
        print(
            f"Name: {self.__name}\nAge: {self.age}\n"
            f"City: {self.address._city}\nStreet: {self.address.street}\n"
            f"Number: {self.address.number}\n\n"
        )

    def speak(self):
        pass


class Cat(Animal):
    __poroda = "cat"

    def __init__(self, name, age, address):
        super().__init__(name, age, address)
        self.__created()

    def __created(self):
        print("New cat was born!")

    def speak(self):
        print(f"{self.get_name()} says Meow Meow")


class Dog(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)

    def speak(self):
        print(f"{self.get_name()} says Gav Gav")


class Fish(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)


geeks_bishkek = Address("Bishkek", "Ibraimova", 103)
cat1 = Cat("Oleg", 3, geeks_bishkek)
cat2 = Cat("Murka", 4, geeks_bishkek)
cat3 = Cat("Snezhok", 3, geeks_bishkek)

dog1 = Dog("Ak-Tosh", 3, geeks_bishkek)
dog2 = Dog("Muhtar", 4, geeks_bishkek)
dog3 = Dog("Napolen", 3, geeks_bishkek)

fish = Fish("Dorry", 3, geeks_bishkek)

animal_list = [cat1, cat2, fish, cat3, dog1, dog2, dog3]
for animal in animal_list:
    animal.speak()


# cat1.__created()
# cat1.info()

# # print(geeks_bishkek._city)

# animal1 = Animal("Валис", 5, geeks_bishkek)

# animal1.info()


# print(animal1.address)

# print(type(geeks_bishkek))

# animal2 = Animal("Dog", 2, Address("Osh", "Myrzaly Amatova", 1))
# animal3 = Animal("fish", 3, geeks_bishkek)

# print(animal2.address.street)


# animal1.set_name("Bobik")
# print(animal1.get_name())

# animal1.age = '2f'
# print(animal1.age)

# animal1.set_name(2)

# print(animal1.get_name())

# animal1.age = -2
# print(animal1.name, animal1.age)


class Cow:
    def __init__(self) -> None:
        pass