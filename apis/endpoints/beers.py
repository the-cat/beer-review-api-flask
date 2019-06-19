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


@api.route('/<int:id>')
@api.response(404, 'Beer not found.')
class BeerItem(Resource):
    
    @api.marshal_with(beer)
    def get(self, id):
        return Beer.query.filter(Beer.id==id).one()

    @api.response(204, 'Beer successfully deleted.')
    def delete(self, id):
        actions.delete_beer(id)
        return None, 204
