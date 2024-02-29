def check_palindrome(user_input):
    user_input = user_input.strip(" ")
    if user_input == user_input[::-1]:
        print("palindrome: " + user_input)
    print("not a palindrome: " + user_input)
    
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
