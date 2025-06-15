import json
import os

HISTORY_PATH = "calc_history.json"

# --------------------------
# File Handling Functions
# --------------------------

def read_history():
    """Read previous expressions from the history file."""
    if not os.path.isfile(HISTORY_PATH):
        return []
    try:
        with open(HISTORY_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def write_history(entries):
    """Write the updated history list to file."""
    with open(HISTORY_PATH, "w") as f:
        json.dump(entries, f, indent=2)

# --------------------------
# Core Calculator Logic
# --------------------------

def evaluate_expression():
    """Accepts an expression from user and evaluates it."""
    expr = input("🔢 Enter a math expression (e.g., 5 + 3 * 2): ")
    try:
        result = eval(expr)
        print(f"✅ Output: {result}\n")
        history = read_history()
        history.append({"expression": expr, "result": result})
        write_history(history)
    except Exception as err:
        print(f"❌ Error: Invalid expression!\n")

def show_all_history():
    """Displays all previous calculations."""
    history = read_history()
    if not history:
        print("📂 History is empty.\n")
        return
    print("\n📖 Previous Calculations:")
    for idx, record in enumerate(history, 1):
        print(f"{idx}. {record['expression']} = {record['result']}")
    print()

# --------------------------
# Main Application Loop
# --------------------------

def calculator_menu():
    while True:
        print("\n========= SIMPLE CALCULATOR =========")
        print("1️⃣  Calculate an Expression")
        print("2️⃣  View Calculation History")
        print("3️⃣  Exit Program")
        choice = input("👉 Your choice (1/2/3): ").strip()

        if choice == "1":
            evaluate_expression()
        elif choice == "2":
            show_all_history()
        elif choice == "3":
            print("👋 Thank you for using the calculator!")
            break
        else:
            print("⚠️ Invalid selection. Please try again.\n")

# --------------------------
# Entry Point
# --------------------------

if __name__ == "__main__":
    calculator_menu()
