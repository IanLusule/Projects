import os
from datetime import datetime

def log_workout(file_name):
    print("Workout Tracker")
    print("Log your workout activities (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            activity = input("Workout Activity: ")
            if activity.lower() == "done":
                break
            duration = input("Duration: ")
            notes = input("Notes: ")
            file.write(f"Activity: {activity}\nDuration: {duration}\nNotes: {notes}\n\n")
    
    print(f"Your workout log has been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 workout_tracker.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    log_workout(file_name)

