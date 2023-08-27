import game_logic
from decouple import config

bank = config('MY_MONEY', cast=int)
while bank >= 0:
    print(f'Your balance: {bank}')
    answer = input("Continue? (yes/no): ")
    if answer == 'yes':
        bet = int(input("Enter your bet: "))
        bank -= bet
        bank += game_logic.play_game(bet)
    elif answer == 'no':
        break
    else:
        print('Error')
