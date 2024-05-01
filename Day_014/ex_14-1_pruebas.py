# Lista de diccionarios
# Las listas de diccionarios son una estructura de datos muy útil que combina las capacidades de las listas
# (para almacenar múltiples elementos ordenados) y los diccionarios (para almacenar pares clave-valor).
# Esto te permite manejar colecciones de elementos estructurados de una manera flexible y poderosa.

# En este ejemplo, personas es una lista que contiene tres diccionarios.
# Cada diccionario representa una persona con ciertos atributos (nombre, edad, ciudad).

personas = [
    {"nombre": "Ana",
     "edad": 30,
     "ciudad": "Madrid"
     },
    {"nombre": "Juan",
     "edad": 25,
     "ciudad": "Barcelona"
     },
    {"nombre": "María",
     "edad": 35,
     "ciudad": "Sevilla"
    }
]

# Cómo interactuar ccon esta lista de diccionarios

# 1.- Acceder a un elemento:
# Puedes acceder a un diccionario específico dentro de la lista usando su índice:
primera_persona = personas[0]

print(primera_persona)

# 2.- Acceder a un valor específico:
# Puedes acceder a un valor dentro de un diccionario específico utilizando la clave correspondiente:
print(personas[2]['nombre'])

# 3.- Iterar sobre la lista de diccionarios:
# Puedes usar un bucle for para recorrer todos los elementos de la lista:
for persona in personas:
    print(persona["nombre"], persona["ciudad"])

# 4.- Agregar nuevos elementos:
# Puedes agregar un nuevo diccionario a la lista utilizando append():

nueva_persona = {"nombre": "Luisa", "edad": 28, "ciudad": "Valencia"}
personas.append(nueva_persona)

# 5.- Modificar valores existentes:
# Puedes actualizar los valores de un diccionario existente dentro de la lista:

personas[0]["edad"] = 32


# Las listas de diccionarios son muy útiles para representar datos estructurados y complejos en Python.
# Puedes realizar operaciones como búsqueda, actualización, inserción y eliminación de elementos de manera eficiente
# utilizando esta estructura.