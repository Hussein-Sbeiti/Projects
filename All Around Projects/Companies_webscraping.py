import requests 
import json 
import pandas as pd 
from bs4 import BeautifulSoup
import os 

def companies_webscraping(symbol_lists):
    
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_component_stocks"
    page = requests.get(url, verify = True)
    soup = BeautifulSoup(page.content, 'html.parser')

    symbol_lists = []
    security_lists = []
    gics_sector_lists = []
    gics_sub_industy_lists = []
    headquarters_location_lists = []
    date_added_lists = []
    cik_lists = []
    founded_lists = []

    rows = soup.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 7:
            symbols = cols[0].get_text(strip=True) 
            securitys = cols[1].get_text(strip=True)
            gics_sector = cols[2].get_text(strip=True)
            gics_sub_industries = cols[3].get_text(strip=True)
            headquarters = cols[4].get_text(strip=True)
            date_addeds = cols[5].get_text(strip=True)
            ciks = cols[6].get_text(strip=True)
            foundeds = cols[7].get_text(strip=True)

            symbol_lists.append(symbols)
            security_lists.append(securitys)
            gics_sector_lists.append(gics_sector)
            gics_sub_industy_lists.append(gics_sub_industries)
            headquarters_location_lists.append(headquarters)
            date_added_lists.append(date_addeds)
            cik_lists.append(ciks)
            founded_lists.append(foundeds)

    companies = {
        'Symbols': symbol_lists,
        'Security' : security_lists,
        'GICS Sector' : gics_sector_lists, 
        'GICS Industry' : gics_sub_industy_lists, 
        'Headquarters Locations' : headquarters_location_lists, 
        'Date Added' : date_added_lists, 
        'CIK' : cik_lists, 
        'Founded' : founded_lists 
    }
    companies_df = pd.DataFrame(companies)
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, f'S&P500 companies.csv')
    companies_df.to_csv(file_path, index=False)

    print(companies_df)
    print(companies_df.describe())
