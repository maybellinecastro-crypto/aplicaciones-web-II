def analizar_ventas(lista):
    mayor = max(lista)
    menor = min(lista)
    promedio = sum(lista) / len(lista)
    return mayor, menor, promedio


# Prueba
ventas = [1200, 850, 1020, 2100, 1750, 980]

mayor, menor, promedio = analizar_ventas(ventas)

print("Venta mayor:", mayor)
print("Venta menor:", menor)
print("Promedio:", promedio)
