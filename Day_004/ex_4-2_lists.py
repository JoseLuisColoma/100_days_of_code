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

