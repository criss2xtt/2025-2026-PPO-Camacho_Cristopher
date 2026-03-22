import tkinter as tk
from tkinter import ttk, messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # ===== Frame para la lista =====
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripcion"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripcion", text="Descripción")

        self.tree.pack()

        # ===== Frame para entradas =====
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        # Fecha (manual)
        tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = tk.Entry(frame_entrada)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        # Descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # ===== Frame para botones =====
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=10)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=10)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        """Agrega un evento a la lista"""
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos")
            return

        # Validación básica
        if len(fecha) != 10 or "-" not in fecha:
            messagebox.showerror("Error", "Formato de fecha inválido. Usa YYYY-MM-DD")
            return

        if ":" not in hora:
            messagebox.showerror("Error", "Formato de hora inválido. Usa HH:MM")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina el evento seleccionado"""
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("Selección vacía", "Selecciona un evento para eliminar")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Deseas eliminar este evento?")
        if confirm:
            for item in selected:
                self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

