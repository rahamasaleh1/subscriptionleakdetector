Small monthly payments are easy to forget. A free trial that turned into a subscription or a gym you stopped going to months ago. I built this tool to find them. It reads a bank statement, spots payments that come back every month at the same price and works out what each one costs over a year. On the sample statement it found five subscriptions worth £839 a year, while correctly ignoring everyday spending like groceries.

```
Recurring charges found:

  NETFLIX.COM           £191.88 / year
  SPOTIFY               £143.88 / year
  PURE GYM LONDON       £299.88 / year
  AMAZON PRIME          £107.88 / year
  DISNEY PLUS           £95.88 / year

Estimated total annual leak: £839.40
```

## How it works

1. Load the bank statement from a CSV file and convert each date and amount into a usable format.
2. Group every payment by merchant.
3. Test each merchant against three rules. A charge counts as a subscription only when all three are true:
- It appears at least three times.
- The price stays the same, within 5%.
- The payments arrive roughly once a month, between 25 and 35 days apart.
4. Calculate the yearly cost of each subscription from its average monthly payment.

The price and timing rules are what separate a real subscription from regular shopping. Tesco appears every month, but the amount changes each time, so it is correctly excluded.

## How to run it

You need Python 3 installed. Download both files into the same folder, then run:

```
python3 my_detector.py
```

To check your own statement, save it as a CSV with the columns `Date`, `Description` and `Amount` (dates written as DD/MM/YYYY), then replace `practice_statement.csv` in the code with your file name.

## Built with

Python, using the built in `csv`, `datetime` and `os` libraries.
