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
  

