monthly_income = float(input("Enter your monthly income: "))

monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12

interest = annual_savings * 0.05

projected_savings = monthly_savings + interest

print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)