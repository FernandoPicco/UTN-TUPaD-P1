# Diccionario de productos y su respectivo stock. Claves (nombres) y Valores (stock)

stock = {
    "filtro de aire": 150,
    "filtro de combustible": 120,
    "bidón de aceite x 4 Lts.": 75,
    "filtro de polen": 111
}

while True:
    print("Opciones de Menú")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades de stock a un producto existente")
    print("3. Agregar un producto nuevo")
    print("4. Salir.")

    opcion = input("Elige una de las opciones: ").strip()

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ").strip().lower()

        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]} unidades")
        else: 
            print(f"El producto seleccionado '{producto}' no existe en el inventario")
    
    elif opcion == "2":
        producto = input("producto al que desea agregar stock: ").strip().lower()
        if producto in stock:
            while True:
                cantidad = input("Cantidad a agregar: ").strip()
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    stock[producto] += cantidad
                    print(f"Se agregaron {cantidad} unidades de stock a {producto}. Nuevo Stock: {stock[producto]}")
                    break
                else: 
                    print("Ingrese un número válido.")
        else:
            print("El producto no existe. Ingrese la opción 3 para adicionarlo.")
        
    elif opcion == "3":
        producto_nuevo = input("Ingrese el nombre del nuevo producto: ").strip().lower()
        if producto_nuevo in stock:
            print("El producto ingresado existe.")
        else:
            while True:
                cantidad = input("Ingrese la cantidad inicial: ").strip()
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    stock[producto_nuevo] = cantidad
                    print(f"El producto '{producto_nuevo}' agregado con {cantidad} unidades.")
                    break
                else:
                    print("Ingrese un número válido.")
    
    elif opcion == "4":
        print("Hasta pronto!")
        break    
    else: 
        print("Opción inválida.")
