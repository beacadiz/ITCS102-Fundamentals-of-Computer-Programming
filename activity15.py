#String Formatting

#first part
surname = 'Cadiz'
mddlname = 'Zantua'
frstname = 'Beatrice'
nickname = 'Bea'

print(f"I am {surname}, {frstname} {mddlname}. You can call me {nickname} for short.\n")

#Second Part
sum = 0
for b in range(1,11,1):
    num = eval(input(f"b - Input a number --> "))
    sum += num
print(f"The sum of all the numbers given is {sum}")