from flask import Blueprint, request

from myproject import db
from myproject.models import UsersModel, Question

admin = Blueprint("admin", __name__, template_folder="temp", static_folder='static')


@admin.post("/new-question")
def new_question():
    data = request.get_json()
    try:
        if data["a"] == "" or \
                data["b"] == "" or \
                data["c"] == "" or \
                data["d"] == "" or \
                len(data["right"]) != 1 or \
                data["module"] == "" or \
                data["chapter"] == "" or \
                data["subject"] == "":
            return "failed", 403
        q = Question(
            text=data["text"],
            choice_1=data["a"],
            choice_2=data["b"],
            choice_3=data["c"],
            choice_4=data["d"],
            right=data["right"],
            chapter=data["chapter"],
            subject=data["subject"],
            module=data["module"],
        )
        db.session.add(q)
        db.session.commit()
        return "success", 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return "failed", 403


@admin.put("/delete-question/<int:i>")
def delete_question(i):
    q = Question.query.get_or_404(i)
    try:
        db.session.delete(q)
        db.session.commit()
        return "success", 200
    except:
        db.session.rollback()
        return "failed", 403
