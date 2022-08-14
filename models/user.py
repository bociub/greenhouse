from extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))

    ShoporGarden = db.Column(db.Boolean(), default=False, nullable=True)

    seedingDate = db.Column(db.DateTime(), nullable=True)
    postCode = db.Column(db.String(10), nullable=True)
    forSale = db.Column(db.Boolean(), default=False, nullable=True)
    energyPlan = db.Column(db.Integer, nullable=True)
    
    
    greenHouseS = db.relationship('GreenHouse', backref='user') #where tavles connected

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first() 

    def save(self):
        db.session.add(self)
        db.session.commit()