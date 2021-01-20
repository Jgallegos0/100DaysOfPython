#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

total_bill = input("Welcome to the tip calculator!\nEnter the total bill: $")
tip_percentage = input("What percentage tip would you like to give... 10, 12, or 15? ")
total_people = input("How many people will the bill be split with? ")

total_people_as_float = float(total_people)
total_bill_as_float = float(total_bill)
tip_percentage_as_float = float(tip_percentage)
percentage = tip_percentage_as_float/100
total_tip = percentage * total_bill_as_float
bill_total = total_tip + total_bill_as_float
split = bill_total/total_people_as_float
official_split_cost = round(split,2)

#Formatting error to display full 2 decimals
official_split_cost = "{:.2f}".format(split)

print(f"Each person should pay: ${official_split_cost}")
