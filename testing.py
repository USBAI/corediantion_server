import requests

# The URL for the API endpoint
url = "http://127.0.0.1:8000/coredination/get-job-data/"

# The API key to authenticate the request
api_key = "jhgyfidtsryefyigu-jugyuftdyrtfugiho-ouiygfy8tu878"

# Set up the headers with the API key
headers = {
    'STVN-API-Key': api_key
}

try:
    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        jobs_data = response.json()
        print("Jobs Data:", jobs_data)
    elif response.status_code == 401:
        print("Unauthorized: Invalid API key.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Handle exceptions that occur during the API request
    print("An error occurred:", str(e))
