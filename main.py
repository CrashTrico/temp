import random
import time
import sys

def show_menu():
    print("\n=== TEMP TOOL ===")
    print("1. Quick Calculator")
    print("2. Save a  Note")
    print("3. Show Saved Notes")
    print("4. Random Number Generator")
    print("5. Exit")

def calculator():
    try:
        expr = input("Enter calculation (e.g. 5 + 3 * 2): ")
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

def save_note():
    note = input("Write your note: ")
    with open("temp_notes.txt", "a") as f:
        f.write(f"{time.ctime()} - {note}\n")
    print("Note saved!")

def show_notes():
    try:
        with open("temp_notes.txt", "r") as f:
            print("\n--- Saved Notes ---")
            print(f.read())
    except FileNotFoundError:
        print("No notes found.")

def random_number():
    try:
        a = int(input("From: "))
        b = int(input("To: "))
        print("Random number:", random.randint(a, b))
    except ValueError:
        print("Invalid input. Please enter numbers.")

# 🔥 Detect CI/CD (Jenkins) mode
is_ci = not sys.stdin.isatty()

while True:
    show_menu()

    if is_ci:
        print("Running in CI mode → auto exit")
        choice = "5"
    else:
        choice = input("Choose an option: ")

    if choice == "1":   # FIXED (was "12")
        calculator()
    elif choice == "2":
        save_note()
    elif choice == "3":
        show_notes()
    elif choice == "4":
        random_number()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
