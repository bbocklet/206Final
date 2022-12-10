import sqlite3
import requests
import json
# import jwt
import os
import matplotlib.pyplot as plt
import numpy as np

API_KEY = 'c5b2c0372bedaf0f1f2f3f6415b95d57'
USER_AGENT = 'Dataquest'

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def create_taylor_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS taylor_table3 (song_id INTEGER, artist TEXT, rank INTEGER, track_title TEXT PRIMARY KEY,playcount INTEGER, listeners INTEGER)")
    conn.commit()

def create_justin_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS justin_table3 (song_id INTEGER, artist TEXT, rank INTEGER, track_title TEXT PRIMARY KEY,playcount INTEGER, listeners INTEGER)")
    conn.commit()

def create_drake_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS drake_table3 (song_id INTEGER, artist TEXT, rank INTEGER, track_title TEXT PRIMARY KEY,playcount INTEGER, listeners INTEGER)")
    conn.commit()

def create_adele_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS adele_table3 (song_id INTEGER, artist TEXT, rank INTEGER, track_title TEXT PRIMARY KEY,playcount INTEGER, listeners INTEGER)")
    conn.commit()

def get_taylor_data(cur,conn):
    link = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=taylorswift&api_key={}&limit=25&format=json'.format(API_KEY)
    topsongdict_taylor = requests.get(link)
    dataTaylor = topsongdict_taylor.json()

    song_id = cur.execute('SELECT COUNT(song_id) FROM taylor_table3').fetchone()[0] + 1
    start = song_id
    print(dataTaylor)
    global data_list
    data_list = []
    song_id = 0
    for obj in dataTaylor["toptracks"]['track']:
        track_title = obj['name']
        artist = obj['artist']['name']
        playcount = int(obj['playcount'])
        listeners = int(obj['listeners'])
        rank = int(obj['@attr']['rank'])
        song_id += 1
        tup1 = (song_id,artist, rank, track_title,playcount, listeners)
        print(tup1)
        data_list.append(tup1)

        cur.execute('INSERT OR IGNORE INTO taylor_table3 (song_id, artist, rank, track_title, playcount, listeners) VALUES (?,?,?,?,?,?)', (song_id, artist, rank, track_title, playcount, listeners))

    #print(data_list)
    # return(data_list)

    conn.commit()

        # cur.execute('INSERT OR IGNORE INTO taylortable (rank, track_title, playcount, listeners) VALUES (?,?,?,?)', (rank, track_title, playcount, listeners))

def get_justin_data(cur,conn):
    link = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=justinbieber&api_key={}&limit=25&format=json'.format(API_KEY)
    topsongdict_justin = requests.get(link)
    dataJustin = topsongdict_justin.json()

    song_id = cur.execute('SELECT COUNT(song_id) FROM justin_table3').fetchone()[0] + 1
    start = song_id
    global data_list
    data_list = []
    song_id = 25
    for obj in dataJustin["toptracks"]['track']:
        track_title = obj['name']
        artist = obj['artist']['name']
        playcount = int(obj['playcount'])
        listeners = int(obj['listeners'])
        rank = int(obj['@attr']['rank'])
        song_id += 1
        tup1 = (song_id, artist, rank, track_title,playcount, listeners)
        print(tup1)
        data_list.append(tup1)

        cur.execute('INSERT OR IGNORE INTO justin_table3 (song_id, artist, rank, track_title, playcount, listeners) VALUES (?,?,?,?,?,?)', (song_id, artist, rank, track_title, playcount, listeners))

    conn.commit()


def get_drake_data(cur,conn):
    link = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=drake&api_key={}&limit=25&format=json'.format(API_KEY)
    topsongdict_drake = requests.get(link)
    dataDrake = topsongdict_drake.json()

    song_id = cur.execute('SELECT COUNT(song_id) FROM drake_table3').fetchone()[0] + 1
    start = song_id
    global data_list
    data_list = []
    song_id = 50
    for obj in dataDrake["toptracks"]['track']:
        track_title = obj['name']
        artist = obj['artist']['name']
        playcount = int(obj['playcount'])
        listeners = int(obj['listeners'])
        rank = int(obj['@attr']['rank'])
        song_id += 1
        tup1 = (song_id, artist, rank, track_title,playcount, listeners)
        print(tup1)
        data_list.append(tup1)

        cur.execute('INSERT OR IGNORE INTO drake_table3 (song_id, artist, rank, track_title, playcount, listeners) VALUES (?,?,?,?,?,?)', (song_id, artist, rank, track_title, playcount, listeners))

    conn.commit()

def get_adele_data(cur,conn):
    link = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=adele&api_key={}&limit=25&format=json'.format(API_KEY)
    topsongdict_adele = requests.get(link)
    dataAdele = topsongdict_adele.json()

    song_id = cur.execute('SELECT COUNT(song_id) FROM adele_table3').fetchone()[0] + 1
    start = song_id
    global data_list
    data_list = []
    song_id = 75
    for obj in dataAdele["toptracks"]['track']:
        track_title = obj['name']
        artist = obj['artist']['name']
        playcount = int(obj['playcount'])
        listeners = int(obj['listeners'])
        rank = int(obj['@attr']['rank'])
        song_id += 1
        tup1 = (song_id, artist,rank, track_title,playcount, listeners)
        print(tup1)
        data_list.append(tup1)

        cur.execute('INSERT OR IGNORE INTO adele_table3 (song_id, artist, rank, track_title, playcount, listeners) VALUES (?,?,?,?,?,?)', (song_id, artist, rank, track_title, playcount, listeners))

    conn.commit()

def joiningTables(cur, conn):

    # joinThis = cur.execute("SELECT taylor_table3.song_id, taylor_table3.artist, taylor_table3.track_title,taylor_table3.playcount, taylor_table3.listeners, justin_table3.song_id, justin_table3.artist, justin_table3.track_title,justin_table3.playcount, justin_table3.listeners FROM taylor_table3 JOIN justin_table3 ON justin_table3.rank = taylor_table3.rank")
    joinThis = cur.execute('INSERT INTO taylor_table3(song_id, artist, rank, track_title, playcount, listeners) SELECT song_id, artist, rank, track_title, playcount, listeners FROM justin_table3')
    joinThis2 = cur.execute('INSERT INTO taylor_table3(song_id, artist, rank, track_title, playcount, listeners) SELECT song_id, artist, rank, track_title, playcount, listeners FROM drake_table3')
    joinThis3 = cur.execute('INSERT INTO taylor_table3(song_id, artist, rank, track_title, playcount, listeners) SELECT song_id, artist, rank, track_title, playcount, listeners FROM adele_table3')

    conn.commit()

    # names_and_dates = joinThis.fetchall()

    # print(names_and_dates)

def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('music.db')
    create_taylor_table(cur, conn)
    get_taylor_data(cur, conn)
    create_justin_table(cur, conn)
    get_justin_data(cur,conn)
    create_drake_table(cur,conn)
    get_drake_data(cur,conn)
    create_adele_table(cur, conn)
    get_adele_data(cur,conn)
    joiningTables(cur, conn)

if __name__ == "__main__":
    main()
