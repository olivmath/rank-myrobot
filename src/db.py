import sqlite3 as sql

conn = sql.connect("Ranking.db", check_same_thread=False)
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

6
print(select_all())


# rank = {'rank':[
# 		{'user': 'Saymon',    'color': '#FF1616', 'score': 1600},
# 		{'user': 'Henrico',   'color': '#FF7637', 'score': 1400},
# 		{'user': 'Israel',    'color': '#FF1616', 'score': 1100},
# 		{'user': 'Benjamin',  'color': '#F9B11F', 'score': 1100},
# 		{'user': 'Milena',    'color': '#38B6FF', 'score': 900},
# 		{'user': 'Gustavo',   'color': '#8C52FF', 'score': 600},
# 		{'user': 'Jonhana',   'color': '#CF3190', 'score': 600},
# 		{'user': 'Felipe',    'color': '#2F05FF', 'score': 500},
# 		{'user': 'Alexandre', 'color': '#000000', 'score': 500},
# 		{'user': 'Luigi',     'color': '#008037', 'score': 400},
# 		{'user': 'Daniel',    'color': '#B05A42', 'score': 400},
# 		{'user': 'Daniel G',  'color': '#50AD29', 'score': 400},
# 		{'user': 'Vitor',     'color': '#782A89', 'score': 400},
# 		{'user': 'Luis',      'color': '#FF7637', 'score': 200},
# 		{'user': 'Luca',      'color': '#545454', 'score': 100},
# 	]
# }
