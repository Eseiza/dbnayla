import sqlite3

def conectar():
    conn = sqlite3.connect('mi.db')
    return conn, conn.cursor()

def crear_tablas():
    conn, cursor = conectar()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS proveedor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        proveedor_id INTEGER,
        FOREIGN KEY (proveedor_id) REFERENCES proveedor(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto_id INTEGER,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )
    ''')

    conn.commit()
    conn.close()
