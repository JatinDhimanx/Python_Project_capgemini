from stone_paper_scissors import stone_paper_scissors
from dice_roll_game import dice_roll_game

def game_options():
    while True:
        print("=" * 30)
        print("Welcome to the games!")
        print("=" * 30)
        print("1. stone - paper - scissors")
        print("2. Dice Roll Game")
        print("3. Exit")

        choice = int(input("Enter a Choice(1-3) : ") )

        if choice == 1:
            stone_paper_scissors()
        elif choice == 2:
            dice_roll_game()
        elif choice == 3:
            print("Thanks for playing Game!")
            break
        else:
            print("Invalid Choice! Please try again.")

game_options()