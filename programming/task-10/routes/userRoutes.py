import json

from flask import request, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from passlib.hash import pbkdf2_sha256

from app import app, db, ma
from models.UserModel import User
from schemas.UserSchema import UserSchema
from routes.RouteManager import RouteManager
from Validation import Validation as v


login = LoginManager(app)
login.init_app(app)

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

userRouteManager = RouteManager(User, userSchema, usersSchema)

# ==================================REGISTER ROUTE==========================================
@app.route('/api/users', methods=['POST'])
def registerUser():
    try:
        user = User(**
            {a:request.json[a] for a in User.attributes() 
            if a != 'id'and a != 'products' and a != 'role' and a != 'orders'}
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
        validPassword = pbkdf2_sha256.verify(password, user.password)
        if user and validPassword:
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


@app.route('/api/users', methods=['GET'])
@login_required
def getAllUsers():
    if current_user.role == 'admin':
        try:
            sortBy = request.args.get('sort', default=None, type=str)
            filterBy = request.args.get('filter', default=None, type=str)
            limit = request.args.get('limit', default=None, type=int)
            page = request.args.get('page', default=None, type=int)

            users = userRouteManager.getAll(sortBy, filterBy, limit, page)
            return jsonify({'status': 'success'},
                            {'count': len(users)}, 
                            {'users': users}), 200
        except Exception as e:
            return jsonify({'status': 'fail'}, {'message': str(e)}), 404
    else:
         return jsonify({'status': 'fail'}, {'message': 'access denied'}), 404


# SQLALCHEMY DOESN'T ALLOW ME TO MAKE A DECORATOR ON A ROUTE ==============
# SO THAT'S WHY THIS IF ROLE == ADMIN IS EVERYWHERE =======================

@app.route('/api/users/<id>', methods=['GET'])
@login_required
def getUser(id):
    if current_user.role == 'admin':
        try:
            result = userRouteManager.getSingle(id)
            return jsonify({'status': 'success'}, 
                        {'product': result}), 200
        except Exception as e:
            return jsonify({'status': 'fail'}, {'message': str(e)}), 404
    else:
         return jsonify({'status': 'fail'}, {'message': 'access denied'}), 404


@app.route('/api/users/<id>', methods=['DELETE'])
@login_required
def deleteUser(id):
    if current_user.role == 'admin':
        try:
            user = userRouteManager.deleteSingle(id)
            db.session.delete(user)
            db.session.commit()
            return jsonify({'status': 'success'}), 204
        except Exception as e:
            return jsonify({'status': 'fail'}, {'message': str(e)}), 404
    else:
         return jsonify({'status': 'fail'}, {'message': 'access denied'}), 404



@app.route('/api/users/<id>', methods=['PATCH'])
@login_required
def patchUser(id):
    if current_user.role == 'admin':
        try:
            result = userRouteManager.patchSingle(id)
            db.session.commit()
            return jsonify({'status': 'success'}), 204
        except Exception as e:
            return jsonify({'status': 'fail'}, {'message': str(e)}), 404
    else:
         return jsonify({'status': 'fail'}, {'message': 'access denied'}), 404