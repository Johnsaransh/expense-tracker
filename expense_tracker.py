def main():
    print(f"Running Expense Tracker!")
    
    #get user input for expense.
    get_user_expense()

    #write their expense to a file.
    save_expense_to_file()

    #read file and summarize expenses.
    summarize_expenses()
    pass


def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: ")) 
    print(f"you have entered {expense_name}, {expense_amount}")

    expense_categories = [
        "Food", "Home", "Work", "Fun", "Misc"
    ]

       #loop and index adjustment
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
            
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}:")) - 1

        if selected_index in range(5)    
        break    
    pass 

def save_expense_to_file():
    print(f"Saving User Expense")
    pass

def summarize_expenses():
    print(f"Summarizing User Expense")
    pass

if __name__ == "__main__":
   main()