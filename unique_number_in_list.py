# Python program to find unique numbers in a given list.
L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []
for digit in L1:
    if digit not in L2:
        L2.append(digit)
print("Unique numbers in the list : ",L2)
