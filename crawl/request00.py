import requests
import sys
from bs4 import BeautifulSoup
from kleaguestats.players.daejeon2023 import basicURL, dhc2023gk, dhc2023mf, dhc2023fw

# 골키퍼 정보 모두 다 가져오기

# for el in dhc2023gk:
#     url1 = basicURL+str(dhc2023gk[el])
#     response = requests.get(url1)
#     print(f"{el} : " + url1)
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')

url2 = basicURL+str(dhc2023gk["이창근"])
response = requests.get(url2)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
totalApp = soup.select_one("body > div.searchDataset.sub-team-table > div > table:nth-child(9) > tbody > tr:nth-child(3) > td:nth-child(3)")

print(totalApp)