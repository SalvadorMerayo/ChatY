# cliente/interfaz.py
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MenuInicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
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

class PantallaLogin(Screen):
    pass

class PantallaRegistro(Screen):
    pass

class PantallaAjustes(Screen):
    pass

class PantallaAyuda(Screen):
    pass

class InterfazChat(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MenuInicio(name='menu'))
        self.add_widget(PantallaLogin(name='login'))
        self.add_widget(PantallaRegistro(name='registro'))
        self.add_widget(PantallaAjustes(name='ajustes'))
        self.add_widget(PantallaAyuda(name='ayuda'))
