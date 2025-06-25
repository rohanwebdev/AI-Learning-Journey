def is_prime(num):
    if (num>0):
        if (num == 1):
            print(f"No {num} is not a prime number")
            return False
        else:
            for i in range(2, int(num**0.5) + 1):
                if (num % i == 0):
                    print(f"No {num} is not a prime number")
                    return False
                else:
                    print(f"Yes! {num} is a prime number")
    else:
        print(f"No {num} is a prime number")
        return False

number = int(input("Enter the number to check: "))
result = is_prime(number)
