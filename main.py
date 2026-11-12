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

  choice = input("Choose an option: ")

  if choice == "1":
    date = input("Enter date (YYYY-MM-DD): ")

    try:
      datetime.strptime(date, "%Y-%M-%D")
    except ValueError:
      print("Invalid date. Use YYY-MM-DD.")
      continue

    category = input("Enter category: ")

  try: 
    amount = float(input("Enter amount: "))
    if amount < 0:
      print("Amount can't be negative.")
      continue
  except ValueError:
    print("Please enter a valid amount.")
    continue 

  description = input("Enter description: ")

  expense = {
    "date": date,
    "category": category,
    "amount": amount,
    "description": description
  }

  expenses.append(expenses)
  save_expenses(filename, expenses)

  print("Expenses added and saved!")

elif choice == "2":
if not expenses:
    print("No expenses found.")
  else:
    for expense in expenses:
      print(expenses)

elif choice == "3":
  start = input("Start date (YYY-DD-MM, or Enter to skip): ")
  end = input("End date (YYYY-MM-DD, or Enter to skip): ")
  category = input("Category (or Enter to skip): ")

  try:
    for date in [start, end]:
      if date:
        date.time.strptime(date, "%Y-%m-%d")
except ValueError:
  print("Invalid date format.")
  continue


    
                 


  

