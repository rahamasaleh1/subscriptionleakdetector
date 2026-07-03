"""
Goal: read practice_statement.csv, and print out any subscription that
charges the same amount roughly every month.

"""

import csv
from datetime import datetime


def load_transactions(filepath):
    """
    Step 1: Read the CSV and turn it into a list of dictionaries.

    Each row in practice_statement.csv looks like:
        01/01/2026,TESCO STORES,-38.20

    You want to end up with something like:
        [
            {"date": datetime(2026, 1, 1), "description": "TESCO STORES", "amount": 38.20},
            {"date": datetime(2026, 1, 2), "description": "NETFLIX.COM", "amount": 15.99},
            ...
        ]

    Notes:
    - The amount in the CSV is negative (money going out). You probably
      want to store it as a positive number to make maths easier later.
    - The date is a string like "01/01/2026" (day/month/year). Use
      datetime.strptime() to turn it into a real date object, e.g.:
          datetime.strptime("01/01/2026", "%d/%m/%Y")
    - Python's built-in csv module has a DictReader that's useful here:
          with open(filepath) as f:
              reader = csv.DictReader(f)
              for row in reader:
                  ...

    Return: a list of dicts (see shape above)
    """
    # YOUR CODE HERE
    pass


def group_by_merchant(transactions):
    """
    Step 2: Group transactions by their description (merchant name).

    Input: the list of dicts from load_transactions()

    Output: a dictionary where each key is a merchant name, and each
    value is a list of that merchant's transactions, e.g.:
        {
            "NETFLIX.COM": [ {...jan charge...}, {...feb charge...}, {...} ],
            "TESCO STORES": [ {...}, {...}, {...} ],
        }

    Hint: a plain dict works fine here. For each transaction, check if
    its description is already a key in your result dict. If not, add
    it with an empty list. Then append the transaction to that list.

    (Later, once this works, look up collections.defaultdict, it makes
    this exact pattern shorter, but get it working the manual way first.)
    """
    # YOUR CODE HERE
    pass


def is_recurring(transaction_list):
    """
    Step 3: Decide whether a merchant's list of transactions looks like
    a subscription.

    A simple starting rule (you can make this smarter later):
      - There need to be at least 3 charges
      - The amount needs to be roughly the same each time (say, within
        a few pence, or within a small percentage)

    Input: a list of transactions for ONE merchant (one value from the
    dictionary that group_by_merchant() returned)

    Return: True or False

    Hint: to check if amounts are "roughly the same", you could compare
    the minimum and maximum amount in the list, and see if the
    difference is small.
    """
    # YOUR CODE HERE
    pass


def calculate_annual_cost(transaction_list):
    """
    Step 4: Work out what a subscription costs per year.

    A simple starting approach: take the average amount charged, and
    multiply by 12 (assuming it's monthly, which is true for every
    subscription in the practice dataset).

    Input: a list of transactions for ONE merchant
    Return: a number (the estimated annual cost)
    """
    # YOUR CODE HERE
    pass


def main():
    transactions = load_transactions("practice_statement.csv")
    grouped = group_by_merchant(transactions)

    print("Recurring charges found:\n")

    total_annual = 0

    for merchant, charges in grouped.items():
        if is_recurring(charges):
            annual_cost = calculate_annual_cost(charges)
            total_annual += annual_cost
            print(f"  {merchant:20s}  £{annual_cost:.2f} / year")

    print(f"\nEstimated total annual leak: £{total_annual:.2f}")


if __name__ == "__main__":
    main()
