# cliente/main.py
# cd C:\Users\salva\Documents\GitHub\CHATY\Chaty
# $env:PYTHONPATH="."; python cliente/main.py
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from servidor.database import registrar_usuario, verificar_usuario
import hashlib

class MenuInicio(MDScreen):
    pass

class PantallaLogin(MDScreen):
    pass

class PantallaRegistro(MDScreen):
    pass

class PantallaAjustes(MDScreen):
    pass

class PantallaAyuda(MDScreen):
    pass

class PaginaInicio(MDScreen):
    pass

class ChatYApp(MDApp):
    def build(self):
        self.title = "ChatY"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("interfaz.kv")

    def registrar_usuario(self, username, email, password):
        if not username or not email or not password:
            print("Todos los campos son obligatorios.")
            return

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        exito = registrar_usuario(username, email, password_hash)

        if exito:
            print("Usuario registrado correctamente.")
            self.root.current = "login"
        else:
            print("El nombre de usuario ya está en uso.")

    def iniciar_sesion(self, username, password):
        if not username or not password:
            print("Faltan datos")
            return

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        valido = verificar_usuario(username, password_hash)

        if valido:
            print("Inicio de sesión exitoso.")
            self.root.current = "inicio"
        else:
            print("Usuario o contraseña incorrectos.")

if __name__ == '__main__':
    ChatYApp().run()
