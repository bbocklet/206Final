import requests 
import unittest
import sqlite3
import json
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# Crating a database called music.db
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Creating a table called taylorHarry which will hold song, year, artist, album
def create_taylorHarry_table(cur, conn):
    # cur.execute("drop table if exists taylorHarry")
    cur.execute("CREATE TABLE IF NOT EXISTS taylorHarry (song_id INTEGER, artist_id INTEGER, trackName TEXT PRIMARY KEY, album_id INTEGER, releaseDate INTEGER)")
    conn.commit()
    pass

# To prevent string duplicates in artist, this table matches an artist name to an artist id
def create_artist_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS artist (artist_id INTEGER PRIMARY KEY, artistsName TEXT)")
    conn.commit()
    pass

# To prevent string duplicates in album, this table matches an album name to an album id
def create_album_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS albums (album_id INTEGER PRIMARY KEY, albumName TEXT)")
    conn.commit()
    pass

# Calling to the itunes api to get Taylor Swift data
def taylorData(cur, conn):
    responseTaylor = requests.get('https://itunes.apple.com/search?', params= 
                            {'term': 'Taylor Swift','media' : 'music'})

    dataTaylor = responseTaylor.json()
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id

    # start is divided by 5 since I am calling 5 at a time, when I run the code the next time, I want to pick back up where I left off
    taylorStart = start // 5

    # since i want to end 5 entries later, i am only adding 5 entries from my starting point
    taylorEnd = taylorStart + 5

    for obj in dataTaylor["results"][taylorStart:taylorEnd]:
        trackName = obj["trackName"]
        artistName= obj["artistName"]
        album = obj['collectionName']
        releaseDate = int(obj['releaseDate'][:4])
        artist_id = obj['artistId']
        album_id = obj['collectionId']

    # inserting data into my three tables
        cur.execute('INSERT OR IGNORE INTO artist (artist_id, artistsName) VALUES (?,?)', ( artist_id, artistName))

        cur.execute('INSERT OR IGNORE INTO albums (album_id, albumName) VALUES (?,?)', ( album_id, album))

        cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artist_id, trackName, album_id, releaseDate) VALUES (?,?,?,?,?)', (song_id, artist_id, trackName, album_id, releaseDate))

        song_id += 1
        
        
    conn.commit()

# Calling to the itunes api to get Harry Styles data
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

# Calling to the itunes api to get Drake data
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

# Calling to the itunes api to get Noah Kahan data
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

# Calling to the itunes api to get Mac Miller data
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


# This function joins files, performs a calculation, and generates a visual
def join_calc_visual(cur, conn, show):

    # joining the artist name, artist ID, and the songs release date
    cur.execute("SELECT artist.artistsName, taylorHarry.artist_id, taylorHarry.releaseDate FROM artist JOIN taylorHarry ON taylorHarry.artist_id = artist.artist_id")
    conn.commit()

    names_and_dates = cur.fetchall()

    # print(names_and_dates)

    theMost = {}
    totalSongs = 0

    # calculating who released the most music in 2012-22 by using a dictionary and incrementing it by one for each song and increasing the total song count each entry into the dictionary 
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

    # Now I am taking the above data, converting it to a percentage, and putting it into a new dictionary 
    for key in theMost:
        percentages[key] = round((theMost[key] / totalSongs) * 100,2)

    # Assigning the values from the dictionary to variables
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


    # Making my first visualization, a pie chart with percent of total songs released in 2012-2022
    labels = 'Taylor Swift', 'One Direction', 'Harry Styles', 'Drake', 'Gryffin, Seven Lions & Noah Kahan', 'Noah Kahan', 'Mac Miller'
    sizes = [taylorVal, oneVal, harryVal, drakeVal, noahVal2, noahVal, macVal]
    explode = (0, 0, 0, 0, 0, 0, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=["#BC4B51","#DD614A", "#F7CB15", "#2A4494", "#76BED0", "#D2D6EF", "#85CC66"])
    ax1.axis('equal') 

    plt.title("Artists Contribution to Music \n" + "2012-2022 by Percent", size=8, weight = 'bold')

    if show == True:
        plt.show()
    
    return percentages


# Chart showing songs per album for Taylor Swift
def second_calc_visual(cur, conn):

    # Joining the album, artisr, and trackName
    cur.execute("SELECT albums.albumName, taylorHarry.artist_id, taylorHarry.trackName FROM albums JOIN taylorHarry ON taylorHarry.album_id = albums.album_id")
    conn.commit()

    albums_and_songs = cur.fetchall()

    albums = {}
    # print(albums_and_songs)

    # If the artist ID matches Taylor Swift, I add the album name to a dictionary and increment the count for each song on that album
    for tup in albums_and_songs:
        if tup[1] == 159260351:
            if tup[0] not in albums:
                albums[tup[0]] = 0
            albums[tup[0]] += 1
    
    # print(albums)

    # Making a bar graph of songs per Taylor Swift album
    albumList = []
    songValues = []
    for key in albums:
        albumList.append(key)
        songValues.append(albums[key])

    fig, ax = plt.subplots()

    albumChart = albumList
    songChart = songValues
    bar_labels = albumList

    ax.bar(albumChart, songChart, label=bar_labels, color=["#2A4494", "#F7CB15"])
    plt.xticks(albumChart, rotation=5,size = 6)

    ax.set_ylabel('Number of Songs')
    ax.set_title('Songs Per Album by Taylor Swift 2012-2022')


    plt.show()    

# Writing my calculations of artists percentage to total songs in 2012-22 into a csv file
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
    writeFile(join_calc_visual(cur, conn, False), "blairData.csv")
    join_calc_visual(cur, conn, True)
    second_calc_visual(cur, conn)

if __name__ == "__main__":
    main()

