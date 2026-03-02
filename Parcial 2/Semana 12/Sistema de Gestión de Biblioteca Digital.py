# =========================
# Clase Libro
# =========================
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para almacenar título y autor (inmutables)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True  # Controla si el libro está prestado o no

    def __str__(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}, Disponible: {self.disponible}"


# =========================
# Clase Usuario
# =========================
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para gestionar libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_prestados(self):
        if not self.libros_prestados:
            return "No tiene libros prestados."
        return "\n".join([libro.info[0] for libro in self.libros_prestados])

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# =========================
# Clase Biblioteca
# =========================
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar libros por ISBN
        self.libros = {}
        # Diccionario para almacenar usuarios por ID
        self.usuarios = {}
        # Conjunto para asegurar IDs únicos
        self.ids_usuarios = set()

    # -------------------------
    # Gestión de libros
    # -------------------------
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")

    # -------------------------
    # Gestión de usuarios
    # -------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("El ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario dado de baja.")
        else:
            print("Usuario no encontrado.")

    # -------------------------
    # Préstamo y devolución
    # -------------------------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no encontrado.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro.disponible:
            libro.disponible = False
            usuario.prestar_libro(libro)
            print("Libro prestado correctamente.")
        else:
            print("El libro no está disponible.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro.disponible = True
                usuario.devolver_libro(libro)
                print("Libro devuelto correctamente.")
                return

        print("El usuario no tiene este libro prestado.")

    # -------------------------
    # Búsquedas
    # -------------------------
    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]


# =========================
# Ejecucion del sistema
# =========================

if __name__ == "__main__":
        biblioteca = Biblioteca()

        while True:
            print("\n--- SISTEMA BIBLIOTECA ---")
            print("1. Añadir libro")
            print("2. Registrar usuario")
            print("3. Prestar libro")
            print("4. Devolver libro")
            print("5. Buscar por título")
            print("6. Listar libros prestados de un usuario")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                categoria = input("Categoría: ")
                isbn = input("ISBN: ")
                libro = Libro(titulo, autor, categoria, isbn)
                biblioteca.añadir_libro(libro)

            elif opcion == "2":
                nombre = input("Nombre del usuario: ")
                id_usuario = input("ID del usuario: ")
                usuario = Usuario(nombre, id_usuario)
                biblioteca.registrar_usuario(usuario)

            elif opcion == "3":
                id_usuario = input("ID del usuario: ")
                isbn = input("ISBN del libro: ")
                biblioteca.prestar_libro(id_usuario, isbn)

            elif opcion == "4":
                id_usuario = input("ID del usuario: ")
                isbn = input("ISBN del libro: ")
                biblioteca.devolver_libro(id_usuario, isbn)

            elif opcion == "5":
                titulo = input("Título a buscar: ")
                resultados = biblioteca.buscar_por_titulo(titulo)
                for libro in resultados:
                    print(libro)

            elif opcion == "6":
               id_usuario = input("Ingrese el ID del usuario: ")
               if id_usuario in biblioteca.usuarios:
                usuario = biblioteca.usuarios[id_usuario]
                print("\nLibros prestados:")
                print(usuario.listar_prestados())
               else:
                print("Usuario no encontrado.")

            elif opcion == "7":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida")