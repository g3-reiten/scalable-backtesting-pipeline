from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from create_db import User, db, app
from flask_cors import CORS, cross_origin
CORS(app)

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
	
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		
		if not token:
			return jsonify({'message' : 'Token is missing !!'}), 401

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
			current_user = User.query\
				.filter_by(public_id = data['public_id'])\
				.first()
		except:
			return jsonify({
				'message' : 'Token is invalid !!'
			}), 401
		return f(current_user, *args, **kwargs)

	return decorated

@app.route('/user', methods =['GET'])
@token_required
def get_all_users(current_user):
	users = User.query.all()
	output = []
	for user in users:
		output.append({
			'public_id': user.public_id,
			'name' : user.name,
			'email' : user.email,
		})

	return jsonify({'users': output})

@app.route('/login', methods =['POST'])
def login():
	auth =  request.json

	if not auth or not auth.get('email') or not auth.get('password'):
		return make_response(
			'Could not verify',
			401,
			{'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
		)

	user = User.query\
		.filter_by(email = auth.get('email'))\
		.first()
	
	if not user:
		return make_response(
			'Could not verify',
			401,
			{'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
		)
	
	if check_password_hash(user.password, auth.get('password')):
		token = jwt.encode({
			'public_id': user.public_id,
			'exp' : datetime.utcnow() + timedelta(minutes = 30)
		}, app.config['SECRET_KEY'])
	
		return make_response(
			jsonify({'token' : token.decode('UTF-8')}), 201)
		
	return make_response(
		'Could not verify',
		403,
		{'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
	)

@app.route('/signup', methods =['POST'])
def signup():
	data = request.json
	firstName, lastName = data.get('firstName'), data.get('lastName')
	email= data.get('email')
	password = data.get('password')

	user = User.query\
		.filter_by(email = email)\
		.first()
	if not user:
		user = User(
			public_id = str(uuid.uuid4()),
			firstName = firstName,
			lastName = lastName,
			email = email,
			password = generate_password_hash(password)
		)
		db.session.add(user)
		db.session.commit()
		print(user)
		return make_response('Successfully registered.', 201)
	else:
		return make_response('User already exists. Please Log in.', 202)

@app.route('/backtest', methods =['get'])
def getBacktestOutput():
	name = request.args.get('name')
	staratagy = request.args.get('stratagy')
	cash = request.args.get('cash')
	commision = request.args.get('commision')
	print(name, staratagy, cash, commision)
	filename = "output.txt"
	with open(filename) as f:
		content = f.readlines()
	return jsonify(content)

if __name__ == "__main__":
	app.run(debug = True)