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
    cur.execute("CREATE TABLE IF NOT EXISTS taylorHarry (song_id INTEGER PRIMARY KEY, artistsName TEXT, trackName TEXT, album TEXT, releaseDate TEXT)")
    conn.commit()
    pass

# Artist One - Taylor Swift -- gives 50 songs
def taylorData(cur, conn):
    responseTaylor = requests.get('https://itunes.apple.com/search?', params= 
                            {'term': 'Taylor Swift','media' : 'music'})

    dataTaylor = responseTaylor.json()
    # print(dataTaylor)
    song_id = 1
    current = 1
    end = 25

    for obj in dataTaylor["results"]:
        while current < end:
            trackName = obj["trackName"]
            artistName= obj["artistName"]
            album = obj['collectionName']
            releaseDate = obj['releaseDate']

            cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artistsName, trackName, album, releaseDate) VALUES (?,?,?,?,?)', (song_id, artistName, trackName, album, releaseDate))
                
            song_id += 1
        current += 1
        
    
    conn.commit()

# Artist Two - Harrry Styles -- gives 50 songs
def harryData(cur, conn):
    responseHarry = requests.get('https://itunes.apple.com/search?', params= 
                            {'term': 'Harry Styles','media' : 'music'})

    dataHarry = responseHarry.json()

    song_id = 51
    for obj in dataHarry["results"]:
        artistName= obj["artistName"]
        trackName = obj["trackName"]
        album = obj['collectionName']
        releaseDate = obj['releaseDate']

        print(song_id, artistName, trackName, album, releaseDate)

        cur.execute('INSERT OR IGNORE INTO taylorHarry (song_id, artistsName, trackName, album, releaseDate) VALUES (?,?,?,?,?)', (song_id, artistName, trackName, album, releaseDate))

        song_id += 1
    
    conn.commit()


def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('music.db')
    create_taylorHarry_table(cur, conn)
    taylorData(cur, conn)
    harryData(cur, conn)

if __name__ == "__main__":
    main()


    #  check data to database, insert 25 into database at a time
    # select max or select count from the column 
    #  im going to insert -- make sure not duplicated!!