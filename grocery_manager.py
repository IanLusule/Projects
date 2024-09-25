import os
from datetime import datetime

def log_grocery(file_name):
    print("Grocery List Manager")
    print("Log your grocery items (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            item = input("Item: ")
            if item.lower() == "done":
                break
            quantity = input("Quantity: ")
            notes = input("Notes: ")
            file.write(f"Item: {item}\nQuantity: {quantity}\nNotes: {notes}\n\n")
    
    print(f"Your grocery list has been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 grocery_manager.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    log_grocery(file_name)

