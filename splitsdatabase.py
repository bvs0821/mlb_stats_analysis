import _pickle as pickle
import pandas as pd
import pybaseball as pybb
import sqlite3
from playerdatabase import StatDatabase

with open('hitter_mapping.pkl', 'rb') as f:
    hitter_map = pickle.load(f)

with open('pitcher_mapping.pkl', 'rb') as f:
    batter_map = pickle.load(f)

# implement the SQLite engine
conn = sqlite3.connect('mlb_splits.db')
cur = conn.cursor()

bbID = hitter_map['key_bbref']
personID = hitter_map['personID']
firstName = hitter_map['firstName']
lastName = hitter_map['lastName']

print(bbID)
print(personID)

for i in range(0, len(firstName)):
    firstName[i] = firstName[i].capitalize()
    lastName[i] = lastName[i].capitalize()
    fullName = lastName[i] + ", " + firstName[i]
    print(fullName)
    df_splits = pybb.get_splits(bbID[i])
    table_name = fullName + " Splits"
    df_splits.to_sql(table_name, conn, if_exists='replace', index=True)
    pd.read_sql('SELECT * FROM "{}"'.format(table_name), conn)

