dataset = []
dataset_summary = {}

def display_summary(data):
    """Displays basic statistics using built-in functions."""
    if not data:
        print("Dataset is empty!")
        return
    print("\nData Summary:")
    print(f"- Total elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all values: {sum(data)}")
    print(f"- Average value: {sum(data) / len(data):.2f}")

def calculate_average(data):
    """Calculates average of dataset."""
    return sum(data) / len(data)

def find_duplicates(data):
    """Finds duplicate values in dataset."""
    return list(set([x for x in data if data.count(x) > 1]))

def unique_values(data):
    """Returns unique values."""
    return list(set(data))

def show_args(*args):
    """Displays multiple values using *args."""
    print("Values passed using *args:", args)

def show_kwargs(**kwargs):
    """Displays dataset summary using **kwargs."""
    print("Dataset Characteristics:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

def factorial(n):
    """Calculates factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def filter_data(data, threshold):
    """Filters data using lambda function."""
    return list(filter(lambda x: x >= threshold, data))

def dataset_statistics(data):
    """Returns multiple statistics."""
    return min(data), max(data), sum(data), sum(data) / len(data)


def sort_data(data, order="asc"):
    """Sorts data in ascending or descending order."""
    if order == "asc":
        return sorted(data)
    else:
        return sorted(data, reverse=True)

def main_menu():
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

while True:
    main_menu()
    choice = input("Please enter your choice: ")

    if choice == "1":
        dataset = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
        dataset_summary["Total Values"] = len(dataset)
        dataset_summary["Average"] = calculate_average(dataset)
        print("Data has been stored successfully!")

    elif choice == "2":
        display_summary(dataset)

    elif choice == "3":
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"Factorial of {num} is: {factorial(num)}")

    elif choice == "4":
        threshold = int(input("Enter a threshold value to filter data above this value: "))
        filtered = filter_data(dataset, threshold)
        print(f"Filtered Data (values >= {threshold}): {filtered}")

    elif choice == "5":
        print("Choose sorting option:")
        print("1. Ascending")
        print("2. Descending")
        opt = input("Enter your choice: ")
        if opt == "1":
            print("Sorted Data in Ascending Order:", sort_data(dataset, "asc"))
        else:
            print("Sorted Data in Descending Order:", sort_data(dataset, "desc"))

    elif choice == "6":
        min_val, max_val, total, avg = dataset_statistics(dataset)
        print("\nDataset Statistics:")
        print(f"- Minimum value: {min_val}")
        print(f"- Maximum value: {max_val}")
        print(f"- Sum of all values: {total}")
        print(f"- Average value: {avg:.2f}")

    elif choice == "7":
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
