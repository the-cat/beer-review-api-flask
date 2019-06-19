from database import db


class Beer(db.Model):
    __tablename__ = 'beers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    abv = db.Column(db.Float)

    def __init__(self, name, description, abv):
        self.name = name
        self.description = description
        self.abv = abv
    
    def __repr__(self):
        return f'<Beer {self.name}>'


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'))
    beer = db.relationship('Beer', backref=db.backref('beers', lazy='dynamic'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(50))
    __table_args__ = (db.CheckConstraint("rating BETWEEN 1 AND 5", name='rating_check'),)

    def __init__(self, beer, rating, comment):
        self.beer = beer
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return f'<Review {self.rating} Star for {self.beer}>'

