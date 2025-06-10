import tkinter as tk

def create_interface():
    root = tk.Tk()
    root.title("AutoLCPR")

    # Cabeçalho
    header_frame = tk.Frame(root)
    header_frame.pack(fill=tk.X)
    producer_name_label = tk.Label(header_frame, text="Nome do Produtor", font=("Arial", 16)) #Centralizar
    producer_name_label.pack(side=tk.RIGHT, padx=10)

    # Menu lateral
    sidebar_frame = tk.Frame(root)
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
    buttons = ["Importar", "Receitas", "Despesas", "Rebanho", "Relatórios", "Produtor"]
    for button_text in buttons:
        button = tk.Button(sidebar_frame, text=button_text, font=("Arial", 12))
        button.pack(fill=tk.X, pady=5)

    # Área de conteúdo principal
    content_frame = tk.Frame(root)
    content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    root.mainloop()

create_interface()