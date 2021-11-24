print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
bill_with_tip=((tip/100)*bill)+bill
result = round((bill_with_tip/people),2)
result = "{:.2f}".format(result)
print("Each person should pay: $"+str(result))

#print ((bill/people)*(1+(tip/100)))
