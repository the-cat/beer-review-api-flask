from flask_restplus import Namespace, Resource, fields
from database.models import Beer
from apis import actions

api = Namespace('beers', description='Beer related operations')

beer = api.model('Beer', {
    'id': fields.Integer(readOnly=True, description='The beer id'),
    'name': fields.String(required=True, description='The beer name'),
    'description': fields.String(required=True, description='The beer description'),
    'abv': fields.Float(required=True, description='The beer alcohol percentage')
})

@api.route('/')
class BeerList(Resource):
    """ 
    """
    @api.doc('list_beers')
    @api.marshal_list_with(beer)
    def get(self):
        '''List all beers'''
        return Beer.query.all()
    
    @api.doc('create_beer')
    @api.expect(beer)
    @api.marshal_with(beer, code=201)
    def post(self):
        '''Create a new beer'''
        actions.create_beer(api.payload)


# @api.route('/<int:id>')
# @api.response(404, 'Category not found.')
# class BeerItem(Resource):
#     def get(self, id):
#         pass # get beer
