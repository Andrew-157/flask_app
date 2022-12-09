from flask import current_app as app
from flask import request
from app.models import User, db


@app.route('/users', methods=['POST'])
def create_user():

    username = request.json['username']
    email = request.json['email']

    new_user = User(username=username, email=email)

    db.session.add(new_user)
    db.session.commit()

    return f"User {username} has been created"


@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):
    pass
