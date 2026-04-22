import random

def dice_roll_game():
    while True:
        computer_roll = random.randint(1, 6)
        user_roll = int(input("Enter your dice roll (1-6, or 0 to exit): "))

        if user_roll == 0:
            print("Thanks for playing Game!")
            break

        print(f"Computer rolled: {computer_roll}")
        print(f"Your roll: {user_roll}")

        if user_roll == computer_roll:
            print("It's a tie!")
        elif user_roll > computer_roll:
            print("You win!")
        else:
            print("Computer wins!") 