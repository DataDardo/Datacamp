"""Calculations with variables

Remember how you calculated the money you ended up with after 7 years of investing $100? You did somethings like this:

100 * 1.1 ** 7

Instead of calculating the actual values, you can use variables instead. The savings variable you've created in the
previous exercise represents the $100 you started with. It's up to you to create a new variable to represent 1.1
and then redo the calculations!"""

# Create a variable savings
savings = 100

# Create a variable growth_multiplier, equal to 1.1
growth_multiplier = 1.1

# Create a variable, result, equal to the amount of money you saved after 7 years.
result = savings * growth_multiplier ** 7

# Print out the value of result.
print(result)