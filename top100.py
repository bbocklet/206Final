from xml.sax import parseString
from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import sqlite3
import json
import unittest
import matplotlib.pyplot as plt


r = requests.get("https://acharts.co/us_singles_top_100")
data = BeautifulSoup(r.text, "html.parser")
top_list = []

top_data = data.find_all("td", class_="cPrinciple")

for td_tag in top_data:
    song_name = td_tag.find("span", itemprop="name")
    artist_name = td_tag.find("span", itemprop='byArtist')
    if song_name != None:
        top_list.append((song_name.text.strip(), artist_name.text.strip()))
        
# print(top_list)


def create_topchart_table(cur, conn):
    cur.execute('create table if not exists topChart (song_id INTEGER PRIMARY KEY, song TEXT, artist_id INTEGER)')
    conn.commit()

def create_artist_id(cur, conn):
    cur.execute('create table if not exists artistID (artist_id INTEGER PRIMARY KEY, artist TEXT UNIQUE)')
    conn.commit()


def add_artist_data(cur, conn):
    start = cur.execute('SELECT MAX(artist_id) FROM artistID').fetchone()[0]
    if start is None:
        start = 0
    print(start)
    end = start + 25
    id = start + 1
    for item in range(start,end):
        try:
            artist = top_list[item][1]
            artist_id = id
            cur.execute('insert or ignore into artistID (artist_id, artist) values (?,?)', (artist_id, artist))
            id+=1
        except:
            print('exceeds 74 items')
       
        
    conn.commit()

def add_data(cur, conn):
    try:
        start = cur.execute('SELECT song_id FROM topChart').fetchall()[-1][0] + 1
    except:
        start = 0
    song_id = start
    end = start + 25

    for item in top_list[start:end]:
        songs = item[0]
        artist_id = cur.execute('SELECT artist_id FROM artistID WHERE artist = ?', (item[1],)).fetchone()
        if artist_id is None:
            continue
        else:
            artist_id = artist_id[0]
            cur.execute('insert or ignore into topChart (song_id, song, artist_id) values (?,?,?)', (song_id, songs, artist_id))
            song_id += 1
    conn.commit()

def join_tables(cur, conn):
    cur.execute("SELECT artistID.artist, topChart.artist_id FROM artistID JOIN topChart ON topChart.artist_id = artistID.artist_id")
    conn.commit()
    info = cur.fetchall()
    # print(info)

# calculations: artists with 2 or more songs in the top 100 chart 
artist_count = {}
for item in top_list:
    if item[1] in artist_count:
        artist_count[item[1]] += 1
    else:
        artist_count[item[1]] = 1
# print(artist_count)

over_two = {}
for item in artist_count:
    if artist_count[item] >= 2:
        over_two[item] = artist_count[item]
# print(over_two)

total = 0
for item in over_two:
    total += over_two[item]
# print(total)

percent_dict = {}
for item in over_two:
    percent_dict[item] = round(((over_two[item] / total) * 100), 2)
print(percent_dict)

def writeFile(percent_dict, file_name):

    header = "Artists with 2 or More Songs in the Top Charts by Percent"

    with open(file_name, "w") as f:
        f.write(header)
        f.write("\n")
        for artist in percent_dict:
            f.write(artist + ": " + str(percent_dict[artist]) + "%")
            f.write("\n")


# Pie chart
labels = 'Taylor Swift', 'Drake', 'Nat King Cole', 'Morgan Wallen', 'Gene Autry', 'Lizzo', 'Bailey Zimmerman', 'Lil Baby'
sizes = [26.47, 35.29, 5.88, 5.88, 5.88, 5.88, 5.88, 8.82]
explode = (0, 0, 0, 0, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90, colors=['#c24040', '#d67c45', '#e3b946', '#a7e346', '#46e3e3', '#4a4fa8', '#8f62d1', '#ed79d8'])
ax1.axis('equal')  

plt.show()

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/music.db')
    cur = conn.cursor()
    create_artist_id(cur, conn)
    add_artist_data(cur, conn)
    create_topchart_table(cur, conn)
    add_data(cur, conn)
    join_tables(cur, conn)

    conn.close()
    writeFile(percent_dict, "aishaniData.csv")

main()