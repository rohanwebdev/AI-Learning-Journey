"WAF Given a list of numbers, write a function remove_duplicates(lst) that returns a new list with duplicates removed (preserving order)."
def remove_duplicates(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

input_str = input("Enter numbers separated by space: ")
input_list = [int(x) for x in input_str.split()]

result = remove_duplicates(input_list)
print("List after removing duplicates:", result)