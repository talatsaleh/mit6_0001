current_savings = 0
r = .04
annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your dream home:'))
semi_annual_salary = float(input('Enter the semi­annual raise, as a decimal:'))
portion_down_payment = 0.25
months = 0
down_payment = portion_down_payment*total_cost
while current_savings < down_payment:
    if months%6 == 0 and months > 0:
        annual_salary+= annual_salary*semi_annual_salary
    current_savings+= current_savings*r/12
    current_savings+= portion_saved*annual_salary/12
    print(current_savings)
    months+=1
print('Number of Months:',months)