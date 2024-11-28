import requests 
import json 
import pandas as pd 
from bs4 import BeautifulSoup
import os 

def companies_webscraping():
    
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
    return symbol_lists

def companies_api(symbol_lists):
    symbols_list = []
    companyNames_list = []
    prices_list = []
    betas_list = []
    volAvgs_list = []
    marketCaps_list = []
    lastDivs_list = []
    ranges_list = []
    changes_list = []
    currencies_list = []
    ciks_list = []
    isins_list = []
    cusips_list = []
    exchanges_list = []
    exchangeShortNames_list = []
    industries_list = []
    websites_list = []
    ceos_list = []
    sectors_list = []
    countries_list = []
    fullTimeEmployees_list = []
    phones_list = []
    addresses_list = []
    cities_list = []
    states_list = []
    zips_list = []
    dcfDiffs_list = []
    dcfs_list = []
    ipoDates_list = []
    isEtfs_list = []
    isActivelyTradings_list = []
    isAdrs_list = []
    isFunds_list = []

    for sym in symbol_lists: 
        url = f"https://financialmodelingprep.com/api/v3/profile/{sym}?apikey=UYDtTId9b4uHrxsIAsWv6xtfvX5QZOGv"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()  
            
            for item in data: 
                symbols_list.append(item['symbol'])  
                companyNames_list.append(item['companyName'])  
                prices_list.append(item['price']) 
                betas_list.append(item['beta'])  
                volAvgs_list.append(item['volAvg'])  
                marketCaps_list.append(item['mktCap'])  
                lastDivs_list.append(item['lastDiv'])  
                ranges_list.append(item['range']) 
                changes_list.append(item['changes'])  
                currencies_list.append(item['currency']) 
                ciks_list.append(item['cik'])  
                isins_list.append(item['isin']) 
                cusips_list.append(item['cusip'])  
                exchanges_list.append(item['exchange'])  
                exchangeShortNames_list.append(item['exchangeShortName'])  
                industries_list.append(item['industry'])  
                websites_list.append(item['website']) 
                ceos_list.append(item['ceo'])  
                sectors_list.append(item['sector'])  
                countries_list.append(item['country']) 
                fullTimeEmployees_list.append(item['fullTimeEmployees'])  
                phones_list.append(item['phone'])  
                addresses_list.append(item['address'])  
                cities_list.append(item['city']) 
                states_list.append(item['state'])  
                zips_list.append(item['zip'])  
                dcfDiffs_list.append(item['dcfDiff'])  
                dcfs_list.append(item['dcf']) 
                ipoDates_list.append(item['ipoDate'])  
                isEtfs_list.append(item['isEtf'])  
                isActivelyTradings_list.append(item['isActivelyTrading']) 
                isAdrs_list.append(item['isAdr'])  
                isFunds_list.append(item['isFund']) 
        else:
            print(f"Failed to fetch data for {sym}")


    data = {
        "symbol": symbols_list,
        "companyName": companyNames_list,
        "price": prices_list,
        "beta": betas_list,
        "volAvg": volAvgs_list,
        "mktCap": marketCaps_list,
        "lastDiv": lastDivs_list,
        "range": ranges_list,
        "changes": changes_list,
        "currency": currencies_list,
        "cik": ciks_list,
        "isin": isins_list,
        "cusip": cusips_list,
        "exchange": exchanges_list,
        "exchangeShortName": exchangeShortNames_list,
        "industry": industries_list,
        "website": websites_list,
        "ceo": ceos_list,
        "sector": sectors_list,
        "country": countries_list,
        "fullTimeEmployees": fullTimeEmployees_list,
        "phone": phones_list,
        "address": addresses_list,
        "city": cities_list,
        "state": states_list,
        "zip": zips_list,
        "dcfDiff": dcfDiffs_list,
        "dcf": dcfs_list,
        "ipoDate": ipoDates_list,
        "isEtf": isEtfs_list,
        "isActivelyTrading": isActivelyTradings_list,
        "isAdr": isAdrs_list,
        "isFund": isFunds_list
    }

    df = pd.DataFrame(data)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, 'S&P500_financial_data.csv')
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

    print(df)

symbol_lists = companies_webscraping()

companies_api(symbol_lists)