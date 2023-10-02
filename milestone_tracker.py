import os
from datetime import datetime

def log_milestone(file_name):
    print("Project Milestone Tracker")
    print("Log your project milestones (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            milestone = input("Milestone Name: ")
            if milestone.lower() == "done":
                break
            status = input("Status (Completed/In Progress): ")
            notes = input("Notes: ")
            file.write(f"Milestone: {milestone}\nStatus: {status}\nNotes: {notes}\n\n")
    
    print(f"Your project milestones have been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 milestone_tracker.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    log_milestone(file_name)

