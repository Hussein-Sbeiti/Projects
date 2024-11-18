import json
import requests
import pandas as pd

# API endpoint and parameters
url = "https://calendarific.com/api/v2/holidays"
parameter = {
    "api_key": "EEMuLa8bTU3w9kksjPXjtB6WsafBR8hW",  
    "country": "US",  # Country code for holidays
    "year": "2024"  # Year for which holidays are fetched
}

# Make GET request to the API
res = requests.get(url, params=parameter)

# Check if the response status is OK (200)
if res.status_code == 200:
    data = res.json()  # Parse the response JSON
    formatted_data = json.dumps(data, indent=1, sort_keys=True)  # Format JSON for readability (optional)

    # Initialize lists to store holiday details
    name_all = []
    id_all = []
    locations_all = []
    primary_type_all = []
    day_all = []
    month_all = []
    year_all = []

    # Extract relevant fields from the API response
    for results in data['response']['holidays']:
        name_all.append(results['name'])  # Holiday name
        id_all.append(results['country']['id'])  # Country ID
        locations_all.append(results['locations'])  # Locations associated with the holiday
        primary_type_all.append(results['primary_type'])  # Primary type of holiday
        month_all.append(results['date']['datetime']['month'])  # Month of the holiday
        year_all.append(results['date']['datetime']['year'])  # Year of the holiday
        day_all.append(results['date']['datetime']['day'])  # Day of the holiday

    # Create a dictionary for storing extracted holiday data
    holidays = {
        'Name' : name_all,
        'Country ID' : id_all,
        'Locations' : locations_all,
        'Primary Type' : primary_type_all,
        'Month' : month_all,
        'Year' : year_all,
        'Day' : day_all,
    }

    # Convert the dictionary to a DataFrame
    holidays_df = pd.DataFrame(holidays)
    print(holidays_df)  # Print the DataFrame
    print(holidays_df.describe())  # Print a summary of numerical columns in the DataFrame

    # Save the DataFrame to a CSV file
    holidays_df.to_csv('/Users/husseinsbeiti/Desktop/holiday.csv', index=True)
