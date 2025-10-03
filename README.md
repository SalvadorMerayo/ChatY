# ChatY - Mensajería Instantánea

Un servicio de mensajería instantánea con chat aleatorio, foros y grupos.

## Características
- Chat en tiempo real
- Salas de chat y grupos
- Foros de discusión
- Chat aleatorio anónimo (similar a Omegle)

## Instalación

### Backend
1. Crear un entorno virtual:
   ```bash
   cd server
   python -m venv venv
   venv\Scripts\activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar variables de entorno:
   ```bash
   copy .env.example .env
   ```

4. Ejecutar el servidor:
   ```bash
   python app.py
   ```

### Frontend
Abre el archivo `public/index.html` en tu navegador o usa Live Server.

## Estructura del Proyecto
```
ChatY/
├── server/              # Backend (Python/Flask)
│   ├── app.py          # Aplicación principal
│   ├── config.py       # Configuraciones
│   ├── requirements.txt
│   ├── models/         # Modelos de BD
│   ├── routes/         # Rutas/endpoints
│   ├── services/       # Lógica de negocio
│   └── database/       # Configuración de BD
├── public/             # Frontend (archivos estáticos)
│   ├── index.html
│   ├── css/
│   ├── js/
│   ├── images/         # Imágenes
│   └── assets/         # Otros recursos
├── database/           # Archivos de BD
├── uploads/            # Archivos de usuarios
├── .env.example
├── .gitignore
└── README.md
```

## Tecnologías
- **Backend**: Python, Flask, Flask-SocketIO, SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Comunicación**: WebSockets
- **Base de datos**: SQLite (desarrollo)
