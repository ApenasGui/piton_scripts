import tkinter as tk
from tkinter import messagebox

contador = 0
garrafitas = 0
multiplicador = 10 + garrafitas

def somarUm():
    global contador
    contador += 1
    label_contador.config(text = str(contador))

def garrafaAgua():
    global contador
    contador += garrafitas
    label_contador.config(text=str(contador))
    janela.after(1000, garrafaAgua)

def comprar_garrafa():
    global contador, garrafitas
    if contador >= multiplicador:
        contador -= multiplicador
        garrafitas += 1
        label_garrafas.config(text=str(garrafitas))
        label_garrafas.config(f"Melhorias = {garrafitas}")
    else:
        messagebox.showerror(f"Goles insuficiente", f"Você precisa de pelo menos {multiplicador} goles!!")
    

janela = tk.Tk()
janela.title("Testes")
janela.geometry("800x400")

label_contador = tk.Label(janela, text=str(contador), font=("Arial", 24))
label_contador.pack(pady=10)

botao_somar = tk.Button(janela, text="Ganhe 1 gole d'água", command=somarUm)
botao_somar.pack(pady=20)

botao_comprarGarrafa = tk.Button(janela, text=f'Comprar garrafa por {multiplicador} goles', command=comprar_garrafa)
botao_comprarGarrafa.pack(pady=10)

label_garrafas = tk.Label(janela, text=str(garrafitas), font=("Arial", 16))
label_garrafas.pack(pady=5)

janela.after(1000, garrafaAgua)

janela.mainloop()