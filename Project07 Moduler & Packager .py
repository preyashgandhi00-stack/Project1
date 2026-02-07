import math
import random
import uuid
from datetime import datetime
import time

print("============================")
print(" Welcome to Multi-Utility Toolkit ")
print("============================")

# date and time
def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def date_difference(date1, date2):
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return abs((d2 - d1).days)


def countdown(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} sec", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nCountdown finished!")

def stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()
    input("Press Enter to stop stopwatch...")
    end = time.time()
    print(f"Elapsed Time: {end - start:.2f} seconds")

# Date menu
def date_menu():
    while True:
        print("\nDatetime and Time operations:")
        print("1. Display Current Date & Time")
        print("2. Calculate difference between two dates/times")
        print("3. Formate date into custom date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to main menu")

        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                print(current_datetime())
                print("============================")
            case "2":
                d1 = input("Enter the first date (YYYY-MM-DD): ")
                d2 = input("Enter the second date (YYYY-MM-DD): ")
                print(f"Difference: {date_difference(d1, d2)} days")
                print("============================")

            case "3":
                 fmt = input("Enter format: ")
                 print("Formatted Date:",datetime.now().strftime(fmt))
            case "4":
                stopwatch()
            case "5":
                sec = int(input("Enter seconds: "))
                countdown(sec)
                print("============================")
            case "6":
                break
            case _:
                print("Invalid choice!")

# maths
def factorial(n):
    return math.factorial(n)

def compound_interest(principal, rate, time_period):
    return principal * (1 + rate / 100) ** time_period

def circle_area(radius):
    return math.pi * radius ** 2

# math menu
def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. solve compund Intrest")
        print("3. Trignomatric Calculation")
        print("4. Area of Geomatrics shapes")
        print("5. Back to main menu")

        choice = input("\nEnter  your choice: ")

        match choice:
            case "1":
                n = int(input("Enter number: "))
                print(f"Factorial:{factorial(n)}")
                print("============================")
            case "2":
                p = float(input("Enter a principal amount: "))
                r = float(input("Enter rate of intress(%): "))
                t = float(input("Enter time (in years): "))
                print(f"Compound Interest: {compound_interest(p, r, t)}")
                print("============================")
                
            case "3":
                angle = float(input("Angle in degrees: "))
                rad = math.radians(angle)
                print("Sin:", math.sin(rad))
                print("Cos:", math.cos(rad))
                print("Tan:", math.tan(rad))
                print("============================")
               
            case "4":
                r = float(input("Radius: "))
                print(f"Circle area:{circle_area(r)}")
                print("============================")
            case "5":
                break
            case _:
                print("Invalid choice!")

# Genrate uuid
def generate_uuid():
    return str(uuid.uuid4())

# Random
def generate_random_number():
    return random.randint(1, 100)

def generate_random_password(name, digits=4):
    number = ''.join(str(random.randint(0, 9)) for _ in range(digits))
    return f"{name}@{number}"

# random menu
def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Genrate Random Number")
        print("2. Genrate Random List")
        print("3. Create Random Password")
        print("4. Genrate Random OTP")
        print("5. Back to main menu")

        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                print(f"Random Number: {generate_random_number()}")
                print("============================")
            case "2":
                n = int(input("List size: "))
                print("Random List:", [random.randint(1, 50) for _ in range(n)])
                print("============================")

            case "3":
                length = int(input("Password length: "))
                print(f"Genrated password:{generate_random_password(length)}")
                print("============================")

            case "4":
                print("Generated OTP:",
                random.randint(100000, 999999))
                print("============================")
            case "5":
                break
            case _:
                print("Invalid choice!")

# file handaling
def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
    print(f"Data written to {filename}")

def append_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data)
    print(f"Data appended to {filename}")

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# file menu
def file_menu():
    while True:
        print("\nFile Operations:")
        print("1.Create a new file")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to main menu")

        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                name = input("File name: ")
                open(name, "w").close()
                print("File created successfully!")
                print("============================\n")
            case "2":
                name = input("Filename: ")
                data = input("Data: ")
                write_file(name, data+"\n")
                print("Data Written successfully!")
                print("============================\n")
            case "3":
                name = input("Filename: ")
                print(read_file(name))
                print("============================\n")
            case "4":
                name = input("Filename: ")
                data = input("Data: ")
                append_file(name, data+"\n")
                print("============================\n")
            case "5":
                break
            case _:
                print("Invalid choice!")

#explore module
def explore_module():
    try:
        mod = input("Enter module name to explore: ")
        module = __import__(mod)
        print("Available Attributes in math mopdule:")
        print(dir(module))
        print("============================\n")
    except ModuleNotFoundError:
        print("Module not found!")
    except Exception as e:
        print("Error:", e)

# main menu 
def main():
    while True:
        print("Choose an options:")
        print("1. Datetime and Time operations")
        print("2. Mathmatic operation")
        print("3. Random Data Genration")
        print("4. Genrate Unique Identifiers(uuid)")
        print("5. File Operations")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("============================")

        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                date_menu()
            case "2":
                math_menu()
            case "3":
                random_menu()
            case "4":
                print(f"Genrate uuid:{generate_uuid()}")
                print("============================")
            case "5":
                file_menu()
            case "6":
                explore_module()
                print("============================")
            case "7":
                print("============================")
                print("Thank you for using the Multi-Utility Toolkit!")
                print("============================\n")
                break
            case _:
                print("Invalid choice!")

if __name__ == "__main__":
    main()
