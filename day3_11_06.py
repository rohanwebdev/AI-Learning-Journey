import numpy as np

"6. Create a 3x3 NumPy array with values from 1 to 9"
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# len = len(arr)
# for i in range(len):
#     for j in range(len):
#         print(arr[i][j])

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in range(0,9):
    # print(arr[i])

# matrix = arr.reshape(3,3)
# for i in range (3):
    # print(matrix)
    # print(matrix[i])


" 7. Find the mean, median, and standard deviation of the array"
# arr = np.arange(1,10)
# print(arr) 
# len = len(arr)  
# print(len)
# matrix = arr.reshape(3,3)
# print(matrix)
# mean = np.mean(matrix)
# print("Mean of the matrix is: ", mean)
# median = np.median(matrix)
# print("Meadian of the matrix is: ", median)
# std = np.std(matrix)
# print("St. Dev of the matrix is: ", std)
# mean2 = matrix.mean()
# print("Mean2 of the matrix is: ", mean2)

" 8. Slice the first row and second column of a matrix"
# arr = np.arange(1,10)
# matrix = arr.reshape(3,3)
# print(matrix)
# print("First row:", matrix[0, :])
# print("Second column:", matrix[:, 1])

" 9. Reshape a 1D array of 12 elements into a 3x4 matrix"
# arr = np.arange(1,13)
# print(arr)
# matrix = arr.reshape(3,4)
# print(matrix)

" 10. Multiply two NumPy arrays of same shape element-wise"
# arr1 = np.arange(1,10)
# arr2 = np.arange(10,19)
# matrix1 = arr1.reshape(3,3)
# matrix2 = arr2.reshape(3,3)
# print("Matrix 1: ", matrix1)
# print('\n')
# print("Matrix 2: ", matrix2)
# print('\n')
# new = matrix1*matrix2
# print("New metrix :",new)


"INSTITUTE QUESTIONS"
"WAP to find out wheather the entered alphabet is vowel or consonent"
# alpha = input("Enter the char to find out vowel or consonent: ")
# if(alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u' ):
#     print("Entered char", alpha,  "is vowel.")
# elif(alpha == 'A' or alpha == 'E' or alpha == 'I' or alpha == 'O' or alpha == 'U' ):
#     print("Entered char", alpha,  "is vowel.")
# else:
#     print("Entered char", alpha,  "is consonent.")

"WAP to find the greatest number from THREE numbers"
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if(a>b and a>c):
#     print(a, "is the greatest")
# elif(b>a and b>c):
#     print(b, "is the greatest")
# elif(c>a and c>b):
#     print(c, "is the greatest")
# else:
#     print("All numbers are EQUAL")

"WAP to calculate the electricity bill(accept number of unit from user), accordingly to the following criteria"
"Units = first 100, next 100, after 200 & Charges = NO charges, 5rs per unit, 10rs per unit"
"For e.g. (if unit is 350 than total bill amount is 2000rs)"
# unit = int(input("Enter the number of units: "))
# bill_amt =  0
# first100 = 0
# second100 = 0
# if(unit<=100):
#     print("NO Charges")
# elif(unit<=200):
#     bill_amt += (unit-100)*5
#     print("The bill amount is ", bill_amt)
# elif(unit>200):
#     first100 += (unit-100) 
#     second100 = (first100 - 100)
#     bill_amt = (first100 + (second100*5) + second100*10)
# else:
#     print("Ivalid Input")

"OR"

# unit = int(input("Enter the number of units: "))
# bill_amt = 0

# if unit <= 100:
#     bill_amt = 0
# elif unit <= 200:
#     bill_amt = (unit - 100) * 5
# else:
#     # First 100 units: free
#     # Next 100 units (101 to 200): ₹5 per unit
#     # Units above 200: ₹10 per unit
#     bill_amt = (100 * 5) + (unit - 200) * 10

# print("The total bill amount is ₹", bill_amt)



"Day 2: NumPy + Logic Building"
"🧠 Core Concepts You'll Learn Today:"
"Concept	             -   Use in AI/ML"
"NumPy Arrays	         -   Base structure for data manipulation"
"Reshaping & Slicing	 -   Feeding proper shapes into ML models"
"Conditional Operations	 -   Building decision logic for data preprocessing"
"Vectorized Computation	 -   Fast processing over large datasets"

"1. Create a 1D NumPy array from 1 to 10"
# arr = np.arange(1,11)
# print(arr)

"2. Reshape it into a 2×5 matrix"
# arr = np.arange(1,11)
# matrix = arr.reshape(2,5)
# print(matrix)

"3. Slice and print the first row"
# arr = np.arange(1,11)
# matrix = arr.reshape(2,5)
# print(matrix[0])



"4. Print the last column"
# arr = np.arange(1,11)
# matrix = arr.reshape(2,5)
# print(matrix[:,-1])

"5. Print only the even numbers"
# arr = np.arange(1,11)
# matrix = arr.reshape(2,5)
# for i in range(2):
#     for j in range (5):
#         if(matrix[i][j]%2==0):
#             print(matrix[i][j])

"6. Replace all odd numbers with -1"
# arr = np.arange(1,11)
# matrix = arr.reshape(2,5)
# for i in range(2):
#     for j in range (5):
#         if(matrix[i][j]%2!=0):
#             matrix[i][j] = -1

# print(matrix)

"7. Multiply the matrix by 2"
# arr = np.arange(1,11)
# matrix = arr.reshape(2,5)
# matrix = matrix*2
# print(matrix)

"8. Find max value in each row"
# arr = np.arange(1,11)
# matrix = arr.reshape(2,5)
# for i in range(2):
#     print(f"Max in row {i+1}: {max(matrix[i])}")

"9. From array 1–100, print values divisible by 7"
# arr = np.arange(1,101)
# matrix = arr.reshape(10,10)
# for i in range(10):
#     for j in range (10):
#         if(matrix[i][j]%7==0):
#             print(matrix[i][j])

"10. Check if a number (like 42) exists in the array"
arr = np.arange(1,101)
matrix = arr.reshape(10,10)
for i in range(10):
    for j in range(10):
        if(matrix[i][j]==42):
            print("Yes, 42 exist")