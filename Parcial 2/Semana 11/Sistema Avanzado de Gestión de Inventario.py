import os


# =========================
# CLASE PRODUCTO
# =========================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


# =========================
# CLASE INVENTARIO
# =========================
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        # Diccionario: clave = ID, valor = Producto
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def buscar_producto(self, criterio):
        encontrado = False

        # Intentar buscar por ID (si es número)
        if criterio.isdigit():
            id_producto = int(criterio)
            if id_producto in self.productos:
                print("\n🔎 Producto encontrado por ID:")
                print(self.productos[id_producto])
                encontrado = True

        # Buscar por nombre
        for producto in self.productos.values():
            if producto.get_nombre().lower() == criterio.lower():
                print("\n🔎 Producto encontrado por nombre:")
                print(producto)
                encontrado = True

        if not encontrado:
            print("❌ No se encontraron productos.")

    # =========================
    # CARGAR INVENTARIO (DESERIALIZACIÓN)
    # =========================
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                print("📁 Archivo inventario.txt creado.")
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(
                            int(id_producto),
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                        # Guardar en diccionario usando ID como clave
                        self.productos[producto.get_id()] = producto
                    except ValueError:
                        print("⚠ Línea corrupta ignorada.")

            print("✅ Inventario cargado correctamente.")

        except PermissionError:
            print("❌ No tienes permisos para leer el archivo.")
        except Exception as e:
            print("❌ Error inesperado:", e)

    # =========================
    # GUARDAR INVENTARIO (SERIALIZACIÓN)
    # =========================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(
                        f"{producto.get_id()},"
                        f"{producto.get_nombre()},"
                        f"{producto.get_cantidad()},"
                        f"{producto.get_precio()}\n"
                    )
            print("💾 Cambios guardados en archivo.")
        except PermissionError:
            print("❌ No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print("❌ Error inesperado:", e)

    # =========================
    # CRUD
    # =========================
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ Error: El ID ya existe.")
            return

        self.productos[producto.get_id()] = producto
        self.guardar_en_archivo()
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("🗑 Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]

            if cantidad is not None:
                producto.set_cantidad(cantidad)

            if precio is not None:
                producto.set_precio(precio)

            self.guardar_en_archivo()
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("📭 Inventario vacío.")
            return

        print("\n📋 Inventario:")
        for producto in self.productos.values():
            print(
                f"ID: {producto.get_id()} | "
                f"Nombre: {producto.get_nombre()} | "
                f"Cantidad: {producto.get_cantidad()} | "
                f"Precio: ${producto.get_precio():.2f}"
            )


# =========================
# MENÚ
# =========================
def menu():
    inventario = Inventario()

    print("\n📦 Productos cargados al iniciar:")
    inventario.mostrar_productos()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "2":
                id_producto = int(input("ID a eliminar: "))
                inventario.eliminar_producto(id_producto)

            elif opcion == "3":
                id_producto = int(input("ID del producto: "))
                cantidad = input("Nueva cantidad (Enter para no cambiar): ")
                precio = input("Nuevo precio (Enter para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "4":
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                criterio = input("Ingrese el ID o el nombre del producto: ")
                inventario.buscar_producto(criterio)

                if resultados:
                    for producto in resultados:
                        print(
                            f"{producto.get_id()} | "
                            f"{producto.get_nombre()} | "
                            f"{producto.get_cantidad()} | "
                            f"${producto.get_precio():.2f}"
                        )
                else:
                    print("❌ No se encontraron productos.")

            elif opcion == "5":
                inventario.mostrar_productos()

            elif opcion == "6":
                print("👋 Saliendo...")
                break

            else:
                print("❌ Opción inválida.")

        except ValueError:
            print("⚠ Error: Ingrese valores numéricos válidos.")


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    menu()