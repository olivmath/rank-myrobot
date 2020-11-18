from flask import Flask, jsonify, request
from json import loads, dump


app = Flask(__name__)

rank = {'rank':[
		{'user': 'Saymon',    'color': '#FF1616', 'score': 1600},
		{'user': 'Henrico',   'color': '#FF7637', 'score': 1400},
		{'user': 'Israel',    'color': '#FF1616', 'score': 1100},
		{'user': 'Benjamin',  'color': '#F9B11F', 'score': 1100},
		{'user': 'Milena',    'color': '#38B6FF', 'score': 900},
		{'user': 'Gustavo',   'color': '#8C52FF', 'score': 600},
		{'user': 'Jonhana',   'color': '#CF3190', 'score': 600},
		{'user': 'Felipe',    'color': '#2F05FF', 'score': 500},
		{'user': 'Alexandre', 'color': '#000000', 'score': 500},
		{'user': 'Luigi',     'color': '#008037', 'score': 400},
		{'user': 'Daniel',    'color': '#B05A42', 'score': 400},
		{'user': 'Daniel G',  'color': '#50AD29', 'score': 400},
		{'user': 'Vitor',     'color': '#782A89', 'score': 400},
		{'user': 'Luis',      'color': '#FF7637', 'score': 200},
		{'user': 'Luca',      'color': '#545454', 'score': 100},
	]
}


@app.route('/home')
def home():
	return 'ok!'


@app.route('/rank')
def get_rank():
	new = {'rank': [sorted(rank['rank'], key=lambda user: user['score'], reverse=True)]}
	return new


@app.route('/new-user')
def new_user():
	""" 
		Exemplo de requisição -> user: Lucas, color: #FF0, score: 9991
		http://127.0.0.1:5000/new-user?user=Lucas&color=FF0&score=9991
	"""
	query = request.args
	new = {
		'user': query['user'],
		'color': query['color'],
		'score': int(query['score'])
	}
	rank['rank'].append(new)
	return f'{new}<br> Adiconado com Sucesso!'


@app.route('/update')
def update():
	""" 
		Exemplo de requisição -> user: Lucas, color: #FF0, score: +9
		http://127.0.0.1:5000/update?user=Lucas&color=FF0&score=9
	"""
	query = request.args
	for i in range(len(rank['rank'])):
		if query['user'] in rank['rank'][i]['user']:
			rank['rank'][i]['score'] += int(query['score'])
			x = [True, i]
			break
		else:
			x = False

	if x[0]:
		return rank['rank'][x[1]] 
	else:
		return f"{query['user']} não existe"


app.run(debug=True)