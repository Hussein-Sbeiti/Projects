import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import json
import time

def web_scraping():
    url = 'https://en.wikipedia.org/wiki/List_of_sports_cars'
    page = requests.get(url, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')

    manufacturer_list = []
    model_list = []
    year_list = []
    styles_list = []
    country_of_origin_list = []

    rows = soup.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        try:
            if len(cols) >= 5:
                manufacturers = cols[0].get_text(strip=True)
                models = cols[1].get_text(strip=True)
                years = cols[2].get_text(strip=True)
                styles = cols[3].get_text(strip=True)
                country_of_origin = cols[4].get_text(strip=True)

                manufacturer_list.append(manufacturers)
                model_list.append(models)
                year_list.append(years)
                styles_list.append(styles)
                country_of_origin_list.append(country_of_origin)
        except IndexError:
            continue

    cars = {
        'Manufacturer': manufacturer_list,
        'Model': model_list,
        'Year': year_list,
        'Styles': styles_list,
        'Country_of_origin': country_of_origin_list
    }

    cars_df = pd.DataFrame(cars)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, f'cars_web.csv')
    cars_df.to_csv(file_path, index=False)

    return manufacturer_list, cars_df


def cars_api(manufacturer_list):
   
    unique_manufacturers = list(set(manufacturer_list))  

    for manufacturer in unique_manufacturers:
        
        api_url = f'https://api.api-ninjas.com/v1/cars?make={manufacturer}&limit=2'
        headers = {'X-Api-Key': 'sF6ZzR1r4zEfkuh5UjgBzw==pKVdznL6qajQkiy7'} 
        
        response = requests.get(api_url, headers=headers)
        
        city_mpg_list = []
        class_list = []
        combination_mpg_list = []
        cylinders_list = []
        displacement_list = []
        drive_list = []
        fuel_type_list = []
        highway_mpg_list = []
        make_list_result = [] 
        model_list_result = []
        transmission_list = []
        year_list = []
        
        if response.status_code == 200:
            data = response.json()

            if data:
                for results in data:
                    try:
                        city_mpg_list.append(results['city_mpg'])
                        class_list.append(results['class'])
                        combination_mpg_list.append(results['combination_mpg'])
                        cylinders_list.append(results['cylinders'])
                        displacement_list.append(results['displacement'])
                        drive_list.append(results['drive'])
                        fuel_type_list.append(results['fuel_type'])
                        highway_mpg_list.append(results['highway_mpg'])
                        make_list_result.append(results['make'])
                        model_list_result.append(results['model'])
                        transmission_list.append(results['transmission'])
                        year_list.append(results['year'])
                    except KeyError as error:
                        print(f'Missing key {error} in data for manufacturer: {manufacturer}')
            else:
                print(f"No data found for manufacturer: {manufacturer}")
        else:
            print(f"Failed to fetch data for manufacturer: {manufacturer}, Status Code: {response.status_code}")
        
        time.sleep(1) 

    car_attributes = {
        'city_mpg': city_mpg_list,
        'class': class_list,
        'combination_mpg': combination_mpg_list,
        'cylinders': cylinders_list,
        'displacement': displacement_list,
        'drive': drive_list,
        'fuel_type': fuel_type_list,
        'highway_mpg': highway_mpg_list,
        'make': make_list_result,
        'model': model_list_result,
        'transmission': transmission_list,
        'year': year_list
    }

    car_attributes_df = pd.DataFrame(car_attributes)
    print(car_attributes_df)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, f'cars_api.csv')
    car_attributes_df.to_csv(file_path, index=False)
    
    return car_attributes_df


def main():
    manufacturer_list, cars_df = web_scraping()


    cars_api_df = cars_api(manufacturer_list)  

    merged_df = pd.concat([cars_df, cars_api_df], axis=1)

    print("Web Scraping Results:")
    print(cars_df)

    print("\nAPI Results:")
    print(cars_api_df)

    print("\nMerged DataFrame:")
    print(merged_df)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, f'merged_cars_data.csv')
    merged_df.to_csv(file_path, index=False)

    print(f"\nMerged data saved to: {file_path}")

main()
