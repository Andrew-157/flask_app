from flask import current_app as app
from flask import request
from app.models import User, db


@app.route('/users', methods=['POST'])
def create_user():

    username = request.json['username']
    email = request.json['email']
    age = request.json['age']

    user = User.query.filter_by(username=username).first()

    if user:
        return f"User {username} already exists", 409

    new_user = User(username=username, email=email, age=age)

    db.session.add(new_user)
    db.session.commit()

    return f"User {username} has been created"


@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):

    user = User.query.filter_by(id=user_id).first_or_404()

    return f"User: {user.username}\nEmail: {user.email}\nAge: {user.age}"


@app.route('/users', methods=['GET'])
def get_users():

    username = request.args.get('username')
    email = request.args.get('email')

    user = User.query.filter(
        User.username == username).first_or_404()

    return f"User: {user.username}\nEmail: {user.email}\nAge: {user.age}"
