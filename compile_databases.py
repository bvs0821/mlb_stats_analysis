from mlbstats import MLB_HitterCall
from mlbstats import MLB_PitcherCall
from mapping import HitterMapping
from mapping import PitcherMapping
import statsapi as mlb
import pandas as pd
import numpy as np

from tables import *

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.db_engine)
session = Session()

engine = db.db_engine

add_hit_data = db.insert_mlb_hitting()
#session.add(add_hit_data)

add_pitch_data = db.insert_mlb_pitching()
#session.add(add_pitch_data)

add_hitter_mapping = db.insert_hitter_mapping()
add_pitcher_mapping = db.insert_pitcher_mapping()



