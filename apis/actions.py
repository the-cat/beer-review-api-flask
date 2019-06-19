from sqlalchemy.orm.exc import NoResultFound

from database import db
from database.models import Beer, Review

def create_beer(data):
    name = data['name']
    description = data['description']
    abv = data['abv']
    beer = Beer(name, description, abv)
    db.session.add(beer)
    db.session.commit()

def delete_beer(id):
    beer = Beer.query.filter(Beer.id==id).one()
    db.session.delete(beer)
    db.session.commit()

def create_review(data):
    beer_id = data['beer_id']
    try:
        beer = Beer.query.filter(Beer.id == beer_id).one()
    except NoResultFound:
        raise Exception(f'No Beer found with id={beer_id}')
    rating = data['rating']
    comment = data['comment']
    review = Review(beer, rating, comment)
    db.session.add(review)
    db.session.commit()