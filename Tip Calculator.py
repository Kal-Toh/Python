print("Welcome to the tip calculator!")
bill = input ("What was the total bill? $")
percent = input("How much tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

tip = (float(percent) / 100) * float(bill) + float(bill)
total = float(tip) / float(split)

round = ((round)(float(total), 2))
print (f"Each person should pay: ${float(round)}")
