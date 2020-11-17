import sqlite3 as sql

conn = sql.connect("Ranking.db")
cursor = conn.cursor()


# cria uma tabela
def create_db():
    command = """CREATE TABLE IF NOT EXISTS rank
                 (name text, color text, score integer)"""
    cursor.execute(command)
    conn.commit()
    return True


# pega os dados
def select():
    command = "SELECT * FROM rank"
    cursor.execute(command)
    data = cursor.fetchall()
    conn.commit()
    return [print(i) for i in data]


# insere dados
def insert(*args):
    """
        data tem que um lista do tipo:
        [nome, cor, score]
    """
    command = "INSERT INTO rank VALUES (?, ?, ?)"
    cursor.executemany(command, [args])
    conn.commit()
    return select()


create_db()


insert('Lucas', '#000000', 12000)
