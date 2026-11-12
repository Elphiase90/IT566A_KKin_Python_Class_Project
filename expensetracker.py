"""Expense Tracker Project"""

import json
import csv


# Save my expenses into a JSON file
def save_expenses(filename, expenses):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

    print("My expenses have been saved!")


# Open my expense file and get the saved information
def load_expenses(filename):
    try:
        with open(filename, "r") as file:
            expenses = json.load(file)
            return expenses

    except FileNotFoundError:
        print("No expense file was found. Starting with an empty list.")
        return []

    except json.JSONDecodeError:
        print("The expense file does not contain valid JSON.")
        raise


# Search my expenses using dates or categories
def filter_expenses(expenses, start_date, end_date, category):
    matching_expenses = []

    for expense in expenses:

        # Get the date and category for each expense
        expense_date = expense["date"]
        expense_category = expense["category"]

        # Skip expenses before my start date
        if start_date and expense_date < start_date:
            continue

        # Skip expenses after my end date
        if end_date and expense_date > end_date:
            continue

        # Skip expenses that are not in my chosen category
        if category and expense_category.lower() != category.lower():
            continue

        # Keep expenses that match my search
        matching_expenses.append(expense)

    return matching_expenses


# Export my expenses to a CSV file for Excel
def export_csv(filename, expenses):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Add column names to my CSV file
        writer.writerow(["Date", "Category", "Amount", "Description"])

        # Add each expense to my CSV file
        for expense in expenses:
            writer.writerow([
                expense["date"],
                expense["category"],
                expense["amount"],
                expense["description"]
            ])

    print("My expenses were exported to CSV successfully!")
