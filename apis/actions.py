from database import db, models

def create_beer(data):
    name = data['name']
    description = data['description']
    abv = data['abv']
    beer = models.Beer(name, description, abv)
    db.session.add(beer)
    db.session.commit()