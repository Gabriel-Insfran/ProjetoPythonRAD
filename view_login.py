import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
from os import system

#_____Conecta ao banco de dados SQLite_____
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

#_____Cria a tabela de usuários se ela não existir_____
cursor.execute('''
CREATE TABLE IF NOT EXISTS bancodeusuarios (
    nomedeusuario TEXT PRIMARY KEY,
    senha TEXT NOT NULL);
''')

#_____Funções da tela de login/cadastro_____

#_____Cadastra email e senha no banco_____
def register():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute('SELECT * FROM bancodeusuarios WHERE nomedeusuario = ?', (username,))

    #_____regex de regra na criação do email_____
    if not re.match(r'\b[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,7}\b', username):
        messagebox.showinfo("Erro!", "Necessário ser um email válido!")
        return

    if cursor.fetchone() is not None:
        messagebox.showinfo("Erro", "Nome de usuário já existe")
    else:
        cursor.execute('INSERT INTO bancodeusuarios VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

#_____Permitir fazer login____
def login():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute('SELECT * FROM bancodeusuarios WHERE nomedeusuario = ? AND senha = ?', (username, password))
    if cursor.fetchone() is not None:
        janeladelogin.destroy()
        system('view_manager.py')

    else:
        messagebox.showinfo("Erro", "Nome de usuário ou senha incorretos")

#_____Janela da tela de login_____
janeladelogin = tk.Tk()
janeladelogin.title('Cadastro de Jogos')
width = 250
height = 250
#_____coletando informacoes do monitor_____
sc_width = janeladelogin.winfo_screenwidth()
sc_height = janeladelogin.winfo_screenheight()
x = (sc_width / 2) - (width / 2)
y = (sc_height / 2) - (height / 2)
#_____tamanho da janela principal_____
janeladelogin.geometry("%dx%d+%d+%d" % (width, height, x, y))
janeladelogin.resizable(0, 0)

#____Labels de cadastro/login_____

label_username = tk.Label(janeladelogin, text="Endereço de e-mail:")
label_username.pack()

entry_username = tk.Entry(janeladelogin)
entry_username.pack(padx=10, pady=10)

label_password = tk.Label(janeladelogin, text="Senha:")
label_password.pack()

entry_password = tk.Entry(janeladelogin, show="*")
entry_password.pack(padx=10, pady=10)

#_____Botões Cadastrar e Entrar_____
button_register = tk.Button(janeladelogin, text="Cadastrar", command=register)
button_register.pack(padx=30, pady=30)

button_login = tk.Button(janeladelogin, text="Entrar", command=login)
button_login.pack()

if __name__ == '__main__':
    janeladelogin.mainloop()