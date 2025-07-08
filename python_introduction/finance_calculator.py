#prompt user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Whats your total monthly expenses: "))

#monthly savings
monthly_savings = monthly_income - monthly_expenses

#yearly savings
yearly_savings = monthly_savings * 12

#interest
interest =yearly_savings * 0.05

projected_savings = yearly_savings + interest
print(f"Your monthly savings are: {monthly_savings}")
print (f"Your projected annual savings are:  {projected_savings}")