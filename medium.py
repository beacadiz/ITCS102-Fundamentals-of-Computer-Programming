# medium

print("Multiplication Columns Table")
columns = eval(input("Enter the number of colmuns: "))

for b in range (1, 11, 1):
    for e in range (1, columns + 1, 1):
        print(f"{b}x{e}={b*e}", end = "\t\t")
    print()

print("\n\nAsterisk Sequence Triangle")
for c in range (1, 6, 1):
    for a in range (6, c, -1):
        print(" ", end="")
    for d in range (1, c + 1, 1):
        print("* ", end="")
    print()