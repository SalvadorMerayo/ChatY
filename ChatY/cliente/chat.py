import socket
import threading

class ClienteChat:
    def __init__(self, callback_actualizar):
        self.callback = callback_actualizar
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", 12345))

        hilo = threading.Thread(target=self.recibir, daemon=True)
        hilo.start()

    def enviar_mensaje(self, mensaje):
        self.sock.send(mensaje.encode('utf-8'))

    def recibir(self):
        while True:
            try:
                datos = self.sock.recv(1024).decode('utf-8')
                self.callback(datos)
            except:
                break
