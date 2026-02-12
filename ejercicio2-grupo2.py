def agregar_estudiante(lista, nombre, nota):
    estudiante = {
        "nombre": nombre,
        "nota": nota
    }
    lista.append(estudiante)


def mostrar_estudiantes(lista):
    for est in lista:
        print(f"Nombre: {est['nombre']} - Nota: {est['nota']}")


def promedio_general(lista):
    suma = 0
    for est in lista:
        suma += est["nota"]
    return suma / len(lista)


# Prueba
estudiantes = []

agregar_estudiante(estudiantes, "Ana", 4.5)
agregar_estudiante(estudiantes, "Luis", 3.8)
agregar_estudiante(estudiantes, "Maria", 4.2)

mostrar_estudiantes(estudiantes)
print("Promedio:", promedio_general(estudiantes))
