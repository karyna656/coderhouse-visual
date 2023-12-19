# # Crea una clase llamada "Perro" que represente a un perro. 
# La clase debe tener los siguientes atributos: "nombre" y "edad". 
# Además, debe tener los siguientes métodos:
# "ladrar": imprime un mensaje que simula el ladrido del perro.
# "presentarse": imprime un mensaje que muestra el nombre y la edad del perro.
# Escribe el código de la clase "Perro" y crea dos instancias de la misma. 
# Luego, utiliza los métodos para que los perros ladren y se presenten.
# ""
class Perro:
    def __init__(self, nombre, edad=0) -> None:
        self.nombre = nombre
        self.edad = edad
   
    def ladrar(self):
        print(f"{self.nombre} está ladrando: ¡guau!")

    def presentarse(self):
        print(f"¡Hola! Soy {self.nombre} y tengo {self.edad} años")


perro1 = Perro("Max", 3)
perro2 = Perro("Luna", 5)

# print(perro1.__dict__)
# print(perro2.__dict__)
perro1.presentarse()
perro1.ladrar()
perro2.presentarse()
perro2.ladrar()
