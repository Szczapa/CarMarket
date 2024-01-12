from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    pseudo = Column(String(50), unique=True)
    first_name = Column(String(50), unique=True)
    last_name = Column(String(50), unique=True)
    mail = Column(String(120), unique=True)

    def __init__(self, pseudo=None, mail=None):
        self.pseudo = pseudo
        self.mail = mail

    def __repr__(self):
        return '<User %r>' % (self.pseudo)
