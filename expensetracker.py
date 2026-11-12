"""Expense Tracker Project"""

import json
import csv

#save my expenses into a Json File
def save_expenses(filename, expenses):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

    print("My expenses have been saved!")

#Open my expense file and get the saved information
def load_expenses(filename):
    try:
        with open(filename, "r") as file:
            expenses = json.load(file)
            return expenses

    except FileNotFoundError:
        print("No expenses file was found. Starting with an empty list.")
        return []
# Search my expenses using dates or categories 
def filter_expenses(expenses, start_date, end_date, category):
    matching_expenses = []

    for expense in expenses:

        #Get the date and category for each expense
        expense_date = expense ["date"]
        expense_category = expense["category"]

        #skip expenses that are not in my chosen category
        if category and expense_category.lower() != category.lower():
            continue
        #keep expenses that match my search
        matching_expenses.append(expense)
    return matching_expenses

#Export my expenses to a csv file for excel 
def export_csv(filename, expenses):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file) 

    #Add column names to my csv file
    writer.writerow(["Date", "Category", "Amount", "Description"])

    #Add each expense to the csv file
    for expense in expenses:
        writer.writerow([
            expenses["date"],
            expenses["category"],
            expenses["amount"],
            expenses["description"]
        ])

print("My expenses were exported to the CSV successfully!")



        
