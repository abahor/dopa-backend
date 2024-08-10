from flask import Flask

from myproject.constants import usern, password, database_url, databasename

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# ------------- BUILD
app.config['SECRET_KEY'] = 'mykeyasdfghjklsdfghnjm'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{usern}:{password}@{database_url}/{databasename}?charset=utf8mb4"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 20,
                                           'pool_recycle': 60, }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



# --------------- DATABASE
db = SQLAlchemy(app)
Migrate(app, db)

from myproject.student.student import students

app.register_blueprint(students)

