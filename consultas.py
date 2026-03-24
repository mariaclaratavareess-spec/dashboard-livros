import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
dados = cursor.fetchall()

for linha in dados:
    print(linha)

conn.close()