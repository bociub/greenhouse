greenHouse_list = []


def get_last_id():
    if greenHouse_list:
        last_greenHouse = greenHouse_list[-1]
    else:
        return 1
    return last_greenHouse.id + 1


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
        self.currentParameters = 1 #read databasedescription
        




    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'plant': self.plant,
            'forSale': self.forSale

        }
