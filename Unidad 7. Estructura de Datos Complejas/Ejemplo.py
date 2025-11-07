# creamos el diccionario donde se guardan los nombres de los alumnos y las notas correspondientes:
alumnos = {}

# ciclo for para pedir nombres y notas de los 3 alumnos

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip()
    #print(nombre)

    print(f"Ingrese las 3 notas de {nombre}: ")
    primera_nota = float(input("Primera nota: "))
    segunda_nota = float(input("Segunda nota: "))
    tercera_nota = float(input("Tercera nota: "))

    # guardo las notas en una tupla (diccionario)
    alumnos[nombre] = (primera_nota, segunda_nota, tercera_nota)

# Procedimiento para obtener y mostrar el promedio
print("Promedio de alumnos: ")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)

    print(f"{nombre}: {promedio:.2f}") # el promedio se muestra con 2 decimales