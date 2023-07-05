# Snack Inventory Management System

# Dictionary to store the snack inventory
inventory = {}

# Dictionary to store the sales record
sales_record = {}

def add_snack():
    """
    Function to add a snack to the inventory.
    """
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    price = float(input("Enter price: "))
    availability = input("Is the snack available? (yes/no): ")
    
    snack = {
        "snack_name": snack_name,
        "price": price,
        "availability": availability
    }
    
    inventory[snack_id] = snack
    print("Snack added to inventory successfully.")

def remove_snack():
    """
    Function to remove a snack from the inventory.
    """
    snack_id = input("Enter snack ID to remove: ")
    
    if snack_id in inventory:
        del inventory[snack_id]
        print("Snack removed from inventory successfully.")
    else:
        print("Snack not found in inventory.")

def update_availability():
    """
    Function to update the availability of a snack in the inventory.
    """
    snack_id = input("Enter snack ID to update availability: ")
    
    if snack_id in inventory:
        availability = input("Is the snack available? (yes/no): ")
        inventory[snack_id]["availability"] = availability
        print("Snack availability updated successfully.")
    else:
        print("Snack not found in inventory.")

def make_sale():
    """
    Function to record a snack sale.
    """
    snack_id = input("Enter snack ID sold: ")
    
    if snack_id in inventory:
        if inventory[snack_id]["availability"] == "yes":
            # Update inventory
            inventory[snack_id]["availability"] = "no"
            
            # Update sales record
            if snack_id in sales_record:
                sales_record[snack_id] += 1
            else:
                sales_record[snack_id] = 1
            
            print("Sale recorded successfully.")
        else:
            print("Snack is not available.")
    else:
        print("Snack not found in inventory.")

def display_inventory():
    """
    Function to display the current snack inventory.
    """
    print("Snack Inventory:")
    for snack_id, snack in inventory.items():
        print(f"ID: {snack_id}\tName: {snack['snack_name']}\tPrice: {snack['price']}\tAvailability: {snack['availability']}")
    print("")

def display_sales_record():
    """
    Function to display the sales record.
    """
    print("Sales Record:")
    for snack_id, quantity in sales_record.items():
        snack = inventory[snack_id]
        print(f"ID: {snack_id}\tName: {snack['snack_name']}\tQuantity Sold: {quantity}")
    print("")

# Main program loop
while True:
    print("Welcome to Mumbai Munchies - Snack Inventory Management System")
    print("Please select an option:")
    print("1. Add Snack to Inventory")
    print("2. Remove Snack from Inventory")
    print("3. Update Snack Availability")
    print("4. Record Snack Sale")
    print("5. Display Inventory")
    print("6. Display Sales Record")
    print("7. Quit")
    
    choice = input("Enter your choice (1-7): ")
    print("")
    
    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        make_sale()
    elif choice == "5":
        display_inventory()
    elif choice == "6":
        display_sales_record()
    elif choice == "7":
        print("Thank you for using the Snack Inventory Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-7).")
    
    print("")
