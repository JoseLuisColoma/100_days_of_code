'''

# usual dictionary
capitals = {"France": "Paris", "Germany": "Berlin"}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visites": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visites": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
              }

# Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12},
    {
        "country" : "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5}
]

'''

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])





