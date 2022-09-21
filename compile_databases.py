import statsapi as mlb
import pandas as pd
import numpy as np
from mlbstats import MLB_HitterCall
from mlbstats import MLB_PitcherCall
from mapping import HitterMapping
from mapping import PitcherMapping
from playerdatabase import StatDatabase
from sqlalchemy.orm import sessionmaker

# implement the SQLite engine
db = StatDatabase()
engine = db.db_engine
conn = engine.connect()

# user decision to delete tables from mlb_stats.db
delete_criteria = input("Would you like to delete all tables? [Y/N] \n>")
if delete_criteria == 'Y':
    for i in range(1, 6):
        try:
            pd.read_sql('DROP TABLE IF EXISTS mlb_hitting_stats_int{}'.format(str(i)), conn)
        except:
            pass
        try:
            pd.read_sql('DROP TABLE IF EXISTS mlb_pitching_stats_int{}'.format(str(i)), conn)
        except:
            pass
elif delete_criteria == 'N':
    pass

# create SQL tables with tables.py
from tables import *


# instantiated classes from playerdatabase.py functions

add_hit_data = db.insert_mlb_hitting()
add_pitch_data = db.insert_mlb_pitching()
add_hitter_mapping = db.insert_hitter_mapping()
add_pitcher_mapping = db.insert_pitcher_mapping()


Session = sessionmaker(bind=db.db_engine)
session = Session()

