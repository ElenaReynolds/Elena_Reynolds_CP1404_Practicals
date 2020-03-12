finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a Valid Integer: "))
        finished = True
    except ValueError:
        print("Please Enter a Valid Integer.")
print("Valid Result Is:", result)