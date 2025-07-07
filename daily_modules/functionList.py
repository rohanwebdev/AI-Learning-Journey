"Exercise 1: Write a function is_prime(n) that returns True if n is prime, otherwise False."
# def isPrime(n):
#     #since 0 and 1 is not prime return false.
#     if(n==1 or n==0):  return False

#     #Run a loop from 2 to n-1
#     for i in range(2,n):
#     #if the number is divisible by i, then n is not a prime number.
#         if(n%i==0):
#             return False

#     #otherwise, n is prime number.
#     return True



# def add_nums(a,b):
#     result = a+b
#     return result

# sum = add_nums(3,5)
# print(f"Sum is {sum}")


"Write a recursive function."
def parentFunc():
    hello()
def hello():
    print("Hello Function.")
    today()
def today():
    print("Today's Function.")
    jump()
def jump():
    print("Jump Function.")
    addition()
def addition():
    print("Addition Function.")
    bye()
def bye():
    print("Bye Function.")
    exit()
def exit():
    print("Exit Function.")
parentFunc()