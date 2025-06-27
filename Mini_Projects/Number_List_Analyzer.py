"Build a Python script that:"
"Takes a list of numbers input by the user (e.g. 2 5 5 9 3 2)"
"Outputs:"
"Max, min, sum, and average"
"Number of unique elements"
"Sorted list (ascending & descending)"

def number_list_analyzer():
    # Step 1: Get input from the user
    user_input = input("Enter numbers separated by spaces: ")
    
    # Step 2: Convert the input string to a list of integers
    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Please enter only valid integers.")
        return

    # Step 3: Analyze the numbers
    maximum = max(numbers)
    minimum = min(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    unique_elements = len(set(numbers))
    sorted_asc = sorted(numbers)
    sorted_desc = sorted(numbers, reverse=True)

    # Step 4: Display the results
    print(f"\nMaximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Sum: {total_sum}")
    print(f"Average: {average:.2f}")
    print(f"Unique Elements: {unique_elements}")
    print(f"Sorted Ascending: {sorted_asc}")
    print(f"Sorted Descending: {sorted_desc}")

# Run the function
number_list_analyzer()