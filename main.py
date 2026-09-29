from inventory import (
    add_product,
    remove_product,
    search_product,
    update_quantity,
    display_inventory,
    low_stock_products,
    total_inventory_value,
)
from storage import load_inventory, save_inventory


DATA_FILE = "data/inventory.pkl"


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter 0 or a positive integer.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a number.")


def show_menu():
    print("\n" + "=" * 42)
    print("        INVENTORY MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Display Inventory")
    print("6. Show Low-Stock Products")
    print("7. Calculate Total Inventory Value")
    print("8. Exit")
    print("=" * 42)


def main():
    inventory = load_inventory(DATA_FILE)
    print("Inventory Management System")
    print("Data loaded successfully.")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter product name: ").strip()
            if not name:
                print("Product name cannot be empty.")
                continue
            price = get_positive_float("Enter price: ")
            quantity = get_non_negative_int("Enter quantity: ")

            if add_product(inventory, name, price, quantity):
                save_inventory(DATA_FILE, inventory)
                print("Product added successfully.")
            else:
                print("Product already exists.")

        elif choice == "2":
            name = input("Enter product name to remove: ").strip()
            if remove_product(inventory, name):
                save_inventory(DATA_FILE, inventory)
                print("Product removed successfully.")
            else:
                print("Product not found.")

        elif choice == "3":
            name = input("Enter product name to search: ").strip()
            product = search_product(inventory, name)
            if product:
                print(f"\nProduct: {product['name']}")
                print(f"Price: ₹{product['price']:.2f}")
                print(f"Quantity: {product['quantity']}")
                print(f"Value: ₹{product['price'] * product['quantity']:.2f}")
            else:
                print("Product not found.")

        elif choice == "4":
            name = input("Enter product name: ").strip()
            quantity = get_non_negative_int("Enter new quantity: ")
            if update_quantity(inventory, name, quantity):
                save_inventory(DATA_FILE, inventory)
                print("Quantity updated successfully.")
            else:
                print("Product not found.")

        elif choice == "5":
            display_inventory(inventory)

        elif choice == "6":
            threshold = get_non_negative_int("Show products with quantity at or below: ")
            products = low_stock_products(inventory, threshold)
            if products:
                print("\nLow-stock products:")
                for product in products:
                    print(f"- {product['name']}: {product['quantity']} units")
            else:
                print("No products match the low-stock condition.")

        elif choice == "7":
            total = total_inventory_value(inventory)
            print(f"\nTotal inventory value: ₹{total:.2f}")

        elif choice == "8":
            save_inventory(DATA_FILE, inventory)
            print("Inventory saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 to 8.")


if __name__ == "__main__":
    main()
