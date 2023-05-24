# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculator.")
total_bil = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people_split_bill = input("How many people to split the bill? ")

tip_percentage = int(tip_percentage)
tip_percentage /= 100
tip_percentage += 1

each_person_pay = (float(total_bil) / int(people_split_bill)) * tip_percentage

each_person_pay = "{:.2f}".format(each_person_pay)
message = f"Each person should pay: {each_person_pay} bdt"
print(message)
