from flask import jsonify, url_for, request, render_template, redirect
from json import loads, dump
from rank.work import *
from os import getenv
from rank import app, settings

user = getenv("LOGIN")
pwd = getenv("PASSWORD")
print(user, pwd)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/rank')
def rank():
	rank = select_all()
	return render_template('rank.html', rank=rank)


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/verify', methods=['POST'])
def verify():
	form = dict(request.form)
	if form['user'] == user and form['pwd'] == pwd:
		return redirect(url_for('edit'))
	else:
		return redirect(url_for('rank'))

@app.route('/edit')
def edit():
	return render_template('edit.html')


@app.route('/update_user', methods=['POST'])
def update_user():
	form = dict(request.form)
	print(form)
	update_db(name=form['user'], score=int(form['score']))
	return render_template('edit.html')

@app.route('/insert_user', methods=['POST'])
def insert_user():
	form = dict(request.form)
	print(form)
	insert_db(form['user'], form['color'], int(form['score']))
	return render_template('edit.html')

@app.route('/delete_user', methods=['POST'])
def delete_user():
	form = dict(request.form)
	print(form)
	delete_db(form['user'])
	return render_template('edit.html')

