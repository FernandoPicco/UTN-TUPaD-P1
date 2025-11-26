
# Pasos para resolver el TPI Programación I

# 1) Resuelvo el menú. Es decir lo creo y diseño.
    # 1.1) para poder mostrar el menú, primero defino la función "mostrar_menu()"


# 3) Importo el módulo csv
# 3.1) Defino la función "obtener_datos_paises".
import csv
nombre_archivo = "dataset_paises.csv"

# 3.2) Funciones auxiliares para quitar acentos y normalizar texto

    # Función para quitar acentos
def quitar_acentos(texto):
    texto = texto.replace("á", "a").replace("Á", "a")
    texto = texto.replace("é", "e").replace("É", "e")
    texto = texto.replace("í", "i").replace("Í", "i")
    texto = texto.replace("ó", "o").replace("Ó", "o")
    texto = texto.replace("ú", "u").replace("Ú", "u")
    texto = texto.replace("ñ", "n").replace("Ñ", "n")
    return texto

def normalizar(texto):
    # quita acentos y convierte a minúsculas
    return quitar_acentos(texto.casefold())

def obtener_datos_paises():
    paises = []
    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo) # La función DictReader(), devuelve un iterador devolviendo un
                                         # diccionario clave/valor a partir de la lectura de las líneas 
                                         # del archivo csv. 
        for fila in lector:
            paises.append({"nombre": fila["nombre"], "poblacion": float(fila["poblacion"]), "superficie": float(fila["superficie"]), "continente": fila["continente"]})
    return paises

# 2) Resuelvo las funciones asociadas al menú principal

# 2.1) Función auxiliar para mostrar país
def mostrar_pais(pais):
    print(
        f"{pais['nombre']:<12} | "
        f"Población: {pais['poblacion']:>12.0f} | "
        f"Superficie: {pais['superficie']:>10.0f} | "
        f"Continente: {pais['continente']}"
    )

# 2.2) Función auxiliar para validar la entrada de población
def solicitar_entero_no_negativo(mensaje):
    #Pide un número entero >= 0. Repite hasta que el usuario ingrese bien.
    while True:
        texto_ingresado = input(mensaje).strip()
        if not texto_ingresado.isdigit(): #verificamos que contenga solo digitos.
            print("Debe ingresar un número entero 0 o mayor.")
            continue
        return int(texto_ingresado)
    
    # Opción 1
def buscar_nombre_paises():
    
    paises = obtener_datos_paises() # Esta función se encargará de devolver todos los datos asociados 
                                    # a cada país (nombre, población, continente, etc.)

    termino = input("Ingrese el nombre del país o parte del nombre: ").strip()
    if termino == "":
        print("No ingresó ningún nombre en la búsqueda.")
        return
    
    # validación mayúsculas y minúsculas
    termino_normalizado = normalizar(termino)

    # lista para guardar los países que coinciden:
    coincidencia = []

    for pais in paises:
        nombre_normalizado = normalizar(pais["nombre"])
        # coincidencia normal o exacta
        if termino_normalizado in nombre_normalizado:
            coincidencia.append(pais)

    if len(coincidencia) == 0:
        print("No se encontraron países que coincidan con la búsqueda.")
    else:
        print(f"Se encontraron {len(coincidencia)} país(es): ")
        for pais in coincidencia:
            mostrar_pais(pais)
    print()

    # Opción 2
