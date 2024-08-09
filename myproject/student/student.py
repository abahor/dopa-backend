from flask import Blueprint

students = Blueprint("students", __name__, template_folder="temp", static_folder='static')


@students.route("/", methods=["post", "get"])
def main():
    return "hello world"
