def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    total = 10
    s1 = service_choice1 != "-"
    s2 = service_choice2 != "-"
    if s1:
        p1 = services[service_choice1]
        total += p1
    if s2:
        p2 = services[service_choice2]
        total += p2
        
    print("ZyCar Wash")
    print("Base car wash - $10")
    if s1: print(f"{service_choice1} - ${p1}")
    if s2: print(f"{service_choice2} - ${p2}")
    print("-----") # THIS WAS NOT IN THE INSTRUCTIONS
    print(f"Total price: ${total}")

    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
