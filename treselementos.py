#Archivo: treselementos.py
#Fecha: 08/04/2025
#proy.: estudio de algoritmos
#
# Ordenar crecientemente una lista de tres valores
# Existe un error, ya que según los valores, puede cambiar
# dos que entre ellos había que cambiar, perogenera mal orden 
# en los posteriores. 

n = [252 , 14, 58]

# Bucle para tomar datos del teclado y guardarlos en la variable n de tipo lista
def swap(j):
    a = n[j]
    n[j] = n[j+1]
    n[j+1] = a
 

for i in range(5):
    for j in range(5):
        if n[j]>n[j+1]:
            swap(j)

print(n) 