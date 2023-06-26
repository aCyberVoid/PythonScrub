# Grab a list of student scores and find the highest score in the class.
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Determine the highest score in the class
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

# Print the highest score in the class
print(f"The highest score in the class is: {highest_score}")