#Astronauts in space - On the test

import requests 
import json 
import pandas as pd 

key = ''

url = 'http://api.open-notify.org/astros.json'

data = requests.get(url)

if data.status_code == 200:
    result = data.json()
    formatted = json.dumps(result , indent = 5 , sort_keys = True)
    
    #print(formatted)
    #print (result['people'])
    
    names = []
    crafts = []
    
    for results in result['people']:
        crafts.append(results['craft'])
        names.append(results['name'])
        
    results = {
            'Spacecraft' : crafts,
            'Astronauts' : names
    }
    
    results_df = pd.DataFrame(results)
    
    print (results_df)

    results_df = results_df.to_csv("/Users/husseinsbeiti/Desktop/Atronauts in space.csv" , index=True)
