
#while loop
#laundry analogy
#keywords -- while, continue, break
#requirements - boolean variable

isDirty = True #boolean initial value
sum = 0

while isDirty == True:
    confirm = input("Do you wish to continue washing (yes / no)").lower()
    sum += 1

    if confirm == 'yes':
        print("Washing  Continues .... ")
        continue
    else:
        print("Washing stops... ")
        break

print("Number of cycle is", sum)
