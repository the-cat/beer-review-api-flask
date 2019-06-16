from flask_restplus import Namespace, Resource, fields

api = Namespace('reviews', description='Review related operations')

review = api.model('Review', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})