"""
    Programa5
    Nombre:Janneth Santos Molina
    Fecha:30/01/2023
    Descripción:Suma, resta, división y potencia de dos        números
"""

numero1= input("Número 1: ") #Pide que insertes un valor mediante teclado
numero2= input("Número 2: ") #Le asigna un valor

suma= int(numero1) + int(numero2) #Concatena dos valor
print(f"La suma de los números es: {suma}") #Imprime el resultado de la suma

resta= int(numero1) - int(numero2) #Resta las dos variables
print ("La resta de los números es: ", (resta)) #Imprime el resultado de la resta

division= int(numero1) / int(numero2) #Divide las variables
print (f"El resultado de la división es: {division}") #Imprime el resultado de la división

potencia= int(numero1) ** int(numero2) #Realiza la potencia de variables
print ("El resultado de la potencia es: {}" .format(potencia)) #Imprime el resultado de la potencia





