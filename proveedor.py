from db import conectar

def crear_proveedor(nombre, telefono):
    conn, cursor = conectar()
    cursor.execute('INSERT INTO proveedor (nombre, telefono) VALUES (?, ?)', (nombre, telefono))
    conn.commit()
    conn.close()

def leer_proveedor(proveedor_id):
    conn, cursor = conectar()
    cursor.execute('SELECT * FROM proveedor WHERE id = ?', (proveedor_id,))
    proveedor = cursor.fetchone()
    conn.close()
    return proveedor

def actualizar_proveedor(proveedor_id, nombre, telefono):
    conn, cursor = conectar()
    cursor.execute('UPDATE proveedor SET nombre = ?, telefono = ? WHERE id = ?', (nombre, telefono, proveedor_id))
    conn.commit()
    conn.close()

def eliminar_proveedor(proveedor_id):
    conn, cursor = conectar()
    cursor.execute('DELETE FROM proveedor WHERE id = ?', (proveedor_id,))
    conn.commit()
    conn.close()
