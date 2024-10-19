"""
Author: Corey Keller
File Name: lab6utility.py
Created: 2/29/24
Purpose: Create functions to be used in Lab 6
"""

def incomeValidation(): #validates that digits were used in income input and returns an int type if so
    while True:
        income = input("Please enter the client's income without any commas.\n")
        if not income.isdigit():
            print("Invalid entry.\n")
            continue
        else:
            income=int(income)
            return income
            break
def detTaxBracket(income): #determines the tax bracket based off of income input and returns the tax bracket as a str
    if income<=11000:
        return "10%"
    elif 11000<income<=44725:
        return "12%"
    elif 44725<income<=95375:
        return "22%"
    elif 95375<income<=182100:
        return "24%"
    elif 182100<income<=231250:
        return "32%"
    elif 231250<income<=578125:
        return "35%"
    else:
        return "37%"