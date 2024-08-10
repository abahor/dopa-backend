from flask import Blueprint

from myproject import db
from myproject.models import UsersModel

students = Blueprint("students", __name__, template_folder="temp", static_folder='static')


@students.route("/", methods=["post", "get"])
def main():
    UsersModel.query.all()
    # db.session.add()
    # db.session.commit()
    return "hello world"
