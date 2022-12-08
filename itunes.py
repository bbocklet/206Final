import requests 
import unittest
import sqlite3
import json
import csv
import os
import matplotlib.pyplot as plt

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_taylorHarry_table(cur, conn):
    # cur.execute("drop table if exists taylorHarry")
    cur.execute("CREATE TABLE IF NOT EXISTS taylorHarry (song_id INTEGER, artist_id INTEGER, trackName TEXT PRIMARY KEY, album_id INTEGER, releaseDate INTEGER)")
    conn.commit()
    pass

def create_artist_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS artist (artist_id INTEGER PRIMARY KEY, artistsName TEXT)")
    conn.commit()
    pass

def create_album_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS albums (album_id INTEGER PRIMARY KEY, albumName TEXT)")
    conn.commit()
    pass

def taylorData(cur, conn):
    responseTaylor = requests.get('https://itunes.apple.com/search?', params= 
                            {'term': 'Taylor Swift','media' : 'music'})

    dataTaylor = responseTaylor.json()
    # print(dataTaylor)
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id
    taylorStart = start // 5
    taylorEnd = taylorStart + 5

    for obj in dataTaylor["results"][taylorStart:taylorEnd]:
        trackName = obj["trackName"]
        artistName= obj["artistName"]
        album = obj['collectionName']
        releaseDate = int(obj['releaseDate'][:4])
        artist_id = obj['artistId']
        album_id = obj['collectionId']

        cur.execute('INSERT OR IGNORE INTO artist (artist_id, artistsName) VALUES (?,?)', ( artist_id, artistName))

        cur.execute('INSERT OR IGNORE INTO albums (album_id, albumName) VALUES (?,?)', ( album_id, album))

        cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artist_id, trackName, album_id, releaseDate) VALUES (?,?,?,?,?)', (song_id, artist_id, trackName, album_id, releaseDate))

        song_id += 1
        
        
    conn.commit()

def harryData(cur, conn):
    responseHarry = requests.get('https://itunes.apple.com/search?', params= 
                            {'term': 'Harry Styles','media' : 'music'})

    dataHarry = responseHarry.json()
    
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id
    harryStart = start // 5
    harryEnd = harryStart + 5

    for obj in dataHarry["results"][harryStart:harryEnd]:
        trackName = obj["trackName"]
        artistName= obj["artistName"]
        album = obj['collectionName']
        releaseDate = int(obj['releaseDate'][:4])
        artist_id = obj['artistId']
        album_id = obj['collectionId']

        cur.execute('INSERT OR IGNORE INTO artist (artist_id, artistsName) VALUES (?,?)', ( artist_id, artistName))

        cur.execute('INSERT OR IGNORE INTO albums (album_id, albumName) VALUES (?,?)', ( album_id, album))

        cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artist_id, trackName, album_id, releaseDate) VALUES (?,?,?,?,?)', (song_id, artist_id, trackName, album_id, releaseDate))

        song_id += 1

      
    conn.commit()


def drakeData(cur, conn):
    responseHarry = requests.get('https://itunes.apple.com/search?', params= 
                            {'term': 'Drake','media' : 'music'})

    dataDrake = responseHarry.json()
    
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id
    drakeStart = start // 5
    drakeEnd = drakeStart + 5

    for obj in dataDrake["results"][drakeStart:drakeEnd]:
        trackName = obj["trackName"]
        artistName= obj["artistName"]
        album = obj['collectionName']
        releaseDate = int(obj['releaseDate'][:4])
        artist_id = obj['artistId']
        album_id = obj['collectionId']

        cur.execute('INSERT OR IGNORE INTO artist (artist_id, artistsName) VALUES (?,?)', ( artist_id, artistName))

        cur.execute('INSERT OR IGNORE INTO albums (album_id, albumName) VALUES (?,?)', ( album_id, album))

        cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artist_id, trackName, album_id, releaseDate) VALUES (?,?,?,?,?)', (song_id, artist_id, trackName, album_id, releaseDate))

        song_id += 1

      
    conn.commit()


def noahData(cur, conn):
    responseHarry = requests.get('https://itunes.apple.com/search?', params= 
                            {'term': 'Noah Kahan','media' : 'music'})

    dataNoah = responseHarry.json()
    # print(dataNoah)
    
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id
    noahStart = start // 5
    noahEnd = noahStart + 5

    for obj in dataNoah["results"][noahStart:noahEnd]:
        trackName = obj["trackName"]
        artistName= obj["artistName"]
        album = obj['collectionName']
        releaseDate = int(obj['releaseDate'][:4])
        artist_id = obj['artistId']
        album_id = obj['collectionId']

        cur.execute('INSERT OR IGNORE INTO artist (artist_id, artistsName) VALUES (?,?)', ( artist_id, artistName))

        cur.execute('INSERT OR IGNORE INTO albums (album_id, albumName) VALUES (?,?)', ( album_id, album))

        cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artist_id, trackName, album_id, releaseDate) VALUES (?,?,?,?,?)', (song_id, artist_id, trackName, album_id, releaseDate))

        song_id += 1

      
    conn.commit()


