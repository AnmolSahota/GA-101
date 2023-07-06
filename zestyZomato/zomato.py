def add_dish(menu):
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available? (yes/no): ")
    menu.append({"dish_id": dish_id, "dish_name": dish_name, "price": price, "availability": availability})
    print("Dish added to the menu.")

def remove_dish(menu):
    dish_id = input("Enter the dish ID to remove: ")
    for dish in menu:
        if dish["dish_id"] == dish_id:
            menu.remove(dish)
            print("Dish removed from the menu.")
            return
    print("Dish ID not found in the menu.")

def update_availability(menu):
    dish_id = input("Enter the dish ID to update availability: ")
    for dish in menu:
        if dish["dish_id"] == dish_id:
            availability = input("Is the dish available now? (yes/no): ")
            dish["availability"] = availability
            print("Availability updated.")
            return
    print("Dish ID not found in the menu.")

def take_order(menu, orders):
    customer_name = input("Enter customer name: ")
    order_dishes = input("Enter dish IDs (comma-separated): ").split(",")
    order = {"order_id": len(orders) + 1, "customer_name": customer_name, "dish_ids": order_dishes, "status": "received"}
    
    for dish_id in order_dishes:
        dish_available = False
        for dish in menu:
            if dish["dish_id"] == dish_id and dish["availability"] == "yes":
                dish_available = True
                break
        if not dish_available:
            print(f"Dish ID {dish_id} is either unavailable or doesn't exist. Order cannot be processed.")
            return
    
    orders.append(order)
    print("Order placed successfully.")

def update_order_status(orders):
    order_id = int(input("Enter the order ID to update status: "))
    for order in orders:
        if order["order_id"] == order_id:
            status = input("Enter the new status: ")
            order["status"] = status
            print("Order status updated.")
            return
    print("Order ID not found.")

def review_orders(orders):
    print("All orders:")
    for order in orders:
        print(f"Order ID: {order['order_id']}, Customer: {order['customer_name']}, Status: {order['status']}")

def exit_system():
    print("Exiting the system...")
    # Additional clean-up or saving operations can be performed here, if needed.
    exit()

# Initialize menu and orders
menu = []
orders = []

# Main program loop
while True:
    print("\n----- Zesty Zomato Menu Management -----")
    print("1. Add a new dish to the menu")
    print("2. Remove a dish from the menu")
    print("3. Update dish availability")
    print("4. Take a new order")
    print("5. Update order status")
    print("6. Review all orders")
    print("7. Exit system")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_dish(menu)
    elif choice == "2":
        remove_dish(menu)
    elif choice == "3":
        update_availability(menu)
    elif choice == "4":
        take_order(menu, orders)
    elif choice == "5":
        update_order_status(orders)
    elif choice == "6":
        review_orders(orders)
    elif choice == "7":
        exit_system()
    else:
        print("Invalid choice. Please try again.")
