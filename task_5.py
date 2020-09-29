revenue = int(input("What was the company's revenue over the last year? "))
costs = int(input("And what were the costs? "))
profit = revenue - costs
if profit > 0:
    print("Good results! The profit is positive. Seems like the company is rather stable.")
elif profit == 0:
    print("Not bad.. The profit is 0. Could've been better.")
else:
    print("Well... Seems like your company has a lot work to do this year to get better results vs last year.")

if profit > 0:
    print("The profitability is " + f'{(profit/revenue*100):0.2f}%')

employee_number = 0
if profit > 0:
    employee_number = int(input("How many employees did work in your company last year? "))
    print(f"The profit per employee is {profit / employee_number:0.2f}")




