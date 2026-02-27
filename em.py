expenses = []
def show_menu():
    print("\nExpense Manager")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        expenses.append((amount, category))
        print("Expense added successfully.")
    except Exception as e:
        print(e)
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nRecorded Expenses:")
    for idx, (amount, category) in enumerate(expenses, start=1): 
        print(f"{idx}. {category}: ${amount:.2f}")
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting Expense Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
main()