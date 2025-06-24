confirm_pin = int(input("Enter the PIN: "))
pin = 123
bal = 1000
check = 2  

while True:
    if confirm_pin == pin:
        while True:
            print("\n====== ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")
            
            user_input = int(input("Enter your choice (1-5): "))

            if user_input == 1:
                print(f"Your balance is ₹{bal}")
            elif user_input == 2:
                add = int(input("Enter amount to deposit: ₹"))
                bal += add
                print(f"₹{add} deposited successfully!")
            elif user_input == 3:
                withdraw = int(input("Enter amount to withdraw: ₹"))
                if withdraw > bal:
                    print("Insufficient balance.")
                else:
                    bal -= withdraw
                    print(f"₹{withdraw} withdrawn successfully!")
            elif user_input == 4:
                old_pin = int(input("Enter current PIN: "))
                if old_pin == pin:
                    new_pin1 = int(input("Enter new PIN: "))
                    new_pin2 = int(input("Re-enter new PIN: "))
                    if new_pin1 == new_pin2:
                        pin = new_pin1
                        print("PIN changed successfully.")
                    else:
                        print("New PINs do not match.")
                else:
                    print("Incorrect current PIN.")
            elif user_input == 5:
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid option. Try again.")
        break  

    else:
        if check > 0:
            print(f"Incorrect PIN. You have {check} attempts left.")
            confirm_pin = int(input("Re-enter the PIN: "))
            check -= 1
        else:
            print("Too many incorrect attempts. Exiting for security reasons.")
            break
