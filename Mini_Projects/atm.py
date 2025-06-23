# confirm_pin = int(input("Enter the PIN: "))
# pin = 123
# bal = 1000
# check = 3
# while True:
#     if(confirm_pin == pin):
#         print("\nEnter '1' to CHECK BALANCE \n Enter '2' to DEPOSIT MONEY \n Enter '3' to WITHDRAW MONEY \n Enter '4' to CHANGE PIN \n Enter '5' to EXIT\n")
#         user_input = int(input (f"Enter the command between 1-5: "))
#         if(user_input == 1):
#             print(f"Your Balance is {bal} ")
#         elif(user_input == 2):
#             add = int(input("Enter the amount to be added: "))
#             bal += add
#             print(f"{add} added sucessfully!!!")
#         elif(user_input == 3):
#             withdraw = int(input("Enter the amount to be Withdraw: "))
#             if(withdraw > bal):
#                 print("Insufficient balance. ")
#             elif(bal >= withdraw):
#                 bal -= withdraw
#                 print(f"{withdraw} withdrawed sucessfully.")
#             else:
#                 print("Invalid input")
#         elif(user_input == 4):
#             check = 3
#             old_Pin = int(input("Enter the current PIN: "))
#             if(check > 0):
#                 if(old_Pin == pin):
#                     print(f"PIN verified sucessfully! ")
#                     newPin1 = int(input(f"Enter the new PIN: "))
#                     newPin2 = int(input(f"Re-enter the new PIN: "))
#                     pin = newPin1
#                     verify = 2
#                     if(verify>0):
#                         if(newPin1 == newPin2):
#                             print(f"New PIN upgraded successfully!!!")
#                         elif(newPin1 != newPin2):
#                             verify -= 1
#                             print("PIN not matched1.")
#                         else:
#                             verify -= 1
#                             print("PIN not matched2.")
#                 elif(old_Pin != pin):
#                     check -= 1
#                     print(f"PIN not matched3.")
#                 else:
#                     check -= 1
#                     print("Invalid PIN")
#         elif(user_input == 5):
#             print("Exiting...")
#             break
#         else:
#             print("Invalid Input. ")
            
#     elif(confirm_pin != pin):
#         if(check > 0):
#             check -= 1
#             confirm_pin = int(input("Enter the PIN: "))
#         else:
#             break
#     else:
#         print(f"Invalid Input!")



pin = 123
balance = 1000
attempts = 3

while attempts > 0:
    confirm_pin = int(input("Enter your PIN: "))
    
    if confirm_pin == pin:
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")

            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                print(f"💰 Your balance is ₹{balance}")

            elif choice == 2:
                deposit = int(input("Enter amount to deposit: ₹"))
                balance += deposit
                print(f"✅ ₹{deposit} deposited successfully!")

            elif choice == 3:
                withdraw = int(input("Enter amount to withdraw: ₹"))
                if withdraw > balance:
                    print("❌ Insufficient balance.")
                else:
                    balance -= withdraw
                    print(f"✅ ₹{withdraw} withdrawn successfully!")

            elif choice == 4:
                current = int(input("Enter your current PIN: "))
                if current == pin:
                    new_pin = int(input("Enter new PIN: "))
                    re_pin = int(input("Re-enter new PIN: "))
                    if new_pin == re_pin:
                        pin = new_pin
                        print("✅ PIN changed successfully.")
                    else:
                        print("❌ PINs do not match. Try again.")
                else:
                    print("❌ Incorrect current PIN.")

            elif choice == 5:
                print("👋 Exiting ATM. Have a great day!")
                exit()

            else:
                print("❗ Invalid option. Try again.")
        break  # Exit the outer loop if PIN is correct and menu ends

    else:
        attempts -= 1
        if attempts > 0:
            print(f"❌ Incorrect PIN. {attempts} attempt(s) left.")
        else:
            print("🚫 Too many incorrect attempts. Card blocked!")

