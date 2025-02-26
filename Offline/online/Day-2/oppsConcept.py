'''way to desing and write software by using objects 

key concepts: 
    object
    Class: Blueprint for creating the objects
    Attributes: variables belonging to an object or class
    Methods: Function belonging to n object or class
'''



class EnergySystem:
    def __init__(self, building_name, energy_consumption, emissio_factor):
        # Initialise the attributes
        self.building_name = building_name
        self.energy_consumption = energy_consumption   # in kWh
        self.emissio_factor = emissio_factor  # kg CO2 per kWh