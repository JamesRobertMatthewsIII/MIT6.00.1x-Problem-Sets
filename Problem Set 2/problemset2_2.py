#! python3
"""
Problem 2.2
Paying Debt Off in a Year
15.0/15.0 points (graded)
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.
"""

def minimumMonthlyPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumFixedMonthly = 0
    while True:
        balance2 = balance
        for month in range(12):
            monthlyUnpaidBalance = balance2 - minimumFixedMonthly
            balance2 = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        if balance2 <= 0:
            return minimumFixedMonthly
        minimumFixedMonthly += 10

print("Lowest Payment: {}".format(minimumMonthlyPayment(balance, annualInterestRate)))