def filtrar_por_continente():
    # cargar todos los países desde el archivo csv
    paises = obtener_datos_paises()

    # obtener desde el dataset el conjunto de continentes disponibles   
    continentes_disponibles = sorted({pais["continente"] for pais in paises})

    print("Continentes disponibles en le dataset: ")
    for cont in continentes_disponibles:
        print(f" - {cont}")
    # Pedir a usuario el continente (o parte del nombre)
    termino = input("Ingrese el continente o parte del nombre: ").strip()
    if termino == "":
        print("No ingresó ningún continente en la búsqueda.")
        return
    # validación mayúsculas y minúsculas
    termino_normalizado = normalizar(termino)

    # Buscar coincedencias
    coincidencia = []
    for pais in paises:
        continente_normalizado = normalizar(pais["continente"])
        if termino_normalizado in continente_normalizado:
            coincidencia.append(pais)
    
    #Mostrar resultados
    if len(coincidencia)==0:
        print("No se encontraron países para ese continente.")
    else:
        print(f"Se encontraron {len(coincidencia)} país(es): ")
        for pais in coincidencia:
            mostrar_pais(pais)
    print()

    # Opción 3
def filtrar_por_rango_poblacion():
    # cargar todos los países
    paises = obtener_datos_paises()
    print("***Filtrar por rango de población***")
    print("Los valores se ingresan en cantidad de habitantes (ej: 10000000)")  

    # Pedir población mínima y máxima con validación
    minimo = solicitar_entero_no_negativo("Ingrese población mínima: ")
    maximo = solicitar_entero_no_negativo("Ingrese población máxima: ")

    # Validar coherencia del rango
    if maximo < minimo:
        print("La población máxima no puede ser menor que la mínima.")
        print(f"Intercambiando valores: mínimo = {maximo}, máximo = {minimo}")
        minimo, maximo = maximo, minimo
    
    #Filtrar países dentro del rango [minimo, maximo]
    coincidencia = []
    for pais in paises:
        poblacion = pais["poblacion"]
        if minimo <= poblacion <= maximo:
            coincidencia.append(pais)
    # Mostrar resultados
    if len(coincidencia) == 0:
         print("No se encontraron países en ese rango de población.")
    else:
        print(f"Se encontraron {len(coincidencia)} país(es) en ese rango: ")
        for pais in coincidencia:       
            mostrar_pais(pais)
    print()

    # Opción 4
def filtrar_por_rango_superficie():
    # cargar todos los países
    paises = obtener_datos_paises()
    print("***Filtrar por rango de superficie***")
    print("Los valores se ingresan en km² (ej: 1000000)")

    # Pedir superficie mínima y máxima
    minimo = solicitar_entero_no_negativo("Ingrese superficie mínima (km²): ")
    maximo = solicitar_entero_no_negativo("IIngrese superficie máxima (km²): ")

    # Validar coherencia del rango
    if maximo < minimo:
        print("La superficie máxima no puede ser menor que la mínima.")
        print(f"Intercambiando valores: mínima = {maximo}, máxima = {minimo}")
        minimo, maximo = maximo, minimo
    
    # Filtrar países dentro del rango
    filtrados = []
    for pais in paises:
        sup = pais["superficie"]
        if minimo <= sup <= maximo:
            filtrados.append(pais)
    if len(filtrados) == 0:
        print("No se encontraron países en ese rango de superficie.")
        print()
        return
    # Preguntar orden: ascendente o descendente
    print("¿Cómo desea ordenar los resultados?")
    print("A- Ascendente (de menor a mayor superficie)")
    print("D- Descendente (de mayor a menor superficie)")
    orden = input("Ingrese A ó D >> : ").strip().casefold()

    if orden == "d":
        descencente = True
    else:
        descencente = False
    
    # Ordenar por superficie 
    filtrados_ordenados = sorted(filtrados, key=lambda p:p["superficie"], reverse=descencente)

    # Mostrar resultados
    print(f"Se encontraron {len(filtrados_ordenados)} país(es) en ese rango: ")
    for pais in filtrados_ordenados:
        mostrar_pais(pais)
    print()

    # Opción 5
