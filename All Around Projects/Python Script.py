from urllib.parse import quote
import requests
import pandas as pd
import os
import time
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def hw_3_pt1():
    def fill_missing_with_mean(df):
        
        # Identify numeric columns in the DataFrame
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        # Replace NaN values in numeric columns with the column mean
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        
        return df

    def countries_web_scraping():
        # URL of the Wikipedia page to scrape
        url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

        # Send a GET request to the URL and fetch the page content
        page = requests.get(url, verify=False)

        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')

        # Locate the target table on the Wikipedia page
        table = soup.find("table", {"class": "wikitable"})

        # Initialize empty lists to store scraped data
        location_list = []  # List to store country names
        population_list = []  # List to store populations
        percentage_of_the_world_list = []  # List to store percentages of world population
        date_list = []  # List to store dates of data
        source_list = []  # List to store data sources

        # Get all rows from the table, skipping the header row
        rows = table.find_all("tr")[1:]

        # Iterate over each row in the table
        for row in rows:
            # Get all columns (cells) in the current row
            cols = row.find_all("td")

            # Check if the row contains enough columns (at least 5)
            if len(cols) >= 5:
                # Extract and clean text from each relevant column
                location = cols[1].get_text(strip=True)  # Country name
                population = cols[2].get_text(strip=True)  # Population
                percentage = cols[3].get_text(strip=True)  # Percentage of world population
                date = cols[4].get_text(strip=True)  # Date of population data
                source = cols[5].get_text(strip=True)  # Source of population data

                # Append the extracted data to corresponding lists
                location_list.append(location)
                population_list.append(population)
                percentage_of_the_world_list.append(percentage)
                date_list.append(date)
                source_list.append(source)

        # Create a DataFrame from the collected data
        countries_df = pd.DataFrame({
            'Location': location_list,  # Column for country names
            'Population': population_list,  # Column for populations
            'Percentage of the world': percentage_of_the_world_list,  # Column for population percentages
            'Date': date_list,  # Column for dates of data
            'Source': source_list  # Column for data sources
        })

        # Return the DataFrame and the list of country names
        return countries_df, location_list

    def countries_api(location_list):
        
        # Initialize lists to store API response data for each attribute
        gdp_list = []
        sex_ratio_list = []
        surface_area_list = []
        life_expectancy_male_list = []
        unemployment_list = []
        imports_list = []
        homicide_rate_list = []
        currency_code_list = []
        currency_name_list = []
        iso2_list = []
        gdp_growth_list = []
        employment_services_list = []
        urban_population_growth_list = []
        secondary_school_enrollment_female_list = []
        employment_agriculture_list = []
        capital_list = []
        co2_emissions_list = []
        forested_area_list = []
        tourists_list = []
        exports_list = []
        life_expectancy_female_list = []
        post_secondary_enrollment_female_list = []
        post_secondary_enrollment_male_list = []
        primary_school_enrollment_female_list = []
        infant_mortality_list = []
        secondary_school_enrollment_male_list = []
        threatened_species_list = []
        population_list = []
        urban_population_list = []
        employment_industry_list = []
        country_name_list = []
        pop_growth_list = []
        region_list = []
        pop_density_list = []
        internet_users_list = []
        gdp_per_capita_list = []
        fertility_list = []
        refugees_list = []
        primary_school_enrollment_male_list = []

        # Set the API key and base URL
        key = 'sF6ZzR1r4zEfkuh5UjgBzw==pKVdznL6qajQkiy7'
        api_url = f'https://api.api-ninjas.com/v1/country?'

        # Iterate over each country in the provided location list
        for loc in location_list:
            # Construct the API request URL
            url = f"{api_url}name={quote(loc)}"
            print(f"Requesting data for: {loc}")
            
            # Make the API request
            response = requests.get(url, headers={'X-Api-Key': key})
            print(f"Status Code: {response.status_code}")

            if response.status_code == 200:
                # Parse the response as JSON
                country_info = response.json()
                if country_info:
                    # Extract the first country's data from the response
                    info = country_info[0]
                    
                    # Append the data for each attribute, using None if missing
                    gdp_list.append(info.get('gdp', None))
                    sex_ratio_list.append(info.get('sex_ratio', None))
                    surface_area_list.append(info.get('surface_area', None))
                    life_expectancy_male_list.append(info.get('life_expectancy_male', None))
                    unemployment_list.append(info.get('unemployment', None))
                    imports_list.append(info.get('imports', None))
                    homicide_rate_list.append(info.get('homicide_rate', None))
                    currency_code_list.append(info.get('currency', {}).get('code', None))
                    currency_name_list.append(info.get('currency', {}).get('name', None))
                    iso2_list.append(info.get('iso2', None))
                    gdp_growth_list.append(info.get('gdp_growth', None))
                    employment_services_list.append(info.get('employment_services', None))
                    urban_population_growth_list.append(info.get('urban_population_growth', None))
                    secondary_school_enrollment_female_list.append(info.get('secondary_school_enrollment_female', None))
                    employment_agriculture_list.append(info.get('employment_agriculture', None))
                    capital_list.append(info.get('capital', None))
                    co2_emissions_list.append(info.get('co2_emissions', None))
                    forested_area_list.append(info.get('forested_area', None))
                    tourists_list.append(info.get('tourists', None))
                    exports_list.append(info.get('exports', None))
                    life_expectancy_female_list.append(info.get('life_expectancy_female', None))
                    post_secondary_enrollment_female_list.append(info.get('post_secondary_enrollment_female', None))
                    post_secondary_enrollment_male_list.append(info.get('post_secondary_enrollment_male', None))
                    primary_school_enrollment_female_list.append(info.get('primary_school_enrollment_female', None))
                    infant_mortality_list.append(info.get('infant_mortality', None))
                    secondary_school_enrollment_male_list.append(info.get('secondary_school_enrollment_male', None))
                    threatened_species_list.append(info.get('threatened_species', None))
                    population_list.append(info.get('population', None))
                    urban_population_list.append(info.get('urban_population', None))
                    employment_industry_list.append(info.get('employment_industry', None))
                    country_name_list.append(info.get('name', None))
                    pop_growth_list.append(info.get('pop_growth', None))
                    region_list.append(info.get('region', None))
                    pop_density_list.append(info.get('pop_density', None))
                    internet_users_list.append(info.get('internet_users', None))
                    gdp_per_capita_list.append(info.get('gdp_per_capita', None))
                    fertility_list.append(info.get('fertility', None))
                    refugees_list.append(info.get('refugees', None))
                    primary_school_enrollment_male_list.append(info.get('primary_school_enrollment_male', None))
                else:
                    # If the response is empty, append None for all attributes
                    for field in [
                        gdp_list, sex_ratio_list, surface_area_list, life_expectancy_male_list, unemployment_list,
                        imports_list, homicide_rate_list, currency_code_list, currency_name_list, iso2_list,
                        gdp_growth_list, employment_services_list, urban_population_growth_list,
                        secondary_school_enrollment_female_list, employment_agriculture_list, capital_list,
                        co2_emissions_list, forested_area_list, tourists_list, exports_list, life_expectancy_female_list,
                        post_secondary_enrollment_female_list, post_secondary_enrollment_male_list,
                        primary_school_enrollment_female_list, infant_mortality_list, secondary_school_enrollment_male_list,
                        threatened_species_list, population_list, urban_population_list, employment_industry_list,
                        country_name_list, pop_growth_list, region_list, pop_density_list, internet_users_list,
                        gdp_per_capita_list, fertility_list, refugees_list, primary_school_enrollment_male_list
                    ]:
                        field.append(None)
            else:
                # For failed requests, append None for all attributes
                print(f"Error fetching data for {loc}, appending None for all fields.")
                for field in [
                    gdp_list, sex_ratio_list, surface_area_list, life_expectancy_male_list, unemployment_list,
                    imports_list, homicide_rate_list, currency_code_list, currency_name_list, iso2_list,
                    gdp_growth_list, employment_services_list, urban_population_growth_list,
                    secondary_school_enrollment_female_list, employment_agriculture_list, capital_list,
                    co2_emissions_list, forested_area_list, tourists_list, exports_list, life_expectancy_female_list,
                    post_secondary_enrollment_female_list, post_secondary_enrollment_male_list,
                    primary_school_enrollment_female_list, infant_mortality_list, secondary_school_enrollment_male_list,
                    threatened_species_list, population_list, urban_population_list, employment_industry_list,
                    country_name_list, pop_growth_list, region_list, pop_density_list, internet_users_list,
                    gdp_per_capita_list, fertility_list, refugees_list, primary_school_enrollment_male_list
                ]:
                    field.append(None)

            # Delay to avoid API rate limit
            time.sleep(1)

        # Create DataFrame
        countries_data = pd.DataFrame({
            'gdp': gdp_list,
            'sex_ratio': sex_ratio_list,
            'surface_area': surface_area_list,
            'life_expectancy_male': life_expectancy_male_list,
            'unemployment': unemployment_list,
            'imports': imports_list,
            'homicide_rate': homicide_rate_list,
            'currency_code': currency_code_list,
            'currency_name': currency_name_list,
            'iso2': iso2_list,
            'gdp_growth': gdp_growth_list,
            'employment_services': employment_services_list,
            'urban_population_growth': urban_population_growth_list,
            'secondary_school_enrollment_female': secondary_school_enrollment_female_list,
            'employment_agriculture': employment_agriculture_list,
            'capital': capital_list,
            'co2_emissions': co2_emissions_list,
            'forested_area': forested_area_list,
            'tourists': tourists_list,
            'exports': exports_list,
            'life_expectancy_female': life_expectancy_female_list,
            'post_secondary_enrollment_female': post_secondary_enrollment_female_list,
            'post_secondary_enrollment_male': post_secondary_enrollment_male_list,
            'primary_school_enrollment_female': primary_school_enrollment_female_list,
            'infant_mortality': infant_mortality_list,
            'secondary_school_enrollment_male': secondary_school_enrollment_male_list,
            'threatened_species': threatened_species_list,
            'population': population_list,
            'urban_population': urban_population_list,
            'employment_industry': employment_industry_list,
            'country_name': country_name_list,
            'pop_growth': pop_growth_list,
            'region': region_list,
            'pop_density': pop_density_list,
            'internet_users': internet_users_list,
            'gdp_per_capita': gdp_per_capita_list,
            'fertility': fertility_list,
            'refugees': refugees_list,
            'primary_school_enrollment_male': primary_school_enrollment_male_list
        })
        
        columns = ['country_name'] + [col for col in countries_data.columns if col != 'country_name']
        countries_data = countries_data[columns]

        return countries_data

    # Main function to orchestrate scraping, API data fetching, and missing value handling
    def main():
        
        print("Starting web scraping...")
        countries_df, location_list = countries_web_scraping()  # Scrape data
        print("Web scraping completed. Starting API data fetch...")

        # Fetch data via API
        countries_data = countries_api(location_list)
        print("API data fetch completed. Filling missing values with column means...")

        # Fill missing values with column means
        countries_data_filled = fill_missing_with_mean(countries_data)
        print("Missing values filled. Saving the cleaned data...")
        
        # Round all numeric columns to 2 decimal places
        countries_data_filled = countries_data_filled.round(2)

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, 'countries_data_filled.csv')
        countries_data_filled.to_csv(file_path, index=False)
        print(f'Data saved to {file_path}')
        
        print(countries_data_filled)
        print(countries_data_filled.describe())

    main()
    
