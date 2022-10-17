#Ask user what the total amount of the bill was to calulate tax. Note: needs to be in a function.
def calculator():
    print("Hello, Welcome to The Handy Dandy Tip Calculator!!")
#Ask user what the total amount of the bill was to calulate tax. 
    bill = float(input("What was the total bill, without tax? $"))
#Ask the user how much they would like to tip the server?
    tip = float(input("What percentage tip would you like to give your friendly server? Do not enter % sign."))
#Ask the user how many people will be need paying the total cost of the tab. 
    number_of_people = int(input("How many people will be paying?"))
#calculate sales tax and print 
    sales_tax = bill*.10
    print('Sales tax is $', \
    format (sales_tax,'.2f'))
#calculate the bill  and sales tax, print.
    total_price_with_tax= bill + sales_tax
    print('Your total bill with tax before tip is $',\
        format (total_price_with_tax,'.2f'))
#calculate the amount tip total, print. Calualte the amount per person.
    tip_amount_per_person = "%.2f" % float(tip / 100 * bill) #* total_price) / number_of_people)  
    print(f"Tip amount: ${tip_amount_per_person}")
    tip_due = "%.2f" % float(((tip / 100 * bill) + total_price_with_tax )/ number_of_people)
    print (f'Total amount due per person!!!: ${tip_due}')
    return tip_due, number_of_people

#Ask if customer would like to add aditional tip to check, continue to ask until they say no. 
def additional_tip_request():
    tip_due , number_of_people= calculator()
    additional_tip = bool(input("Would you like to give this server an additional tip? Type yes or no:"))
    while True:
        
        if additional_tip == "yes":
            extra_tip = float(input('How much would you like to add?:$'))
        new_bill = (tip_due + extra_tip)
        print (f'Total amount due per person!!!: ${new_bill}')
        additional_tip = bool(input("Would you like to give this server an additional tip? Type yes or no:"))
    
    
        if additional_tip == "no":
            print('Thank you and Have a wonderful day!')
        else :
            additional_tip != "yes","no"
        print('Please enter yes or no only!')
        break
        return  additional_tip_request()

#I am having an issue with the addition tip request, 



additional_tip_request()       
calculator()



 
