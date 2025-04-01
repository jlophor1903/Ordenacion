n = [65, 23 ,42]

# Comparamos los valores y los ordenamos
for i in range(2):
    if n[i] > n[i+1]:
        n[i], n[i+1] = n[i+1], n[i]


print(n)