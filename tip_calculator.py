#Ask the user what the total amount of the bill was to calculate tax. Note: needs to be in a function.
def calculator():
    print("Hello, Welcome to The Handy Dandy Tip Calculator!!")
#Ask the user what the total amount of the bill was to calculate tax. 
    try:
        bill = float(input("What was the total bill, without tax? $"))
    #Ask the user how much they would like to tip the server?
        tip = float(input("What percentage tip would you like to give your friendly server? Do not enter % sign."))
    #Ask the user how many people will be  paying the total cost of the tab. 
        number_of_people = int(input("How many people will be paying?"))
    except ValueError:
        print('Oops! Please try again!')
        calculator()
    #Calculate sales tax and print 
    sales_tax = bill*.10
    print('Sales tax is $', \
    format (sales_tax,'.2f'))
#Calculate the bill  and sales tax, print.
    total_price_with_tax= bill + sales_tax
    print('Your total bill with tax before tip is $',\
        format (total_price_with_tax,'.2f'))
#Calculate the amount tip total, print. Calculate the amount per person.
    tip_amount_per_person = "%.2f" % float(tip / 100 * bill) #* total_price) / number_of_people)  
    print(f"Tip amount: ${tip_amount_per_person}")
    tip_due = "%.2f" % float(((tip / 100 * bill) + total_price_with_tax )/ number_of_people)
    print (f'Total amount due per person!!!: ${tip_due}')
    

#Ask if the customer would like to add anaditional tip to check, and lscontinue to ask until they say no. 
def additional_tip_request():
    additional_tip = input("Would you like to calculate a new bill? Type yes or no:")
    while  additional_tip == "yes":
        calculator()
        additional_tip = input("We are inside the while loop. Would you like to calculate a new bill? Type yes or no:")

 
    print('Thank you and have a wonderful day!')
      


calculator()
additional_tip_request()



 
