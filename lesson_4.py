import random

total_rounds = 0


class GameEntity:
    def __init__(self, name, health, damage) -> None:
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self) -> str:
        return f'{self.name} health: {self.health} [{self.damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage)

    def hit(self, heroes: list):
        for hero in heroes:
            if hero.health > 0 and self.health > 0:
                hero.health -= self.damage

    def __str__(self) -> str:
        return "BOSS " + super().__str__()


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability) -> None:
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    @super_ability.setter
    def super_ability(self, value):
        self.__super_ability = value

    def hit(self, boss: Boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass


class Warior(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "CRITICAL DAMAGE")

    def apply_super_power(self, boss: Boss, heroes: list):
        coef = random.randint(0, 5)
        boss.health -= self.damage * coef
        print(f"Warrior {self.name} hits criticaly: {self.damage * coef}")


class Medic(Hero):
    def __init__(self, name, health, damage, heal_point) -> None:
        super().__init__(name, health, damage, "HEAL")
        self.__heal_point = heal_point

    def apply_super_power(self, boss: Boss, heroes: list):
        print(f"Medic: {self.name} heal {self.__heal_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_point


class Mag(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "BOOST")

    def apply_super_power(self, boss: Boss, heroes: list):
        boost_point = random.choice([5, 10, 15])
        print(f"Mag: {self.name} boost {boost_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += boost_point


def is_game_finished(boss: Boss, heroes):
    if boss.health <= 0:
        print("Heroes WON!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False

    if all_heroes_dead:
        print("Boss WON!")

    return all_heroes_dead


def print_statistic(boss: Boss, heroes):
    print(f"___________{total_rounds} Round___________")
    print(boss)
    for hero in heroes:
        print(hero)


def heroes_power(boss: Boss, heroes: list):
    boss_ability = random.choice(["CRITICAL DAMAGE", "HEAL", "BOOST"])
    print(f"Boss {boss.name} blocked {boss_ability}")
    for hero in heroes:
        if boss_ability != hero.super_ability and boss.health > 0 and hero.health > 0:
            hero.apply_super_power(boss, heroes)


def play_round(boss: Boss, heroes: list):
    print_statistic(boss, heroes)
    global total_rounds
    total_rounds += 1
    boss.hit(heroes)
    for hero in heroes:
        hero.hit(boss)
    heroes_power(boss, heroes)


def main():
    boss = Boss("Nashor", 2000, 50)

    warrior = Warior("Darius", 290, 20)
    warrior_2 = Warior("Garen", 260, 15)
    medic = Medic("Senna", 220, 5, 15)
    medic_asistent = Medic("Tresh", 240, 10, 5)
    magic = Mag("Zeeks", 290, 20)

    heroes = [warrior, medic, medic_asistent, magic, warrior_2]

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)

    print_statistic(boss, heroes)


main()
