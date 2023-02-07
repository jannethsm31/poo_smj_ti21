"""
    Programa9
    Nombre:Janneth Santos Molina
    Fecha:07/02/2023
    Descripción: Posibles formas de buscar el 
    número mayor entre dos números
"""

n1=int(input("Número 1: "))
n2=int(input("Número 2: "))


""" 
Forma 1
if n1!=n2:
    
    if n1>n2:
        print(n1)
    else:
        print(n2)

else: 
    print(None)

"""

"""
Forma 2
if n1>n2:
    print(n1)
    if n2>n1:
        print(n2)
        if n1==n2:
            print(None)

"""

"""
Forma 3
if n2>n1:
    print(n2)
    if n1>n2:
        print(n1)
    else:
        print(None)

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


#Forma 5
if n1==n2:
    print(None)
elif( n1>n2):
    print(n1)
elif n2>n1:
    print(n2)

#Forma 6
if n1<n2:
    print(n2)
    if n2<n1:
        print(n1)
        if n1==n2:
            print(None)

#Forma 7
if n2>n1:
    print(n2)
    if n2<n1:
        print(n1)
    else:
        print(None)

#Forma 8
if (n2<n1>n2):
    print(n1)
elif (n1>n2>n1):
    print(n2)
else:
    print(None)

#Forma 9
if n1<=n2:
    if n1==n2:
        print(None)
    else:
        print(n2)
else:
    print(n1)

#Forma 10

#Forma 11
    


