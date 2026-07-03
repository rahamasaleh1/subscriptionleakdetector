def load_transactions(filepath):
    transactions = []
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = datetime.strptime(row["Date"], "d/m/Y")
            amount = abs(float(row["Amount"]))
            description = row["Description"]
            transactions.append({
                "date": date,
                "description": description,
                "amount": amount
            })
    return transactions
