import random

print("🎲 Welcome to the AI Dice Simulator!")
print("Type 'roll' to roll the dice or 'exit' to quit.\n")

score = 0
numberOfTurns = 0
while True:
    user_input = input("Your command: ").lower()
    if user_input == "roll":
        numberOfTurns += 1
        guess = int(input("Guess a number between 1-6. "))
        dice_number = random.randint(1, 6)
        print(f"🎲 You rolled a {dice_number}!")
        if(guess == dice_number):
            print("bravo!!!  ")
            score += 1
        else:
            print("Better luck next time.")
        print(f"Your score is {score}/{numberOfTurns}\n")

    elif user_input == "exit":
        print("👋 Exiting the AI Dice Simulator. Bye!")
        if(numberOfTurns > 0):
            print(f"Your score is {score}/{numberOfTurns}")
        break

    else:
        print("❗ Invalid command. Please type 'roll' or 'exit'.\n")
