from urllib.parse import quote
import requests
import pandas as pd
import os
import time
from bs4 import BeautifulSoup

def countries_web_scraping():
    url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", {"class": "wikitable"})

    location_list = []
    population_list = []
    percentage_of_the_world_list = []
    date_list = []
    source_list = []

    rows = table.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 5:
            location = cols[1].get_text(strip=True)
            population = cols[2].get_text(strip=True)
            percentage = cols[3].get_text(strip=True)
            date = cols[4].get_text(strip=True)
            source = cols[5].get_text(strip=True)

            location_list.append(location)
            population_list.append(population)
            percentage_of_the_world_list.append(percentage)
            date_list.append(date)
            source_list.append(source)

    countries_df = pd.DataFrame({
        'Location': location_list,
        'Population': population_list,
        'Percentage of the world': percentage_of_the_world_list,
        'Date': date_list,
        'Source': source_list
    })

    return countries_df, location_list

def countries_api(location_list):
    # Initialize all lists
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

    key = 'sF6ZzR1r4zEfkuh5UjgBzw==pKVdznL6qajQkiy7'
    api_url = f'https://api.api-ninjas.com/v1/country?'

    for loc in location_list:
        url = f"{api_url}name={quote(loc)}"
        print(f"Requesting data for: {loc}")
        response = requests.get(url, headers={'X-Api-Key': key})
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            country_info = response.json()
            if country_info:
                info = country_info[0]
                # Append data or None for each field
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
                # Append None for all fields if no data is returned
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

    return countries_data

def combine_and_save_data(countries_df, countries_data):
    # Merge the two dataframes on the 'Location' and 'country_name' columns
    combined_df = pd.merge(countries_df, countries_data, left_on='Location', right_on='country_name', how='outer')

    # Save the combined dataframe to a CSV file on the Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, 'combined_countries_data.csv')
    combined_df.to_csv(file_path, index=False)

    # Print the combined dataframe and the path where it's saved
    print(combined_df)
    print(f'Data saved to {file_path}')


# Main execution flow
countries_df, location_list = countries_web_scraping()
countries_data = countries_api(location_list)
combine_and_save_data(countries_df, countries_data)
