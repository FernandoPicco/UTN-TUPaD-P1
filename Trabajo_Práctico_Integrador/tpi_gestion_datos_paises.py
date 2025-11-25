# Pasos para resolver el TPI Programación I

# 1) Resuelvo el menú. Es decir lo creo y diseño.
    # 1.1) para poder mostrar el menú, primero defino la función "mostrar_menu()"


# 3) Importo el módulo csv
# 3.1) Defino la función "obtener_datos_paises".
import csv
nombre_archivo = "dataset_paises.csv"
paises = []
def obtener_datos_paises():
    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo) # La función DictReader(), devuelve un iterador devolviendo un
                                         # diccionario clave/valor a partir de la lectura de las líneas 
                                         # del archivo csv. 
        for fila in lector:
            paises.append({"nombre": fila["nombre"], "poblacion": float(fila["poblacion"]), "superficie": float(fila["superficie"]), "continente": fila["continente"]})

# 2) Resuelvo las funciones asociadas al menú principal
    # Opción 1
def buscar_nombre_paises():
    
    paises = obtener_datos_paises() # Esta función se encargará de devolver todos los datos asociados 
    print(paises)                   # a cada país (nombre, población, continente, etc.)

def mostrar_menu():
    # Para mostrar constantemente el menú:
    while True:
        print("*** Menú Principal ***")
        print("1. Buscar país por nombre (coincidencia parcial o exacta)")
        print("2. Filtrar por continente")
        print("3. Filtrar por rango de población")
        print("4. Filtrar por rango de superficie")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Ver todos los registros")
        print("8. Salir")

        opcion = input("Ingrese opción: ").strip()
        match opcion:
            case '1':
                print("Buscar por países (coincidencia parc o exacta)")
            case '2':
                print("Filtrar por continente")
            case '3':
                print("Filtrar por rango de población")
            case '4':
                print("Filtrar por rango de superficie")
            case '5':
                print("Ordenar países")
            case '6':
                print("Mostrar estadísticas")
            case '7':
                print("Ver todos los registros")
            case '8':
                print("Gracias por utilizar nuestra aplicación")
                break
            case _:
                print("La opción seleccionada no es válida para nuestra aplicación")
# Invoco la función para poder mostrarla
mostrar_menu()