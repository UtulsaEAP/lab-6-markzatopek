def process_and_print(input_string):
      # Split into separate strings

    # Convert strings to integers and filter out negative values
    input_data = [int(i) for i in input_string.split() if int(i) < 0]

    # Sort integers in reverse order
    input_data.sort(reverse=True)
  
    # Print sorted integers
    print(" ".join(input_data), end=" ")
    
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
