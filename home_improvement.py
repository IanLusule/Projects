import os
from datetime import datetime

def log_home_improvement(file_name):
    print("Home Improvement Tracker")
    print("Log your home improvement projects (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            project = input("Project: ")
            if project.lower() == "done":
                break
            status = input("Status (Completed/In Progress): ")
            notes = input("Notes: ")
            file.write(f"Project: {project}\nStatus: {status}\nNotes: {notes}\n\n")
    
    print(f"Your home improvement projects have been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 home_improvement_tracker.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    log_home_improvement(file_name)

