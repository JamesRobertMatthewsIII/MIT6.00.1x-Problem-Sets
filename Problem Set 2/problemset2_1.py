#! python3
"""
Problem 2.1
Paying Debt off in a Year
10.0 points possible (graded)
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.
"""

def year_balance(balance, annualInterestRate, monthlyPaymentRate):
    for month in range(12):
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        balance = updatedBalance
    return round(updatedBalance, 2)

print("Lowest Payment: {}".format(minimumMonthlyPayment(balance, annualInterestRate)))