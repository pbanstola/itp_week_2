# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers

# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.


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


    #multiply total by tax amount
    total_tax = float(bill_total) * float(tax_rate)
    print("Total tax amount: " + str(float(total_tax)))

    #add tax amount to total
    total_plus_tax = total_tax + float(bill_total)
    print("Total, plus tax: " + str(total_plus_tax))

    #divide total by number of diners
    total = total_plus_tax / int(number_of_diners)

    #output float number
    print("Each person should pay: " + str(math.floor(total)))

find_bill_total()