# transaction.py

# This module handles sales transactions and receipts

class Transaction:
    def __init__(self, item, amount, price):
        self.item = item
        self.amount = amount
        self.price = price
        self.total = self.calculate_total()

    def calculate_total(self):
        return self.amount * self.price

    def receipt(self):
        return f'Receipt: {self.amount} x {self.item} - Total: ${self.total:.2f}'

# Example usage:
# sale = Transaction('Apples', 3, 0.5)
# print(sale.receipt())
