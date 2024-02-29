def process_user_contacts(user_input):
    user_contacts = {token[0]: token[1] for token in [element.split(",") for element in user_input.split()]}

    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    print(user_contacts[contact_name])
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
