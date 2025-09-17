#COUNTDOWN TIMER SIMULATOR

#Ask the user to enter the starting number
start = int(input(" COUNTDOWN TIMER SIMULATOR Enter the starting number for countdown: "))

print("Countdown started:")

#Use a for loop to count down from the starting number to 1
for i in range(start, 0, -1):
    print(i)

#Print Liftoff! after the countdown
print("Liftoff!")
