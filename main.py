"""Expense Tracker Project Main"""

from datetime import datetime
from expensetracker import save_expenses, load_expenses, filter_expenses, export_csv

#Choose an expense file
filename = input("Enter expense filename (example: expenses.json): ")

if not filename:
  filename = "expense_tracker.json"

try:
  expenses = load_expenses(filename)
except (ValueError, OSError):
  print("Could not open the expense tracker file.")
  expenses = []
  filename = "expensetracker.json"

while True:
  print("\n--- Expense Tracker ---")
  print("1. Add Expense")
  print("2. View All Expenses")
  print("3. Filter Expenses")
  print("4. Export to CSV")
  print("5. Open Another Expense File")
  print("6. Exit")

  choice = input ("Choose an option: ")

if choice == "1":
  date = input(Enter date (YYYY-MM-DD): ")

  try:
    datetime.strptime(date, "%Y-%M-%D")
  except ValueError:
    print("Invalid date. Use YYY-MM-DD.")
    continue


  

