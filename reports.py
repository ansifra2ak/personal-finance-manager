
from collections import defaultdict
from storage import load_expenses


def generate_report():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses available for reports.")
        return

    total = 0
    category_totals = defaultdict(float)
    count = 0

    for expense in expenses:
        try:
            amount = float(expense["Amount"])
            category = expense["Category"]

            total += amount
            category_totals[category] += amount
            count += 1

        except (ValueError, TypeError, KeyError):
            print("Skipping an invalid expense record.")

    if count == 0:
        print("No valid expenses found.")
        return

    average = total / count

    print("\n===== EXPENSE REPORT =====")
    print(f"Total Expenses: {count}")
    print(f"Total Spending: ₹{total:.2f}")
    print(f"Average Expense: ₹{average:.2f}")

    print("\n--- Category-Wise Spending ---")

    for category, amount in sorted(category_totals.items()):
        percentage = (amount / total) * 100
        print(f"{category}: ₹{amount:.2f} ({percentage:.1f}%)")

    print("==========================")

