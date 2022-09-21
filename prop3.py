total_cost = 1000000
high = 10000
low = 0
semi_annual_raise = .07
months = 36
portion_down_payment = 0.25
current_savings = 0
r = .04
time = 0
portion_saved = None
guess = None
annual_salary = None
annual_salary = float(input('enter your annual salary:'))
down_payment = portion_down_payment*total_cost
def calcmonths(annual,months,semi,portion):
    savings = 0
    for month in range(0,months):
        if month % 6 == 0 and months != 0:
            annual+= annual * semi
        savings += portion*annual/12
        savings += savings*r/12
    return savings 
print('portion needed for hosue:',down_payment)
while abs(current_savings - down_payment) > 100:
    current_savings = 0
    guess = int((low + high)/2)
    portion_saved = guess/10000
    current_savings = calcmonths(annual_salary,months,semi_annual_raise,portion_saved)
    print(guess)
    print('h',high)
    print('l',low)
    if current_savings < down_payment:
        low = guess
    elif current_savings > down_payment + 100:
        high = guess
    if time > 13:
        print('no posiple')
        break
    time+=1
print('times:',time) 
print('current saving:',current_savings,'$')
print('porthion saved:',portion_saved)


