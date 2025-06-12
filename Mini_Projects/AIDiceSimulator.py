import random

print("🎲 Welcome to the AI Dice Simulator!")
print("Type 'roll' to roll the dice or 'exit' to quit.\n")

while True:
    user_input = input("Your command: ").lower()

    if user_input == "roll":
        dice_number = random.randint(1, 6)
        print(f"🎲 You rolled a {dice_number}!\n")

    elif user_input == "exit":
        print("👋 Exiting the AI Dice Simulator. Bye!")
        break

    else:
        print("❗ Invalid command. Please type 'roll' or 'exit'.\n")
