#wap to print pattern using nested for loop
n = 5
for a in range(1, n + 1):
    for b in range(a):
        print("* ", end="")
    print()
for a in range(n - 1, 0, -1):
    for b in range(a):
        print("* ", end="")
    print()