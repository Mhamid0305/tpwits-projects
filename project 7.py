import json
import os

DATA_FILE = "expenses_data.json"

# ------------------------------
# File I/O Helpers
# ------------------------------

def load_data():
    """Load existing expense entries from the data file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(expense_list):
    """Write the current list of expenses to the file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expense_list, file, indent=2)

# ------------------------------
# Core Features
# ------------------------------

def record_expense():
    """Prompt user to input a new expense and store it."""
    date = input("🗓️  Date (YYYY-MM-DD): ").strip()
    category = input("📁 Category (e.g., Rent, Utilities, Groceries): ").strip()
    amount_text = input("💵 Amount: ").strip()

    if not amount_text.isdigit():
        print("❌ Invalid input: Amount must be a number.\n")
        return

    amount = int(amount_text)
    entry = {"date": date, "category": category, "amount": amount}

    expenses = load_data()
    expenses.append(entry)
    save_data(expenses)

    print("✅ Expense successfully added!\n")

def list_expenses():
    """Display all saved expenses."""
    expenses = load_data()
    if not expenses:
        print("📭 No recorded expenses.\n")
        return

    print("\n📋 Expense Records:")
    for idx, item in enumerate(expenses, start=1):
        print(f"{idx}. {item['date']} | {item['category']} | Rs. {item['amount']}")
    print()

def calculate_total_expense():
    """Calculate and print the total amount spent."""
    expenses = load_data()
    total = sum(item['amount'] for item in expenses)
    print(f"\n🧾 Total Expenditure: Rs. {total}\n")

def search_expenses_by_date():
    """Find and display expenses for a given date."""
    target_date = input("🔍 Enter date to search (YYYY-MM-DD): ").strip()
    records = [item for item in load_data() if item['date'] == target_date]

    if not records:
        print("📅 No expenses recorded for this date.\n")
    else:
        print(f"\n📆 Expenses on {target_date}:")
        for record in records:
            print(f"- {record['category']} | Rs. {record['amount']}")
        print()

def summarize_by_category():
    """Summarize total spending in each category."""
    expenses = load_data()
    summary = {}

    for item in expenses:
        category = item['category']
        summary[category] = summary.get(category, 0) + item['amount']

    if not summary:
        print("📂 No expense data available to summarize.\n")
        return

    print("\n📊 Spending by Category:")
    for category, total in summary.items():
        print(f"- {category}: Rs. {total}")
    print()

# ------------------------------
# User Interaction Loop
# ------------------------------

def main_menu():
    while True:
        print("\n========= PERSONAL EXPENSE MANAGER =========")
        print("1️⃣  Add New Expense")
        print("2️⃣  View All Entries")
        print("3️⃣  Check Total Expenses")
        print("4️⃣  Search Expenses by Date")
        print("5️⃣  View Spending by Category")
        print("6️⃣  Exit")

        option = input("👉 Choose an option (1-6): ").strip()

        if option == "1":
            record_expense()
        elif option == "2":
            list_expenses()
        elif option == "3":
            calculate_total_expense()
        elif option == "4":
            search_expenses_by_date()
        elif option == "5":
            summarize_by_category()
        elif option == "6":
            print("👋 Exiting. Stay mindful of your spending!\n")
            break
        else:
            print("⚠️ Invalid selection. Please try again.\n")

# ------------------------------
# Run the App
# ------------------------------

if __name__ == "__main__":
    main_menu()
