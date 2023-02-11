import os
from datetime import datetime

def log_travel(file_name):
    print("Travel Diary")
    print("Log your travel experiences (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            location = input("Location: ")
            if location.lower() == "done":
                break
            description = input("Experience: ")
            file.write(f"Location: {location}\nExperience: {description}\n\n")
    
    print(f"Your travel diary has been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 travel_diary.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    log_travel(file_name)

