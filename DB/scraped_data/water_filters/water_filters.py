import requests
from bs4 import BeautifulSoup

url = 'https://gearatlas.com/compare-gear/hiking_and_backpacking_water_filter'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

gear_table = soup.find('table', class_ = "tablesorter")

for item in gear_table.find_all('tbody'):
    rows = item.find_all('tr')

    for row in rows:
        name = row.find_all('td')[0].text
        msrp = row.find_all('td')[2].text
        weight = row.find_all('td')[4].text
        use_case = str(row.find_all('td')[5].text).replace(',', ' |')
        method = row.find_all('td')[6].text
        output = row.find_all('td')[7].text

        print(name + ', ' + msrp + ', ' + weight + ', ' + use_case + ', ' + method + ', ' + output)
