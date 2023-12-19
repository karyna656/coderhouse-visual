class Cliente:
    def __init__(self, nombre:str, edad, sexo, dni) -> None:
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.dni=dni
    def __str__(self) -> str:
        return self.nombre
    
class Usuario(Cliente):
    def __init__(self, nombre: str, edad, sexo, dni, user, password) -> None:
        super().__init__(nombre, edad, sexo, dni)
        self.user= user
        self.password = password
        self.nombre=nombre

    def __str__(self) -> str:
        return f"Usuario= {self.user} \nContraseña= {self.password}"
    
    def saludar(self) -> None:
        print(f"Hola, {self.nombre}!")
    
    def cambiar_contraseña(self, new_pass: str) -> None:
        self.password = new_pass
 
marina= Usuario(nombre='Marina', edad= "15", sexo= "F", dni= '40563703', user= 'marina123', password= 'mari123')
print(marina)

marina.saludar()
marina.cambiar_contraseña("nueva_contraseña")
print(marina)