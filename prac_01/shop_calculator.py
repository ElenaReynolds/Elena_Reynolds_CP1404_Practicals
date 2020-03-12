total = 0
number = int(input("Number Of Items: "))
while number < 0:
    print("Invalid Number Of Items!")
    number = int(input('Number Of Items: '))
for i in range(number):
    price = float(input('Price Of Item: '))
    total += price
if total > 100:
    total *= 0.9
print('Total price For ', number, " items is $", total, sep='')
print("Total price for {} items is ${:.2f}".format(number, total))