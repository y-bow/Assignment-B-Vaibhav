starting_salary = float(input("Enter the starting salary: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi annual raise, as a decimal: "))

portion_down_payment = 0.25
annual_return = 0.04
months = 36
epsilon = 100

down_payment = total_cost * portion_down_payment

def calculate_savings(rate):
    savings = 0
    annual_salary = starting_salary
    monthly_salary = annual_salary / 12

    for month in range(1, months + 1):
        savings += savings * (annual_return / 12)
        savings += monthly_salary * rate
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12

    return savings

if calculate_savings(1.0) < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    low = 0
    high = 1
    steps = 0

    while True:
        steps += 1
        mid = (low + high) / 2
        savings = calculate_savings(mid)

        if abs(savings - down_payment) <= epsilon:
            best_rate = mid
            break
        elif savings < down_payment:
            low = mid
        else:
            high = mid

    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)