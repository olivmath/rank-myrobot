from flask import Flask, jsonify, url_for, request, render_template, redirect
from json import loads, dump
from db import *
from flask_cors import CORS


user = "lucas"
pwd = '147258'

app = Flask(__name__, static_url_path='/static')
CORS(app)

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

@app.route('/update')
def update():
	pass

if __name__ == "__main__":
	app.run(port=5000, debug=True)