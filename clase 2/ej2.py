from pprint import pprint

colores = {
    "azul": "blue",
    "rojo": "red",
    "verde": "green",
}
pprint(colores["azul"])

# get es para traerlo
mis_colores = colores.get("azul")
pprint(mis_colores)
# para crear otro color en diccionario

colores["blanco"] = "whitte"
pprint(colores)
colores["blanco"] = "white"
pprint(colores)

mas_colores = {
    "amarillo": "yellow",
    "negro": "black",
}
colores.update(mas_colores)
pprint(colores)

del colores["rojo"]
pprint(colores)
colores.pop("negro")
pprint(colores)


#creo un diccionario, y agrego argentina
from pprint import pprint

campeones_mundiales = {
    "1990": "alemania",
    "1994": "brasil",
    "1998": "francia",
    "2002": "brasil",
}   
print(campeones_mundiales)

campeones_mundiales[2022] ="argentina"
print(campeones_mundiales)



nueva_lista = "Esto esto es una prueba".lower().split()
print(nueva_lista)
print(len(nueva_lista))
print(type(nueva_lista))
nueva_lista.append("1234")
print(nueva_lista)
nueva_lista.remove("es")
print(nueva_lista)
print(nueva_lista.count("esto"))
#
from pprint import pprint

colores = {
    "azul": "blue",
    "rojo": "red",
    "verde": "green",
}

mi_color = colores["azul"]
print(mi_color)

mi_color = colores.get("azul", "No se encontro el color")
print(mi_color)

colores["blanco"] = "wite"
pprint(colores)
colores["blanco"] = "white"
pprint(colores)

más_colores = {
    "amarillo": "yellow",
    "negro": "black",
    "rojo": "red",
}

print(colores.update(más_colores))
pprint(colores)

del colores["rojo"]
pprint(colores)

colores.pop("negro")
pprint(colores)

#
lista_nombres_italianos = [
    "Gianluigi Buffon",
    "Cristiano Ronaldo",
    "Gianluigi Donnarumma",
    "Andrea Pirlo",
    "Andrea Agnelli",
]

lista_nombres_italianos.sort()
print(lista_nombres_italianos)
lista_nombres_italianos.reverse()
print(lista_nombres_italianos)

nombres_franceses = [
    "Zinedine Zidane",
    "Kylian Mbappe",
]

lista_nombres_italianos.extend(nombres_franceses)
lista_nombres_italianos.insert(0, "Giorgio Chiellini")
print(lista_nombres_italianos)
# lista_numeros_palabras = [
#     1.2, 4.4, -.34
# ]
# lista_numeros_palabras.sort(reverse=True)
# print(lista_numeros_palabras)
#
lista_nombres_italianos = [
    "Gianluigi Buffon",
    "Cristiano Ronaldo",
    "Gianluigi Donnarumma",
    "Andrea Pirlo",
    "Andrea Agnelli",
]

lista_nombres_italianos.sort()
print(lista_nombres_italianos)
lista_nombres_italianos.reverse()
print(lista_nombres_italianos)

nombres_franceses = [
    "Zinedine Zidane",
    "Kylian Mbappe",
]

lista_nombres_italianos.extend(nombres_franceses)
lista_nombres_italianos.insert(0, "Giorgio Chiellini")
print(lista_nombres_italianos)
# lista_numeros_palabras = [
#     1.2, 4.4, -.34
# ]
# lista_numeros_palabras.sort(reverse=True)
# print(lista_numeros_palabras)

lista_nombres_italianos = [
    "Gianluigi Buffon",
    "Cristiano Ronaldo",
    "Gianluigi Donnarumma",
    "Andrea Pirlo",
    "Andrea Agnelli",
]

lista_nombres_italianos.sort()
# print(lista_nombres_italianos)
lista_nombres_italianos.reverse()

nombres_franceses = [
    "Zinedine Zidane",
    "Kylian Mbappe",
]

lista_nombres_italianos.extend(nombres_franceses)
lista_nombres_italianos.insert(0, "Giorgio Chiellini")
print(lista_nombres_italianos)

indice_nombre = lista_nombres_italianos.index("Cristiano Ronaldo")
nombre = lista_nombres_italianos[indice_nombre]
lista_nombres_italianos.remove("Cristiano Ronaldo")
# del lista_nombres_italianos[indice_nombre]
lista_nombres_italianos.insert(0, nombre)
print(lista_nombres_italianos)


# print(lista_nombres_italianos)
# lista_numeros_palabras = [
#     1.2, 4.4, -.34
# ]
# lista_numeros_palabras.sort(reverse=True)
# print(lista_numeros_palabras)

# ejemplo con la función join
joined_list = "\n".join(lista_nombres_italianos)
print(joined_list)

# conjuntos
conjunto = {1, 2, 3, 4}
print(type(conjunto))

print(conjunto)

conjunto.add(5)
print(conjunto)

conjunto = {1, 2, 3, 4}
print(type(conjunto))

conjunto.add(5)
conjunto.remove(5)
conjunto.discard(555555)

conjunto_2 = {3, 4, 5, 6}
# operacion = conjunto.union(conjunto_2)
# print(operacion)
# operacion = conjunto | conjunto_2
# print(operacion)
# operacion = conjunto.intersection(conjunto_2)
# print(operacion)
# operacion = conjunto & (conjunto_2)
# print(operacion)
# operacion = conjunto.symmetric_difference(conjunto_2)
# print(operacion)
# operacion = conjunto ^ conjunto_2
# # print(operacion)
# operacion = conjunto.isdisjoint(conjunto_2)
# print(operacion)
 
base_de_datos: list[dict]  
base_de_datos = []


nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
formulario = {}
formulario["usuario"] = nombre
formulario["edad"] = edad
base_de_datos.append(formulario)
print(base_de_datos)

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
formulario = {}
formulario["usuario"] = nombre
formulario["edad"] = edad
base_de_datos.append(formulario)
print(base_de_datos)

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
domicilio = input("Ingresa tu domicilio: ")

diccionario = {
    "nombre": nombre,
    "edad": edad,
    "domicilio": domicilio,
}
print(diccionario)
mensaje = (f"FORMULARIO\n{diccionario['nombre']} tiene {diccionario['edad']} años y vive en {diccionario['domicilio']}")
print(mensaje)

