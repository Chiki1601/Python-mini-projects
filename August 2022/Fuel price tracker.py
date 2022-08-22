#Build Fuel Price Tracker Using Python
# import module
import pandas as pd
import requests
from bs4 import BeautifulSoup

# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url)
	return r.text

# link for extract html data
htmldata = getdata("https://www.goodreturns.in/petrol-price.html")
soup = BeautifulSoup(htmldata, 'html.parser')
result = soup.find_all("div", class_="gold_silver_table")
print(result)
