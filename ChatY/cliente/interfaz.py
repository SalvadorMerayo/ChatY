from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from cliente.chat import ClienteChat

class InterfazChat(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.mensajes = Label(size_hint_y=8)
        self.add_widget(self.mensajes)

        self.entrada = TextInput(size_hint_y=1, multiline=False)
        self.add_widget(self.entrada)

        boton = Button(text="Enviar", size_hint_y=1)
        boton.bind(on_press=self.enviar)
        self.add_widget(boton)

        self.cliente = ClienteChat(self.actualizar_mensajes)

    def enviar(self, _):
        texto = self.entrada.text
        self.cliente.enviar_mensaje(texto)
        self.entrada.text = ''
        self.actualizar_mensajes(texto)

    def actualizar_mensajes(self, texto):
        self.mensajes.text += texto + '\n'
