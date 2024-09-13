from db import conectar

def crear_venta(producto_id, cantidad, fecha):
    conn, cursor = conectar()
    cursor.execute('INSERT INTO ventas (producto_id, cantidad, fecha) VALUES (?, ?, ?)', (producto_id, cantidad, fecha))
    conn.commit()
    conn.close()

def leer_venta(venta_id):
    conn, cursor = conectar()
    cursor.execute('SELECT * FROM ventas WHERE id = ?', (venta_id,))
    venta = cursor.fetchone()
    conn.close()
    return venta

def actualizar_venta(venta_id, producto_id, cantidad, fecha):
    conn, cursor = conectar()
    cursor.execute('UPDATE ventas SET producto_id = ?, cantidad = ?, fecha = ? WHERE id = ?', (producto_id, cantidad, fecha, venta_id))
    conn.commit()
    conn.close()

def eliminar_venta(venta_id):
    conn, cursor = conectar()
    cursor.execute('DELETE FROM ventas WHERE id = ?', (venta_id,))
    conn.commit()
    conn.close()
