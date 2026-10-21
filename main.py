
from expense import Expense
from storage import save_expense, load_expenses
from reports import generate_report
from backup import create_backup, restore_backup



def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        expense = Expense(
            amount, category, date, description
        )

        save_expense(expense)

    except ValueError as error:
        print(f"Invalid input: {error}")
    except OSError as error:
        print(f"Could not save expense: {error}")



def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Your Expenses ---")

    for expense in expenses:
        print(
            f"{expense['Date']} | "
            f"{expense['Category']} | "
            f"₹{float(expense['Amount']):.2f} | "
            f"{expense['Description']}"
        )




def main():
    while True:
        print("\n===== PERSONAL FINANCE MANAGER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Reports")
        print("4. Create Backup")
        print("5. Restore Backup")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            create_backup()
        elif choice == "5":
            restore_backup()
        elif choice == "6":
            print("Thank you for using Personal Finance Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
