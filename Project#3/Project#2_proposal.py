import requests
import pandas as pd
import os
import json
from bs4 import BeautifulSoup

# Function to fetch country data from the API
def countries_api():
    # List of countries to query
    countries = [
        "United States", "China", "Germany", "Japan", "India", "United Kingdom", "France", "Italy", 
        "Canada", "Brazil", "Russia", "South Korea", "Mexico", "Australia", "Spain", "Indonesia", 
        "Turkey", "Netherlands", "Saudi Arabia", "Switzerland", "Poland", "Belgium", "Sweden", 
        "Argentina", "Ireland", "United Arab Emirates", "Austria", "Singapore", "Thailand", "Israel", 
        "Norway", "Philippines", "Vietnam", "Bangladesh", "Malaysia", "Iran", "Colombia", "Denmark", 
        "South Africa", "Hong Kong", "Romania", "Egypt", "Pakistan", "Czech Republic", "Chile", 
        "Finland", "Portugal", "Kazakhstan", "Peru", "Iraq", "Algeria", "Greece", "New Zealand", 
        "Hungary", "Qatar", "Nigeria", "Ukraine", "Kuwait", "Morocco", "Ethiopia", "Slovakia", 
        "Dominican Republic", "Ecuador", "Puerto Rico", "Kenya", "Angola", "Uzbekistan", "Guatemala", 
        "Oman", "Bulgaria", "Costa Rica", "Luxembourg", "Croatia", "Panama", "Ivory Coast", 
        "Sri Lanka", "Uruguay", "Turkmenistan", "Lithuania", "Serbia", "Tanzania", "Azerbaijan", 
        "Ghana", "Slovenia", "Belarus", "DR Congo", "Myanmar", "Uganda", "Macau", "Cameroon", 
        "Jordan", "Tunisia", "Bolivia", "Bahrain", "Cambodia", "Latvia", "Paraguay", "Libya", 
        "Nepal", "Estonia", "Honduras", "Zimbabwe", "El Salvador", "Cyprus", "Senegal", "Georgia", 
        "Iceland", "Papua New Guinea", "Zambia", "Bosnia and Herzegovina", "Trinidad and Tobago", 
        "Sudan", "Guinea", "Albania", "Armenia", "Haiti", "Mozambique", "Malta", "Mongolia", 
        "Burkina Faso", "Mali", "Botswana", "Benin", "Guyana", "Gabon", "Jamaica", "Nicaragua", 
        "Niger", "Chad", "Palestine", "Moldova", "Lebanon", "Madagascar", "Mauritius", 
        "North Macedonia", "Kyrgyzstan", "Congo", "Laos", "Afghanistan", "Bahamas", "Rwanda", 
        "Brunei", "Tajikistan", "Somalia", "Namibia", "Kosovo", "Malawi", "Equatorial Guinea", 
        "Mauritania", "Togo", "Montenegro", "Maldives", "Barbados", "Fiji", "Eswatini", "Liberia", 
        "Sierra Leone", "Djibouti", "Suriname", "Aruba", "Andorra", "Belize", "Bhutan", "Burundi", 
        "Central African Republic", "Cape Verde", "Gambia", "Saint Lucia", "Lesotho", "Seychelles", 
        "Guinea-Bissau", "Antigua and Barbuda", "San Marino", "East Timor", "Solomon Islands", 
        "Comoros", "Grenada", "Vanuatu", "Saint Kitts and Nevis", "Saint Vincent and the Grenadines", 
        "Samoa", "São Tomé and Príncipe", "Dominica", "Tonga", "Micronesia", "Kiribati", "Palau", 
        "Marshall Islands", "Nauru", "Tuvalu"
    ]

    # API key and endpoint
    key = '8WzCflJqeJgCZ0oNC7EmYA==exSdSMS7q3kIjOGG'
    api_url = 'https://api.api-ninjas.com/v1/country'

    # List to store API response data
    countries_api_list = []

    # Loop through each country to fetch its data
    for country in countries:
        url = f"{api_url}?name={country}"  # Construct API URL
        response = requests.get(url, headers={'X-Api-Key': key})  # API request
        
        if response.status_code == 200:  # Check for successful response
            country_info = response.json()
            if country_info:
                try:
                    # Extract required information
                    info = country_info[0]
                    currency = (info['currency']['name'])
                    gdp_growth = (info['gdp_growth'])
                    gdp_per_capita = (info['gdp_per_capita'])
                    population_density = (info['pop_density'])
                    region = (info['region'])
                    unemployment = (info['unemployment'])
                    sex_ratio = (info['sex_ratio'])
                    life_expectancy_female = (info['life_expectancy_female'])
                    life_expectancy_male = (info['life_expectancy_male'])
                except KeyError:
                    print('N/A')  # Handle missing fields gracefully
        
                # Append extracted data to the list
                countries_api_list.append({
                    "Country": info.get("name"),
                    "Currency": currency,
                    "GDP Growth": gdp_growth,
                    "GDP Per Capita": gdp_per_capita,
                    "Population Density": population_density,
                    "Region": region,
                    "Unemployment Rate": unemployment,
                    "Sex Ratio": sex_ratio,
                    "Life Expectancy (Female)": life_expectancy_female,
                    "Life Expectancy (Male)": life_expectancy_male
                })

    # Return data as a Pandas DataFrame
    return pd.DataFrame(countries_api_list)

