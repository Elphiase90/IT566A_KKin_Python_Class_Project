"""Diary Entries Application Project Main"""

#Import the diary entries from diary_entry
import diary_entry

while True:
    print("\n--- My Diary ---")
    print("1. Choose a diary filename")
    print("2. Add a new diary entry")
    print("3. View all entries")
    print("4. Search entries by date")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        diary_entry.choose_file()
    elif choice == "2":
        diary_entry.add_entry()
    elif choice == "3":
        diary_entry.view_entries()
    elif choice == "4":
        diary_entry.search_entries()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
