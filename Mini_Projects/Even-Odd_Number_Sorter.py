"🧮 Today's Task: Even-Odd Number Sorter with Summary"
"📝 Task Description:"
"Write a Python script that:"
"Takes a list of numbers from the user (e.g., 3 6 1 4 7 9 2 8)"
"Separates the even and odd numbers into two different lists"

"Outputs:"
"The list of even numbers (sorted ascending)"
"The list of odd numbers (sorted descending)"
"Count of even numbers"
"Count of odd numbers"
"Sum of even and odd numbers"
def sorted_lst(lst): 
    odd_list = []
    even_lst = []
    for num in lst:
        if num % 2 != 0:
            odd_list.append(num)
        else:
            even_lst.append(num)
    
    # Sorting
    odd_list.sort(reverse=True)
    even_lst.sort()
    
    return odd_list, even_lst


input_str = input("Enter numbers separated by space: ")
input_list = [int(x) for x in input_str.split()]

odd_list, even_lst = sorted_lst(input_list)

print("Even numbers (ascending):", even_lst)
print("Odd numbers (descending):", odd_list)
print("Count of even numbers:", len(even_lst))
print("Count of odd numbers:", len(odd_list))
print("Sum of even numbers:", sum(even_lst))
print("Sum of odd numbers:", sum(odd_list))
