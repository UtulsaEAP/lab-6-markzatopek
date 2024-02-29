def filter_and_print_range(input_list, min_val, max_val):
    input_list = [i for i in input_list if min_val <= i <= max_val]
    for i in input_list: print(i, end=",")

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = [int(i) for i in user_input.split()]

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = [int(i) for i in user_input.split()]

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
