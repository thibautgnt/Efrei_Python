# Tax calculator : if the citizen's income <= 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents.
# If the income > 85,528, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Your tax calculator should accept one floating-point value: the income.
"""
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you
If the calculated tax is less than zero, it only means no tax (the tax is zero). Take this into consideration !
"""

income = float(input("Enter the annual income: "))
if income <= 85528:
    tax = round(income * 0.18 - 556.02)
else:
    tax = round(14839.02 + (income - 85528) * 0.32)
if tax < 0:
    tax = 0
print("The tax is:", tax, "thalers")