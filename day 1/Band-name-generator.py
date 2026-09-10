# 1. Display a greeting message to welcome the user to the program
print("Welcome to the Band Name Generator!")

# 2. Ask the user for the city that they grew up in
# The input() function pauses code execution and waits for user text
city = input("What's the name of the city you grew up in?\n")

# 3. Ask the user for the name of a pet
# Store the user's response in the variable 'pet'
pet = input("What's the name of a pet?\n")

# 4. Combine (concatenate) the strings with a space in between to form the band name
# Use print() to output the final result to the terminal
print(f"Your band name could be {city} {pet}")
