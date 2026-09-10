print("Welcome to the tip calculator! ")
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

result = float(bill)/float(people) + float(tip)
print(f"Each Person should pay: {result}")
