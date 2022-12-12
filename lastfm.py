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

def create_artist_table(cur,conn,data_list):
    cur.execute("CREATE TABLE IF NOT EXISTS artist_table (artist_id INTEGER PRIMARY KEY, artist_name TEXT)")
    artist_list = ['Taylor Swift', "Justin Bieber", 'Drake', 'Adele']
    id = 1
    for i in artist_list:
        # artist_name = i[0]
        cur.execute("INSERT OR IGNORE INTO artist_table(artist_id, artist_name) VALUES (?,?)", (id, i))
        id+= 1
    conn.commit()

def create_compiled_table(cur,conn,data_list):
    cur.execute("CREATE TABLE IF NOT EXISTS compiled_table (id INTEGER PRIMARY KEY, artist_id INTEGER, song_title TEXT, rank INTEGER, playcount INTEGER, listeners INTEGER)")
    count = cur.execute("SELECT MAX(id) FROM compiled_table").fetchone()[0]
    if count == None:
        count = 0
    for i in range(count, count+25):
        try:
            # id = i
            artist_id = cur.execute("SELECT artist_id FROM artist_table WHERE artist_name = ?", (data_list[i][0], )).fetchone()[0]
            rank = data_list[i][1]
            song_title = data_list[i][2]
            playcount = data_list[i][3]
            listeners = data_list[i][4]
            cur.execute('INSERT OR IGNORE INTO compiled_table(id, artist_id, song_title, rank, playcount, listeners) VALUES (?,?,?,?,?,?)', (i, artist_id, song_title, rank, playcount, listeners))
        except:
            print('100 items exist')


    conn.commit()


def get_data():
    artist_list = ['taylorswift', 'justinbieber', 'drake', 'adele']
    global combined_all_data
    combined_all_data = []
    for i in artist_list:
        link = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={}&api_key={}&limit=25&format=json'.format(i,API_KEY)
        topsongdict = requests.get(link)
        dataArtist = json.loads(topsongdict.text)

        for obj in dataArtist["toptracks"]['track']:
            track_title = obj['name']
            artist = obj['artist']['name']
            playcount = int(obj['playcount'])
            listeners = int(obj['listeners'])
            rank = int(obj['@attr']['rank'])
            # song_id += 1
            tup1 = (artist, rank, track_title,playcount, listeners)
            combined_all_data.append(tup1)
    print(combined_all_data)
    return combined_all_data


def tables_visuals(cur, conn, data_list, show):

# first visualization: bar chart

    global perc_diff_list
    perc_diff_list = []
    playcount_list = []
    listeners_list = []
    global diff_list
    diff_list = []

    top_taylor = data_list[0]
    top_justin = data_list[25]
    top_drake = data_list[50]
    top_adele = data_list[75]
    data_tup = (top_taylor,top_justin,top_drake,top_adele)
    #print(data_tup)

    for i in data_tup:
        playcount = i[3]
        listeners = i[4]
        # print(playcount)
        # print(listeners)
        average = (playcount + listeners)/2
        diff = abs(playcount - listeners)
        perc_diff = (diff/average) * 100
        round_perc_diff = round(perc_diff, 2)
        #print(round_perc_diff)
        playcount_list.append(playcount)
        listeners_list.append(listeners)
        perc_diff_list.append(round_perc_diff)
        diff_list.append(diff)

    taylor = top_taylor[0]
    justin = top_justin[0]
    drake = top_drake[0]
    adele = top_adele[0]
    global artist_list
    artist_list = []
    artist_list.extend([taylor,justin,drake,adele])


    fig, ax = plt.subplots()

    N = 4
    width = 0.25
    ind = np.arange(N)

    p1 = ax.bar(ind, playcount_list, width, color = 'green')

    p2 = ax.bar(ind+width, listeners_list, width, color = 'blue')

    p3 = ax.bar(ind+0.505, diff_list, width, color = 'yellow')

    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(('Taylor Swift', 'Justin Bieber', 'Drake', 'Adele'))
    ax.legend((p1[0],p2[0],p3[0]), ('Playcount', 'Listeners','Difference'))
    ax.autoscale_view()

    ax.set(xlabel='Artist', ylabel='Amount', title = "Difference of Playcount vs. Listeners \n for Artists' Top Songs")

    ax.grid()

    plt.show()   

def second_visualization(data, show):
    box_plot_tup =[]
    taylor_playcount = []
    adele_playcount = []
    taylor_data = combined_all_data[0:25]
    for i in taylor_data:
        playcount_t = i[3]
        taylor_playcount.append(playcount_t)
    #print(taylor_playcount)
    adele_data = combined_all_data[75:]
    for i in adele_data:
        playcount_a = i[3]
        adele_playcount.append(playcount_a)

    data = [taylor_playcount, adele_playcount]

    plt.boxplot(data,patch_artist=True, labels=['Taylor Swift', 'Adele'])
    plt.title("Box Plot Comparing Taylor Swift vs. Adele \n Playcount for Top 25 Songs")    

    plt.show()

def writeFile(data, file_name):

    header = "Difference and Percent Difference of Playcount vs. Listeners for Artists' Top Songs"

    with open(file_name, "w") as f:
        f.write(header)
        f.write("\n")

        for i in range(len(artist_list)):
            f.write(artist_list[i] + ": " + str(diff_list[i]) + " Percent Difference = " + str(perc_diff_list[i]) + "%")
            f.write("\n")

def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('music.db')
    combined_all_data = get_data()
    create_artist_table(cur,conn,combined_all_data)
    create_compiled_table(cur,conn,combined_all_data)
    tables_visuals(cur, conn, combined_all_data, True)
    second_visualization(combined_all_data, True)
    writeFile(perc_diff_list, 'AlexData1.csv')

if __name__ == "__main__":
    main()