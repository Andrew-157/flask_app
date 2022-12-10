from flask import current_app as app
from flask import request
from app.models import User, db


@app.route('/users', methods=['POST'])
def create_user():

    username = request.json['username']
    email = request.json['email']
    age = request.json['age']

    user = User.query.filter(
        (User.username == username) | (User.email == email)).first()

    if user:
        return f"User {username} already exists", 409

    new_user = User(username=username, email=email, age=age)

    db.session.add(new_user)
    db.session.commit()

    return f"User {username} has been created"


@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):

    user = User.query.filter_by(id=user_id).first_or_404()

    if request.method == 'DELETE':

        user = User.query.filter(User.id == user_id).first()
        db.session.delete(user)
        db.session.commit()

        return f"User {user.username} was deleted"

    if request.method == 'PUT':

        username = request.json['username']
        email = request.json['email']
        age = request.json['age']

        db.session.query(User).filter_by(id=user_id).update(
            {'username': username, 'email': email, 'age': age})
        db.session.commit()

    return f"ID: {user_id}\nUser: {user.username}\nEmail: {user.email}\nAge: {user.age}"


@app.route('/users', methods=['GET'])
def get_users():

    username = request.args.get('username')
    email = request.args.get('email')

    query_filter = User.username == username if username else User.email == email

    user = User.query.filter(query_filter).first_or_404()

    return f"ID: {user.id}\nUser: {user.username}\nEmail: {user.email}\nAge: {user.age}"
