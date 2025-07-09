"WAF to print array"
# def arr():
#     arr = [1, 33, 3, 4, 5]
#     print(arr)
# arr()

"WAF to take numbers separated by space and print it."
# def arr():
#     input_str = input("Enter numbers separated by space: ")
#     num_list = [int(x) for x in input_str.split()]
#     print("The array is:", num_list)
# arr()


"WAF to take numbers separated by space and print it and multiply by 2 each element."
# def arr():
#     input_str = input("Enter numbers separated by space: ")
#     num_list = [int(x) for x in input_str.split()]
#     num = int(input("Enter the number you want to multiply the array/matrix: "))
#     multiplied_arr = [x*num for x in num_list]
#     print("The Original array is:", num_list)
#     print("The Multiplied array is:", multiplied_arr)
# arr()

"WAF to input n numbers and find their sum."
# def arraySum():
#     summ = 0
#     input_str  = input("Enter numbers separated by space: ")
#     num_list = [int(i) for i in input_str.split()]
#     for i in num_list:
#         summ += i
#     return num_list, summ

# num_list, summ= arraySum()
# print(f"The array is {num_list} sum of array is {summ}")


"Write a function to reverse a list without using the built-in reverse() method."
# def reverse_arr(arr):
#     revarr = []
#     for i in range(len(arr)-1, -1, -1):
#         revarr.append(arr[i])
#     return revarr

# input_str = input("Enter numbers separated by space: ")
# num_list = [int(i) for i in input_str.split()]
# revarr = reverse_arr(num_list)
# print(f"The original array: {num_list} \nThe reversed array: {revarr}")

"OR"

# def reverse_arr(arr):
#     return arr[::-1]

# input_str = input("Enter numbers separated by space: ")
# num_list = [int(i) for i in input_str.split()]
# revarr = reverse_arr(num_list)
# print("Reversed array:", revarr)



"Given an array, find the maximum and minimum number in it."
# def min_max(arr):
#     maxx = max(arr)
#     minn = min(arr)
#     return minn, maxx
# input_str = input("Enter numbers separated by space: ")
# num_list = [int(i) for i in input_str.split()]
# minn, maxx = min_max(num_list)
# print(f"The MAX elem in the array is \"{maxx}\"\nThe  MIN elem in array is \"{minn}\"")


# a = ["orange", "mango", "kiwi", "pineapple", "banana"]
# a.sort()
# print(a)


# a = [100, 50, 65, 82, 23]
# a.sort()
# print(a)


# a = [100, 50, 65, 82, 23]
# a.sort(reverse=True)
# print(a)


# def myfunc(n):
#     return abs(n - 50)

# a = [100, 50 , 65, 82, 23]
# a.sort(key = myfunc)
# print(a)
# a = ["banana", "Orange", "Kiwi", "cherry"]
# a.sort()
# print(a)


# a = ["banana", "Orange", "Kiwi", "cherry"]
# a.reverse()
# print(a)


# a = ["hello", "world", "today"]
# b = a.copy()
# b[0] = "hi"
# print(b)
# print(a)


# a = ["hello", "world", "today"]
# a = list(a)
# print(a)


# a = ["hello", "world", "today"]
# a = a[:]
# print(a)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# for i in list2:
#     list1.append(i)
# print(list1)
# print(list2)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)