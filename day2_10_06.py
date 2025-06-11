"WAP to find out the greater number among two numbers"
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if(num1 > num2):
#     print(num1, " is greater")
# elif (num1 < num2):
#     print(num2, " is greater")
# else:
#     print(num1, " and ", num2, " are equal.")    

"WAP to find out whether the number is +ve or -ve"
# num1 = int(input("Enter a number: "))
# if(num1 > 0):
#     print("The number ", num1, " is a +ve number")
# elif(num1 < 0):
#     print("The number ", num1, " is a -ve number")
# else:
#     print("The number ", num1, " is zero.")

"WAP to find out if the number is odd or even"
# num1 = int(input("Enter a number: "))
# if(num1%2==0):
#     print("The number ", num1, " is a even number.")
# else:
#     print("The number ", num1, " is a odd number.")

"A company decided that they will give 10% increment of their employees salary."
"NOTE: They will give only those employees whose YOS[Year of Service] is greater than SIX years."
# new_Salary = 0

# name = input("Enter the name of employee: ")
# salary = int(input("Enter the salary: "))
# year = int(input("Enter the YEAR OF SERVICE (YOS): "))
# if(year>6):
#     print("Yes!!!!", name, " you are eligible for increment. ")
#     increment = salary*(10/100)
#     new_Salary +=(salary+increment)
#     print("Incremented Salary", new_Salary)
# else:
#     print(name, "you are not eligible for the incrememt.")



"Create a function to return factorial of a number"
# factorial = 1
# i = 1 
# num1 = int(input("Enter a number to find it's factorial: "))
# num2 = num1
# while i <= num2:
#     factorial *= num2
#     num2 -= 1

# print("The factorial of " , num1, "is",  factorial)


"Write a program to print the Fibonacci sequence up to n terms"
# n = int(input("Enter the numbers of terms: "))
# a = 0
# b = 1

# for i in range(n):
#     print (a, end =" ")
#     next = a+b
#     a = b
#     b = next

"Write a function to check if a string is a palindrome"
# num = int(input("Enter a number: "))
# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10          # Get last digit
#     reverse = reverse * 10 + digit  # Shift digits in reverse
#     num = num // 10           # Remove last digit

# if original == reverse:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome")


"Create a dictionary with 5 key-value pairs and print all keys"
# my_details = {"name" :  "Rohan", "age": 19, "college" : "BITS Pilani", "sem" : 2 , "CGPA" : 9}
# print(my_details)

# print(list(my_details.keys()))

# for key in my_details:
#     print(key)


