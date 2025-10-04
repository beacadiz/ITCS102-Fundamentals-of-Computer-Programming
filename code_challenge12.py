#NESTED FOR LOOP (Numeric Pyramid Pattern)

print("\t\t1", end = "")
for b in range(1 , 10 ,1):
    for c in range(9, b, -1):
        print(" ", end = " ")
    for z in range(b, 1, -1):
        print(b, end = " ")
    for t in range(1, b + 1, 1):
        print(b, end = " ")
    print()
