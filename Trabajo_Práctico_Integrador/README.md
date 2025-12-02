# Título del proyecto
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

# Datos de la universidad y materia
- Universidad: UTN
- Carrera: Tecnicatura Universitaria en Programación a Distancia (TUPaD)
- Materia: Programación I
- Año: 2025

# Integrante
- Alumno: Fernando Picco
- Comisión: 10

# Datos de los profesores
- Titular: Ariel Enferrel  
- Tutora: Martina Zabala

# Descripción del proyecto
Este proyecto forma parte del Trabajo Práctico Integrador de la materia Programación I.
El objetivo principal es desarrollar una aplicación en Python capaz de:
* Leer datos reales almacenados en un archivo CSV.
* Validar su contenido y convertirlo en una estructura manipulable.
* Aplicar búsquedas, filtros, ordenamientos y estadísticas sobre los datos.
* Interactuar con el usuario mediante un menú principal con múltiples funcionalidades.

El sistema trabaja con información sobre países, incluyendo:
* Nombre
* Continente
* Poblaciçon
* Superficie (km2)

La aplicación está diseñada de forma modular, con funciones independientes, validaciones robustas y una arquitectura clara.

# Estructura del proyecto

*** Proyecto-TPI ***
- tpi_gestion_datos_paises.py  (Script principal del programa)
- dataset_paises.csv           (Archivo CSV con los datos)  
- README.md                    (Este archivo)
- Presentación_TPI_P1.pdf      (Presentación en diapositivas)
- Video_demostración.mp4:       (ejecución del programa) 

# Instrucciones de ejecución 
1. Asegurarse de tener Python 3.10 o superior.
(El proyecto utiliza match-case, introducido en Python 3.10).

2. Clonar o descargar el repositorio:
https://github.com/FernandoPicco/UTN-TUPaD-P1.git

3. Ejecutar el script principal:
python tpi_gestion_datos_paises.py

4. Asegurarse de que el archivo dataset_paises.csv se encuentre en la misma carpeta que el script.

# Librerías utilizadas
El proyecto utiliza solo librerías estándar de Python:
* csv → para lectura del archivo CSV
* unicodedata (opcional según implementación) → para normalización de acentos
* math (opcional) → si se usa en estadísticas

*** No requiere instalación de librerías externas.

# Links importantes
* Repositorio GitHub: https://github.com/FernandoPicco/UTN-TUPaD-P1.git
* Video explicativo del TPI:
* Video demostración de ejecución: https://drive.google.com/file/d/1U-DWCy-qgcVD1f0nC3KkpIZr55us2dP-/view?usp=sharing

# Ejemplos de entrada y salida
==> Ejemplo de menú principal 

*** Menú principal ***
1. Buscar país por nombre
2. Filtrar por continente
3. Filtrar por rango de población
4. Filtrar por rango de superficie
5. Ordenar países
6. Mostrar estadísticas
7. Ver todos los registros
6. Salir

# Ejemplo de búsqueda de países por nombre
==> Entrada:

Ingrese el nombre o parte del nombre: argen

==> Salida:

Se encontraron 1 país(es):
Argentina  | Población:   45376763 | Superficie:   2780400 | Continente: América

# Ejemplo de estadísticas

***Estadísticas del dataset de países***

Cantidad total países: 10
Población total: 2156641833 habitantes.
Población promedio: 215664183 habitantes.

Superficie total: 35768356 km².
Superficie promedio: 3576836 km².

País con mayor población:
India        | Población:   1393409038 | Superficie:    3287263 | Continente: Asia

País con menor población:
Australia    | Población:     25925600 | Superficie:    7692024 | Continente: Oceanía

País con mayor superficie:
Canadá       | Población:     38008005 | Superficie:    9984670 | Continente: América

País con menor superficie:
Alemania     | Población:     83149300 | Superficie:     357022 | Continente: Europa

Cantidad de países por continente:
 - América: 3
 - Asia: 2
 - Europa: 2
 - Oceanía: 1
 - África: 2

# Conclusión
Este proyecto integra los conceptos fundamentales de Programación I:
listas, diccionarios, funciones, condicionales, bucles, ordenamientos, manejo de archivos, estadísticas y validaciones.

A través del desarrollo, se buscó construir una aplicación robusta, modular y clara, capaz de manipular datos reales de forma eficiente.

# Licencia
Este proyecto es de uso académico para la materia Programación I.


