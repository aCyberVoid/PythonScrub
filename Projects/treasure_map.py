# Initialize a 3x3 map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
# Combine the rows into a list
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# Ask the user where they want to put the treasure, i.e. 23 - 2nd Column, 3rd Row
position = input("Where do you want to put the treasure? ")
# Get the horizontal and vertical positions
horizontal = int(position[0])
vertical = int(position[1])
# Use the horizontal and vertical to locate the treasure
map[vertical - 1][horizontal - 1] = "X"
# Print the map
print(f"{row1}\n{row2}\n{row3}")
