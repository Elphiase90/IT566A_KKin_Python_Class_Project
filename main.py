"""Expense Tracker Project Main"""

from datetime import datetime
from expensetracker import save_expenses, load_expenses, filter_expenses, export_csv

#Choose an expense file
filename = input("Enter expense filename (example: expensetracker.json): ")

if not filename:
  filename = "expensetracker.json"

try:
  expenses = load_expenses(filename)
except (ValueError, OSError):
  print("Could not open the expense tracker file.")
  expenses = []
  filename = "expensetracker.json"

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
    date = input("Enter date (YYYY-MM-DD): ")

    try:
      datetime.strptime(date, "%Y-%m-%d")
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
          datetime.strptime(date, "%Y-%m-%d")
  
    except ValueError:
      print("Invalid date format.")
      continue

    if start and end and start > end:
      print("Start date must be before end date.")
      continue

    results = filter_expenses(expenses, start, end, category)

    if not results:
      print("No matching expenses found.")
    else: 
      for expenses in results:
        print(expense)

  elif choice == "4":
    csv_filename = input("Enter csv filename (example: expensetracker.csv): ")

    if not csv_filename:
      csv_filename = "expensetracker.csv"
      
    export_csv(csv_filename, expenses)

  elif choice == "5":
    new_filename = input("Enter json filename: ")

    try:
      new_expenses = load_expenses(new_filename)
      expenses = new_expenses
      filename = new_filename
      print("Expense file opened!")

    except (ValueError, OSError):
      print("Could not open that file!")

  elif choice == "6":
    print("Goodbye!")
    break

  else:
    print("Invalid choice. Try again")



    
                 


  

