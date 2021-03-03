from flask import jsonify, url_for, request, render_template, redirect
from json import loads, dump
from rank.work import *
from os import getenv
from rank import settings, api, Resource

user = getenv("LOGIN")
pwd = getenv("PASSWORD")

class Rank(Resource):
	def get(self):
		rank = select_all()
		return rank


class Login(Resource):
	def get(self):
		return render_template('login.html')


class Verify(Resource):
	def post(self):
		form = dict(request.form)
		if form['user'] == user and form['pwd'] == pwd:
			return redirect(url_for('edit'))
		else:
			return redirect(url_for('rank'))

class Edit(Resource):
	def get(self):
		return render_template('edit.html')

class Update_user(Resource):
	def post(self):
		form = dict(request.form)
		print(f"Usuario {form['user']} Atualizado")
		update_db(name=form['user'], score=int(form['score']))
		return render_template('edit.html')

class Insert_user(Resource):
	def post(self):
		form = dict(request.form)
		print(f"Usuario {form['user']} inserido")
		insert_db(form['user'], form['color'], int(form['score']))
		return render_template('edit.html')

class Delete_user(Resource):
	def post(self):
		form = dict(request.form)
		print(f"Usuario {form['user']} Deletado")
		delete_db(form['user'])
		return render_template('edit.html')


api.add_resource(Rank, '/')
api.add_resource(Login, '/login')
api.add_resource(Verify, '/verify')
api.add_resource(Edit, '/edit')
api.add_resource(Update_user, '/update_user')
api.add_resource(Insert_user, '/insert_user')
api.add_resource(Delete_user, '/delete_user')