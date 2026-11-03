import json
import os

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

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

main()
