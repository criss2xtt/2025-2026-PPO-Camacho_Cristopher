class GestorArchivo:
    """
    Clase que representa un gestor de archivos.
    Demuestra el uso del constructor (__init__) y el destructor (__del__).
    """

    def __init__(self, nombre_archivo):
        """
        CONSTRUCTOR
        Se ejecuta automáticamente cuando se crea un objeto de la clase.
        Inicializa los atributos del objeto y abre el archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "w")
        print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir texto dentro del archivo.
        """
        self.archivo.write(texto + "\n")
        print("Texto escrito en el archivo.")

    def __del__(self):
        """
        DESTRUCTOR
        Se ejecuta automáticamente cuando el objeto es eliminado
        o cuando el programa finaliza.
        Se encarga de liberar recursos (cerrar el archivo).
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

# Se crea un objeto, lo que activa el constructor (__init__)
gestor = GestorArchivo("ejemplo.txt")

# Se utilizan los métodos del objeto
gestor.escribir("Hola, este es un ejemplo de uso de constructores.")
gestor.escribir("El destructor se ejecutará al eliminar el objeto.")

# Se elimina explícitamente el objeto para activar el destructor (__del__)
del gestor

print("Programa finalizado.")
