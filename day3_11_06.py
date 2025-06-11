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