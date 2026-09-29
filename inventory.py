def add_product(inventory, name, price, quantity):
    """Add a new product if the name does not already exist."""
    key = name.strip().lower()

    if key in inventory:
        return False

    inventory[key] = {
        "name": name.strip(),
        "price": price,
        "quantity": quantity,
    }
    return True


def remove_product(inventory, name):
    """Remove a product by name."""
    key = name.strip().lower()

    if key in inventory:
        del inventory[key]
        return True

    return False


def search_product(inventory, name):
    """Return product information if the product exists."""
    key = name.strip().lower()
    return inventory.get(key)


def update_quantity(inventory, name, quantity):
    """Update the quantity of an existing product."""
    key = name.strip().lower()

    if key in inventory:
        inventory[key]["quantity"] = quantity
        return True

    return False


def display_inventory(inventory):
    """Display all products in a simple table."""
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n" + "-" * 68)
    print(f"{'Product':<25}{'Price':>12}{'Quantity':>12}{'Value':>15}")
    print("-" * 68)

    for product in inventory.values():
        value = product["price"] * product["quantity"]
        print(
            f"{product['name']:<25}"
            f"₹{product['price']:>10.2f}"
            f"{product['quantity']:>12}"
            f"₹{value:>13.2f}"
        )

    print("-" * 68)


def low_stock_products(inventory, threshold):
    """Return products whose quantity is at or below threshold."""
    result = []

    for product in inventory.values():
        if product["quantity"] <= threshold:
            result.append(product)

    return result


def total_inventory_value(inventory):
    """Calculate the total value of all products."""
    total = 0

    for product in inventory.values():
        total += product["price"] * product["quantity"]

    return total
