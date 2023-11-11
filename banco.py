import sqlite3 as sql

#_____Conecta ao banco de dados SQLite_____
def connect():
    conn = sql.connect('jogos.db')
    cursor = conn.cursor()
    # ____Cria o banco de dados do gerenciador____
    cursor.execute('''CREATE TABLE IF NOT EXISTS jogos
                    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    status TEXT,
                    genero TEXT,
                    plataforma TEXT,
                    nota TEXT)''')
    conn.commit()
    conn.close()
