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
# N = int(input("Enter the number: "))

# # Outer loop runs N times, once for each row
# for i in range(1, N + 1):
# 	# Inner loop prints 'N - i' spaces
# 	for j in range(1, N - i + 1):
# 		print(" ", end="")
		
# 	# Inner loop prints 'i' stars
# 	for j in range(1, i + 1):
# 		print("*", end="")
# 	# Move to the next line
# 	print()


#           * 
#         * * 
#       * * * 
#     * * * *
#   * * * * *



rows = 6
# def reverse_left_half_pyramid(rows):
"""Prints a reverse left half pyramid pattern.

    Args:
        rows: The number of rows in the pyramid.
    """
for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * i)

# Example usage:
# rows = 5
# reverse_left_half_pyramid(rows)

