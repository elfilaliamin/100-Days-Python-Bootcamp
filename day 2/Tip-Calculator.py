print("Welcome to the tip calculator! ")
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_with_tip = float(bill) + float(bill)/100*float(tip)

result = bill_with_tip/float(people)
print(f"Each Person should pay: {round(result, 2)}$")
