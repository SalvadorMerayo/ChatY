# cliente/main.py
# cd C:\Users\salva\Documents\GitHub\CHATY\Chaty
# $env:PYTHONPATH="."; python cliente/main.py
from kivy.app import App
from cliente.interfaz import InterfazChat

class ChatYApp(App):
    def build(self):
        return InterfazChat()

if __name__ == '__main__':
    ChatYApp().run()
