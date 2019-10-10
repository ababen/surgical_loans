from datetime import date

def get_balance(fund_date, fund_amount):
    # Do something
    fee = 499.00
    rate = .00299

    loan_date = date(2019,1,1)
    balance_date = date(2019,2,1)
    delta = balance_date - loan_date
    print("Date Difference is ", delta.days)

    

def get_amount(principal, rate, time):
    # num_comp is number of times interest compounds per year
    amount = principal * (pow((1 + rate / 100), time)) 
    print("Compound interest is", amount) 

def get_max(self):
    # Do something

def get_estimate(self):
    # Do something
