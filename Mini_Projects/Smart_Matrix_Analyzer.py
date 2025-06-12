import numpy as np

# # Create a 3x3 empty matrix (initialized with zeros)
# arr = np.zeros((3, 3), dtype=int)

# # Taking input from user
# for i in range(3):
#     for j in range(3):
#         arr[i][j] = int(input(f"Enter the value at index [{i}][{j}]: "))

# print("\nYour 3x3 Matrix:")
# print(arr)

import numpy as np

# 📥 Step 1: Take matrix input from user in one line
user_input = input("Enter 9 numbers separated by space (for 3x3 matrix): ")
numbers = list(map(int, user_input.strip().split()))

# ✅ Validate length
if len(numbers) != 9:
    print("❌ Please enter exactly 9 numbers.")
    exit()

# 🧠 Step 2: Reshape into 3x3 matrix
matrix = np.array(numbers).reshape(3, 3)

# 📊 Step 3: Calculations
total_sum = np.sum(matrix)
max_value = np.max(matrix)
min_value = np.min(matrix)
primary_diagonal_sum = np.trace(matrix)
secondary_diagonal_sum = np.trace(np.fliplr(matrix))  # flip left-right

# 🖨 Step 4: Pretty print matrix
print("\n🧾 Matrix (3x3):")
for row in matrix:
    print("  ".join(f"{num:2}" for num in row))

# ✅ Step 5: Display results
print("\n📊 Matrix Analysis:")
print("Total Sum             :", total_sum)
print("Maximum Value         :", max_value)
print("Minimum Value         :", min_value)
print("Primary Diagonal Sum  :", primary_diagonal_sum)
print("Secondary Diagonal Sum:", secondary_diagonal_sum)

# ✨ Bonus: Show diagonals separately
print("\n✨ Diagonal Elements:")
print("Primary Diagonal     :", [matrix[i][i] for i in range(3)])
print("Secondary Diagonal   :", [matrix[i][2 - i] for i in range(3)])


