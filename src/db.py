import sqlite3 as sql

conn = sql.connect("./Ranking.db", check_same_thread=False)
cursor = conn.cursor()


# cria uma tabela
def create_db():
    command = """CREATE TABLE IF NOT EXISTS rank
                 (name text, color text, score integer)"""
    cursor.execute(command)
    conn.commit()
    return True


# pega um dado
def select_single(query):
    command = f"SELECT * FROM rank WHERE name == '{query}'"
    cursor.execute(command)
    data = cursor.fetchall()
    conn.commit()

    return data


# pega todos dados
def select_all():
    command = "SELECT * FROM rank ORDER BY score desc"
    cursor.execute(command)
    data = cursor.fetchall()
    conn.commit()

    rank = {'rank': []}
    # compresão de dicionario
    for i in [i for i in data]:
        new = {'user': i[0], 'color': i[1], 'score': i[2]}
        rank['rank'].append(new)

    return rank


# insere dados novos
def insert(*args):
    """
        ex:
        nome, cor, score
    """
    command = "INSERT INTO rank VALUES (?, ?, ?)"
    cursor.executemany(command, [args])
    conn.commit()
    return True


# faz update de dados
def update_db(data):
    command = f"UPDATE rank SET score = {data['score']}  where name == '{data['user']}'"
    cursor.execute(command)
    conn.commit()
    return True



