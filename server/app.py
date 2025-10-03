from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__, static_folder='../public', static_url_path='')
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['UPLOAD_FOLDER'] = '../uploads'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return send_from_directory('../public', 'index.html')

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
