print("The FACTORIAL program")

#ask user to input
num = int(input("Enter any number: "))

#computer factorial
factorial = 1
for i in range(1, num + 1):
    factorial *= i

#Output result
print(f"The Factorial of {num} is {factorial}")