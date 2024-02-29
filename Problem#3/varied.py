def process_input(input_string):
    if input_string == "": return None, None
    inputs = [float(string_input) for string_input in input_string.split()]
    
    max = inputs[0]
    avg = 0
    for i in inputs:
        if i > max: max = i
        avg += i
    avg /= len(inputs)
    
    return round(max, 2), round(avg, 2)

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
