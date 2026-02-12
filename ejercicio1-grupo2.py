def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Prueba
f, k = convertir_temperatura(25)
print("Fahrenheit:", f)
print("Kelvin:", k)
