import socket
import threading

clientes = []

def reenviar_a_todos(mensaje, cliente_actual):
    for cliente in clientes:
        if cliente != cliente_actual:
            try:
                cliente.send(mensaje)
            except:
                clientes.remove(cliente)

def manejar_cliente(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            reenviar_a_todos(mensaje, cliente)
        except:
            clientes.remove(cliente)
            cliente.close()
            break

def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen()
    print("Servidor iniciado en puerto 12345...")

    while True:
        cliente, _ = server.accept()
        clientes.append(cliente)
        threading.Thread(target=manejar_cliente, args=(cliente,), daemon=True).start()

if __name__ == "__main__":
    iniciar_servidor()
