x = [1, 2, 3, 4, 5,6,3,4]
j = 0

for i in range(len(x)):
    if x[j] % 2 == 0:
        del x[j]
    else:
        j = j + 1

print(x)