def ordenar_paises():
    paises = obtener_datos_paises()
    print("\n***Ordenar Países***")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")

    criterio = input("Elija criterio (1, 2 ó 3): ").strip()
    if criterio not in ("1", "2", "3"):
        print("Criterio inválido. Volviendo al menú principal")
        print()
        return  
    # Elegir orden (ascendente o descendente)
    print("Orden: ")
    print("A- Ascendente (de menor a mayor superficie)")
    print("D- Descendente (de mayor a menor superficie)")
    orden = input("Ingrese A ó D >> : ").strip().casefold()

    if orden == "d":
        descencente = True
    else:
        descencente = False

    # Ordenar según criterio elegido
    if criterio == "1":
        paises_ordenados = sorted(paises, key=lambda p:p["nombre"].casefold(), reverse=descencente)
    elif criterio == "2":
        paises_ordenados = sorted(paises, key=lambda p:p["poblacion"], reverse=descencente)
    else:
        paises_ordenados = sorted(paises, key=lambda p:p["superficie"], reverse=descencente)
    
    # Mostrar resultados
    print("Países Ordenados: ")
    for pais in paises_ordenados:
        mostrar_pais(pais)
    print()

    # Opción 6
def mostrar_estadisticas():
    paises = obtener_datos_paises()

    if len(paises) == 0:
        print("No hay datos de países para calcular estadísticas.")
        print()
        return
    print("\n***Estadísticas del dataset de países***")
    # Cantidad total de paíese
    total_paises = len(paises)

    # Listas auxiliares de población y superficieç
    poblaciones = [p["poblacion"] for p in paises]
    superficies = [p["superficie"] for p in paises]

    # Población total y promedio
    poblacion_total = sum(poblaciones)
    poblacion_promedio = poblacion_total / total_paises

    # Superficie total y promedio
    superficie_total = sum(superficies)
    superficie_promedio = superficie_total / total_paises

    # País con mayor y menor población
    pais_mayor_pob = max(paises, key=lambda p:p["poblacion"])
    pais_menor_pob = min(paises, key=lambda p:p["poblacion"])

    # País con mayor y menor superficie
    pais_mayor_sup = max(paises, key=lambda p:p["superficie"])
    pais_menor_sup = min(paises, key=lambda p:p["superficie"])

    # Cantidad de países por continente
    conteo_continentes = {}
    for p in paises:
        cont = p["continente"]
        if cont in conteo_continentes:
            conteo_continentes[cont]+= 1
        else:
            conteo_continentes[cont] =1
    
    #Mostrarr resultados 
    print(f"\nCantidad total países: {total_paises}")
    print(f"Población total: {poblacion_total:.0f} habitantes.")
    print(f"Población promedio: {poblacion_promedio:.0f} habitantes.")
    print()
    print(f"Superficie total: {superficie_total:.0f} km².")
    print(f"Superficie promedio: {superficie_promedio:.0f} km².")
    print()
    print(f"País con mayor población:")
    mostrar_pais(pais_mayor_pob)
    print()
    print(f"País con menor población:")
    mostrar_pais(pais_menor_pob)
    print()
    print(f"País con mayor superficie:")
    mostrar_pais(pais_mayor_sup)
    print()
    print(f"País con menor superficie:")
    mostrar_pais(pais_menor_sup)
    print()
    print("Cantidad de países por continente: ")
    for continente, cantidad in conteo_continentes.items():
        print(f" - {continente}: {cantidad}")
    print()

    # Opción 7
def ver_todos_los_registros():
    paises = obtener_datos_paises()

    if len(paises) == 0:
        print("No hay datos para mostrar.")
        print()
        return
    print("***Lista completa de países en el dataset***")
    for pais in paises:
        mostrar_pais(pais)
    print()

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
                buscar_nombre_paises()
            case '2':
                filtrar_por_continente()
            case '3':
                filtrar_por_rango_poblacion()
            case '4':
                filtrar_por_rango_superficie()
            case '5':
                ordenar_paises()
            case '6':
                mostrar_estadisticas()
            case '7':
                ver_todos_los_registros()
            case '8':
                print("¡Gracias por utilizar nuestra aplicación!¡Hasta pronto!")
                break
            case _:
                print("La opción seleccionada no es válida para nuestra aplicación")
# Invoco la función para poder mostrarla
mostrar_menu()