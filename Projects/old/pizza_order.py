# Write a program that automates pizza order pricing based on user input.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Initialize bill to 0
bill = 0
# Pizza sizes: Small ($15), Medium ($20), Large ($25)
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
# Pizza add-ons: Pepperoni for Small (+$2), Pepperoni for Medium/Large (+$3), Extra cheese (+$1)
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
