from flask import Flask, jsonify, url_for, request, render_template, redirect
from json import loads, dump
from db import *
from flask_cors import CORS


user = "lucas"
pwd = '147258'

app = Flask(__name__, static_url_path='/static')
CORS(app)

def new_user():
	"""
		Exemplo de requisição -> user: Lucas, color: #FF0, score: 9991
		http://127.0.0.1:5000/new-user?user=Lucas&color=FF0&score=9991
	"""
	new = get_data(request.form)
	rank = select_all()
	rank['rank'].append(new)
	insert(new['user'], new['color'], new['score'])
	return f'{new}<br> Adiconado com Sucesso!'


def get_data(received):
	data = {
		'user': received['user'],
		'color': '#' + received['color'],
		'score': int(received['score'])
	}
	return data


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/rank')
def get_rank():
	rank = select_all()
	return render_template('rank.html', rank=rank)


@app.route('/edit')
def edit():
	return render_template('edit.html')



@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/verify', methods=['POST'])
def verify():
	if request.method == 'POST':
		form = dict(request.form)
		if form['user'] == user and form['pwd'] == pwd:
			return redirect(url_for('edit'))
		else:
			return redirect(url_for('home'))

@app.route('/validate', methods=['POST'])
def validate():
	if request.method == "POST":
		form =  dict(request.form)
		if form['color'] != '' and form['user'] != '' and form['score'] != '':
			return '<script>alert("Novo Usuario Adicionado com Sucesso"); window.location="/edit";</script>'
		elif form['color'] == '' and form['user'] != '' and form['score'] != '':
			return '<script>alert("Pontos Atualizados"); window.location="/edit";</script> '
		else:
			return '<script>alert("Campos mal preenchidos"); window.location="/edit";</script>'


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