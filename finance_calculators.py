#Using math module
import math
#Requesting user input
calculator_type = input("""Investment - To calculate the amount of interest you'll earn on your investment
Bond - To calculate the amount you will pay back on a home loan \n
Please enter 'Investment' or 'Bond' to proceed:""").upper().replace(" ","")
#Calculating total amount of interest earned on investment   
if calculator_type == "INVESTMENT":
#Requesting information from user to make calculation
    deposit = float(input("Deposit amount (numbers only): "))
    interest_rate = float(input("Interest rate (without %): "))
    years = int(input("Years of investment (numbers only): "))
    interest = input("Interest type (Simple/Compound): ").upper().replace(" ","")
 #Calculating interest based on user inputting simple or compound
    if interest == "SIMPLE":
      simple_interest = round(deposit *(1+interest_rate/100* years),2)
      print(f"Total: £{simple_interest}")
    elif interest == "COMPOUND":
      compound_interest = round(deposit* math.pow((1+interest_rate/100),years),2)
      print(f"Total: £{compound_interest}")
    else:
#Using else to highlight error depending on user input
        print("Please try again!")
#Calculating amount to pay back on home loan
elif calculator_type == "BOND":
#Requesting information from user to make calculation
    house_value = int(input("Current house value (numbers only): "))
    interest_rate = float(input("Interest rate (without %): "))
    months_payback = int(input("Number of months for repayment (numbers only): "))
    pay_per_month = round((interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months_payback)),2)
    print(f"Total: £{pay_per_month} ")
else:
#Using else to highlight error depending on user input
      print("Input invalid, please try again!")