from flask_restplus import Api

from .endpoints.beers import api as beers_api
from .endpoints.reviews import api as reviews_api

api = Api(
    title='Beer review API',
    version='1.0',
    description='An API for beers and reviews',
    # All API metadatas
)

api.add_namespace(beers_api)
api.add_namespace(reviews_api)