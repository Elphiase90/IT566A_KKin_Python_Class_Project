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
        with open(filename, "r") as file;
            expenses = json.load(files)
            return expenses

    except FileNotFoundError:
        print("No expenses file was found. Starting with an empty list.")
        return []
