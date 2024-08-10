from flask import Blueprint

from myproject.models import UsersModel

admin = Blueprint("students", __name__, template_folder="temp", static_folder='static', url_prefix="/admin")


@admin.route("/", methods=["post", "get"])
def main():
    UsersModel.query.all()
    return "hello world"
