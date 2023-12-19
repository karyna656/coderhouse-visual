usuarios={}

def registro():
    user= input('Ingresa tu nombre de usuario ')

    if user in usuarios:
        print('Ese usuario ya existe')
    else:
        password= input('Ingresa tu contraseña ')
        usuarios[user]=password
        print('Usuario agregado con exito')

def login():
    user= input('Nombre de usuario ')
    password= input('Contraseña ')

    if user in usuarios and usuarios[user] == password:
        print("Inicio de sesión exitoso.")
    else:
        print("¡Error! Usuario o contraseña incorrectos.")

for _ in range(5):
    registro()
