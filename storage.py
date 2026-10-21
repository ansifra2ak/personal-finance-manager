
import csv
import os

FILE_NAME = "expenses.csv"


def save_expense(expense):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(
                ["Date", "Category", "Amount", "Description"]
            )

        writer.writerow([
            expense.date,
            expense.category,
            expense.amount,
            expense.description
        ])

    print("Expense saved successfully!")


def load_expenses():
    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)

    return expenses
