import requests
from bs4 import BeautifulSoup

url = 'https://gearatlas.com/compare-gear/mens_backpacks_for_day_hikes'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

gear_table = soup.find('table', class_ = "tablesorter")

for item in gear_table.find_all('tbody'):
    rows = item.find_all('tr')

    for row in rows:
        name = row.find_all('td')

        mainTitle = name[0].find('span', class_ = 'item_name').text

        subTitle = name[0].find('span', class_ = 'note').text
        subTitle = str(subTitle).replace(',', ' |')

        msrp = row.find_all('td')[2].text.strip()

        weight = row.find_all('td')[4].text
        weight = " ".join(weight.split())

        capacity = row.find_all('td')[5].text.strip()
        capacity = " ".join(capacity.split())

        recomWeight = row.find_all('td')[6].text.strip()

        print(mainTitle + ', ' + subTitle + ', ' + msrp + ', ' + weight + ', ' + capacity + ', ' + recomWeight)


