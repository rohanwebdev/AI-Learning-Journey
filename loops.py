# num = int(input("Enter a number: "))

# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print(" ")

# *  
# * *
# * * *
# * * * *
# * * * * *


# Number of rows
N = int(input("Enter the number: "))

# Outer loop runs N times, once for each row
for i in range(1, N + 1):
	# Inner loop prints 'N - i' spaces
	for j in range(1, N - i + 1):
		print(" ", end="")
		
	# Inner loop prints 'i' stars
	for j in range(1, i + 1):
		print("*", end="")
	# Move to the next line
	print()


#           * 
#         * * 
#       * * * 
#     * * * *
#   * * * * *
