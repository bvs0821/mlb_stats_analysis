import statsapi as mlb
import pandas as pd
import numpy as np
from mlbstats import MLB_HitterCall
from mlbstats import MLB_PitcherCall
from mapping import HitterMapping
from mapping import PitcherMapping

from tables import *

# script used to instantiate classes to populate tables for SQLALchemy Object Relational Mapping

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.db_engine)
session = Session()

engine = db.db_engine

# instantiated classes from playerdatabase.py functions
#

add_hit_data = db.insert_mlb_hitting()
add_pitch_data = db.insert_mlb_pitching()
add_hitter_mapping = db.insert_hitter_mapping()
add_pitcher_mapping = db.insert_pitcher_mapping()