def hw_3_pt2():

    data = '/Users/husseinsbeiti/Desktop/Programs/CIS 3120/Class Work/stock_prices.csv'
    data = pd.read_csv(data)

    #convert pandas data frame 
    data_array = data.to_numpy()

    # Question 1
    stock_data_array = data_array[: , 4] 
    high_closing = np.max(stock_data_array)
    print('*' * 60)
    print(f"The highest closing price of the stock : {high_closing:.2f}")

    # Question 2
    closing_prices = data_array[:, 4] 
    dates = data_array[:, 0] 
    highest_closing_index = np.argmax(closing_prices)
    highest_closing_date = dates[highest_closing_index]
    print(f"The highest closing price of the stock was on {highest_closing_date}.")

    # Question 3
    data_volume = data_array[: , 5]
    average_vol = np.mean(data_volume)
    print(f'The average daily trading volume of the stock: {average_vol}')

    # Question 4 
    data_std = data_array[: , 5]
    std = np.std(data_std)
    print(f'The standard deviation of the daily trading volume of the stock: {std:.2f}')

    # Question 5
    open_prices = data_array[:, 1] 
    close_prices = data_array[:, 4]
    days_higher_close = np.sum(close_prices > open_prices)
    print(f"The stock closed higher than its opening price on {days_higher_close} days.")

    # Question 6 
    total_trading_days = len(data_array)
    percentage_higher_close = (days_higher_close / total_trading_days) * 100
    print(f"The percentage of total trading days the stock closed higher than its opening price is {percentage_higher_close:.2f}%.")
    print('*' * 60)    
        
