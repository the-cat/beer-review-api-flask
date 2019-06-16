from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, CheckConstraint
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    is_admin = Column(Boolean)

    def __init__(self, name=None, email=None, is_admin=False):
        self.name = name
        self.email = email
        self.is_admin = is_admin

    def __repr__(self):
        return f'<User {self.name}>'


class Beer(Base):
    __tablename__ = 'beers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    abv = Column(Float)

    def __init__(self, name=None, abv=0):
        self.name = name
        self.abv = abv
    
    def __repr__(self):
        return f'<Beer {self.name}>'


class Review:
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    beer = Column(Integer, ForeignKey('beers.id'))
    rating = Column(Integer)
    comment = Column(String(50))
    name = Column()
    __table_args__ = [CheckConstraint('1<=rating<=5', name='rating_check')]

    def __init__(self, beer, rating=1, comment=None):
        self.beer = beer
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return f'<Review {self.rating} Star for {self.beer}>'

