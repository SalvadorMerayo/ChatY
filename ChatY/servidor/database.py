import sqlite3
from datetime import datetime

# Crea la base de datos y la tabla si no existen
def crear_base():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT,
        password TEXT NOT NULL,
        fecha_reg TEXT
    )
    """)
    conn.commit()
    conn.close()

# Inserta un usuario nuevo
def registrar_usuario(username, email, password_hash):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d")
    try:
        cursor.execute("INSERT INTO usuarios (username, email, password, fecha_reg) VALUES (?, ?, ?, ?)",
                       (username, email, password_hash, fecha))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Usuario ya existente
    finally:
        conn.close()

if __name__ == "__main__":
    crear_base()
    print("Base de datos creada (o ya existente).")
