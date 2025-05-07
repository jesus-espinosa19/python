#elabora un programa que calcule y escriba el precio de venta para un articulo ,
#se tiene, el nombre del producto y el costo de produccion; el precio de venta se calcula el 120%
#como utilidad y 15% de impuesto.

producto = input("Ingrese el nombre del producto: ")
costo = float(input("Ingrese el costo de produccion: "))
utilidad = float(costo)*0.12
impuesto = float(costo)*0.15
precioVenta = float(costo) + float(utilidad) + float(impuesto)
print("El precio de venta del producto", producto, "es: ", precioVenta)