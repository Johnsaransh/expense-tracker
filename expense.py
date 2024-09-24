import csv
from datetime import datetime

# File where we store expenses
FILE_NAME = "expenses.csv"

# Function to add an expense
def add_expense(amount, description):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, description])
    print(f"Expense of {amount} added: {description}")

# Function to view all expenses
def view_expenses():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            print(f"{'Date':<20} {'Amount':<10} {'Description':<30}")
            print("-" * 60)
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<10} {row[2]:<30}")
    except FileNotFoundError:
        print("No expenses found. Start adding some!")

# Function to delete all expenses
def delete_expenses():
    with open(FILE_NAME, 'w') as file:
        pass  # Overwrite the file with nothing (empty the file)
    print("All expenses deleted!")

# Main program loop
def main():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete All Expenses")
        print("4. Exit")
       
        choice = input("Choose an option: ")
       
        if choice == '1':
            amount = input("Enter the amount: ")
            description = input("Enter the description: ")
            add_expense(amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
