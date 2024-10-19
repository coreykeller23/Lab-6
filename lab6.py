"""
Author: Corey Keller
File Name: lab6.py
Created: 2/28/24
Purpose: Take user inputs to fill and output a list. This list is used to make a new column to display information based off of the user input.
Description: This file takes user input to get clients' first and last names, income.
These are used to make an array that is copied into another array to display their tax bracket according to their income.
"""
#import the utility file
import lab6utility

#create 2 lists to fill. The first with user inputs, the second copying the first and appending the tax bracket info
clientList = [["First Name","Last Name","Salary"]]
clientListTaxBrackets=[["First Name","Last Name","Salary","Income Tax"]]

i=0
while True:
    newClient=[] #list created in the loop to create rows of clients
    firstName = input("Please enter the first name of the client.\n") #ask for first name
    lastName = input("Please enter the client's last name.\n") #ask for last name
    income=lab6utility.incomeValidation() #use income validation to make sure digits are used and return an int type
    newClient.append((firstName, lastName, int(income))) #fill the client row
    clientList.append(newClient) #add the client to the original array

    taxBracket=lab6utility.detTaxBracket(income) #use function to determine the tax bracket based off of income variable
    clientListTaxBrackets.append((newClient,taxBracket)) #copy the first list into the second, while appending the tax bracket info
    i=i+1
    if i>=5:
        while True:
            finalEntry = input("If this was your last client, enter 'done'. Otherwise enter 'continue'.\n") #give user the option to finish or continue adding clients
            if finalEntry.lower() == "continue": #checks for finished list
                break
            else: 
                print("Invalid entry")
        
        if finalEntry.lower() == "done": #if finished, the user can escape the loop
            print("Entries Complete")
            break

for line in clientList:
    print(line)
print("")
for line in clientListTaxBrackets:
    print(line)