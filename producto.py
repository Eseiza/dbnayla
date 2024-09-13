from db import conectar

def crear_producto(nombre, precio, proveedor_id):
    conn, cursor = conectar()
    cursor.execute('INSERT INTO productos (nombre, precio, proveedor_id) VALUES (?, ?, ?)', (nombre, precio, proveedor_id))
    conn.commit()
    conn.close()

def leer_producto(producto_id):
    conn, cursor = conectar()
    cursor.execute('SELECT * FROM productos WHERE id = ?', (producto_id,))
    producto = cursor.fetchone()
    conn.close()
    return producto

def actualizar_producto(producto_id, nombre, precio, proveedor_id):
    conn, cursor = conectar()
    cursor.execute('UPDATE productos SET nombre = ?, precio = ?, proveedor_id = ? WHERE id = ?', (nombre, precio, proveedor_id, producto_id))
    conn.commit()
    conn.close()

def eliminar_producto(producto_id):
    conn, cursor = conectar()
    cursor.execute('DELETE FROM productos WHERE id = ?', (producto_id,))
    conn.commit()
    conn.close()
