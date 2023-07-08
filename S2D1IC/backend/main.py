from flask import Flask, render_template, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Initialize the menu with some sample dishes
menu = [
    {"id": 1, "name": "Pizza", "price": 10.99, "availability": True},
    {"id": 2, "name": "Burger", "price": 5.99, "availability": True},
    {"id": 3, "name": "Pasta", "price": 7.99, "availability": False}
]


# Initialize the orders list
orders = []


# Route to display the menu
@app.route('/menu')
def display_menu():
    
    return menu
# Route to add a new dish to the menu
@app.route('/add_dish', methods=['POST'])
def add_dish():
    data=request.get_json()
    dish_id = data['id']
    dish_name = data['name']
    dish_price = data['price']
    dish_availability = data['availability']
    
    # Convert dish_id and dish_price to the appropriate data types if needed
    
    new_dish = {
        "id": dish_id,
        "name": dish_name,
        "price": dish_price,
        "availability": dish_availability
    }
    menu.append(new_dish)
    
    return "Item created successfully!"

# Route to remove a dish from the menu
@app.route('/remove_dish/<int:item_id>', methods=['DELETE'])
def remove_dish(item_id):
    dish_id = int(item_id)
    
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            break
    
    return "Item deleted successfully!"

# Route to update the availability of a dish
@app.route('/update_availability/<int:item_id>', methods=['PATCH'])
def update_availability(item_id):
    dish_id = int(item_id)
    data=request.get_json()
    new_availability = data["availability"]
    
    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = new_availability
            return "Item updated successfully!"
     

# Route to take a new order
@app.route('/new_order', methods=['POST'])
def new_order():
    data=request.get_json()
    customer_name = data["customer_name"]
    dish_ids = data['dish_ids']
    
    order = {
        "id": len(orders) + 1,
        "customer_name": customer_name,
        "dish_ids": dish_ids,
        "status": "received"
    }
    
    for dish_id in dish_ids:
        dish = next((d for d in menu if d['id'] == dish_id), None)
        if not dish or not dish['availability']:
            return "Error: Invalid dish ID or dish not available"
    
    orders.append(order)
    
    return "Order placed successfully"

# Route to update the status of an order
@app.route('/update_order_status/<int:order_id>', methods=['POST'])
def update_order_status(order_id):
    order_id = order_id
    data=request.get_json()
    new_status = data['status']
    
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return "Error: Invalid order ID"
    
    order['status'] = new_status
    
    return "Order updated successfully!"

# Route to display all orders
@app.route('/orders')
def display_orders():
    return orders


# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
