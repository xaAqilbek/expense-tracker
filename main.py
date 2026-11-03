import json
import os
from datetime import date

FILE_NAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)

def show_menu():
    print("=== Expense tracker menu ===")
    print("1. Add an expense")
    print("2. Show all expenses")
    print("3. Remove an expense")
    print("4. Show results")
    print("5. Exit")

def add_expenses(expenses):
    try:
        amount = float(input("Sum: "))
    except ValueError:
        print("Error: sum should be a number!")
        return

    if amount <= 0:
        print("Error: sum should be a positive number!")
        return

    category = input("Category (food, transport, education...): ").strip()
    if category == "":
        print("Error: category cannot be empty!")
        return

    description = input("Description: ").strip()

    if len(expenses) == 0:
        new_id = 1
    else:
        new_id = expenses[-1]["id"] + 1

    expense = {
        "id": new_id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": str(date.today()),
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!")

def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses!")
        return

    print("ID | Date | Amount | Category | Description")
    print("-" * 55)
    for expense in expenses:
        print(
            f"{expense['id']:<3}| {expense['date']} |"
            f"{expense['amount']:<8} | {expense['category']:<10} | "
            f"{expense['description']}"
        )

def remove_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses to remove.")
        return

    show_expenses(expenses)

    try:
        expense_id = int(input("Enter the ID to remove: "))
    except ValueError:
        print("Error: ID should be a number!")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print("Expense removed!")
            return
    print("Error: no expense with that ID was found!")

def show_results(expenses):
    if len(expenses) == 0:
        print("No expenses to show.")
        return

    total = 0
    by_category = {}

    for expense in expenses:
        total += expense["amount"]
        category = expense["category"]
        by_category[category] = by_category.get(category, 0) + expense["amount"]

    print("=== Total expenses ===")
    for category, amount in by_category.items():
        print(f"{category:<12}: {amount}")
    print("-" * 25)
    print(f"{'Total':<12}: {total}")

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expenses(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            remove_expenses(expenses)

        elif choice == "4":
            show_results(expenses)

        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

main()
