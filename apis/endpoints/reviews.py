from flask_restplus import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest

from database.models import Review
from apis import actions

api = Namespace('reviews', description='Review related operations')

review = api.model('Review', {
    'id': fields.String(required=True, description='The review id'),
    'beer_id': fields.Integer(required=True, description='The id of the reviewed Beer'),
    'rating': fields.Integer(required=True, description='The number of stars 1-5'),
    'comment': fields.String(required=True, description='The review comment')
})


@api.route('/')
class ReviewList(Resource):

    @api.marshal_list_with(review)
    def get(self):
        '''List all reviews'''
        return Review.query.all()
    
    @api.expect(review)
    @api.marshal_with(review, code=201)
    def post(self):
        '''Create a new review'''
        try:
            actions.create_review(api.payload)
        except Exception as e:
            ex = BadRequest('Failed to create review.')
            ex.data = {'error': str(e)}
            raise ex