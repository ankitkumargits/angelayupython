print("Tip Calculator in the Day2")

print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15 "))

people= int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

Each_person = round(bill_with_tip / people, 2)

split_bill = f"Each person should pay: ${Each_person}"

print(split_bill)

