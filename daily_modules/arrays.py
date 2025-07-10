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


"Task: WAF that gets size from user input then append the elems in the list then print it."
# def list(num):
#     list = []
#     for i in range(num):
#         index = int(input(f"Enter the element at index[{i}]: ")) 
#         list.append(index)
#     return list
# number = int(input("Enter the length of the list: "))
# result = list(number)
# print(f"The size of list is {number} and appended list is {result}")


"Count how many even and odd numbers are present in the list."
# def count(numlist):
#     oddCount = 0
#     evenCount = 0
#     size = len(numlist)
#     for i in range (size):
#         if(num_list[i]%2 == 0):
#             evenCount += 1
#         else:
#             oddCount += 1
#     return evenCount, oddCount

# input_str = input("Enter numbers separated by space: ")
# num_list = [int(i) for i in input_str.split()]
# evenCount, oddCount = count(num_list)
# print(f"The no. of EVEN numbers is {evenCount} \nThe no. of ODD numbers is {oddCount}")



# def list(strlist):
#     num_list = [int(i) for i in strlist.split()]
#     return num_list

# str_list = input("Enter the elems of the list separated by space: ")
# result = list(str_list)
# print(f"The list is {result}")


"Given an array, remove all duplicates and return a list of unique elements."
# def dupsremove(strlist):
#     num_list = [int(i) for i in strlist.split()]
#     newList = []
#     for i in num_list:
#         if i not in newList:
#             newList.append(i)
#     return newList

# str_list = input("Enter the elems of the list separated by space: ")
# result = dupsremove(str_list)
# print(f"The list after deleting elems is {result}")

"Find the second highest number in a list."
# def second_Highest_Elem(strlist):
#     num_list = [int(i) for i in strlist.split()]
    
#     # Remove duplicates to get distinct values only
#     unique_nums = list(set(num_list))

#     if len(unique_nums) < 2:
#         return "No second highest found"

#     unique_nums.sort(reverse=True)
#     return unique_nums[1]

# str_list = input("Enter the elems of the list separated by space: ")
# result = second_Highest_Elem(str_list)
# print(f"The second highest number in the list is {result}")


"Sort the list using any sorting logic like bubble sort or selection sort (don't use sort() or sorted())."
# def list(num):
#     list = []
#     for i in range(num):
#         index = int(input(f"Enter the element at index[{i}]: ")) 
#         list.append(index)
#     return list
# number = int(input("Enter the length of the list: "))
# result = list(number)
# print(f"The size of list is {number} and appended list is {result}")


"Sort the list using any sorting logic like bubble sort or selection sort (don't use sort() or sorted())."
"bubble sort"

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         # Track if any swap was made
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 # Swap
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         # If no swaps, list is sorted
#         if not swapped:
#             break
#     return arr



"selection sort"
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         # Swap minimum with current index
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr


"A list is a palindrome if it reads the same forward and backward. Check if a given list is a palindrome."
# def palindrome(listt):
#     rev_list = listt[::-1]
#     if(rev_list == listt):
#         return "Yes"
#     else:
#         return "No"
# str_list = input("Enter the elems of the list separated by spaces: ")
# num_list = [int(i) for i in str_list.split()]
# result = palindrome(num_list)
# print(f"{result}! palindrome list.")


"Multiply each element in the array by a given number (e.g., 2)."
# def multiplied_List(listt, numm):
#     multiplied_list = []
#     for i in range(len(listt)):
#         elem = listt[i]*numm 
#         multiplied_list.append(elem)
#     return multiplied_list
# str_list = input("Enter the elems of the list separated by spaces: ")
# num = int(input("Enter the num to be multiplied: "))
# num_list = [int(i) for i in str_list.split()]
# result = multiplied_List(num_list, num)
# print(f"Original list {num_list}\nMultiplied list by {num}: {result}")


"Take two arrays, merge them into one, and sort the resulting array."
# def mergeSort(list1, list2):
#     list3 = []
#     list3 = list1  + list2
#     originalList = list3.copy()
#     n = len(list3)
#     for i in range(n):
#         # Track if any swap was made
#         swapped = False
#         for j in range(0, n - i - 1):
#             if list3[j] > list3[j + 1]:
#                 # Swap
#                 list3[j], list3[j + 1] = list3[j + 1], list3[j]
#                 swapped = True
#         # If no swaps, list is sorted
#         if not swapped:
#             break
#     return list3, originalList
    
# str_list1 = input("Enter the elems of the list1 separated by spaces: ")
# num_list1 = [int(i) for i in str_list1.split()]
# str_list2 = input("Enter the elems of the list2 separated by spaces: ")
# num_list2 = [int(i) for i in str_list2.split()]
# list3, originalList = mergeSort(num_list1, num_list2)
# print(f"First list: {num_list1}\nSecond List: {num_list2}\nCombined added: {originalList}\nSorted list : {list3}")