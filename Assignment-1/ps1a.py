annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

annual_return = 0.04
monthly = annual_salary / 12
savings = 0
down_payment = total_cost * 0.25
months = 0

while savings < down_payment:
    monthly_return = savings * (annual_return / 12)
    savings += monthly_return
    savings += monthly * portion_saved
    months += 1

print("Number of months:", months)