import json
from pymongo import MongoClient

with open('ticket.json') as f:
    data = json.load(f)

country_city_map = {
    "usa": ["new_york", "dallas", "chicago"],
    "sri_lanka": ["colombo", "kandy"],
    "china": ["beijing", "hong_kong", "wuhan"]
}

city_to_country = {}
for country, cities in country_city_map.items():
    for city in cities:
        city_to_country[city] = country

visa_rates = {list(visa.keys())[0]: list(visa.values())[0] for visa in data['visa_rates']}


def get_visa_rate_by_city(city):
    country = city_to_country.get(city.lower())
    if country:
        visa_rate = visa_rates.get(country)
        if visa_rate:
            return visa_rate
        else:
            return -100000
    else:
        return -1000000

"""----------------------------------------------------------------------------------------------------------------"""

client = MongoClient('mongodb://localhost:27017/')  
db = client['traveldb']  
collection = db['tickets']  


def calculate_total_expenditure(ticket):
    last_visa_location = ticket['visa_stamped_locations'][-1].lower()
    
    visa_cost = get_visa_rate_by_city(last_visa_location)
    
    total_expenditure = int(ticket['ticket_price']) + int(visa_cost)
    
    print(f"last visited visa cost: {visa_cost}")
    print(f"Total Expenditure: {total_expenditure}")

def display_ticket_info(ticket):
    print(f"Passenger Name: {ticket['passenger_name']}")
    print(f"Ticket Number: {ticket['ticket_id']}")
    print(f"Destination: {ticket['destination']}")
    print(f"Ticket Price: {ticket['ticket_price']}")
    calculate_total_expenditure(ticket)

tickets = collection.find()

for ticket in tickets:
    display_ticket_info(ticket)
    print()