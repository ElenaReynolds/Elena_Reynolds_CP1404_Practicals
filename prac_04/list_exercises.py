numbers = []
for i in range (5):
    number = int(input("Number: "))
    numbers.append(number)
print("The First Number - ", numbers[0])
print("The Last Number - ", numbers[-1])
print("The Smallest Number - ", min(numbers))
print("The largest number is - ", max(numbers))
print("The Average- ", sum(numbers) / len(numbers))
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']
username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