def macData(cur, conn):
    responseHarry = requests.get('https://itunes.apple.com/search?', params= 
                            {'term': 'Mac Miller','media' : 'music'})

    dataMac = responseHarry.json()

    
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id
    macStart = start // 5
    macEnd = macStart + 5

    for obj in dataMac["results"][macStart:macEnd]:
        trackName = obj["trackName"]
        artistName= obj["artistName"]
        album = obj['collectionName']
        releaseDate = int(obj['releaseDate'][:4])
        artist_id = obj['artistId']
        album_id = obj['collectionId']

        cur.execute('INSERT OR IGNORE INTO artist (artist_id, artistsName) VALUES (?,?)', ( artist_id, artistName))

        cur.execute('INSERT OR IGNORE INTO albums (album_id, albumName) VALUES (?,?)', ( album_id, album))

        cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artist_id, trackName, album_id, releaseDate) VALUES (?,?,?,?,?)', (song_id, artist_id, trackName, album_id, releaseDate))

        song_id += 1

      
    conn.commit()


# Here is where I want to do calculations and JOIN the artist table with the taylorHarry and the release date -- then for my calculation, I want to take the releaseDate and see which artist released the most in which year


def join_calc_visual(cur, conn):

    cur.execute("SELECT artist.artistsName, taylorHarry.artist_id, taylorHarry.releaseDate FROM artist JOIN taylorHarry ON taylorHarry.artist_id = artist.artist_id")
    conn.commit()

    names_and_dates = cur.fetchall()

    # print(names_and_dates)

    theMost = {}
    totalSongs = 0

# calculating who released the most music in 2012-22
    for tuple in names_and_dates:
        if tuple[2] == 2012:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2013:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2014:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2015:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2016:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2017:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2018:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2019:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2020:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2021:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
        if tuple[2] == 2022:
            if tuple[0] not in theMost:
                theMost[tuple[0]] = 0
            theMost[tuple[0]] += 1
            totalSongs += 1
    
    # print(theMost)
    # print(totalSongs)

    percentages = {}
# taking the total percentage
    for key in theMost:
        percentages[key] = round((theMost[key] / totalSongs) * 100,2)

# make the pie chart values according to values in the percentages dictionary

    if 'Taylor Swift' in theMost.keys():
        taylorVal = percentages['Taylor Swift']
    else:
        taylorVal = 0

    if 'One Direction' in theMost.keys():
        oneVal = percentages['One Direction']
    else:
        oneVal = 0

    if 'Harry Styles' in theMost.keys():
        harryVal = percentages['Harry Styles']
    else:
        harryVal = 0

    if 'Drake' in theMost.keys():
        drakeVal = percentages['Drake']
    else:
        drakeVal = 0
    
    if 'Gryffin, Seven Lions & Noah Kahan' in theMost.keys():
        noahVal2 = percentages['Gryffin, Seven Lions & Noah Kahan']
    else:
        noahVal2 = 0

    if 'Noah Kahan' in theMost.keys():
        noahVal = percentages['Noah Kahan']
    else:
        noahVal = 0
    
    if 'Mac Miller' in theMost.keys():
        macVal = percentages['Mac Miller']
    else:
        macVal = 0



    labels = 'Taylor Swift', 'One Direction', 'Harry Styles', 'Drake', 'Gryffin, Seven Lions & Noah Kahan', 'Noah Kahan', 'Mac Miller'
    sizes = [taylorVal, oneVal, harryVal, drakeVal, noahVal2, noahVal, macVal]
    explode = (0, 0, 0, 0, 0, 0, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    return percentages


def second_calc_visual(cur, conn):
    cur.execute("SELECT taylorHarry.album_id, taylorHarry.trackName, albums.albumName FROM artist JOIN taylorHarry ON taylorHarry.album_id = albums.album_id")
    conn.commit()

    albums_and_songs = cur.fetchall()

    print(albums_and_songs)
     

def writeFile(data, file_name):

    header = "Artists Contribution to Music 2012-2022 by Percent"

    with open(file_name, "w") as f:
        f.write(header)
        f.write("\n")
        for artist in data:
            f.write(artist + ": " + str(data[artist]) + "%")
            f.write("\n")




def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('music.db')
    create_taylorHarry_table(cur, conn)
    create_artist_table(cur, conn)
    create_album_table(cur, conn)
    taylorData(cur, conn)
    harryData(cur, conn)
    drakeData(cur, conn)
    noahData(cur, conn)
    macData(cur, conn)
    writeFile(join_calc_visual(cur, conn), "blairData.csv")
    join_calc_visual(cur, conn)
    # second_calc_visual(cur, conn)

if __name__ == "__main__":
    main()

