import os

def menu_principal():
    while True:
        print("\nMenú de Gestión de Productos")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Ver lista de productos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            ver_productos()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    with open("productos.txt", "a") as file:
        file.write(producto + "\n")
    print("Producto agregado exitosamente.")

def eliminar_producto():
    producto = input("Ingrese el nombre del producto a eliminar: ")
    if not os.path.exists("productos.txt"):
        print("No hay productos registrados.")
        return
    
    with open("productos.txt", "r") as file:
        productos = file.readlines()
    
    with open("productos.txt", "w") as file:
        encontrado = False
        for prod in productos:
            if prod.strip() != producto:
                file.write(prod)
            else:
                encontrado = True
    
    if encontrado:
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")

def ver_productos():
    if not os.path.exists("productos.txt"):
        print("No hay productos registrados.")
        return
    
    with open("productos.txt", "r") as file:
        productos = file.readlines()
    
    if productos:
        print("\nLista de Productos:")
        for producto in productos:
            print(f"- {producto.strip()}")
    else:
        print("No hay productos registrados.")
