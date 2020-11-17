rank = [	
	{'user': 'Saymon',    'color': '#FF1616', 'score': 1600}
	{'user': 'Israel',    'color': '#FF1616', 'score': 1100}
	{'user': 'Benjamin',  'color': '#F9B11F', 'score': 1100}
	{'user': 'Henrico',   'color': '#FF7637', 'score': 900}
	{'user': 'Milena',    'color': '#38B6FF', 'score': 900}
	{'user': 'Gustavo',   'color': '#8C52FF', 'score': 600}
	{'user': 'Jonhana',   'color': '#CF3190', 'score': 600}
	{'user': 'Felipe',    'color': '#2F05FF', 'score': 500}
	{'user': 'Alexandre', 'color': '#000000', 'score': 500}
	{'user': 'Luigi',     'color': '#008037', 'score': 400}
	{'user': 'Daniel',    'color': '#B05A42', 'score': 400}
	{'user': 'Daniel G',  'color': '#50AD29', 'score': 400}
	{'user': 'Vitor',     'color': '#782A89', 'score': 400}
	{'user': 'Luis',      'color': '#FF7637', 'score': 200}
	{'user': 'Luca',      'color': '#545454', 'score': 100}
]


def update(str: nome, str: cor, int: pontos):
	try:
		rank[nome] = pontos
		return True
	except IndexError as e:
		raise 'Nome não encontrado'


def new(str: nome, str: cor, int: pontos):
	new = {'nome': nome, 'cor': cor, 'pontos': pontos}
	rank.append(new)
	rank = sorted(rank, key=lambda user: user['pontos'], reverse=True)
	return True