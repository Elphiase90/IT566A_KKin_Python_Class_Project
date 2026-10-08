"""Diary Entries Application Project"""

#Import the date and datetime diary entries from datetime module
from datetime import date, datetime

diary_file = "diary.txt"

# Choose a diary file
def choose_file():
    global diary_file
    diary_file = input("Enter diary file name: ")


# Add a diary entry
def add_entry():
    today = str(date.today())
    entry = input("Write your diary entry: ")

    file = open(diary_file, "a")
    file.write(today + " | " + entry + "\n")
    file.close()

    print("Entry saved!")


# View all diary entries
def view_entries():
    try:
        file = open(diary_file, "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("Diary file not found.")


# Search entries by date
def search_entries():
    search_date = input("Enter date (YYYY-MM-DD): ")

    try:
        file = open(diary_file, "r")

        for line in file:
            if search_date == line.split(" | ")[0]:
                print(line)

        file.close()
    except FileNotFoundError:
        print("Diary file not found.")

