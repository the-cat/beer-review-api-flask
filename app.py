
from flask import Flask, Blueprint
from flask_restplus import Api

import settings
from apis import api
from database import db, models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
app.register_blueprint(blueprint)
db.init_app(app)

# ßdb.create_all(app=app)

if __name__ == '__main__':
    app.run(debug=True)