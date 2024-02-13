"""
Your task is to write a program which removes all the number repetitions from the list “myList”. The goal is to have a list in which all the numbers appear not more than once. You can Use : for loop, intermediate list and the not in operator
"""

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
for i in myList:
    if i not in newList:
        newList.append(i)
myList = newList
print("The list with unique elements only:")

print(myList)