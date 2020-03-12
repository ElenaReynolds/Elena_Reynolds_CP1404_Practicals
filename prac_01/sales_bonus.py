#Program to calculate and display a user's bonus based on sales.
#If sales are under $1,000, the user gets a 10% bonus.
#If sales are $1,000 or over, the bonus is 15%.
MENU = "Sales Bonus"
print(MENU)
sales = float (input("enter sales: $"))
if sales < 1000 :
    bonus = sales * 0.1
    print("Bonus is $", bonus, sep='')
elif sales > 0 :
    bonus = sales * 0.15
    print("Bonus is $", bonus, sep='')
