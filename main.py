
# Function to display the menu
def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ₹{price:.2f}")

# Function to add an item to the menu


def add_item(menu):
    item = input("Enter the item name: ")
    price = float(input("Enter the item price: ₹"))
    menu[item] = price
    print(f"{item} added to the menu.")

# Function to remove an item from the menu


def remove_item(menu):
    item = input("Enter the item name to remove: ")
    if item in menu:
        del menu[item]
        print(f"{item} removed from the menu.")
    else:
        print(f"{item} not found in the menu.")

# Function to take a customer's order


def take_order(menu):
    order = []
    print("Enter the items you want to order (press 'q' to finish):")
    while True:
        item = input("Item: ")
        if item.lower() == 'q':
            break
        if item in menu:
            order.append(item)
        else:
            print(f"{item} is not available in the menu.")
    return order


# Function to calculate the total bill 


def calculate_bill(order, menu):
    total = 0.0
    print("Order:")
    for item in order:
        price = menu[item]
        print(f"{item}: ₹{price:.2f}")
        total += price
    print(f"Total bill: ₹{total:.2f}")

# Main program loop


def main():
    menu = {}

    while True:
        print("\nRestaurant Management System")
        print("1. Display Menu")
        print("2. Add Item to Menu")
        print("3. Remove Item from Menu")
        print("4. Take Customer Order")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            add_item(menu)
        elif choice == '3':
            remove_item(menu)
        elif choice == '4':
            order = take_order(menu)
            calculate_bill(order, menu)
        elif choice == '5':
            break
        else:
            print("Invalid Input:: Please Enter the valid Input.")


main()
