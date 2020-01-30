# Part 1: assign a variable to your name
myName = 'Carrieann'

# Part 2: assign another string to the classname
className = 'Coding Club (Python)'
theDate = '01/27/2020'

""" Part 3: Print the following in a multi-line print
      Name: <nameVariable>
      Date: 01/30/2020
      Class: <ClassNameVariable>"""

print(F"""Name: {myName}\nDate: {theDate}\nClass: {className}""")

# Part 4: Create a new list with the following numbers... 1, 5, 15, 20, 25, 6*6
list1 = [1, 5, 15, 20, 25, 6*6]

# Part 5: Print the list
print('A new list is created:\n',list1)

# Part 6: Change the last item to show 6*5. Print the list again
list1[5] = 6*5
print('Changed the last number:\n',list1)

# Part 7: Delete the first element from the list. Print the list again
del list1[0]
print('Print the list without the first element:\n',list1)

# Part 8: Print the length of the list
print('The number of the items in the list is',len(list1))

""" Part 9:
        create set1 from a list. Create set2 with brackets."""
list2 = ['y', 'y', 'd', 'd', 'd', 'd', 'e', 's', 'p', 'q', 'e']
set1 = set(list2)
set2 = {'g', 'h', 'h', 'd', 'd', 'e', 'e', 'p', 'p', 'm', 'n'}

# Part 10: print letters that are displayed in both lists
print('Letters that are in both sets:\n',set1 & set2)

# Part 11: create a dictionary for the first three months
year = {1: 'January', 2: 'February', 3: 'March'}

# Part 12: Print the second month
print('The second month of the year dictionary: \n',year[2])

# Part 13
year[4] = 'April'
print('The fourth month is: \n',year[4])
