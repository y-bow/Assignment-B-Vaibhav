annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
portion_down_payment = 0.25 * total_cost
r = 0.04
semi_annual_raise = 0.07

low = 0
high = 10000
steps = 0
best_rate = 0

current_savings = 0
monthly_salary = annual_salary / 12

for month in range(36):
    current_savings += current_savings * (r / 12)
    current_savings += monthly_salary
    if (month + 1) % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

if current_savings < portion_down_payment - 100:
    print("It is not possible to pay the down payment in three years.")
else:
    while True:
        mid = (low + high) // 2
        portion_saved = mid / 10000
        current_savings = 0
        monthly_salary = annual_salary / 12

        for month in range(36):
            current_savings += current_savings * (r / 12)
            current_savings += monthly_salary * portion_saved
            if (month + 1) % 6 == 0:
                monthly_salary += monthly_salary * semi_annual_raise

        steps += 1

        if abs(current_savings - portion_down_payment) <= 100:
            best_rate = portion_saved
            break
        elif current_savings < portion_down_payment:
            low = mid
        else:
            high = mid

    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)