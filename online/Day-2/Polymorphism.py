# Sample climate dataset

climate_data = [

    {"city":"City A", "temperature":25, "carbon_footprint":500},

    {"city":"City B", "temperature":30, "carbon_footprint":450},

    {"city":"City C", "temperature":35, "carbon_footprint":660},

    {"city":"City D", "temperature":22, "carbon_footprint":200},

    {"city":"City E", "temperature":15, "carbon_footprint":350}

]

# High temperature threshold

high_temp_thresh = 26

high_temp_cities = [city for city in climate_data if city["temperature"] > high_temp_thresh]

# print the result

print('Cities with high temperature (> 26 C:)')

for city in high_temp_cities:

    print(f"{city['city']} - {city['temperature']} C")
 