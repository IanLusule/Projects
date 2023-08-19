import os
import sys
import random
from datetime import datetime, timedelta

def generate_random_date(year):
    """Generate a random date within the specified year."""
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    
    # Get a random number of days between start_date and end_date
    random_days = random.randint(0, (end_date - start_date).days)
    random_time = random.randint(0, 86400)  # Random seconds in a day
    random_date = start_date + timedelta(days=random_days, seconds=random_time)
    return random_date.strftime("%Y-%m-%dT%H:%M:%S")

def git_commit_backdated(year, directory):
    # Ensure the year is an integer
    try:
        year = int(year)
    except ValueError:
        print("Error: Year must be a valid integer.")
        sys.exit(1)

    # Check if the current directory is a git repository
    if not os.path.isdir(".git"):
        print("Initializing new git repository...")
        if os.system("git init") != 0:
            print("Error: Failed to initialize git repository.")
            sys.exit(1)
        # Set the default branch to 'main'
        if os.system("git branch -M main") != 0:
            print("Error: Failed to set default branch to 'main'.")
            sys.exit(1)

    # Get all files in the specified directory (ignoring directories and .git)
    files = [f for f in os.listdir(directory) if os.path.isfile(f) and f != ".git"]
    
    if not files:
        print(f"No files found in {directory} to commit.")
        sys.exit(1)

    # Iterate over each file and commit it with a random date
    for file_name in files:
        # Generate a random date within the specified year
        commit_date = generate_random_date(year)
        
        # Add the file to staging
        if os.system(f"git add {file_name}") != 0:
            print(f"Error: Failed to add file '{file_name}' to git staging area.")
            continue  # Skip to the next file
        
        # Commit with the random date
        commit_command = f'GIT_AUTHOR_DATE="{commit_date}" GIT_COMMITTER_DATE="{commit_date}" git commit -m "Backdated commit for {file_name}"'
        if os.system(commit_command) != 0:
            print(f"Error: Failed to commit file '{file_name}'.")
            continue  # Skip to the next file

        print(f"Successfully committed '{file_name}' with date {commit_date}.")

    # Set git user name and email if not set
    if os.system("git config --get user.name") != 0:
        os.system('git config --global user.name "IanLusule"')
    if os.system("git config --get user.email") != 0:
        os.system('git config --global user.email "amlusule@gmail.com"')

    # Check if the remote 'origin' is set and pull the latest changes if necessary
    if os.system("git remote") == 0:
        print("Pulling the latest changes from the remote repository...")
        os.system("git config pull.rebase false")  # Set merge as the default strategy
        if os.system("git pull origin main") != 0:
            print("Error: Failed to pull the latest changes from remote. Resolve conflicts manually.")
            sys.exit(1)

        # Push the changes to the remote repository
        print("Pushing the changes to the remote repository...")
        if os.system("git push -u origin main") != 0:
            print("Error: Failed to push to remote repository. Resolve conflicts and try again.")
            sys.exit(1)
    else:
        print("Warning: No remote 'origin' found. Skipping push step.")
    
    print(f"All files in '{directory}' committed and pushed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <year>")
        sys.exit(1)

    year_str = sys.argv[1]
    directory = "."  # You can change this to a specific directory if needed

    git_commit_backdated(year_str, directory)
