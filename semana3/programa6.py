"""
    Programa6
    Nombre:Janneth Santos Molina
    Fecha:30/01/2023
    Descripción: Programa que calcula el área y perímetro de un 
    triángulo
"""

print("""1) Por lados 2) Por base y altura""") # Opción a elegir como calcular

eligio=input("-Selecciona algo :") # La selección

if eligio=="1": #Qué sucederá al escoger la primera opción
  
  print("Ingresa las medidas para calcular el área y perímetro    de un triángulo") # Muestra que medidas 

  lado1 = float(input("Medida del primer lado: ")) # Ingresa en   la variable del primer lado
  lado2 = float(input("Medida del segundo lado : ")) # Almacena    la variable del segundo lado
  lado3 = float(input("Medida del tercer lado : ")) #Almacena     en la tercera variable

  perimetro = lado1 + lado2 + lado3 # Calcula el perímetro        sumando los lados ingresados
  s = perimetro / 2 # Divide y alamcena en una variable el        perimetro entre 2
  area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5 #   Almacena el resultado del área 

  print("El perimetro es = {}".format(perimetro)) #     Imprime el perimetro del triángulo
  print("El area es = {}" .format(area)) # Imprime el área del triangulo

elif eligio=="2": # Realiza apartir de la segunda opción

  print("Ingresa las medidas")

  base = float(input("Medida de la base: "))
  altura = float(input("Medida de la altura: "))
  lado1 = float(input("Medida de lado 1: "))
  lado2 = float(input("Medida de lado 2: "))

  area = (base*altura) / 2
  perimetro = lado1 + lado2 + base

  print("El area del triangulo es = {}" .format(area))
  print("El perimtro del triangulo es = {}" .format(perimetro))

