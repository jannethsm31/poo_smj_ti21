"""
    Programa9
    Nombre:Janneth Santos Molina
    Fecha:07/02/2023
    Descripción: Posibles formas de buscar el 
    número mayor entre dos números
"""

#n1=int(input("Número 1: ")) # Almacena el número 1
#n2=int(input("Número 2: ")) # Almacena el número 2


""" 
Forma 1
if n1!=n2: # Checa que el pirmer numero sea diferente del segundo
    
    if n1>n2: # Compara ambos números de acuerdo a su jerarquia
        print(n1) #Imprime el numero maypr
    else:
        print(n2) # Imprime el número menor

else: 
    print(None) # Si ninguno es menor imprime el igual

"""

"""
Forma 2
if n1>n2: # Compara dos variables
    print(n1) # Imprime la variable más grande
    if n2>n1: # Compara la segunda variable con la primera
        print(n2) # Imprime la más grande
        if n1==n2: #Compara si las variables son iguales
            print(None) #Imprime None porque soon iguales

"""

"""
Forma 3
if n2>n1: # Compara que la primera variable sea mayor
    print(n2) #Imprime la primera variable
    if n1>n2: # Compara que el primer número sea mayor que el segundo
        print(n1) #Imprime el segundo valor
    else:
        print(None) # Si ninguna de las anteriores se cumplieron entonces quiere decir que es igual

"""

"""
Forma 4
if n1>n2:
    print(n1)
elif n2>n1:
    print(n2)
else:
    print(None)
"""    

"""
#Forma 5
if n1==n2:
    print(None)
elif( n1>n2):
    print(n1)
elif n2>n1:
    print(n2)
"""

"""
#Forma 6
if n1<n2:
    print(n2)
    if n2<n1:
        print(n1)
        if n1==n2:
            print(None)
"""

"""
#Forma 7
if n2>n1:
    print(n2)
    if n2<n1:
        print(n1)
    else:
        print(None)
"""

"""
#Forma 8
if (n2<n1>n2):
    print(n1)
elif (n1>n2>n1):
    print(n2)
else:
    print(None)
"""

"""
#Forma 9
if n1<=n2:
    if n1==n2:
        print(None)
    else:
        print(n2)
else:
    print(n1)
"""

"""
#Forma 10

mayor = max(n1, n2)

if mayor == n1:
  print(f"{n1} es mayor que {n2}")
elif mayor == n2:
    print(f"{n2} es mayor que {n1}")
else:
  print(None)
"""

"""
#Forma 11
mayor = max(n1, n2)

if mayor == n1 and mayor != n2:
  print(f"{n1} es mayor que {n2}")
elif mayor == n2 and mayor != n1:
  print(f"{n2} es mayor que {n1}")
else:
  print(None)
"""
height = float(input())
weight = float(input())

bmi = weight/(height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25.0:
    print("Normal")
elif bmi >= 25.0 and bmi < 30.0 :
    print("Overweigth")
else:
    print("Obesity")

