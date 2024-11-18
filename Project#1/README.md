# Project: 3120-Project-1

This project demonstrates how to collect, process, and visualize data from the web using Python. It integrates web scraping, data manipulation, and visual storytelling to extract meaningful insights from online content.

## Overview

The script is designed to:
- **Scrape data** from web pages using `BeautifulSoup` and `requests`.
- **Organize the extracted information** into structured formats using `pandas`.
- **Visualize trends and patterns** with clear and informative charts through `matplotlib`.

With a modular design, the program allows easy reuse and customization for different datasets or applications.

---

## Key Features

- **Automated Data Collection**: Collects data directly from provided URLs.
- **Data Transformation**: Processes raw information into clean, usable formats.
- **Visual Insights**: Generates charts to reveal relationships and trends in the data.
- **Efficient Design**: Modular code structure makes it adaptable for new projects.

---

## What You’ll Need

To run this project, you’ll need:
- A Python environment with the following libraries installed:
  - `pandas` for data handling.
  - `BeautifulSoup` (from `bs4`) and `requests` for web scraping.
  - `matplotlib` for creating visualizations.
- Internet access to fetch data from web pages.

---

## How It Works

1. **Data Collection**: 
   - The script uses URLs to fetch web pages and extract specific information, like names and heights, using web scraping techniques.
2. **Data Handling**: 
   - Collected data is stored in lists and then organized into a structured format using `pandas` DataFrames for further processing.
3. **Visualization**: 
   - Visual representations of the data are created to highlight trends and findings.

---

## Applications

This project is great for:
- Learning how to scrape and analyze web data.
- Exploring data visualization techniques.
- Building foundational skills for larger data science or machine learning projects.

---

## Important Notes

- **Security**: The script currently disables SSL verification during web requests. For production use, it’s recommended to enable verification to ensure secure connections.
- **Customization**: The script is adaptable for different web data sources but may require adjustments based on the structure of the target web pages.

---

Feel free to explore, modify, and expand this project to suit your needs. Contributions are welcome!
