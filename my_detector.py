import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_transactions(filepath):
    transactions = []
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = datetime.strptime(row["Date"], "%d/%m/%Y")
            amount = abs(float(row["Amount"]))
            description = row["Description"]
            transactions.append({
                "date": date,
                "description": description,
                "amount": amount
            })
    return transactions


def group_by_merchant(transactions):
    grouped = {}
    for transaction in transactions:
        merchant = transaction["description"]
        if merchant not in grouped:
            grouped[merchant] = []
        grouped[merchant].append(transaction)
    return grouped


def is_recurring(transaction_list):

    if len(transaction_list) < 3:
        return False

    amounts = [t["amount"] for t in transaction_list]
    average = sum(amounts) / len(amounts)
    if max(amounts) - min(amounts) > average * 0.05:
        return False

    dates = sorted(t["date"] for t in transaction_list)
    for earlier, later in zip(dates, dates[1:]):
        gap = (later - earlier).days
        if gap < 25 or gap > 35:
            return False

    return True


def calculate_annual_cost(transaction_list):
    amounts = [t["amount"] for t in transaction_list]
    average = sum(amounts) / len(amounts)
    return average * 12

def main():
    transactions = load_transactions(os.path.join(BASE_DIR, "practice_statement.csv"))
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