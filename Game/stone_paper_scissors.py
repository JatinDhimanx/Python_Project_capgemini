import random

def stone_paper_scissors():
    while True:
        choices = ["stone", "paper", "scissors",]
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (stone, paper, scissors,exit): ").lower()

        if user_choice == "exit":
            print("Thanks for playing Game!")
            break
        
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice: {user_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "stone" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "stone") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
