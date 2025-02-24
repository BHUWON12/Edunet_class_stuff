# List of cities with their carbon footprints in tons CO2 per month
cities = [
    {"name": "City A", "carbon_footprint": 500},
    {"name": "City B", "carbon_footprint": 350},
    {"name": "City C", "carbon_footprint": 600},
    {"name": "City D", "carbon_footprint": 200},
]
 
# Lambda function to filter cities below the threshold (400 ton CO2)
sustainability_threshold = 400
sustainable_cities = list(filter(lambda city: city["carbon_footprint"] < sustainability_threshold, cities))
 
# Printing the filtered list of sustainable cities
print("Sustainable Cities:")
for city in sustainable_cities:
    print(city["name"])
    
    
#define the energy class System
class EnergySystem:
    def __init__(self, building_name, energy_consuption, Emission_factor):
        self.
        
    