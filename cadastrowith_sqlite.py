import sqlite3
# 2. Cria ou abre um banco de dados chamado 'banco_usuarios.db'
conn = sqlite3.connect("banco_usuarios.db") # cria arquivo se não existir
cursor = conn.cursor() # cria um cursor para executar comandos SQL

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
idade INTEGER,
curso TEXT
)
""")

nome = input('Digite o seu nome: ')
idade =  input('Digite o sua idade: ')
curso = input('Digite o seu curso: ')

cursor.execute("INSERT INTO usuarios (nome, idade, curso) VALUES (?, ?, ?)", (nome, idade, curso))
conn.commit() # salva a transação no banco

# 6. Recupera e mostra todos os dados cadastrados
cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
    print(linha)
# 7. Encerra a conexão
conn.close()
