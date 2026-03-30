import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista de tareas (texto, estado)
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Enter

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Botones
        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="Añadir", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Completar", command=self.complete_task).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Eliminar", command=self.delete_task).grid(row=0, column=2, padx=5)

        # Atajos de teclado
        self.root.bind("c", self.complete_task)
        self.root.bind("d", self.delete_task)
        self.root.bind("<Delete>", self.delete_task)
        self.root.bind("<Escape>", lambda e: self.root.quit())

    def add_task(self, event=None):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append((task_text, False))  # False = pendiente
            self.update_list()
            self.entry.delete(0, tk.END)

    def complete_task(self, event=None):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            text, status = self.tasks[index]
            self.tasks[index] = (text, True)  # True = completada
            self.update_list()

    def delete_task(self, event=None):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for i, (task, completed) in enumerate(self.tasks):
            if completed:
                self.listbox.insert(tk.END, f"✔ {task}")
                self.listbox.itemconfig(i, fg="gray")
            else:
                self.listbox.insert(tk.END, f"✘ {task}")
                self.listbox.itemconfig(i, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()