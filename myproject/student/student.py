from flask import Blueprint

from myproject.models import UsersModel

students = Blueprint("students", __name__, template_folder="temp", static_folder='static')


@students.route("/", methods=["post", "get"])
def main():
    UsersModel.query.all()
    return "hello world"
