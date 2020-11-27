from flask import Flask, jsonify, request
from json import loads, dump
from db import *


app = Flask(__name__)


@app.route('/home')
def home():
	return 'ok!'


@app.route('/rank')
def get_rank():
	return select_all()


def get_data(received):
	data = {
		'user': received['user'],
		'color': '#' + received['color'],
		'score': int(received['score'])
	}
	return data


@app.route('/new-user')
def new_user():
	"""
		Exemplo de requisição -> user: Lucas, color: #FF0, score: 9991
		http://127.0.0.1:5000/new-user?user=Lucas&color=FF0&score=9991
	"""
	new = get_data(request.args)
	rank = select_all()
	rank['rank'].append(new)
	insert(new['user'], new['color'], new['score'])
	return f'{new}<br> Adiconado com Sucesso!'


@app.route('/update')
def update():
	"""
		Exemplo de requisição -> user: Lucas, color: #FF0, score: +9
		http://127.0.0.1:5000/update?user=Lucas&color=FF0&score=9
	"""
	query = get_data(request.args)
	# consulta dados
	score = select_single(query['user'])[0][2]
	# adiciona
	query['score'] = int(query['score'] + score)
	# update
	update_db(query)

	if int(request.args['score']) > 0:
		return f"""<h1>{query['user']} ganhou {request.args['score']} pontos!<h1>
					<br> :)
				<h2>Pontuação total: {query['score']}<h2>"""
	else:
		return f"""<h1>{query['user']} perdeu {request.args['score']} pontos!<h1>
					<br> :(
				<h2>Pontuação total: {query['score']}<h2>"""


if __name__ == "__main__":
	app.run(port=5000, debug=True)