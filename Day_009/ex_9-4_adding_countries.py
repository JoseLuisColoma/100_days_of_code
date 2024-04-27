# Add country name
country = input()
# Number of visits
visits = int(input())
# Create list from formatted string
list_of_cities = eval(input())

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


# to be added to the travel_log.

def add_new_country(country_added, visits_added, list_of_cities_added):

    new_country = {
        "country": country_added,
        "visits": visits_added,
        "cities": list_of_cities_added
    }
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
