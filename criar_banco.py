import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE livros (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    autor TEXT,
    genero TEXT,
    paginas INTEGER,
    nota REAL
)
''')

conn.commit()
conn.close()

print("Banco criado com sucesso 🚀")