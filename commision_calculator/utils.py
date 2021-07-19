from django.core.exceptions import ObjectDoesNotExist
from .models import City, Reservations


def calculate_total_gr_commision():
    reservations = Reservations.objects.all()
    cities = City.objects.all()
    data = {}
    cities_not_in_db = []
    for city in cities:
        data[city.city_name] = data.get(city.city_name, [0, city.city_commision])
        
    for item in reservations:
        try:
            data[item.city][0] += item.net_income
        except KeyError:
            cities_not_in_db.append(item.city)

    GR_commision = 0
    for key, value  in data.items():
        GR_commision += float(value[0]) * float(value[1])

    return GR_commision, cities_not_in_db

def calculate_gr_commision_per_month():
    reservations = Reservations.objects.all()
    cities = City.objects.all()
    data = {}
    city_rates = {}
    for city in cities:
        city_rates[city.city_name] = city_rates.get(city.city_name, city.city_commision)

    
    for item in reservations:
        try:
            data[item.date.strftime("%Y-%m")] = data.get(item.date.strftime("%Y-%m"), 0) + item.net_income * city_rates[item.city] 
        except KeyError:
            pass

    return data

def calculate_rate_for_city(city_input):
    try:
        city_query = City.objects.get(city_name=city_input)
    except ObjectDoesNotExist:
        return f"City {city_input} does not exist in the database, please contact an administrator."

    reservations = Reservations.objects.filter(city=city_input)
    data = {}
    for item in reservations:
        data[item.city] = data.get(item.city, 0) + item.net_income * city_query.city_commision

    return data[city_input]