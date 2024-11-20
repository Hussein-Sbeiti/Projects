
Country Data Analysis

This project combines country-specific data from an API and GDP-related information scraped from Wikipedia. It fetches economic, demographic, and geographic data, combines the datasets, and outputs a consolidated CSV file for analysis.

Table of Contents

	1.	Features
	2.	Requirements
	3.	Installation
	4.	Usage
	5.	Output
	6.	Data Sources
	7.	License

Features

	•	API Integration: Fetch detailed country data using the API Ninjas Country API.
	•	Web Scraping: Extract GDP data from Wikipedia.
	•	Data Consolidation: Merge API and web-scraped data into a single, clean dataset.
	•	CSV Export: Save the combined data as a CSV file on your desktop.

Requirements

Libraries

Make sure you have the following Python libraries installed:
	•	requests
	•	pandas
	•	os
	•	bs4 (BeautifulSoup)
	•	json

	3.The script will:
	•	Fetch country-specific data from the API.
	•	Scrape GDP-related data from Wikipedia.
	•	Merge both datasets.
	•	Save the combined data as a CSV file to your desktop.

Output

The script outputs a file named Combined_Countries_Data.csv on your desktop.
This file includes:
	•	Country name
	•	Economic indicators (e.g., GDP growth, GDP per capita)
	•	Geographic data (e.g., population density, region)
	•	Demographics (e.g., life expectancy, sex ratio)
	•	GDP data from IMF, World Bank, and United Nations

Data Sources

	•	API: API Ninjas Country API
	•	Web Scraping: Wikipedia GDP Data
