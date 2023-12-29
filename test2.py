import requests
from urllib.parse import urlencode

def get_place_id(api_key, location):
    # API endpoint
    endpoint = "http://py4e-data.dr-chuck.net/json?"

    # Parameters for the API request
    params = {
        'address': location,
        'key': api_key,  # Replace 'YOUR_API_KEY' with your actual key
    }

    try:
        # URL encode the parameters
        encoded_params = urlencode(params)

        # Construct the full URL with encoded parameters
        full_url = f"{endpoint}{encoded_params}"

        # Make the API request
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Check if the response is empty
        if not response.text:
            print("Error: Empty response from the server")
            return None

        # Parse the JSON response
        data = response.json()

        # Check if the request was successful
        if data['status'] == 'OK' and 'place_id' in data['results'][0]:
            place_id = data['results'][0]['place_id']
            return place_id
        else:
            print(f"Error: {data['status']}")
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None

# Prompt the user for a location
location = input("Enter location: ")

# Replace 'YOUR_API_KEY' with your actual key
api_key = 'AIzaSy___IDByT70'

# Call the function and display the result
result = get_place_id(api_key, location)
if result is not None:
    print(f"Place id: {result}")
