from servidor.database import registrar_usuario
import hashlib

# Simulación de inputs del usuario
username = "salva17"
email = "salva@mail.com"
password = "contraseña123"

# Hasheamos la contraseña
password_hash = hashlib.sha256(password.encode()).hexdigest()

# Registramos
exito = registrar_usuario(username, email, password_hash)

if exito:
    print("Usuario registrado correctamente.")
else:
    print("Ese usuario ya existe.")
