import os
from datetime import datetime

def write_daily_entry(file_name):
    print("Personal Journal Logger")
    print("Enter your daily events and activities (type 'done' to finish):")

    # Open the file to append the journal entry
    with open(file_name, "a") as file:
        # Get the current date
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        # Continuously take input from the user
        while True:
            entry = input("> ")
            if entry.lower() == "done":
                break
            file.write(f"- {entry}\n")
    
    print(f"\nYour entry has been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 journal_logger.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    
    # Capture daily events and write them to the file
    write_daily_entry(file_name)

