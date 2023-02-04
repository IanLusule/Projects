import os
from datetime import datetime

def log_pet_care(file_name):
    print("Pet Care Log")
    print("Log your pet care activities (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            activity = input("Activity: ")
            if activity.lower() == "done":
                break
            pet_name = input("Pet Name: ")
            notes = input("Notes: ")
            file.write(f"Activity: {activity}\nPet: {pet_name}\nNotes: {notes}\n\n")
    
    print(f"Your pet care log has been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pet_care_log.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    log_pet_care(file_name)

