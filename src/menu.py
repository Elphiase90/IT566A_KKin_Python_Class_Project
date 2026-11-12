"""Expense Tracker Menu"""

from datetime import datetime
from pathlib import Path
from .expensetracker import save_expenses, load_expenses, filter_expenses, export_csv


# Add a new expense
def add_expense(expenses, filename):
    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date.")
        return

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
        if amount < 0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(filename, expenses)


# Print my saved expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        for expense in expenses:
            print(expense)


# Search expenses by date or category
def search_expenses(expenses):
    start = input("Start date (YYYY-MM-DD, or Enter to skip): ")
    end = input("End date (YYYY-MM-DD, or Enter to skip): ")
    category = input("Category (or Enter to skip): ")

    try:
        for date in [start, end]:
            if date:
                datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    if start and end and start > end:
        print("Start date must be before end date.")
        return

    results = filter_expenses(expenses, start, end, category)
    view_expenses(results)


# Export my expenses for Excel
def export_expenses(expenses):
    filename = input("Enter CSV filename (or press Enter): ")

    if not filename:
        filename = "expensetracker.csv"

    try:
        export_csv(filename, expenses)
    except (OSError, KeyError, TypeError):
        print("Could not export expenses.")


# Display my expense tracker menu
def run_tracker():
    filename = input("Enter JSON filename (or press Enter): ")

    if not filename:
        filename = "expensetracker.json"

    try:
        expenses = load_expenses(filename)
    except (ValueError, OSError):
        print("Could not open the expense file.")
        return

    while True:
        print("\n--- My Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Export to CSV")
        print("5. Open Another Expense File")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses, filename)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expenses(expenses)

        elif choice == "4":
            export_expenses(expenses)

        elif choice == "5":
            new_file = input("Enter JSON filename: ")

            if not Path(new_file).is_file():
                print("File not found.")
                continue

            try:
                new_expenses = load_expenses(new_file)
                expenses = new_expenses
                filename = new_file
                print("Expense file opened!")
            except (ValueError, OSError):
                print("Could not open that file.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
