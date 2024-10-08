# Programmers:Paige and Jalen
# Course:CS*151
# Due Date:10/09/2024
# Lab Assignment:Lab4
# Problem Statement: a program to determine how much a customer owes their mobile phone provider based on their
# subscription package and amount of data used.
# Data In: package type, amount of months, and additional data needed
# Data Out: cost and cost after coupon
# Credits: Class resources

#These two lines prompt the user for their package and converts their answer to a lower case string
package = str(input("What data package do you have?"))
package = package.lower()

#This while loop will prompt the user again for their package if their answer was invalid
while package != "green" and package != "blue" and package != "purple":
    print("That is not a valid package, must choose between green, blue, or purple. Try again!")
    package = input("What data package do you have?")

#Prompts the user and sets variables for their data usage and subscription length
data_used = int(input("How much data did you use?"))
months = int(input("How many months for your subscription?"))

#This if statement sets the constants for the green package to be used in the final bill calculation
if package == "green":
    monthly_cost = 49.99
    data_provided = 2
    additional_data_cost = 15
    coupon = input("Do you have a coupon?")
    coupon = coupon.lower()

#This if statement sets the constants for the blue package to be used in the final bill calculation
elif package == "blue":
     monthly_cost = 70
     data_provided = 4
     additional_data_cost = 10
     coupon = "no"

#This if statement sets the constants for the purple package to be used in the final bill calculation
elif package == "purple":
    monthly_cost = 99.95
    data_provided = 0
    additional_data_cost = 0
    coupon = "no"

#Sets the additional data variable to be used in final bill calculation
additional_data = data_used - data_provided

#This is the final bill equation
bill = (monthly_cost + additional_data * additional_data_cost) * months

#This subtracts their coupon from the bill if the bill total is above 75
if coupon == "yes":
    if bill >= 75:
        bill -= 20

#Round the bill to nearest hundredth place
bill = f"{bill:.2f}"

#Output bill total
print("Your final bill total will be $",bill)