"WAP to print n natural numbers with their sum and avg"
# i = 1
# sum = 0
# num = int(input("Enter a number: "))
# while (i <= num):
#     print(i)
#     sum += i
#     i += 1
# avg = sum/(i-1)
# print("Sum of the first ", num , "natural numbers is: ", sum)
# print("Avg of the first ", num , "natural numbers is: ", avg)

"WAP to find even number till user input and their sum"
# i = 1
# sum = 0
# num = int(input("Enter a number: "))
# while (i <= num):
#     if(i%2==0):
#         print(i)
#         sum += i
#     i += 1
# print(f"Sum is {sum}")


"WAP to find ODD number till user input and their sum"
# i = 1
# sum = 0
# num = int(input("Enter a number: "))
# while (i <= num):
#     if(i%2!=0):
#         print(i)
#         sum += i
#     i += 1
# print(f"Sum is {sum}")


"WAP to print table till 10 of the given number by user"
# i = 1
# num = int(input("Enter a number: "))
# while (i <= 10):
#     print(f"{num} * {i} = {num*i}")
#     i += 1


"WAP to check is the given number is palindrome or not"
# num = int(input("Enter a number to check : "))
# copy = num
# rev = 0
# while(num > 0):
#     digit = num % 10
#     rev = (rev * 10) + digit
#     num = num //10

# if(copy == rev ):
#     print(f"{copy} is a palindrome number>")
# else:
#     print(f"{copy} is not a palindrome number>")


"WAP to check is the given number is armstrong or not"
# num = int(input("Enter a number to check : "))
# copy = num
# count = 0
# sum = 0
# while(num > 0):
#     num % 10
#     count += 1
#     num = num // 10

# num = copy
# while (num  > 0):
#     digit = num % 10
#     sum += digit**count
#     num = num// 10

# if(sum == copy):
#     print(f"Yes! {copy} is an armstrong number")
# else:
#     print(f"No! {copy} is not an armstrong number")



# if(copy == rev ):
#     print(f"{copy} is an armstrong number>")
# else:
#     print(f"{copy} is not an armstrong number>")



"OR"

num = int(input("Enter a number to check : "))
copy = num
count = len(str(num))
sum = 0
while (num  > 0):
    digit = num % 10
    sum += digit**count
    num = num// 10

if(sum == copy):
    print(f"Yes! {copy} is an armstrong number")
else:
    print(f"No! {copy} is not an armstrong number")
