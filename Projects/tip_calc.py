print("Welcome to your Tip Calculator!")
bill = float(input("What is the total bill? - "))
# Error handling if invalid bill amount is entered
if bill <= 0:
    print("Invalid bill amount. Please check for the correct amount of your "
          "bill, please.")
    exit()

tip = int(input("How much of a tip would you like to give? 10, 15, 20? - "))
# Error handling if invalid tip amount is entered
if tip not in [10, 15, 20]:
    print("Invalid tip percentage. Please enter 10, 15, or 20.")
    exit()

people = int(input("How many people are splitting the bill? - "))
# Error Handling if invalid amount of people are entered
if people <= 0:
    print("Invalid number of people. Please enter a positive integer.")
    exit()

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount:.2f}.")
