def generate_pattern():
    """Generates a right angled triangle pattern using nested loops"""
    rows=int(input("Enter the number of row pattern:"))

    if rows<=0:
        print("Invalid number of rows. Must be positive.")
        return
    print("Pattern:")
    for i in range(1, rows+1):
        for j in range(i):
            print("*", end="")
            print()

def analyze_numbers():
    """Analyzes a range of numbers to find odd-even numbers and sums."""
    start= int(input("Enter the start of range:"))
    end = int(input("Enter the end of range:"))

    if end<start:
        print("Invalid range. End must be greater than the start.")
        return
    total_sum= 0
    for num in range(start,end +1):
        if num%2== 0:
            print(f"Number {num} is even")
        else:
            print(f"Number {num} is odd")
        total_sum+= num

    print(f"Sum of all numbers from {start} to {end} is: {total_sum}")

def main():
    """Main menu-driven program"""
    while True:
        print("\nWelcome to the Pattern Generator and Number Analyzer!")
        print("Select an option:")
        print("1. Generate a Pattern")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_pattern()
        elif choice == "2":
            analyze_numbers()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

    