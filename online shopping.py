product_catalog = {
    "1": {"name": "Smartphone", "price": 50000},
    "2": {"name": "Laptop", "price": 10000},
    "3": {"name": "Headphones", "price": 1000},
    "4": {"name": "Tablet", "price": 3000},
}

shopping_cart = {}

def display_catalog():
    print("\nProduct Catalog:")
    for product_id, product_info in product_catalog.items():
        print(f"{product_id}: {product_info['name']} - ₹{product_info['price']}")

def add_to_cart(product_id, quantity):
    if product_id in product_catalog:
        if product_id in shopping_cart:
            shopping_cart[product_id] += quantity
        else:
            shopping_cart[product_id] = quantity
        print(f"Added {quantity} {product_catalog[product_id]['name']} to your cart.")
    else:
        print("Product not found in the catalog.")

def display_cart():
    print("\nShopping Cart:")
    total_cost = 0
    for product_id, quantity in shopping_cart.items():
        product_info = product_catalog[product_id]
        cost = quantity * product_info["price"]
        total_cost += cost
        print(f"{product_info['name']} x{quantity}: ₹{cost}")
    print(f"Total: ₹{total_cost}")

while True:
    print("\nOptions:")
    print("1: Display Product Catalog")
    print("2: Add Item to Cart")
    print("3: Display Shopping Cart")
    print("4: Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_catalog()
    elif choice == "2":
        product_id = input("Enter the product ID: ")
        quantity = int(input("Enter the quantity: "))
        add_to_cart(product_id, quantity)
    elif choice == "3":
        display_cart()
    elif choice == "4":
        print("\nThank you for shopping with us. Welcome!\n")
        break
    else:
        print("\nInvalid choice. Please try again.\n")
