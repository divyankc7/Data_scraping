from bs4 import BeautifulSoup
import requests

url = 'https://datahub.ren.pt/en/natural-gas/monthly-balance/'
page = requests.get(url ,verify = False)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

table = soup.find_all('div', class = "scrollOuter table")
print(table)

table_rows = table.find_all("tr")
print(table_rows)