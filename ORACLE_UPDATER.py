import scipy
import os
import requests
import json
import time
import sqlite3

# download rate
rate = 1 # in minutes

def json_to_sqlite_input(json_file, db_file="./SQLITE_DB/data.db"):
    with open(json_file) as f:
        data = json.load(f)

    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.executemany("INSERT INTO data_in VALUES(?,?,?,?,?,?,?,?,?,?,?,?",data)

    conn.commit()
    conn.close()

def json_to_sqlite_validate(json_file, db_file="./SQLITE_DB/data.db"):
    with open(json_file) as f:
        data = json.load(f)

    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.executemany("INSERT INTO data_in VALUES(?,?,?,?",data)

    conn.commit()
    conn.close()

def getJSON_input_temp():
    input_url = "https://services.swpc.noaa.gov/json/dscovr/dscovr_mag_1s.json"
    response = requests.get(input_url)
    response.raise_for_status()
    with open("./JSON_TEMP/input_temp.json","w") as f:
        f.write(response.text)

def getJSON_validation_temp():
    validation_url = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
    response = requests.get(validation_url)
    response.raise_for_status()
    with open("./JSON_TEMP/validation_temp.json","w") as f:
        f.write(response.text)

while True:
    getJSON_input_temp()
    json_to_sqlite_input("./JSON_TEMP/input_temp.json","./SQLITE_DB/data.db")
    getJSON_validation_temp()
    json_to_sqlite_validate("./JSON_TEMP/validation_temp.json","./SQLITE_DB/data.db")
    time.sleep(60*rate)

