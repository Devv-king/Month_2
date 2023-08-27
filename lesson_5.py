# from calculator import addition, subtruction
# import calculator
# from calculator import *
# from calculator import sum as add

# print(addition(5, 2))
# print(subtruction(54, 22))

# print(calculator.addition(5, 2))
# print(calculator.subtruction(54, 22))

# print(add(23, 43))

# from person import Person

# esen = Person("Esen")
# esen.say_my_name()

# import package.calculator

# package.calculator.sum(1, 3)


# from package import NAME, subtruction

# print(NAME)
# print(subtruction(9, 33))


# Кастомные модули: calculator, functions, person
# Встроеные модули: random, math, datetime
# Внешние модули: 

# import random

# print(random.randrange(1))

# import datetime

# print(datetime.datetime.now().time().replace(microsecond=True, minute=True))

# import time

# a = 0
# while True:
#     time.sleep(2)
#     print(f"Loading {a}...")
#     a += 1

# print(time.localtime())


# from termcolor import cprint

# cprint("Hello", color="blue", on_color="on_yellow", 
#        attrs=["bold", "underline", "reverse"])

# from decouple import config, Csv

# passw = config("PASSWORD", cast=int)
# name = config("NAME", default="Uniknown")
# admins = config("ADMINS", cast=Csv())

# print(name, type(name))
# print(passw, type(passw))
# print(admins)
