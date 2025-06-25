def is_factor(num):
    if (num>0):
        if (num == 1):
            print(f"factors of {num} is {num}")
            return False
        else:
            print("Factors of ",num, "are:")
            for i in range(1, num + 1):
                if (num % i == 0):
                    print(i , end=" ")

    else:
        print(f"{num} has no factors.")
        return False

number = int(input("Enter the number to check: "))
result = is_factor(number)
