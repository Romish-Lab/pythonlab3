# 7. Write a Python program to input n numbers from user, count even and odd numbers, and stop when input is 0.
a = [7, 4, 3, 8, 5, 6, 1, 2, 9, 0]
b = c = 0
for d in a:
    if d == 0:
        break
    if d % 2 == 0:
        b += 1
    else:
        c += 1
print("Number of even numbers:", b)
print("Number of odd numbers:", c)
