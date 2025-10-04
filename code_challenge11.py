#NESTED FOR LOOP (Pyramid or Half Diamond Pattern)

print("\t\t\t   $", end = "")
for c in range(1, 16, 1):
    for e in range(15, c, -1):
        print(" ", end = " ")
    for z in range(1, c, 1):
        print("$", end = " ")
    for d in range(1, c, 1):
        print("$", end = " ")
    print()