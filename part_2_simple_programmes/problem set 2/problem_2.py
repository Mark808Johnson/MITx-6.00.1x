# Now write a program that calculates the minimum fixed monthly payment needed in order
# pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a
# single number which does not change each month, but instead # is a constant amount that
# will be paid each month.
#
# In this problem, we will not be dealing with a minimum monthly payment rate.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year,
# for example:
# Lowest Payment: 180

# Assume that the interest is compounded monthly according to the balance at the end of the month
# (after the payment for that month is made). The monthly payment must be a multiple of $10 and is
# the same for all months. Notice that it is possible for the balance to become negative using this
# payment scheme, which is okay. A summary of the required math is found below:
#
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

def minimum_monthly_payment(balance, annual_interest_rate, monthly_payment):
    monthlyinterestrate = annual_interest_rate/12

    not_found = True
    while not_found:
        temp_balance = balance
        for i in range(0, 12):
            temp_balance -= monthly_payment
            temp_balance += temp_balance * monthlyinterestrate
        if temp_balance > 0:
            monthly_payment += 10
        else:
            not_found = False
    return monthly_payment

balance = 3329
annualInterestRate = 0.2
monthly_payment = 10

print(f"Expected lowest payment to clear credit card balance {balance} within 12 months, "
      f"with annual interest rate of {annualInterestRate}: 310")
print(f"Calculated lowest payment: {minimum_monthly_payment(balance, annualInterestRate, monthly_payment)}")

balance = 4773; annualInterestRate = 0.2

print(f"Expected lowest payment to clear credit card balance {balance} within 12 months, "
      f"with annual interest rate of {annualInterestRate}: 440")
print(f"Calculated lowest payment: {minimum_monthly_payment(balance, annualInterestRate, monthly_payment)}")

balance = 857; annualInterestRate = 0.25

print(f"Expected lowest payment to clear credit card balance {balance} within 12 months, "
      f"with annual interest rate of {annualInterestRate}: 80")
print(f"Calculated lowest payment: {minimum_monthly_payment(balance, annualInterestRate, monthly_payment)}")
