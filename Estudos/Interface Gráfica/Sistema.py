import mysql.connector
import tkinter as tk
from tkinter import messagebox


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="user",
        password="senha", 
        database="cadastros"
    )

def inserir_item():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    
    if not nome or not quantidade:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO itens (nome, quantidade) VALUES (%s, %s)", (nome, quantidade))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Item cadastrado com sucesso!")
        limpar_campos()
        mostrar_itens()
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao cadastrar item: {err}")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

def mostrar_itens():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM itens")
        itens = cursor.fetchall()
        conn.close()
        
        listbox_itens.delete(0, tk.END)
        for item in itens:
            listbox_itens.insert(tk.END, f"{item[1]} - Quantidade: {item[2]}")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao carregar itens: {err}")

root = tk.Tk()
root.title("Cadastro de Itens")

tk.Label(root, text="Nome do Item").grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Quantidade").grid(row=1, column=0, padx=10, pady=10)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=1, column=1, padx=10, pady=10)

btn_cadastrar = tk.Button(root, text="Cadastrar Item", command=inserir_item)
btn_cadastrar.grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="Itens Cadastrados").grid(row=3, column=0, columnspan=2, padx=10, pady=10)
listbox_itens = tk.Listbox(root, width=50, height=10)
listbox_itens.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

mostrar_itens()

root.mainloop()
