def food_input():
    user_input = input()
    tokens = user_input.split()
    while user_input != "quit 0":
        print(f"Eating {tokens[1]} {tokens[0]} a day keeps you happy and healthy.")
        user_input = input()
        tokens = user_input.split()

    

if __name__ == "__main__":
    food_input()
