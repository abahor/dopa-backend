from flask import Flask

from myproject.student.student import students

app = Flask(__name__)

app.register_blueprint(students)

