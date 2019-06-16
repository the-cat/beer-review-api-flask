
from flask import Flask
from flask_restplus import Api
from database import db_session, init_db
from models import User, Beer, Review

app = Flask(__name__)

api = Api(app, version='1.0', title='BeerReview API',
    description='A simple Beer Review API',
)

beers_ns = api.namespace('beers', description='Beer operations')
reviews_ns = api.namespace('reviews', description='Review operations')

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)