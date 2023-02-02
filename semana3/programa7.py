"""
    Programa7
    Nombre:Janneth Santos Molina
    Fecha:31/01/2023
    Descripción: Programa que calcula el área y perímetro de un círculo
"""

print("""1) Círculo 2) Cuadrado""")

seleccion= input("-Selecciona algo :")

if seleccion== "1":
    
    print("Calcula el área y perímetro de un círculo")
  
    radio = float(input("Ingresa la medida del radio: "))
    PI= float(3.1416)
    area = float( PI * ( radio ** 2))
    perimetro = float(( 2 * PI ) * radio)

    print(f"El área de un círculo de {radio} de radio es de {area}")
    print(f"El perímetro de un círculo de {radio} de radio es de {perimetro}")

else:

    print("Calcula el área y perímetro de un cuadrado")
  
    lado = float(input("Ingresa la medida del lado: "))
    area = float( lado ** 2)
    perimetro = float(lado * 4 )

    print(f"El área de un cuadrado de { lado } de lado es de {area}")
    print(f"El perímetro de un cuadrado de { lado } de lado es de {perimetro}")
  
