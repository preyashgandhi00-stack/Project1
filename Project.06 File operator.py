import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    
    def add_entry(self):
        entry = input("\nEnter your journal entry:\n")

        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

        try:
            with open(self.filename, "a") as file: 
                file.write(f"{timestamp}\n{entry}\n\n")
            print("Entry added successfully!")
        except PermissionError:
            print("Error: Permission denied while writing to the file.")

    
    def view_entries(self):
        try:
            with open(self.filename, "r") as file: 
                content = file.read()
                if content.strip() == "":
                    print("No journal entries found.")
                else:
                    print("\nYour Journal Entries:")
                    print("----------------------------------")
                    print(content)
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

    
    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ")

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            matches = []
            for line in lines:
                if keyword.lower() in line.lower():
                    matches.append(line.strip())

            if matches:
                print("\nMatching Entries:")
                print("----------------------------------")
                for match in matches:
                    print(match)
            else:
                print(f"No entries found for keyword: {keyword}")

        except FileNotFoundError:
            print("Error: The journal file does not exist.")

    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        confirm = input("Are you sure you want to delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            try:
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            except PermissionError:
                print("Error: Permission denied while deleting the file.")
        else:
            print("Deletion cancelled.")


def main():
    journal = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            journal.add_entry()
        elif choice == "2":
            journal.view_entries()
        elif choice == "3":
            journal.search_entry()
        elif choice == "4":
            journal.delete_entries()
        elif choice == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
