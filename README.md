# Subscription Leak Detector

A Python tool that scans a bank statement and finds forgotten subscriptions: the small monthly payments that quietly add up over a year.

## The result

Running the detector on the sample statement identified five recurring charges and correctly ignored everyday spending such as groceries and coffee.

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
