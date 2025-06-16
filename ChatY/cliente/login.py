# cliente/login.py

import hashlib
from servidor.database import verificar_usuario

def validar_login(usuario, contraseña):
    if not usuario or not contraseña:
        return False, "Faltan datos"

    password_hash = hashlib.sha256(contraseña.encode()).hexdigest()
    valido = verificar_usuario(usuario, password_hash)

    if valido:
        return True, "Inicio de sesión exitoso"
    else:
        return False, "Usuario o contraseña incorrectos"
