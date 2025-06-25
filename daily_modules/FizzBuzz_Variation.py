def fizzBuzz(num):
    if(num>0):
        for i in range(1, num+1):
            if(i%3==0 and i%5==0):
                print("FizzBuzz", end = " ")
            elif(i%3==0):
                print("Fizz", end = " ")
            elif(i%5==0):
                print("Buzz", end = " ")
            else:
                print(i, end=" ")
    else:
        print(f"Enter number greater than {num}")

number = int(input("Enter the end number: "))
fizzBuzz(number)
