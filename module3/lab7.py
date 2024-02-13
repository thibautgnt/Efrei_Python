"""
You must complete the code to design a vowel eater that :

ask the user to enter a word; use userWord = userWord.upper() to convert the word entered by the user to upper case; use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word; print the uneaten letters to the screen, each one of them on a separate line.
"""

userWord = input("Enter a word: ")
userWord = userWord.upper()
for letter in userWord:
    if letter in "AEIOU":
        continue
    print(letter)