
class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def say_my_name(self):
        print(self.name)


print(__name__)

if __name__ == "__main__":
    p1 = Person("Beksultan")
    p1.say_my_name()
    print("Hello !")
