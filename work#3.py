class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, new_cpu):
        self.__cpu = new_cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, new_memory):
        self.__memory = new_memory

    def make_computations(self):
        add = (self.__cpu + self.__memory)
        return add

    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, new_sim_cards_list):
        self.__sim_cards_list = new_sim_cards_list

    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        return f'“Идет звонок на номер {call_to_number}” с сим-карты - ( {sim_card_number} ) {sim_card}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        return f'Проложен маршрут до {location}'

    def __str__(self):
        return f'cpu: {self.cpu}, memory: {self.memory}, sim_cards_list: {self.sim_cards_list}'


computer = Computer(5, 16)
print(computer.make_computations())

# Создаем объекты класса Computer
computer1 = Computer(9, 32)
computer1.memory = 60
computer2 = Computer(11, 64)
computer2.memory = 52
# Переопределенные методы сравнения
print(computer1 == computer2)  # Вывод: False

sim_list = ["Beeline", "Megacom", "O!"]
phone = Phone(sim_list)
print(phone.call(1, + 996778810761))

sim_list_1 = ["MTS", "Tele2"]
sim_list_2 = ["Tcell", "LycaMobile"]

smart_phone_1 = SmartPhone(125, 16, sim_list_1)
smart_phone_2 = SmartPhone(35, 128, sim_list_2)

print(smart_phone_1)
print(smart_phone_2)

print(SmartPhone.use_gps("USA"))
