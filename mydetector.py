import csv
from datetime import datetime

def load_transactions(filepath):
    transactions = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = datetime.strptime(row["Date"].strip(), "%d/%m/%Y")
            amount = abs(float(row["Amount"]))
            description = row["Description"].strip()
            transactions.append({
                "date": date,
                "description": description,
                "amount": amount
            })
    return transactions
