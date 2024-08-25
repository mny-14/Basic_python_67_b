start = 21
end = 40

# Create lists for odd and even numbers
odd_num = []
even_num = []

# Iterate through the range and categorize each number
for number in range(start, end + 1):
    if number % 2 == 0:
        even_num.append(number)
    else:
        odd_num.append(number)

# Print the results
print("Odd numbers :", odd_num)
print("Even numbers :", even_num)