import requests 
import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_taylorHarry_table(cur, conn):
    # cur.execute("drop table if exists taylorHarry")
    cur.execute("CREATE TABLE IF NOT EXISTS taylorHarry (song_id INTEGER, artist_id INTEGER, trackName TEXT PRIMARY KEY, album_id INTEGER, releaseDate TEXT)")
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
        releaseDate = obj['releaseDate']
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
    # print(dataTaylor)
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id
    harryStart = start // 5
    harryEnd = harryStart + 5

    for obj in dataHarry["results"][harryStart:harryEnd]:
        trackName = obj["trackName"]
        artistName= obj["artistName"]
        album = obj['collectionName']
        releaseDate = obj['releaseDate']
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
    # print(dataTaylor)
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id
    drakeStart = start // 5
    drakeEnd = drakeStart + 5

    if song_id == 85:
        drakeEnd = drakeStart + 6
        for obj in dataDrake["results"][drakeStart:drakeEnd]:
            trackName = obj["trackName"]
            artistName= obj["artistName"]
            album = obj['collectionName']
            releaseDate = obj['releaseDate']
            artist_id = obj['artistId']
            album_id = obj['collectionId']

            cur.execute('INSERT OR IGNORE INTO artist (artist_id, artistsName) VALUES (?,?)', ( artist_id, artistName))

            cur.execute('INSERT OR IGNORE INTO albums (album_id, albumName) VALUES (?,?)', ( album_id, album))

            cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artist_id, trackName, album_id, releaseDate) VALUES (?,?,?,?,?)', (song_id, artist_id, trackName, album_id, releaseDate))

            song_id += 1
    
    else:
        for obj in dataDrake["results"][drakeStart:drakeEnd]:
            trackName = obj["trackName"]
            artistName= obj["artistName"]
            album = obj['collectionName']
            releaseDate = obj['releaseDate']
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
        releaseDate = obj['releaseDate']
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
        releaseDate = obj['releaseDate']
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
    # print(dataNoah)
    
    song_id = cur.execute('SELECT COUNT(song_id) FROM taylorHarry').fetchone()[0] + 1
    start = song_id
    macStart = start // 5
    macEnd = macStart + 5

    for obj in dataMac["results"][macStart:macEnd]:
        trackName = obj["trackName"]
        artistName= obj["artistName"]
        album = obj['collectionName']
        releaseDate = obj['releaseDate']
        artist_id = obj['artistId']
        album_id = obj['collectionId']

        cur.execute('INSERT OR IGNORE INTO artist (artist_id, artistsName) VALUES (?,?)', ( artist_id, artistName))

        cur.execute('INSERT OR IGNORE INTO albums (album_id, albumName) VALUES (?,?)', ( album_id, album))

        cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artist_id, trackName, album_id, releaseDate) VALUES (?,?,?,?,?)', (song_id, artist_id, trackName, album_id, releaseDate))

        song_id += 1

      
    conn.commit()


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

if __name__ == "__main__":
    main()


    #  check data to database, insert 25 into database at a time
    # select max or select count from the column 
    #  im going to insert -- make sure not duplicated!!


    #  when end > 50, go to 50 rather than end
    # read in artist and album, create those tables first -- where you are inserting the artist into the table, i need to use JOIN