import requests

def get_us_states():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        us_states = [state['name']['common'] for state in data if 'states' in state]
        return us_states
    else:
        print("Error: Failed to fetch data from API")
        return []

us_states = get_us_states()
if us_states:
    print("List of US states:")
    for state in us_states:
        print(state)
else:
    print("No data available")

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
otras_frutas = ["pera", "manzana"]
print(len(fruits))
print(fruits.count("banana"))
print(fruits.index("banana", 4))
fruits_orden = fruits.sort()
print(fruits_orden)
print((fruits.reverse()))
print(fruits.index("pear"))
print(fruits.extend(otras_frutas))
print(fruits[-1])
print(fruits.append("uva"))
print(fruits)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)


