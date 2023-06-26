# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
# Combine the names into a single string and convert to lowercase.
combined_names = name1.lower() + name2.lower()
# Count the number of times each letter in "true" appears in the combined string.
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
true = t + r + u + e
# Count the number of times each letter in "love" appears in the combined string.
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
love = l + o + v + e
# Concatenate the true and love counts into a single integer.
score = int(str(true) + str(love))
# Print the score and a message based on the score.
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
