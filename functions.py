import os
import json
import logging

# Configuración de logs
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

INVENTARIO_FILE = "productos.json"

# Función para cargar productos desde el archivo JSON
def cargar_productos():
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):  # Verifica si el JSON es una lista
                    raise ValueError("Formato incorrecto de productos.json")
                return data
            except (json.JSONDecodeError, ValueError):
                logging.error("Error al cargar productos.json. Archivo vacío o corrupto.")
                return []  # Retorna una lista vacía en caso de error
    return []


# Función para guardar productos en el archivo JSON
def guardar_productos(productos):
    with open(INVENTARIO_FILE, "w") as file:
        json.dump(productos, file, indent=4)

def menu_principal():
    while True:
        print("\nMenú de Gestión de Productos")
        print("1. Agregar producto")
        print("2. Consultar inventario de productos")
        print("3. Buscar y filtrar productos") 
        print("4. Gestionar stock")
        print("5. Eliminar producto")
        print("6. Generar reporte de inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            buscar_filtrar_productos()
        elif opcion == "4":
            actualizar_stock()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            generar_reporte()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = input("Ingrese la stock disponible: ")
    precio = input("Ingrese el precio unitario: ")
    categoria = input("Ingrese la categoría del producto: ")

    try:
        cantidad = int(cantidad)
        precio = int(precio)
    except ValueError:
        print("Error: La cantidad y el precio deben ser un número entero.")
        return

    productos = cargar_productos()
    productos.append({
        "nombre": nombre,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "precio": precio,
        "categoria": categoria
    })

    guardar_productos(productos)
    logging.info("Producto agregado: %s", nombre)
    print("Producto agregado exitosamente.")

def ver_productos():
    productos = cargar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    print("\nLista de Productos:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - {producto['descripcion']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']} | Categoría: {producto['categoria']}")

def actualizar_stock():
    productos = cargar_productos()
    if not productos:
        print("No hay productos para actualizar.")
        return

    ver_productos()
    try:
        index = int(input("Ingrese el número del producto a actualizar: ")) - 1
        if index < 0 or index >= len(productos):
            print("Número de producto inválido.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    print("Ingrese el nuevo stock (deje vacío para no modificar):")
    nueva_cantidad = input(f"Cantidad actual ({productos[index]['cantidad']}): ") or productos[index]['cantidad']

    try:
        nueva_cantidad = int(nueva_cantidad)
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        return

    productos[index]["cantidad"] = nueva_cantidad

    guardar_productos(productos)
    logging.info("Stock actualizado: %s - Nueva cantidad: %d", productos[index]["nombre"], nueva_cantidad)
    print(f"Stock de '{productos[index]['nombre']}' actualizado a {nueva_cantidad}.")


def eliminar_producto():
    productos = cargar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    ver_productos()
    try:
        index = int(input("Ingrese el número del producto a eliminar: ")) - 1
        if index < 0 or index >= len(productos):
            print("Número de producto inválido.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    producto_eliminado = productos.pop(index)
    guardar_productos(productos)
    logging.info("Producto eliminado: %s", producto_eliminado["nombre"])
    print(f"Producto '{producto_eliminado['nombre']}' eliminado correctamente.")

def buscar_filtrar_productos():
    productos = cargar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- Búsqueda y Filtro de Productos ---")
    nombre_busqueda = input("Ingrese nombre (o parte del nombre) del producto a buscar [Enter para omitir]: ").strip().lower()
    categoria_filtro = input("Ingrese categoría para filtrar [Enter para omitir]: ").strip().lower()
    
    try:
        precio_min = input("Ingrese precio mínimo [Enter para omitir]: ")
        precio_max = input("Ingrese precio máximo [Enter para omitir]: ")

        precio_min = int(precio_min) if precio_min else None
        precio_max = int(precio_max) if precio_max else None
    except ValueError:
        print("Error: El precio debe ser un número válido.")
        return

    # Generar versiones singulares/plurales de la categoría ingresada
    categoria_filtro_alt = categoria_filtro
    if categoria_filtro.endswith("s"):
        categoria_filtro_alt = categoria_filtro[:-1]  # Elimina la "s" final
    else:
        categoria_filtro_alt = categoria_filtro + "s"  # Agrega una "s" al final

    resultados = []
    for producto in productos:
        nombre = producto["nombre"].lower()
        categoria = producto["categoria"].lower()
        precio = producto["precio"]

        # Condiciones de búsqueda y filtrado
        coincide_nombre = nombre_busqueda in nombre if nombre_busqueda else True
        coincide_categoria = (categoria == categoria_filtro or categoria == categoria_filtro_alt) if categoria_filtro else True
        cumple_precio = (precio_min is None or precio >= precio_min) and (precio_max is None or precio <= precio_max)

        if coincide_nombre and coincide_categoria and cumple_precio:
            resultados.append(producto)

    if resultados:
        print("\n🔎 Productos encontrados:")
        for i, producto in enumerate(resultados, start=1):
            print(f"{i}. {producto['nombre']} - {producto['descripcion']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']} | Categoría: {producto['categoria']}")
    else:
        print("❌ No se encontraron productos con los filtros aplicados.")

def generar_reporte():
    productos = cargar_productos()
    
    if not productos:
        print("No hay productos en el inventario para generar un reporte.")
        return
    
    total_productos = sum(producto["cantidad"] for producto in productos)
    valor_total_inventario = sum(producto["cantidad"] * producto["precio"] for producto in productos)
    productos_agotados = [producto["nombre"] for producto in productos if producto["cantidad"] == 0]
    
    with open("reporte_inventario.txt", "w") as file:
        file.write("===== REPORTE DE INVENTARIO =====\n")
        file.write(f"Total de productos en inventario: {total_productos}\n")
        file.write(f"Valor total del inventario: ${valor_total_inventario}\n")
        file.write("\nProductos agotados:\n")
        
        if productos_agotados:
            for producto in productos_agotados:
                file.write(f"- {producto}\n")
        else:
            file.write("No hay productos agotados.\n")
    
    logging.info("Reporte de inventario generado correctamente.")
    print("📄 Reporte de inventario generado: 'reporte_inventario.txt'.")
