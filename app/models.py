from . import db


class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(64), index=False, unique=True, nullable=False)

    def __repr__(self):
        return f"User {self.username}"
