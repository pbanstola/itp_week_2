# ITP Week 2 Day 3 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers

def add(x, y, z, w):
    return x + y + z + w
add(5, 10, 15, 20)

def subtract(x, y):
    return x - y
subtract(10, 5)

def multiply(x, y, z):
    print(x*y*z)

multiply(5, 4, 6)

# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n")
    # Take input from the user
choice = input("Enter choice(1/2/3): ")

def calculate_function():
    
    # Check if choice is one of the four options
    if choice in ('1', '2', '3'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            # break
        else:
            print("Invalid Input")

calculate_function()
# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

import math

def find_bill_total():
    #input = number diners
    number_of_diners = input("How many diners? ")
    #print(number_of_diners)
    #input = tip amount
    tip_amount = input("Enter tip amount: ")
    #print(tip_amount)
    #input = bill amount
    bill_total = input("Bill total: ")
    #print(bill_total)
    #static = tax amount
    tax_rate = .08

    total =float(bill_total) + float(tip_amount)
    print(total)
    #multiply total by tax amount
    total_tax = float(total) * float(tax_rate)
    #total_tax = float(bill_total) * float(tax_rate)
    print("Total tax amount: " + str(float(total_tax)))

    #add tax amount to total
    total_plus_tax = total_tax + float(total)
    # total_plus_tax = total_tax + float(bill_total)
    print("Total, plus tax: " + str(total_plus_tax))

    #divide total by number of diners
    total = total_plus_tax / int(number_of_diners)

    #output float number
    print("Each person should pay: " + str(math.floor(total)))

find_bill_total()