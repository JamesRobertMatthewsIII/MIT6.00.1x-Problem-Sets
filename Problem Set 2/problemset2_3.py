#! python 3
"""
Problem 2.3
Using Bisection Search to Make the Program Faster
20.0/20.0 points (graded)
"""
def minimumMonthlyPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    fixedMonthlyUpper = balance
    fixedMonthlyLower = balance / 12
    while True:
        minimumFixedMonthly = (fixedMonthlyUpper + fixedMonthlyLower) / 2
        balance2 = balance
        for month in range(12):
            monthlyUnpaidBalance = balance2 - minimumFixedMonthly
            balance2 = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        if abs(balance2) <= 0.01:
            return round(minimumFixedMonthly, 2)
        elif balance2 > 0:
            fixedMonthlyLower = minimumFixedMonthly
        elif balance2 < 0:
            fixedMonthlyUpper = minimumFixedMonthly

print("Lowest Payment: {}".format(minimumMonthlyPayment(balance, annualInterestRate)))
