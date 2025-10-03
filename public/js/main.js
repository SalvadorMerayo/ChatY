// Conexión al WebSocket (se actualizará más adelante)
let socket;

// Elementos del DOM
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-btn');
const chatMessages = document.getElementById('chat-messages');

// Inicializar conexión WebSocket
function initWebSocket() {
    socket = new WebSocket('ws://localhost:5000/ws');
    
    socket.onopen = () => {
        console.log('Conectado al servidor');
    };
    
    socket.onmessage = (event) => {
        const message = document.createElement('div');
        message.textContent = event.data;
        message.style.padding = '0.5rem';
        message.style.marginBottom = '0.5rem';
        message.style.backgroundColor = '#e9ecef';
        message.style.borderRadius = '4px';
        chatMessages.appendChild(message);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };
    
    socket.onerror = (error) => {
        console.error('Error de WebSocket:', error);
    };
    
    socket.onclose = () => {
        console.log('Desconectado del servidor');
    };
}

// Enviar mensaje
function sendMessage() {
    const message = messageInput.value.trim();
    if (message && socket && socket.readyState === WebSocket.OPEN) {
        socket.send(message);
        messageInput.value = '';
    }
}

// Event listeners
sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    // initWebSocket(); // Descomentar cuando el backend esté listo
});
