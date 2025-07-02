"WAP that prints \"DONE\" when it prints all number from 1 to 10."
# for i in range (1,11):
#     print(i)
# print("DONE!!!")


"WAP to get cubes of the number from 1 to user input."
# num = int(input("Enter the number: "))
# for i in range(1, num+1):
#     print(i**3)


"WAP to get the factorial of the number."
# result = 1
# num = int(input("Enter the number: "))
# for i in range(1 , num+1):
#     result *= i
# print(f"Factorial of {num} is {result}.")

"WAP to find the greatest and smallest digit from a number."
num  = int(input("Enter the number: "))
numStr = str(num)
greatestdigi = 0
smallestdigi = 9
for i in numStr:
    digit = int(i)
    if(digit > greatestdigi):
        greatestdigi = digit
print(f"Greatest digit from {num} is {greatestdigi}")

for i in numStr:
    digit = int(i)
    if(smallestdigi > digit):
        smallestdigi = digit
print(f"Smalllest digit from {num} is {smallestdigi}")
