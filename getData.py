from curses import panel
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from collections import defaultdict


def create_csv(team: str) -> dict:

    target_url = "https://data.j-league.or.jp/SFIX02/search?displayId=SFIX02&selectValue=1&displayId=SFIX02&selectValueTeam=" + str(teams[team])
    r = requests.get(target_url)
    soup = BeautifulSoup(r.content, "html.parser")
    raw_data = soup.find_all("div", class_="box-info register-list")
    #print(raw_data)

    cols = ['birthday', 'not_used','birthplace', 'pre_team']
    data = defaultdict(list)

    for a in raw_data:
        print("========================================================")
        print(a.p.span.string)

        player_name = ''.join(a.p.span.string.split())
        data['name'].append(player_name)
        data['position'].append(a.dl.dd.string)

        attrs_data = a.dl.dd.find_next_siblings("dd")
        for i in range(4):
            if i == 1: # 身長体重はいらない
                continue
            data[cols[i]].append(attrs_data[i].string)


    return data




teams = {
    "Antlers" : 1,
    "Reds" : 3,
    "F-Marinos" : 5,
    "Espares" : 7,
    "Grampus" : 8,
    "Gamba" : 9,
    "Sanfrecce" : 10,
    "Reysol" : 11,
    "Bellmare" : 12,
    "Jubilo" : 13,
    "Consadole" : 14,
    "Vissel" : 18,
    "Cerezo" : 20,
    "Frontale" : 21,
    "FC-Tokyo" : 22,
    "Avispa" : 23,
    "Sanga" : 24,
    "Sagan" : 33
}

directory = '/Users/yudaikawano/Library/Mobile'+ ' ' + 'Documents/com~apple~CloudDocs/j-league/dataset/'

for team in list(teams.keys()):
    data = create_csv(team)
    df = pd.DataFrame(data=data)
    df.to_csv(directory + team + '.csv')






