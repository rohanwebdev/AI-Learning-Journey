expenses = 0
grocery = 0
housing = 0
transportaion = 0
electricity = 0
loans = 0
other =0
while True:
    print("1. to add expenses. \n2. to know your expenses.")
    option = int(input("Select the options 1 or 2: "))
    if(option == 1):
        # print("Enter Date:\n")
        # datee = int(input("Enter date: "))
        # month = int(input("Enter month: "))
        # year = int(input("Enter year: "))
        # expense_Date = datee, month, year
        print("1. Grocery \n2. Housing \n3. Transportaion \n4. Electricity Bill \n5. Loans \n6. Other ")
        category = int(input("Select the category between 1 to 5: "))
        if(category == 1):
            price = int(input("Enter the amount: "))
            grocery += price
            print(f"Expense of {price} added in to \"Grocery\"")
        elif(category == 2):
            price = int(input("Enter the amount: "))
            housing += price
        elif(category == 3):
            price = int(input("Enter the amount: "))
            transportaion += price
        elif(category == 4):
            price = int(input("Enter the amount: "))
            electricity += price
        elif(category == 5):
            price = int(input("Enter the amount: "))
            loans += price
        elif(category == 6):
            price = int(input("Enter the amount: "))
            other += price
        else:
            print("Select between 1 to 6")
    # expenses = grocery + transportaion+ electricity + other + loans + housing
    elif(option == 2):
        # print("Enter the start date:\n")
        # datee = int(input("Enter date: "))
        # month = int(input("Enter month: "))
        # year = int(input("Enter year: "))
        # from_expense_Date = datee, month, year
        # print("\nEnter the end date:\n")
        # dateee = int(input("Enter date: "))
        # monthh = int(input("Enter month: "))
        # yearr = int(input("Enter year: "))
        # to = dateee, monthh, yearr
        print("1. to category expenses. \n2. to know all together expenses.")
        optionn = int(input("Select the options 1 or 2: "))
        if(optionn == 1):
            print("1. Grocery \n2. Housing \n3. Transportaion \n4. Electricity Bill \n5. Loans \n6. Other ")
            categoryy = int(input("Select the category between 1 to 5: "))
            if(categoryy == 1):
                print(f"The total expenses in \"Grocery\" category is : {grocery}")
            elif(categoryy == 2):
                print(f"The total expenses in \"Housing\" category is : {housing}")
            elif(categoryy == 3):
                print(f"The total expenses in \"Transportaion\" category is : {transportaion}")
            elif(categoryy == 4):
                print(f"The total expenses in \"Electricity Bill\" category is : {electricity}")
            elif(categoryy == 5):
                print(f"The total expenses in \"Loans\" category is : {loans}")
            elif(categoryy == 6):
                print(f"The total expenses in \"Others\" category is : {other}")
            else:
                print("Select option btween 1 to 6")
        elif(optionn == 2):
            totalExpenses = grocery + transportaion+ electricity + other + loans + housing 
            print(f"Total expenses bill: {totalExpenses}")
        else:
            print("Select option btween 1 or 2")
    else:
        print("Select option btween 1 or 2")
