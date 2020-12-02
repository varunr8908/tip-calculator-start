#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

bill_amount = input("What was the total bill? $")

bill_percent = input("What percentage tip would you like to give ? 10, 12, or 15? ")

bill_split = input("How many people would like to split the bill? ")

total_amount = int(bill_amount) * float("1." + bill_percent)

amount_per_person = round(total_amount / int(bill_split), 2)

print(f"Each person can pay {amount_per_person}")