# Pasos para resolver el TPI Programación I

# 1) Resuelvo el menú. Es decir lo creo y diseño.
    # 1.1) para poder mostrar el menú, primero defino la función "mostrar_menu()"

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