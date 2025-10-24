#easy

print("Asterisk Triangle")
for b in range (1, 6, 1):
    for e in range (7, b, -1):
        print(" ", end="")
    for a in range (1, b*2, 1):
        print("*", end="")
    print()

print("\nNumber Sequence")
for c in range (1, 6, 1):
    for a in range (1, c, 1):
        print(c, end = "")
    print(c)