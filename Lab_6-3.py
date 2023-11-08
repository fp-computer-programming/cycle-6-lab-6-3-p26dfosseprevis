#Create a Python file named lab_6-3

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Create a list of 4 colors and store it as a variable.
colors = ["blue","red","yellow", "green"]
#Use a method to add 3 more colors to the list in a single statement.
colors.extend(["orange","tangrin","purple"])
#Use a different method to add one additional color to the list.
colors.append("pink")
#Use a method to insert a new color at index 3.
colors.insert(3,"amber")
print(colors)
#Use a method to create a copy of the list
colours = colors
#Use a method to remove one element from the copy of the list.
colours.remove("pink")
