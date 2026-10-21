
from datetime import datetime


class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = float(amount)

        if self.amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.category = category.strip()
        if not self.category:
            raise ValueError("Category cannot be empty.")

        self.date = date.strip()
        datetime.strptime(self.date, "%Y-%m-%d")

        self.description = description.strip()
        if not self.description:
            raise ValueError("Description cannot be empty.")

    def __str__(self):
        return (
            f"{self.date} | {self.category}: "
            f"₹{self.amount:.2f} - {self.description}"
        )
