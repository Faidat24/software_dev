"""
Faidat Fahm
April 25, loops assignment
"""

# list of colors
colors = ['red', 'orange', 'olive', 'magenta', 'green']

# get user input, strip whitespace, and convert to lowercase
user_input = input("Enter a color: ").strip().lower()

# flag to track whether we found the color
found = False

# search through the list
for color in colors:
    if user_input == color:
        found = True
        break

# print result
if found:
    print(f"{user_input} is in the list")
else:
    print(f"{user_input} IS NOT in the list")