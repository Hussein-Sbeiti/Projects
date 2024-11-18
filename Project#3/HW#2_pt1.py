import requests
from bs4 import BeautifulSoup
import pandas as pd  

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
data_df.to_csv("Football League Statistics.csv")

