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
    command = f'SELECT * FROM rank WHERE name == "{query}"'
    cursor.execute(command)
    data = cursor.fetchall()
    conn.commit()

    return data[0]


# pega todos dados  
def select_all():
    command = "SELECT * FROM rank ORDER BY score desc"
    cursor.execute(command)
    conn.commit()
    data = cursor.fetchall()

    rank = {'rank': []}
    # compresão de dicionario
    for i in [i for i in data]:
        new = {'name': i[0], 'color': i[1], 'score': i[2]}
        rank['rank'].append(new)

    return rank


# insere dados novos
def insert(*data):
    """
        params:
            'Joaquim',
            '#ff0',
            1100
    """
    print(data)
    command = f'INSERT INTO rank VALUES {data}'
    try:
        cursor.execute(command)
        return True

    except Exception as e:
        return False

    finally:
        conn.commit()


# atualização dados existentes
def update_db(**data):
    """
        params:
            score=100,
            name='Lucas'
    """
    data['score'] += select_single(data['name'])[2]
    command = f'UPDATE rank SET score = {data["score"]} WHERE name == "{data["name"]}"'
    try:
        cursor.execute(command)
        return True

    except Exception as e:
        return False

    finally:
        conn.commit()




pontos = [{'score': 400, 'name': 'Gustavo'},
        {'score': 400, 'name': 'Daniel'},
        {'score': 800, 'name': 'Alexandre'},
        {'score': 400, 'name': 'Joaquim'},
        {'score': 400, 'name': 'Luca'},
        {'score': 600, 'name': 'Luis'},
        {'score': 300, 'name': 'Luigi'},
        {'score': 800, 'name': 'Victor'},
        {'score': 800, 'name': 'Kauã'},
        {'score': 800, 'name': 'Pedro'},
        {'score': 600, 'name': 'Saymon'},
        {'score': 300, 'name': 'Beijamin'},
        {'score': 800, 'name': 'Arthur'}]

a = select_all()
print(a)

