from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.ingredientModel import Ingredient, InventoryIngredient

Base = declarative_base()

user_allergy_association = Table(
    'user_allergy', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('allergy_id', ForeignKey('allergies.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    username = Column(String, unique=True)
    allergies = relationship('Allergy', secondary=user_allergy_association, back_populates='allergic_users')
    inventory = relationship('InventoryIngredient', back_populates='user')
    hasScale = Column(Integer, nullable=False)
    hasThermometer = Column(Integer, nullable=False)


    def __init__(
            self, first_name="", username="", 
            allergies="", inventory="", hasScale=False, hasThermometer=False):
        self.first_name = first_name
        self.username = username
        self.allergies = allergies
        self.inventory = inventory
        self.hasScale = hasScale
        self.hasThermometer = hasThermometer
    
    def __repr__(self):
        return f"""<id={self.id}, User(<first_name={self.first_name}, username={self.username},
                allergies={self.allergies}, inventory={self.inventory},
                hasScale={self.hasScale}, hasThermometer={self.hasThermometer})>"""

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "username": self.username,
            "allergies": self.allergies,
            "inventory": self.inventory,
            "hasScale": self.hasScale,
            "hasThermometer": self.hasThermometer
        }