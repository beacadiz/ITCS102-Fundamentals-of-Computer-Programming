odd_sum = 0  # To store the sum of odd numbers

for i in range(7):
    number = int(input("Enter a number: "))
    if number % 2 != 0:  # Check if the number is odd
        odd_sum += number

print("The sum of all odd numbers is", odd_sum)

