"📘 Day 3: Smart Number Crunching & Conditional Logic"

"1. Check Even or Odd"
"Input a number and print whether it's even or odd"
# num = int(input("Enter a number: "))
# if(num%2==0):
#     print("Entered number ", num, "is even.")
# else:
#     print("Entered number ", num, "is odd.")

"2. Leap Year Checker"
"Input a year and check if it's a leap year"
# year = int(input("Enter the year to check if it's a leap year: "))
# if(year%4==0):
#     print("Entered year ", year, "is leap year.")
# else:
#     print("Entered year ", year, "is not a leap year.")

"3. Vowel or Consonant"
"Input a letter and check whether it is a vowel or consonant"
# char = input("Enter a letter and check whether it is a vowel or consonant: ")

# if( char == "a" or  char == "e" or  char == "i" or  char == "o" or  char == "u"):
#     print("Entered letter", char, "is vowel.")

# elif( char == "A" or  char == "E" or  char == "I" or  char == "O" or  char == "U"):
#     print("Entered letter", char, "is vowel.")

# else: 
#     print("Entered letter", char, "is consonant.")

"4. Grade Calculator"
"# Input marks (0–100), then display grade: "
# A (90+), B (80–89), C (70–79), D (60–69), F (<60)
# marks = int(input("Enter the marks: "))
# if(marks > 90):
#     print("Bravo! your grade is A")
# elif(marks >= 80):
#     print("Your grade is B")
# elif(marks >= 70):
#     print("Your grade is C")
# elif(marks >= 60):
#     print("Your grade is D")
# elif(marks < 60):
#     print("Your grade is F")
# else:
#     print("Invalid input")

"5. Simple Calculator"
"Ask the user: Enter expression (like '5' + '3')"
"Split it and perform the calculation"
# expr = input("Enter the expression (eg. 5 + 3): ")
# parts = expr.split()
# num1 = float(parts[0])
# op = parts[1]
# num2 = float(parts[2])

# if(op == '+'):
#     result = num1 + num2
# elif(op == '-'):
#     result = num1 - num2
# elif(op == '*'):
#     result = num1 * num2
# elif(op == '/'):
#     if(num2 != 0):
#         result = num1 / num2
#     else: 
#         print("Error!, zero division error")
# elif(op == '**'):
#     result = num1 ** num2
# elif(op == '//'):
#     result = num1 // num2
# elif(op == '%'):
#     result = num1 % num2
# else:
#     print("Invalid operator!")

# print(parts[0] ,parts[1] , parts[2], "=", result)


"BMI Calculator"
# Input height (in meters) and weight (in kg)
# Calculate BMI and print the category:
# Underweight: < 18.5
# Normal: 18.5–24.9
# Overweight: 25–29.9
# Obese: 30+

# height = int(input("Enter the height (in meters): "))
# weight = int(input("Enter the weight (in kg): "))
# bmi = weight/(height)**2
## bmi = 32
# print("BMI is", bmi)

# if(bmi < 18.5):
#     print("Underweight")
# elif(bmi <= 24.9):
#     print("Normal")
# elif(bmi <= 29.9):
#     print("Overweight")
# elif(bmi > 30):
#     print("Obese")
# else:
#     print("Invalid input!")


"7. ATM Simulator"
"""Start with a balance (e.g., ₹5000)
User can withdraw, deposit, or check balance
Keep running until user exits"""

bal = 5000
while True:
    print("\n====== ATM Menu ======")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Choose an option (1-4): "))

    if (choice == 1):
        amount = float(input("Enter amount to withdraw: ₹"))
        if(amount> bal):
            print("Insufficient balance!")
        else:
            bal-= amount
            print(amount, "debited new balance: ", bal)

    elif(choice == 2):
        amount = int(input("Enter the amount to be deposited: "))
        bal += amount
        print(amount, "credited new balance: ", bal)

    elif(choice == 3):
        print("Available balance: ", bal)

    elif(choice == 4):
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid option. Please try again.")
        