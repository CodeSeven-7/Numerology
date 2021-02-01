# This program adds together Birthday numbers provided by the user to determine his Life Path number.

print("Hello :)")
print("In order to calculate your Life Path Number please answer the following questions:")

# Store input numbers
year = input("Enter your Birth Year:")
month = input("Enter your Birth Month:")
day = input("Enter your Birth Day:")

# Add Day + Month + Year
number = int(day) + int(month) + int(year)

digits = [int(x) for x in str(number)]

a = sum(digits)

b = [int(x) for x in str(a)]

c = sum(b)

# Display the sum

print("Your Life Path Number is: ")
print(c)
