n = [65, 23 ,42]

# Comparamos los valores y los ordenamos
if n[0] > n[1]:
    n[0], n[1] = n[1], n[0]
if n[1] > n[2]:
    n[1], n[2] = n[2], n[1]
if n[0] > n[1]:
    n[0], n[1] = n[1], n[0]

print(n)