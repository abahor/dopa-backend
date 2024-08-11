from flask import Blueprint, jsonify
from sqlalchemy import and_
from myproject import db
from myproject.models import UsersModel, Question

students = Blueprint("students", __name__, template_folder="temp", static_folder='static')


@students.route("/", methods=["post", "get"])
def main():
    return "hello world"


@students.route("/practice/<chap>/<mod>/<sub>")
def practice(chap, mod, sub):
    q = Question.query.filter(and_(Question.chapter == chap, Question.module == mod, Question.subject == sub)).all()
    t = []
    for i in q:
        t.append({
            "chapter": i.chapter,
            "subject": i.subject,
            "module": i.module,
            "a": i.a,
            "b": i.b,
            "c": i.c,
            "d": i.d,
            "right": i.right,
            "text": i.text
        })
    return jsonify(t)


@students.route("/exam/<chap>/<mod>/<sub>")
def exam(chap, mod, sub):
    q = Question.query.filter(and_(Question.chapter == chap, Question.module == mod, Question.subject == sub)).limit(
        10).all()
    t = []
    for i in q:
        t.append({
            "chapter": i.chapter,
            "subject": i.subject,
            "module": i.module,
            "a": i.a,
            "b": i.b,
            "c": i.c,
            "d": i.d,
            "right": i.right,
            "text": i.text
        })
    return jsonify(t)
