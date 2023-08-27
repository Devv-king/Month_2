from random import randint


def play_game(bet):
    result = randint(1, 31)
    my_choice = int(input("Input number: "))
    if result == my_choice:
        print(f'Your choice: {my_choice} == Result {result}.YOU WIN!!!')
        return bet * 2
    else:
        print(f'Your choice: {my_choice} == Result {result}.YOU LOSE!!!')
        return 0


