#NESTED FOR LOOP (Diamond Pattern)


for c in range(1, 16, 1):
    for z in range(15, c, -1):
        print(" ", end = " ")
    for a in range(1, c, 1):
        print("$", end = " ")
    for e in range(1, c + 1, 1):
        print("$", end = " ")
    print()

for c in range(14, 0, -1):
    for d in range(15, c, -1):
        print(" ", end = " ")
    for t in range(1, c, 1):
        print("$", end = " ")
    for a in range(1, c + 1, 1):
        print("$", end = " ", )
    print()