def hw_3_pt3():

    # Prompt the user for a search query
    search_query = input("Enter your Google search query: ")

    # Set up the WebDriver (Make sure ChromeDriver is installed and in PATH)
    driver = webdriver.Chrome()

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Wait for the page to load
        time.sleep(2)

        # Find the search bar, enter the query, and press Enter
        search_bar = driver.find_element(By.NAME, "q")
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(3)

        # Extract titles and hyperlinks from the search results
        results = driver.find_elements(By.XPATH, "//div[@class='tF2Cxc']")
        print("\nSearch Results:")
        for index, result in enumerate(results, start=1):
            title_element = result.find_element(By.XPATH, ".//h3")
            link_element = result.find_element(By.XPATH, ".//a")
            title = title_element.text
            link = link_element.get_attribute("href")
            print(f"{index}. {title} - {link}")

    finally:
        # Close the browser
        driver.quit()
import requests
from bs4 import BeautifulSoup
import pandas as pd  
import json

def hw_2_pt1():
    
    # URL of the NFL team stats webpage
    url = 'https://www.nfl.com/stats/team-stats/'

    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Initialize lists to store extracted data
    all_names = []
    yards_pass = []
    touchdowns = []
    ints = []

    # Find all table rows in the HTML content
    rows = soup.find_all('tr')

    # Iterate over each row to extract data
    for row in rows:
        cols = row.find_all('td')  # Find all table data (columns) in the row
        if cols:  # Skip rows without columns
            team_name = cols[0].get_text(strip=True).split(' ')[0]  
            pass_yards = cols[5].get_text(strip=True)  
            touchdown = cols[6].get_text(strip=True) 
            interception = cols[7].get_text(strip=True) 

            # Append data to respective lists
            all_names.append(team_name)
            yards_pass.append(float(pass_yards)) 
            touchdowns.append(int(touchdown)) 
            ints.append(int(interception))  

    # Create a DataFrame using the extracted data
    data_df = pd.DataFrame({
        'Team' : all_names,
        'Pass Yds' : yards_pass,
        'TD' : touchdowns,
        'INT' : ints
    })

    print(data_df) 
    print(data_df.describe())  

    # Save the DataFrame to a CSV file
    data_df.to_csv("/Users/husseinsbeiti/Desktop/Football League Statistics.csv")

