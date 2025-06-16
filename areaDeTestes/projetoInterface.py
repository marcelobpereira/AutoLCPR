import tkinter as tk
from tkinter import ttk
from selenium import webdriver
import time
import pickle

#Função para chamar o Selenium e importar dados
def importar_dados():
    print("Importando dados")
    driver = webdriver.Chrome()
    driver.get("https://eservicos.sefaz.ms.gov.br/")
    # Aguarde o login manual ou automatize o preenchimento
    time.sleep(60)  # tempo para você logar manualmente
    #Capture os cookies
    with open("cookies.pkl", "wb") as f:
	    pickle.dump(driver.get_cookies(), f)
    #Anexe
    driver = webdriver.Chrome()
    driver.get("https://eservicos.sefaz.ms.gov.br/")
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()
    print("sucesso no login")
# Função para mudar o conteúdo principal
def mostrar_conteudo(nome):
    if(nome=="Importar"):
         importar_dados()
    else:
        area_conteudo.config(text=f"Você selecionou: {nome}")

# Janela principal
app = tk.Tk()
app.title("AutoLCPR")
app.geometry("800x500")
app.configure(bg="#f0f0f0")

# Cabeçalho
header = tk.Label(app, text="AutoLCPR", bg="#004d4d", fg="white", font=("Helvetica", 18, "bold"), pady=10)
header.pack(fill="x")

# Área principal
frame_principal = tk.Frame(app, bg="#f0f0f0")
frame_principal.pack(fill="both", expand=True)

# Menu lateral
menu_lateral = tk.Frame(frame_principal, width=200, bg="#e0e0e0")
menu_lateral.pack(side="left", fill="y")

botoes = ["Importar", "Receitas", "Despesas", "Rebanho", "Relatórios", "Produtor"]
for nome in botoes:
    tk.Button(menu_lateral, text=nome, width=20, pady=8, bg="#c0c0c0", command=lambda n=nome: mostrar_conteudo(n)).pack(pady=5)

# Área de conteúdo
frame_conteudo = tk.Frame(frame_principal, bg="white")
frame_conteudo.pack(side="right", fill="both", expand=True)

# Campo para nome do produtor
label_nome = tk.Label(frame_conteudo, text="Nome do Produtor:", font=("Helvetica", 12), bg="white")
label_nome.pack(anchor="nw", padx=20, pady=(20, 5))

entrada_nome = tk.Entry(frame_conteudo, width=40, font=("Helvetica", 12))
entrada_nome.pack(anchor="nw", padx=20)

# Espaço onde o conteúdo mudará
area_conteudo = tk.Label(frame_conteudo, text="", bg="white", font=("Helvetica", 12), anchor="nw", justify="left")
area_conteudo.pack(fill="both", expand=True, padx=20, pady=20)

app.mainloop()