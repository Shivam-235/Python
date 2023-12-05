#pascals triangle
rows = int(input("rows: "))
for i in range(rows):
    coef = 1
    for space in range(1, rows-i+1):
        print(" ", end="")
    for j in range(0, i+1):
        print(coef, end=" ")
        coef = int(coef * (i - j) / (j + 1))
    print()