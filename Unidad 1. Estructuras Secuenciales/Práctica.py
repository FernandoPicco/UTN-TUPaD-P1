#Enunciado
#Una tienda de ropa vende remeras a $4000 cada una y pantalones a $8000 cada uno.
#El programa debe:
#Pedir al usuario cuántas remeras quiere.
#Pedir cuántos pantalones quiere.
#Calcular el total a pagar.
#Calcular cuánto dinero debería pagar si decide dar una seña del 30% del total.
#Mostrar en pantalla:
#Precio de las remeras
#Precio de los pantalones
#Total general
#Monto de la seña
 
pantalones = int(input("Ingrese la cantidad de pantalones: "));
remeras = int(input("Ingrese la cantidad de remeras: "));
valor_remera = 4000;
valor_pantalon = 8000;

total_pantalon = pantalones * valor_pantalon;
total_remeras = remeras * valor_remera;
total_pagar = total_pantalon + total_remeras;
monto_adelanto = total_pagar * 0.30;

print(f"El precio de compra de los pantalones es $ {total_pantalon}");
print(f"El precio de compra de las remeras es $ {total_remeras}");
print(f"El precio de compra total a pagar es de $ {total_pagar}");
print(f"El precio de la seña en concepto de compra es de $ {monto_adelanto}");

