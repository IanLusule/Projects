import os
from datetime import datetime

def log_expense(file_name):
    print("Expense Tracker")
    print("Log your daily expenses (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            item = input("Item: ")
            if item.lower() == "done":
                break
            cost = input("Cost: ")
            notes = input("Notes: ")
            file.write(f"Item: {item}\nCost: {cost}\nNotes: {notes}\n\n")
    
    print(f"Your expenses have been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 expense_tracker.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    log_expense(file_name)

