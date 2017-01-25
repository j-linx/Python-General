# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 01:18:33 2016

@author: linjen
"""
import os
os.chdir(r"C:\Users\linjen\Dropbox\Data Science\Datasets")

import requests
from lxml import html
from bs4 import BeautifulSoup
import pandas as pd

##### METHOD 1

url = 'http://www.science.co.il/International/Currency-codes.php'
# Scrape the HTML at the url
r = requests.get(url)
# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, 'lxml')

# Create four variables to score the scraped data in
country = []
capital = []
currency = []
fx = []

## Create an object of the first object that is class=dataframe

#table = soup.find(class_='dataframe')
table = soup.find_all('table')[1]
print(table)

## Find all the <tr> table row tag pairs
rows = table.find_all('tr')[0:]

## Initialize dictionary
data = {
    'country' : [],
    'capital' : [],
    'currency' : [],
    'fx' : []
}

for row in rows:
    cols = row.find_all('td')
    # Create a variable of all the <td> tag pairs in each <tr> tag pair
    data['country'].append( cols[0].get_text() )
    data['capital'].append( cols[1].get_text() )
    data['currency'].append( cols[2].get_text() )
    data['fx'].append( cols[3].get_text() )
    
fxData = pd.DataFrame( data )
fxData.to_csv("FXlist.csv")



##### METHOD 2

page = requests.get('http://www.science.co.il/International/Currency-codes.php')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')