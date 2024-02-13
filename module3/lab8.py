"""
upgraded (pretty) the vowel eater coded in the last lab.
You have to created wordWithoutVovels and assigned an empty string to it.
Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the wordWithoutVovels variable.
"""

userWord = input("Enter a word: ")
userWord = userWord.upper()
wordWithoutVovels = ""
for letter in userWord:
    if letter in "AEIOU":
        continue
    wordWithoutVovels += letter
print(wordWithoutVovels)