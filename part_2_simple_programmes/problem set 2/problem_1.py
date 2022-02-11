# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# For each month, calculate statements on the monthly payment and remaining balance.
# At the end of 12 months, print out the remaining balance.
# Be sure to print out no more than two decimal digits of accuracy - so print
#
# Remaining balance: 813.41
# instead of
#
# Remaining balance: 813.4141998135
# So your program only prints out one thing: the remaining balance at the end of the year in the format:
#
# Remaining balance: 4784.0
# A summary of the required math is found below:
#
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#

def credit_card_balance(balance, annualInterestRate, monthlyPaymentRate):
    month = 0
    monthlyinterestrate = annualInterestRate / 12
    while month < 12:
        balance -= balance * monthlyPaymentRate
        balance += balance * monthlyinterestrate
        month += 1
    return round(balance, 2)

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

print("_______")
print(f"Expected balance for credit card balance with balance {balance}, annual interest rate {annualInterestRate} "
      f"and monthly payment rate {monthlyPaymentRate}: 31.38")

print(f"Computed balance: {credit_card_balance(balance, annualInterestRate, monthlyPaymentRate)}")

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

print("_______")
print(f"Expected balance for credit card balance with balance {balance}, annual interest rate {annualInterestRate} "
      f"and monthly payment rate {monthlyPaymentRate}: 31.38")

print(f"Computed balance: {credit_card_balance(balance, annualInterestRate, monthlyPaymentRate)}")

balance = 259
annualInterestRate = 0.22
monthlyPaymentRate = 0.05

print("______")
print(f"Expected balance for credit card balance with balance {balance}, annual interest rate {annualInterestRate} "
      f"and monthly payment rate {monthlyPaymentRate}: 174.05")

print(f"Computed balance: {credit_card_balance(balance, annualInterestRate, monthlyPaymentRate)}")
