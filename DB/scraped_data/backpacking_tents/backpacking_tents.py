import requests
from bs4 import BeautifulSoup

url = 'https://gearatlas.com/compare-gear/backpacking_tents'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

gear_table = soup.find('table', class_ = "tablesorter")

for item in gear_table.find_all('tbody'):
    rows = item.find_all('tr')

    for row in rows:
        name = row.find_all('td')

        mainTitle = name[0].find('span', class_ = 'item_name').text

        msrp = row.find_all('td')[2].text.strip()

        weight = row.find_all('td')[4].text
        weight = " ".join(weight.split())

        capacity = row.find_all('td')[5].text.strip()

        volume = row.find_all('td')[6].text.strip()

        dimensions = row.find_all('td')[7].text.strip()
        dimensions = " ".join(dimensions.split())

        packedSize = row.find_all('td')[8].text.strip()

        vestibuleVolume = row.find_all('td')[9].text.strip()

        print(mainTitle + ', ' + msrp + ', ' + weight + ', ' + capacity + ', ' + volume+ ', ' + dimensions + ', ' + packedSize + ', ' + vestibuleVolume)


