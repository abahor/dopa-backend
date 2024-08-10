from flask import Blueprint, request

from myproject import db
from myproject.models import UsersModel, Question

admin = Blueprint("admin", __name__, template_folder="temp", static_folder='static')


@admin.post("/new-question")
def new_question():
    data = request.get_json()
    try:
        if data["choice_1"] == "" or data["choice_2"] == "" or data["choice_3"] == "" or data["choice_4"] == "" or len(data["right"]) != 1:
            print("----------- here ------------- ")
            print(data["right"])
            print(len(data["right"]))
            raise Exception
        q = Question(
            text=data["text"],
            choice_1=data["choice_1"],
            choice_2=data["choice_2"],
            choice_3=data["choice_3"],
            choice_4=data["choice_4"],
            right=data["right"],
        )
        db.session.add(q)
        db.session.commit()
        return "success", 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return "failed", 403

    # UsersModel.query.all()

