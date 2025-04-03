n = [252 , 14, 58]
def swap(j):
    a = n[j]
    n[j] = n[j+1]
    n[j+1] = a
 

for i in range(5):
    for j in range(5):
        if n[j]>n[j+1]:
            swap(j)

print(n) 