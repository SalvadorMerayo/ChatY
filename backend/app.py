from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Backend de ChatY funcionando"

@socketio.on('message')
def handle_message(message):
    print('Mensaje recibido:', message)
    emit('message', message, broadcast=True)

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
