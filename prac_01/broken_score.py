"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from cgitb import reset

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    elif score < 90:
        if score > 49:
            print("Passable")
    elif score > 90:
        print("Excellent")
    elif not score != 90:
        print("Excellent")
if score > 0:
    if score < 50:
        print("Bad")
elif score > -1:
    if score < 1:
        print("Bad")
