# cliente/main.py
# cd C:\Users\salva\Documents\GitHub\CHATY\Chaty
# $env:PYTHONPATH="."; python cliente/main.py
from kivymd.app import MDApp
from kivy.lang import Builder

class ChatYApp(MDApp):
    def build(self):
        self.title = "ChatY"
        return Builder.load_file("interfaz.kv")

if __name__ == '__main__':
    ChatYApp().run()
