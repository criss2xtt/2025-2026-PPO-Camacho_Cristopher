import tkinter as tk

# Lista para guardar las tareas (texto + estado)
tareas = []

# Función para añadir tarea
def añadir_tarea(event=None):
    texto = entrada.get().strip()
    if texto != "":
        tareas.append({"texto": texto, "completada": False})
        actualizar_lista()
        entrada.delete(0, tk.END)

# Función para actualizar la lista visual
def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in tareas:
        if tarea["completada"]:
            lista.insert(tk.END, "✔ " + tarea["texto"])
        else:
            lista.insert(tk.END, tarea["texto"])

# Función para marcar como completada
def marcar_completada():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = True
        actualizar_lista()

# Función para eliminar tarea
def eliminar_tarea():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas.pop(index)
        actualizar_lista()

# Evento opcional: doble clic para completar
def doble_click(event):
    marcar_completada()

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Evento Enter
entrada.bind("<Return>", añadir_tarea)

# Lista de tareas
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Doble clic
lista.bind("<Double-Button-1>", doble_click)

# Botones
btn_añadir = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Ejecutar app
ventana.mainloop()