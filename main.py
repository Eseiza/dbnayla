from proveedor import crear_proveedor, leer_proveedor, actualizar_proveedor, eliminar_proveedor
from producto import crear_producto, leer_producto, actualizar_producto, eliminar_producto
from venta import crear_venta, leer_venta, actualizar_venta, eliminar_venta
from db import crear_tablas

def menu_proveedor():
    print("\n--- Menú Proveedor ---")
    print("1. Crear Proveedor")
    print("2. Leer Proveedor")
    print("3. Actualizar Proveedor")
    print("4. Eliminar Proveedor")
    print("5. Volver al Menú Principal")

def menu_producto():
    print("\n--- Menú Producto ---")
    print("1. Crear Producto")
    print("2. Leer Producto")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Volver al Menú Principal")

def menu_venta():
    print("\n--- Menú Venta ---")
    print("1. Crear Venta")
    print("2. Leer Venta")
    print("3. Actualizar Venta")
    print("4. Eliminar Venta")
    print("5. Volver al Menú Principal")

def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Proveedores")
    print("2. Productos")
    print("3. Ventas")
    print("4. Salir")

def manejar_proveedor():
    while True:
        menu_proveedor()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            nombre = input("Nombre del proveedor: ")
            telefono = input("Teléfono del proveedor: ")
            crear_proveedor(nombre, telefono)
            print("Proveedor creado con éxito.")
        elif opcion == '2':
            proveedor_id = int(input("ID del proveedor: "))
            proveedor = leer_proveedor(proveedor_id)
            print("Proveedor:", proveedor)
        elif opcion == '3':
            proveedor_id = int(input("ID del proveedor: "))
            nombre = input("Nuevo nombre del proveedor: ")
            telefono = input("Nuevo teléfono del proveedor: ")
            actualizar_proveedor(proveedor_id, nombre, telefono)
            print("Proveedor actualizado con éxito.")
        elif opcion == '4':
            proveedor_id = int(input("ID del proveedor a eliminar: "))
            eliminar_proveedor(proveedor_id)
            print("Proveedor eliminado con éxito.")
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

def manejar_producto():
    while True:
        menu_producto()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            proveedor_id = int(input("ID del proveedor: "))
            crear_producto(nombre, precio, proveedor_id)
            print("Producto creado con éxito.")
        elif opcion == '2':
            producto_id = int(input("ID del producto: "))
            producto = leer_producto(producto_id)
            print("Producto:", producto)
        elif opcion == '3':
            producto_id = int(input("ID del producto: "))
            nombre = input("Nuevo nombre del producto: ")
            precio = float(input("Nuevo precio del producto: "))
            proveedor_id = int(input("Nuevo ID del proveedor: "))
            actualizar_producto(producto_id, nombre, precio, proveedor_id)
            print("Producto actualizado con éxito.")
        elif opcion == '4':
            producto_id = int(input("ID del producto a eliminar: "))
            eliminar_producto(producto_id)
            print("Producto eliminado con éxito.")
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

def manejar_venta():
    while True:
        menu_venta()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            producto_id = int(input("ID del producto: "))
            cantidad = int(input("Cantidad vendida: "))
            fecha = input("Fecha de la venta (YYYY-MM-DD): ")
            crear_venta(producto_id, cantidad, fecha)
            print("Venta creada con éxito.")
        elif opcion == '2':
            venta_id = int(input("ID de la venta: "))
            venta = leer_venta(venta_id)
            print("Venta:", venta)
        elif opcion == '3':
            venta_id = int(input("ID de la venta: "))
            producto_id = int(input("Nuevo ID del producto: "))
            cantidad = int(input("Nueva cantidad vendida: "))
            fecha = input("Nueva fecha de la venta (YYYY-MM-DD): ")
            actualizar_venta(venta_id, producto_id, cantidad, fecha)
            print("Venta actualizada con éxito.")
        elif opcion == '4':
            venta_id
    main()