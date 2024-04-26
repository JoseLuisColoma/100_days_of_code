
# Simple function
def greet():
    print("Hola")
    print("Qué tal estás?")
    print("Adios!")


greet()


# Function that allows input


def greet_with_name(name):
    print("Hi, " + name)


greet_with_name("Jose")


# Functions with more than 1 input


def greet_with(name, location):
    print(name + " - " + location)


greet_with("Pedro", "Cartagena")


# Keywords arguments

def greet_with_arg(**kwargs):
    key_list = []
    value_list = []
    dic = {}
    for key, value in kwargs.items():
        key_list.append(key)
        value_list.append(value)
        dic[key] = value
    print(key_list)
    print(value_list)
    print(dic)


greet_with_arg(a="Juan", b="Pedrito", c="Andres")


frutas = ['pera', 'manzana', 'platano']
posiciones = []
for fruta in frutas:
    posicion = frutas.index(fruta)
    posiciones.append(posicion)

print(posiciones)