# Function to scrape GDP data from Wikipedia
def webscraping():
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'  # Target URL
    page = requests.get(url, verify=False)  # Fetch the page content
    soup = BeautifulSoup(page.content, 'html.parser')  # Parse HTML content with BeautifulSoup
    table = soup.find("table", {"class": "wikitable"})  # Find the target table

    # Lists to store scraped data
    country_all = []
    IMF_forecast_values = []
    IMF_years = []
    world_bank_estimates = []
    world_bank_years = []
    united_nations_estimates = []
    united_nations_years = []

    # Loop through each row in the table
    rows = table.find_all("tr")[1:]  # Skip header row
    for row in rows:
        cols = row.find_all("td")  # Get all columns
        if len(cols) >= 7:  # Ensure row has sufficient columns
            # Extract column values
            country = cols[0].get_text(strip=True) 
            imf_forecast = cols[1].get_text(strip=True)
            imf_year = cols[2].get_text(strip=True) 
            wb_estimate = cols[3].get_text(strip=True) 
            wb_year = cols[4].get_text(strip=True)  
            un_estimate = cols[5].get_text(strip=True) 
            un_year = cols[6].get_text(strip=True)  
            
            # Append values to corresponding lists
            country_all.append(country)
            IMF_forecast_values.append(imf_forecast)
            IMF_years.append(imf_year)
            world_bank_estimates.append(wb_estimate)
            world_bank_years.append(wb_year)
            united_nations_estimates.append(un_estimate)
            united_nations_years.append(un_year)

    # Construct and return a Pandas DataFrame
    countries_gdp = {
        "Country": country_all,
        "IMF Forecast": IMF_forecast_values,
        "IMF Year": IMF_years,
        "World Bank Estimate": world_bank_estimates,
        "World Bank Year": world_bank_years,
        "United Nations Estimate": united_nations_estimates,
        "United Nations Year": united_nations_years,
    }

    return pd.DataFrame(countries_gdp)

# Function to combine API and web-scraped data and save to a CSV file
def combine_and_save():
    api_df = countries_api()  # Fetch country data from API
    gdp_df = webscraping()  # Scrape GDP data from Wikipedia
    
    # Merge both datasets on the "Country" column
    combined_df = pd.merge(api_df, gdp_df, on="Country", how="inner")
    
    # Remove commas from all numerical columns
    combined_df = combined_df.applymap(lambda x: x.replace(",", "") if isinstance(x, str) and x.replace(",", "").isdigit() else x)
    
    # Define the file path for saving the combined data
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, 'Combined_Countries_Data.csv')
    
    # Save the combined DataFrame to a CSV file
    combined_df.to_csv(file_path, index=False)
    
    print(f"Combined data saved to {file_path}")

# Execute the function to combine and save data
combine_and_save()
