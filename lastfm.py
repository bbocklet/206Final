import sqlite3
import requests
import json
# import jwt
import os
import matplotlib.pyplot as plt
import numpy as np

API_KEY = 'c5b2c0372bedaf0f1f2f3f6415b95d57'
USER_AGENT = 'Dataquest'


link = "http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=taylorswift&api_key={}&format=json".format(API_KEY)
newdict = requests.get(link)
lastfmdata = newdict.json()
print(lastfmdata)

