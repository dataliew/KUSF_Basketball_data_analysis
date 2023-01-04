import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

url = "https://www.kusf.or.kr/club/club_league_ranking_player.html?e_code=1&l_year=2020&l_code=108&t_code=&srch_word="

#Getting data in csv format
write_wb = Workbook()
writer_ws = write_wb.active

#Setting column names
columns_name = ["Matches", "Scores", "Assists", "Rebounds", "Steals", "Blocks", "2-pointers", "3-pointers", "Free_Throw"]
writer_ws.append(columns_name)

# Requesting to web server
res = requests.get(url)
res.raise_for_status()

# Generating soup object
soup = BeautifulSoup(res.text, "lxml")
StatBox = soup.find('tbody', attrs={"id": "LeagueStatsTable_table"})
Stats = StatBox.find_all('tr')


for stat in Stats:
    tds = stat.find_all('td')
    data_rows = []
    for td in tds[1:]:
        data_rows.append(td.text)
    writer_ws.append(data_rows)
write_wb.save('2020_finals_stat.xlsx')
