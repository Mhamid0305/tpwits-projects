import json
import os

INVENTORY_FILE = 'inventory.json'

# -------------------------------
# Utility Functions
# -------------------------------

def load_data():
    """Retrieve inventory from the file."""
    if not os.path.exists(INVENTORY_FILE):
        return []
    try:
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(data):
    """Save the inventory to the file."""
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# -------------------------------
# Inventory Functionalities
# -------------------------------

def add_item():
    """Add a new item to the inventory."""
    name = input("Enter product name: ").strip()
    product_id = input("Enter product ID: ").strip()
    quantity = input("Enter quantity: ").strip()

    if not quantity.isdigit():
        print("❗ Quantity must be a numeric value.\n")
        return

    product = {"name": name, "id": product_id, "qty": int(quantity)}
    inventory = load_data()
    inventory.append(product)
    save_data(inventory)

    print("✅ Item added to inventory.\n")

def show_inventory():
    """Show the complete inventory list."""
    inventory = load_data()
    if not inventory:
        print("📂 Inventory is currently empty.\n")
        return

    print("\n📦 Current Inventory:")
    for idx, item in enumerate(inventory, 1):
        print(f"{idx}. Name: {item['name']} | ID: {item['id']} | Qty: {item['qty']}")
    print()

def update_item():
    """Update the quantity of an existing product."""
    target_id = input("Enter the ID of the product to update: ").strip()
    inventory = load_data()

    for item in inventory:
        if item['id'] == target_id:
            new_qty = input("Enter new quantity: ").strip()
            if not new_qty.isdigit():
                print("❌ Quantity must be a number.\n")
                return
            item['qty'] = int(new_qty)
            save_data(inventory)
            print("✅ Product quantity updated.\n")
            return

    print("🔍 No product found with this ID.\n")

def remove_item():
    """Remove an item by its ID."""
    target_id = input("Enter the ID of the product to delete: ").strip()
    inventory = load_data()
    new_inventory = [item for item in inventory if item['id'] != target_id]

    if len(new_inventory) == len(inventory):
        print("❌ No matching product found.\n")
    else:
        save_data(new_inventory)
        print("🗑️ Product successfully removed.\n")

def find_item():
    """Search for a product by name or ID."""
    query = input("Search by Name or ID: ").strip()
    inventory = load_data()
    results = [item for item in inventory if item['name'] == query or item['id'] == query]

    if results:
        for item in results:
            print(f"🔎 Found -> Name: {item['name']}, ID: {item['id']}, Qty: {item['qty']}")
    else:
        print("❌ No product matched your search.\n")

# -------------------------------
# Application Loop
# -------------------------------

def menu():
    while True:
        print("\n========= INVENTORY MENU =========")
        print("1. ➕ Add New Product")
        print("2. 📋 View Inventory")
        print("3. 🔄 Update Product Quantity")
        print("4. ❌ Delete Product")
        print("5. 🔍 Search Product")
        print("6. 🚪 Exit")

        choice = input("Select an option (1-6): ").strip()

        match choice:
            case '1': add_item()
            case '2': show_inventory()
            case '3': update_item()
            case '4': remove_item()
            case '5': find_item()
            case '6':
                print("👋 Exiting program. Goodbye!\n")
                break
            case _: print("⚠️ Invalid choice. Try again.\n")

# -------------------------------
# Run the Program
# -------------------------------

if __name__ == "__main__":
    menu()
