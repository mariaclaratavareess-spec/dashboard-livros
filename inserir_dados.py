import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

livros = [
    # FANTASIA
    ('O Príncipe Cruel', 'Holly Black', 'Fantasia', 322, 4.1),
    ('O Rei Perverso', 'Holly Black', 'Fantasia', 308, 4.3),
    ('A Rainha do Nada', 'Holly Black', 'Fantasia', 294, 4.2),
    ('A Rainha Vermelha', 'Victoria Aveyard', 'Fantasia', 416, 4.0),
    ('A Seleção', 'Kiera Cass', 'Fantasia', 368, 4.1),
    ('O Hobbit', 'J.R.R. Tolkien', 'Fantasia', 310, 4.3),
    ('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Fantasia', 223, 4.5),
    ('Trono de Vidro', 'Sarah J. Maas', 'Fantasia', 416, 4.2),
    ('Corte de Espinhos e Rosas', 'Sarah J. Maas', 'Fantasia', 432, 4.2),
    ('Eragon', 'Christopher Paolini', 'Fantasia', 544, 3.9),

    # ROMANCE
    ('É Assim que Acaba', 'Colleen Hoover', 'Romance', 336, 4.2),
    ('9 de Novembro', 'Colleen Hoover', 'Romance', 320, 4.1),
    ('Amor & Gelato', 'Jenna Evans Welch', 'Romance', 320, 4.0),
    ('Todas as Suas Imperfeições', 'Colleen Hoover', 'Romance', 304, 4.1),
    ('Confesse', 'Colleen Hoover', 'Romance', 320, 4.0),
    ('Orgulho e Preconceito', 'Jane Austen', 'Romance', 432, 4.3),
    ('Como Eu Era Antes de Você', 'Jojo Moyes', 'Romance', 320, 4.3),
    ('A Hipótese do Amor', 'Ali Hazelwood', 'Romance', 336, 4.2),
    ('Vermelho, Branco e Sangue Azul', 'Casey McQuiston', 'Romance', 400, 4.2),
    ('Depois de Você', 'Jojo Moyes', 'Romance', 352, 4.0),

    # DISTOPIA
    ('Estilhaça-me', 'Tahereh Mafi', 'Distopia', 338, 4.0),
    ('Liberta-me', 'Tahereh Mafi', 'Distopia', 464, 4.2),
    ('Incendeia-me', 'Tahereh Mafi', 'Distopia', 416, 4.4),
    ('Restaura-me', 'Tahereh Mafi', 'Distopia', 448, 4.1),
    ('Desafia-me', 'Tahereh Mafi', 'Distopia', 368, 4.2),
    ('Imagina-me', 'Tahereh Mafi', 'Distopia', 448, 4.0),
    ('1984', 'George Orwell', 'Distopia', 328, 4.2),
    ('Jogos Vorazes', 'Suzanne Collins', 'Distopia', 374, 4.3),
    ('Divergente', 'Veronica Roth', 'Distopia', 487, 4.2),
    ('O Doador de Memórias', 'Lois Lowry', 'Distopia', 240, 4.1),

    # SUSPENSE
    ('Verity', 'Colleen Hoover', 'Suspense', 336, 4.3),
    ('A Paciente Silenciosa', 'Alex Michaelides', 'Suspense', 336, 4.1),
    ('Garota Exemplar', 'Gillian Flynn', 'Suspense', 432, 4.1),
    ('O Homem de Giz', 'C.J. Tudor', 'Suspense', 304, 4.0),
    ('Caixa de Pássaros', 'Josh Malerman', 'Suspense', 272, 4.0),
    ('Sharp Objects', 'Gillian Flynn', 'Suspense', 254, 4.1),
    ('O Código Da Vinci', 'Dan Brown', 'Suspense', 480, 4.2),
    ('Anjos e Demônios', 'Dan Brown', 'Suspense', 616, 4.2),
    ('A Garota no Trem', 'Paula Hawkins', 'Suspense', 378, 4.0),
    ('O Silêncio da Cidade Branca', 'Eva García Sáenz', 'Suspense', 480, 4.1),

    # JOVEM ADULTO
    ('A Culpa é das Estrelas', 'John Green', 'YA', 288, 4.2),
    ('Quem é Você, Alasca?', 'John Green', 'YA', 272, 4.0),
    ('Cidades de Papel', 'John Green', 'YA', 368, 3.9),
    ('Eleanor & Park', 'Rainbow Rowell', 'YA', 328, 4.1),
    ('Extraordinário', 'R.J. Palacio', 'YA', 320, 4.4),
    ('O Ódio que Você Semeia', 'Angie Thomas', 'YA', 464, 4.5),
    ('Os 13 Porquês', 'Jay Asher', 'YA', 288, 3.9),
    ('Se Eu Ficar', 'Gayle Forman', 'YA', 208, 3.9),
    ('Para Todos os Garotos que Já Amei', 'Jenny Han', 'YA', 355, 4.0),
    ('Aristóteles e Dante Descobrem os Segredos do Universo', 'Benjamin Alire Sáenz', 'YA', 359, 4.3)
]

cursor.executemany("""
INSERT INTO livros (titulo, autor, genero, paginas, nota)
VALUES (?, ?, ?, ?, ?)
""", livros)

conn.commit()
conn.close()

print("Livros inseridos 🚀")