def hw_2_pt2():
        
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

def hw_2_pt3():
    def read_original_date():
        # Prompt user for a date
        print("************************************************************")
        date = input("Enter a date in the form of MM/DD/YY or MM/DD/YYYY: ")
        print("************************************************************")
        return date

    def break_original_date(date):
        # Split the date into parts and validate format
        try:
            date_result = date.split("/")
            # Check if input has exactly 3 parts
            if len(date_result) != 3:  
                # Raise error for invalid format
                raise ValueError  
            month, day, year = date_result
        except ValueError:
            # Print error message for invalid input
            print("Invalid date format. Please enter in MM/DD/YY or MM/DD/YYYY format.")
            return None, None, None  
        
        # Print the date components
        print(f"{date} is the original date")
        print(f"{month} is the month")
        print(f"{day} is the day")
        print(f"{year} is the year")
        return month, day, year

    def print_date_3_ways(month, day, year):
        
        # Convert two-digit year to four-digit
        if len(year) == 2:
            year_full = f"20{year}"
        else:
            year_full = year
        
        # List of month names
        months = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]
        
        # Get month name
        month_name = months[int(month) - 1]
        
        # Print in European format
        european_date = f"{day}-{month}-{year}"
        print(f"European way of printing: {european_date}")
        
        # Print in American format
        american_date = f"{month_name} {int(day)}, {year_full}"
        print(f"American way of printing: {american_date}")
        
        # Print in full format
        full_date = f"{month.zfill(2)}-{day.zfill(2)}-{year_full}"
        print(f"Full way of printing: {full_date}")

    def main():
        # Main loop to process multiple dates
        while True:
            original_date = read_original_date()  
            if original_date.lower() == "quit": 
                print("Exiting program.")
                break
            # Split date
            month, day, year = break_original_date(original_date) 
            # Skip invalid dates
            if month is None: 
                continue
            # Print date in 3 formats
            print_date_3_ways(month, day, year) 

    main()
