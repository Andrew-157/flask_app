from flask import current_app as app


@app.route('/users', methods=['POST'])
def create_user():
    pass


@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):
    pass
