from extensions import db
greenHouse_list = []


def get_last_id():
    if greenHouse_list:
        last_greenHouse = greenHouse_list[-1]
    else:
        return 1
    return last_greenHouse.id + 1

"""Without database
class GreenHouse:

    def __init__(self, name, plant, postcode, plantingDate=0, forSale=False, bookedForSale=0,
                 energyPlan=0, harvestDate=0, counterForAVG=0, AVGofAirTemperature=0, 
                 GivenDaysWeather=0, currentParameters=0):
        self.id = get_last_id() #function above
        self.name = name
        self.plant = plant
        self.postcode = postcode
        self.plantingDate = 9
        self.forSale = True
        self.bookedForSale = 7
        self.energyPlan = 6
        self.harvestDate = 5
        self.counterForAVG = 4
        self.AVGofAirTemperature = 3
        self.GivenDaysWeather = 2
        self.currentParameters = 1 
    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'plant': self.plant,
            'forSale': self.forSale

        }"""
class GreenHouse(db.Model):
    __tablename__ = 'greenhouses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    plant = db.Column(db.String(200))
    postcode = db.Column(db.String(200))
    plantingDate = db.Column(db.Integer)
    forSale = db.Column(db.Boolean(), default=False)
    bookedForSale = db.Column(db.Boolean(), default=False)
    energyPlan = db.Column(db.Integer)
    harvestDate = db.Column(db.String(1000))
    counterForAVG = db.Column(db.Integer)
    AVGofAirTemperature = db.Column(db.Integer)
    GivenDaysWeather = db.Column(db.Integer)
    currentParameters = db.Column(db.Integer)
  
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))    
