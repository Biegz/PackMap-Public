import requests
from bs4 import BeautifulSoup

url = 'https://gearatlas.com/compare-gear/headlamp'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

gear_table = soup.find('table', class_ = "tablesorter")

for item in gear_table.find_all('tbody'):
    rows = item.find_all('tr')

    for row in rows:
        name = row.find_all('td')[0].text.strip()
        msrp = row.find_all('td')[2].text.strip()
        weight = row.find_all('td')[4].text
        # weight = weight.replace(' ', '')
        #weight = weight.rstrip()

        # tmp = ""
        # for line in str(weight).split("\n"):
        #     tmp = line.rstrip()

        #weight = str(weight).replace(" ", "")
        weight = " ".join(weight.split())

        #weight = weight.replace("\n", "" "")
        max_lumens = row.find_all('td')[5].text.strip()
        max_beam_distance = row.find_all('td')[6].text.strip()
        max_run_time = row.find_all('td')[7].text.strip()
        battery_type = row.find_all('td')[8].text.strip()

        print(name + ', ' + msrp + ', ' + weight + ', ' + max_lumens + ', ' + max_beam_distance + ', ' + max_run_time + ', ' + battery_type)
