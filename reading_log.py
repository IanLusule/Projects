import os
from datetime import datetime

def log_books(file_name):
    print("Book Reading Log")
    print("Log your completed books (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            book = input("Book Title: ")
            if book.lower() == "done":
                break
            author = input("Author: ")
            notes = input("Notes/Review: ")
            file.write(f"Book: {book}\nAuthor: {author}\nReview: {notes}\n\n")
    
    print(f"Your reading log has been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 book_reading_log.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    log_books(file_name)

