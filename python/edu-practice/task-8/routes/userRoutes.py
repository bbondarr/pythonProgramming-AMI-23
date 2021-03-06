import json

from flask import request, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user
from passlib.hash import pbkdf2_sha256

from app import app, db, ma
from models.UserModel import User
from Validation import Validation as v


login = LoginManager(app)
login.init_app(app)


# ==================================REGISTER ROUTE==========================================
@app.route('/api/users', methods=['POST'])
def registerUser():
    try:
        user = User(**
            {a:request.json[a] for a in User.attributes() if a != 'id'}
        )

        # Checking if user already exists
        v.validateUser(User, user.email)

        # Hashing the password
        user.password = pbkdf2_sha256.hash(user.password)

        db.session.add(user)
        db.session.commit()

        return jsonify({'status': 'success'}, 
                       {'message': f'Thanks for using Products API, {user.firstName}.Now you\'re registered and can log in'}), 201
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


# ===================================LOGIN ROUTE============================================
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/api/login', methods=['POST'])
def loginUser():
    try:
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter(User.email == email).first()
        if user:
            validPassword = pbkdf2_sha256.verify(password, user.password)
            if validPassword:
                login_user(user)
                return jsonify({'status': 'success'}), 204

    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404
    return jsonify({'status': 'fail'}, {'message': 'Bad login or password'}), 404


# ===================================LOGOUT ROUTE===========================================
@app.route('/api/logout', methods=['GET'])
def logoutUser():
    try:
        logout_user()
        return jsonify({'status': 'success'}), 204 
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404