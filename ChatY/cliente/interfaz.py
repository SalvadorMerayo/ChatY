from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Menú principal con navegación
class MenuInicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(Button(text="Iniciar sesión", on_press=self.ir_a_login))
        layout.add_widget(Button(text="Registrarse", on_press=self.ir_a_registro))
        layout.add_widget(Button(text="Ajustes", on_press=self.ir_a_ajustes))
        layout.add_widget(Button(text="Ayuda", on_press=self.ir_a_ayuda))
        self.add_widget(layout)

    def ir_a_login(self, instance):
        self.manager.current = 'login'

    def ir_a_registro(self, instance):
        self.manager.current = 'registro'

    def ir_a_ajustes(self, instance):
        self.manager.current = 'ajustes'

    def ir_a_ayuda(self, instance):
        self.manager.current = 'ayuda'


# Pantalla de inicio de sesión
class PantallaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(Label(text="Usuario"))
        layout.add_widget(TextInput(multiline=False))
        layout.add_widget(Label(text="Contraseña"))
        layout.add_widget(TextInput(password=True, multiline=False))
        layout.add_widget(Button(text="Iniciar sesión"))
        self.add_widget(layout)


# Pantalla de registro
class PantallaRegistro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(Label(text="Nombre de usuario"))
        layout.add_widget(TextInput(multiline=False))
        layout.add_widget(Label(text="Correo electrónico"))
        layout.add_widget(TextInput(multiline=False))
        layout.add_widget(Label(text="Contraseña"))
        layout.add_widget(TextInput(password=True, multiline=False))
        layout.add_widget(Button(text="Registrarse"))
        self.add_widget(layout)


# Pantalla de ajustes
class PantallaAjustes(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(Label(text="Ajustes de la aplicación"))
        layout.add_widget(Button(text="Volver"))
        self.add_widget(layout)


# Pantalla de ayuda
class PantallaAyuda(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(Label(text="¿Necesitás ayuda? Contactanos en soporte@chaty.com"))
        layout.add_widget(Button(text="Volver"))
        self.add_widget(layout)


# Gestor de pantallas
class InterfazChat(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MenuInicio(name='menu'))
        self.add_widget(PantallaLogin(name='login'))
        self.add_widget(PantallaRegistro(name='registro'))
        self.add_widget(PantallaAjustes(name='ajustes'))
        self.add_widget(PantallaAyuda(name='ayuda'))
