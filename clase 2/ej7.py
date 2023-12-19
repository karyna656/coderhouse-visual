# class Auto:
    # """Documentación de la clase"""

    # def __init__(self , marca: str, modelo: str) -> None:  # método constructor
        # print("Hola estás creando un objeto")
        
        # self.marca = marca  # variable o atributo de instancia self.modelo = modelo  # variable o atributo de instancia
        # self.tocar_bocina()

    #   def tocar_bocina(self):  # método de instancia
        # print(f"🚘 {self.marca} {self.modelo} está tocando bocina...")


# mi_auto = Auto(marca="Chevrolet", modelo="Camaro")  #  mi_auto es un objeto o instancia de Auto
# mi_auto2 = Auto(marca="Chevrolet", modelo="Cruze")  #  mi_auto2 es un objeto o instancia de Auto

# print(mi_auto.la_marca, mi_auto.el_modelo)
# print(mi_auto2.la_marca, mi_auto2.el_modelo)
# mi_auto.tocar_bocina()
# mi_auto2.tocar_bocina()  


class Alumno:
    escuela = "Mi Escuelita"
    
    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self.nota = nota

    def imprimir(self) -> None:
        print(f"El alumno {self.nombre} obtuvo la nota {self.nota}")
        
    def resultado(self) -> str:
        if self.nota >= 7:
            return "aprobado"
        else:
            return "desaprobado"
        
    alumno_1 = Alumno(nombre="Agustina", nota=10)
    alumno_2 = Alumno("Juana", 4)
    
    alumno_1. imprimir()
    resultado = alumno_1.resultado()
    print(resultado)
    
    alumno_2. imprimir()
    resultado = alumno_2.resultado()
    print(resultado)
    
   
