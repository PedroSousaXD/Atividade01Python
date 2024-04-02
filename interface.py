import tkinter as tk

def toggle_show_password():
    if show_password.get():
        for entry in entries:
            if entry.label == "Senha:":
                entry.config(show="")
    else:
        for entry in entries:
            if entry.label == "Senha:":
                entry.config(show="*")

root = tk.Tk()
root.title("Informe os dados")
root.configure(bg="black")

# Primeiro container
container1 = tk.Frame(root, bg="black", pady=20, padx=20)
container1.pack(fill=tk.X, padx=(100, 0))

label_id_usuarios = tk.Label(container1, text="idUsuarios:", bg="black", fg="white", padx=5)
label_id_usuarios.pack(side=tk.LEFT)

entry_id_usuarios = tk.Entry(container1, bg="gray", fg="white", width=14)
entry_id_usuarios.pack(side=tk.LEFT, padx=10)

button_buscar = tk.Button(container1, text="Buscar", width=10)
button_buscar.pack(side=tk.LEFT)

# Segundo container
container2 = tk.Frame(root, bg="black", pady=10, padx=10)
container2.pack(fill=tk.BOTH, expand=True, padx=(100, 0))

labels = ["Nome:", "Telefone:", "E-mail:", "Usuário:", "Senha:"]
entries = []

for label_text in labels:
    entry_frame = tk.Frame(container2, bg="black")
    entry_frame.pack(fill=tk.X, pady=5)

    label = tk.Label(entry_frame, text=label_text, bg="black", fg="white", width=10)
    label.pack(side=tk.LEFT, padx=5)

    entry = tk.Entry(entry_frame, bg="gray", fg="white", width=30)  # Ajustando o tamanho da entrada
    if label_text == "Senha:":
        entry.config(show="*")
    entry.pack(side=tk.LEFT, fill=tk.X, expand=False)

    entry.label = label_text
    entries.append(entry)

# Terceiro container
container3 = tk.Frame(root, bg="black", pady=20, padx=20)
container3.pack(fill=tk.X)

show_password = tk.BooleanVar()
show_password.set(False)

button_show_password = tk.Checkbutton(container3, text="Mostrar Senha", variable=show_password, command=toggle_show_password, bg="black", fg="white")
button_show_password.pack()

# Adicionando espaço antes dos outros botões
tk.Label(container3, text="", bg="black").pack()

button_inserir = tk.Button(container3, text="Inserir", width=20)
button_inserir.pack(side=tk.LEFT)

button_alterar = tk.Button(container3, text="Alterar", width=20)
button_alterar.pack(side=tk.LEFT, padx=10)

button_excluir = tk.Button(container3, text="Excluir", width=20)
button_excluir.pack(side=tk.LEFT)

root.mainloop()
