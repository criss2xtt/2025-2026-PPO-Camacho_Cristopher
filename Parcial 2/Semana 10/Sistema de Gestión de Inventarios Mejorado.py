import os


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
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # =========================
    # CARGAR DESDE ARCHIVO
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
                        self.productos.append(producto)
                    except ValueError:
                        print("⚠ Línea corrupta ignorada.")

            print("✅ Inventario cargado correctamente.")

        except PermissionError:
            print("❌ Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print("❌ Error inesperado al cargar archivo:", e)

    # =========================
    # GUARDAR EN ARCHIVO
    # =========================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(
                        f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    )
            print("💾 Cambios guardados en archivo.")
        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print("❌ Error inesperado al guardar archivo:", e)

    # =========================
    # CRUD
    # =========================
    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("🗑️ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                self.guardar_en_archivo()
                print("🔄 Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("📭 Inventario vacío.")
            return

        print("\n📋 Inventario:")
        for p in self.productos:
            print(
                f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | "
                f"Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}"
            )


# =========================
# MENÚ PRINCIPAL
# =========================
def menu():
    inventario = Inventario()
    # Mostrar automáticamente productos cargados
    print("\n📦 Productos cargados al iniciar:")
    inventario.mostrar_productos()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
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
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)

            elif opcion == "3":
                id_producto = int(input("ID del producto: "))
                cantidad = input("Nueva cantidad (Enter para no cambiar): ")
                precio = input("Nuevo precio (Enter para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "4":
                nombre = input("Ingrese el nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)

                if resultados:
                    print("\n🔍 Resultados encontrados:")
                    for p in resultados:
                        print(
                            f"ID: {p.get_id()} | {p.get_nombre()} | "
                            f"Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}"
                        )
                else:
                    print("❌ No se encontraron productos.")

            elif opcion == "5":
                inventario.mostrar_productos()

            elif opcion == "6":
                print("👋 Saliendo del sistema...")
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
