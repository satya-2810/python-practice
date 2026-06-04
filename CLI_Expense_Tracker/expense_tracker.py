def add_expense(expenses):
    try:
        amount = int(input("Enter amount:"))
        if amount<=0:
            print("Invalid Input: Invalid amount")
            return
        description = input("Enter description of expense:").strip()
        if not description:
            print("Invalid Input: Description cannot be blank")
            return
        expenses.append({"amount": amount, "description": description})
        print("Expense Added Successfully")
    except ValueError:
        print("Invalid Input: Input must be a number")

def display_expenses(expenses):
    if expenses:
        print(f"{'Amount':<12} {'Description':<12}")
        
        for row in expenses:
            print(f"{row['amount']:<12} {row['description']:<20}")
        
    else:
        print("No expenses recorded yet!")
    
def total_expenses(expenses):
    total = 0
    if expenses:
        for expense in expenses:
            total += expense["amount"]
        print(f"Total Expense is {total}")
    else:
        print("No expenses recorded yet!")
    
print("Welcome to CLI Expense Tracker")
expenses = []
while True:
    try:
        choice = int(input("Enter the operation you want to perform: \n1. Add an Expense \n2. View Expenses \n3. Total Expenses \n4. Quit\n"))
        if choice==1:
            add_expense(expenses)
        elif choice==2:
            display_expenses(expenses)
        elif choice==3:
            total_expenses(expenses)
        elif choice==4:
            break
        else:
            print("Invalid Input: Input must be between 1-4")
    except ValueError:
        print("Invalid Input: Input must be a number")
        