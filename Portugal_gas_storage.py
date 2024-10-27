from bs4 import BeautifulSoup
import requests

url = 'https://datahub.ren.pt/en/natural-gas/monthly-balance/'
page = requests.get(url ,verify = False)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

table = soup.find_all('table')[3]
# print(table)

table_rows = table.find_all("td")
Final_table_rows = [rows.text.strip() for rows in table_rows]
print(Final_table_rows)