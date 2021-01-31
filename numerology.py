# This program adds together Birthday numbers provided by the user to determine his Life Path number.

print("Hello :)")
print("In order to calculate your Number please answer the following questions:")

# Store input numbers
year = input("Enter your Birth Year:")
month = input("Enter your Birth Month:")
day = input("Enter your Birth Day:")

# Add Day + Month + Year
sum = int(day) + int(month) + int(year)

# Display the sum

print("Your number is: {0}" .format(sum))
