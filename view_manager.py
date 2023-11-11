# _____Bibliotecas_____
import tkinter as tk
from tkinter import *
from tkinter import ttk, StringVar
import sqlite3 as sql
import tkinter.messagebox as msb
from banco import connect

#_____Funções do Gerenciador_____
id = None

#_____Insere no banco e adiciona na treeview_____
def cadastrando():
    if nome.get() == "" or status.get() == "" or genero.get() == "" or plataforma.get() == "" or nota.get() == "":
        msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sql.connect('jogos.db')
        cursor = conn.cursor()
        query="""INSERT INTO jogos (nome, status, genero, plataforma, nota) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), str(status.get()), str(genero.get()), str(plataforma.get()), str(nota.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'jogos' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        status.set("")
        genero.set("")
        plataforma.set("")
        nota.set("")

#_____Seleciona um item na tree view, para sua manipulação_____
def select(event):
    global id
    item = tree.focus()
    conteudo = (tree.item(item))
    item_selecionado = conteudo['values']
    id = item_selecionado[0]
    nome.set("")
    status.set("")
    genero.set("")
    plataforma.set("")
    nota.set("")
    nome.set(item_selecionado[1])
    status.set(item_selecionado[2])
    genero.set(item_selecionado[3])
    plataforma.set(item_selecionado[4])
    nota.set(item_selecionado[5])


#_____Deleta um cadastro da tree view e do banco_____
def delete():
    if not tree.selection():
        msb.showwarning('ALERTA DE ERRO', 'Por favor, selecione o item na lista.', icon='warning')
    else:
        resultado = msb.askquestion('', 'Tem certeza que deseja deletar o contato?')
        if resultado == 'yes':
            item = tree.focus()
            conteudo = (tree.item(item))
            item_selecionado = conteudo['values']
            tree.delete(item)
            conn = sql.connect("jogos.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM jogos WHERE id=?", (id,))
            conn.commit()
            cur.close()
            conn.close()


#_____Atualiza registro no banco e depois o adiciona na tree view_____

def update():
    if nome.get() == "" or status.get() == "" or genero.get() == "" or plataforma.get() == "" or nota.get() == "":
        msb.showwarning("", "Por favor, clique duas vezes na linha desejada.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sql.connect("jogos.db")
        cursor = conn.cursor()
        cursor.execute(""" UPDATE 'jogos' SET nome = ?, status = ?, genero = ?, plataforma = ?, nota = ? WHERE id = ?""",
                    (str(nome.get()), str(status.get()), str(genero.get()), str(plataforma.get()), str(nota.get()),
                        int(id)))
        conn.commit()
        cursor.execute("SELECT * FROM 'jogos' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        status.set("")
        genero.set("")
        plataforma.set("")
        nota.set("")


#_____Configurações da janela_____
janela = tk.Tk()
janela.title('Gerenciador de Tarefas')
width = 920
height = 500
#_____Coletando informações do monitor_____
sc_width = janela.winfo_screenwidth()
sc_height = janela.winfo_screenheight()
x = (sc_width / 2) - (width / 2)
y = (sc_height / 2) - (height / 2)
# tamanho da janela principal
janela.geometry("%dx%d+%d+%d" % (width, height, x, y))
janela.resizable(0, 0)

#_____Frame esquerdo_____
frame_esquerdo = Frame(janela, width=300, height=500, bg='#171616', relief='groove')
frame_esquerdo.grid(row=0, column=0)
# Frame direito:
frame_direito = Frame(janela, width=620, height=500, relief='groove')
frame_direito.grid(row=0, column=1)

#_____Label de cadastro e entrys_____
nome = StringVar()
l_nome = Label(frame_esquerdo, text='Nome:', bg='#171616', fg='white')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_esquerdo, textvariable=nome, width=30, bg='white', fg='grey')
e_nome.place(x=10, y=40)

status = StringVar()
list_status = ['FINALIZADO', 'EM ANDAMENTO', 'NÃO INICIADO']
l_status = Label(frame_esquerdo, text='Status:', bg='#171616', fg='white')
l_status.place(x=10, y=70)
c_status = ttk.Combobox(frame_esquerdo, textvariable=status, values=list_status, width=27)
c_status.place(x=10, y=100)

genero = StringVar()
l_genero = Label(frame_esquerdo, text='Gênero:', bg='#171616', fg='white')
l_genero.place(x=10, y=125)
e_genero = Entry(frame_esquerdo, textvariable=genero, width=30, bg='white', fg='grey')
e_genero.place(x=10, y=150)

plataforma = StringVar()
l_plataforma = Label(frame_esquerdo, text='Plataforma:', bg='#171616', fg='white')
l_plataforma.place(x=10, y=175)
e_plataforma = Entry(frame_esquerdo, textvariable=plataforma, width=30, bg='white', fg='grey')
e_plataforma.place(x=10, y=200)

nota = StringVar()
list_notas = ['1.0', '2.0', '3.0', '4.0', '5.0']
l_nota = Label(frame_esquerdo, text='Nota:', bg='#171616', fg='white')
l_nota.place(x=10, y=225)
c_nota = ttk.Combobox(frame_esquerdo, textvariable=nota, values=list_notas, width=27)
c_nota.place(x=10, y=250)

#____Botões de inserir, atualizar e deletar_____
b_salvar = Button(frame_esquerdo, width=10, height=1, text='Salvar', relief='groove', fg='white', bg='blue', command=cadastrando)
b_salvar.place(x=10, y=340)

b_atualizar = Button(frame_esquerdo, width=12, height=1, text='Atualizar', relief='groove', fg='white',bg='#ffb005', command=update)
b_atualizar.place(x=100, y=340)

b_excluir = Button(frame_esquerdo, width=10, height=1, text='Excluir', relief='groove', fg='white', bg='#cf1508', command= delete)
b_excluir.place(x=200, y=340)

#_____Configurações da tree view_____
ScrollbarX = Scrollbar(frame_direito, orient=HORIZONTAL)
ScrollbarY = Scrollbar(frame_direito, orient=VERTICAL)

tree = ttk.Treeview(frame_direito, columns=("ID", "Nome", "Status", "Gênero", "Plataforma", "Nota"),
                    height=23, selectmode="extended", yscrollcommand=ScrollbarY.set, xscrollcommand=ScrollbarX.set)
ScrollbarY.config(command=tree.yview)
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview)
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=N)
tree.heading("Nome", text="Nome", anchor=N)
tree.heading("Status", text="Status", anchor=N)
tree.heading("Gênero", text="Gênero", anchor=N)
tree.heading("Plataforma", text="Plataforma", anchor=N)
tree.heading("Nota", text="Nota", anchor=N)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', select)

connect()
janela.mainloop()
