# MULTIPLICATION TABLE MAKER

# Ask the user to enter a number
num = int(input("MULTIPLICATION TABLE MAKER\nEnter a number: "))

print(f"\nMultiplication table for {num}:")

# Loop through 1 to 10 and print the multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
