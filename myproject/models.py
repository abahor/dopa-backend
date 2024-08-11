from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from myproject import db


# @login.user_loader
# def load_user(user_id):
#     return UsersModel.query.get(user_id)


class UsersModel(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    # posts = db.relationship('Posts', backref='workers_posts', cascade="all,delete", lazy='select')

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, field):
        return check_password_hash(self.password, field)

    def __repr__(self):
        return f"{self.username}"


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    a = db.Column(db.Text, nullable=False)
    b = db.Column(db.Text, nullable=False)
    c = db.Column(db.Text, nullable=False)
    d = db.Column(db.Text, nullable=False)
    right = db.Column(db.Text, nullable=False)
    module = db.Column(db.Text, nullable=False)
    chapter = db.Column(db.Text, nullable=False)
    subject = db.Column(db.Text, nullable=False)

    def __init__(self, text, choice_1, choice_2, choice_3, choice_4, right, module, subject, chapter):
        self.text = text
        self.a = choice_1
        self.b = choice_2
        self.c = choice_3
        self.d = choice_4
        self.right = right
        self.module = module
        self.chapter = chapter
        self.subject = subject
