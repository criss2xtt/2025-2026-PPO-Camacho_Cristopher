# Importamos la librería Tkinter
import tkinter as tk

# ------------------------------
# FUNCIONES DE LA APLICACIÓN
# ------------------------------

# Función para agregar un dato a la lista
def agregar_dato():
    dato = entrada.get()  # Obtiene el texto escrito en el campo

    # Verifica que no esté vacío
    if dato != "":
        lista.insert(tk.END, dato)  # Agrega el dato a la lista
        entrada.delete(0, tk.END)   # Limpia el campo de texto


# Función para limpiar la información
def limpiar_dato():
    entrada.delete(0, tk.END)  # Borra el texto del campo

    # También elimina el elemento seleccionado en la lista
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion)


# ------------------------------
# VENTANA PRINCIPAL
# ------------------------------

ventana = tk.Tk()
ventana.title("Gestor de Datos")
ventana.geometry("350x300")

# ------------------------------
# COMPONENTES DE LA INTERFAZ
# ------------------------------

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_dato)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()