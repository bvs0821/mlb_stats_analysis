import os
import pandas as pd
import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.exc import IntegrityError
from mlbstats import MLB_HitterCall
from mlbstats import MLB_PitcherCall
from mapping import HitterMapping
from mapping import PitcherMapping

# class for instantiating a SQLAlchemy connection for a SQLite DBMS

class MyDatabase:
    # Use sqlite for engine
    DB_ENGINE = {
        'SQLITE': 'sqlite:///{DB}'
    }

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self):

        self.db_engine = create_engine('sqlite:///mlb_stats.db', echo=True)
        print(self.db_engine)

        self.Base = declarative_base(bind=self.db_engine)
        self.meta = self.Base.metadata

    # populates a SQL table for hitting stats from mlbstats.py using MLB_HitterCall()
    def insert_mlb_hitting(self):

        conn = self.db_engine.connect()
        call = MLB_HitterCall()
        table = self.meta.tables['mlb_hitting_stats']
        #self.meta.table.values()


        #self.meta.table.values()
        #cols = [x.name for x in table]

        print(call)
        record = call.hitters
        days = call.number_of_days

        for day in days:
            df_hitters = record[day]
            df_hitters.to_sql('mlb_hitting_stats', conn, if_exists='replace', index=False)
            pd.read_sql('SELECT * FROM mlb_hitting_stats', conn)

        print('Hitting Records Added')

    # populates a SQL table for pitching stats from mlbstats.py using MLB_PitcherCall()
    def insert_mlb_pitching(self):

        conn = self.db_engine.connect()
        call = MLB_PitcherCall()
        table = self.meta.tables['mlb_pitching_stats']
        #self.meta.table.values()

        #self.meta.table.values()
        #cols = [x.name for x in table]

        print(call)
        record = call.pitchers
        days = call.number_of_days

        for day in days:
            df_pitchers = record[day]
            df_pitchers.to_sql('mlb_pitching_stats', conn, if_exists='replace', index=False)
            pd.read_sql('SELECT * FROM mlb_pitching_stats', conn)

        print("Pitching Records Added")

    # populates a SQL table for hitter mapping from mapping.py using HitterMapping()
    def insert_hitter_mapping(self):

        conn = self.db_engine.connect()
        call = HitterMapping()
        table = self.meta.tables['hitter_mapping']

        record = call.hittermapping
        df_hitter_map = pd.DataFrame({key: pd.Series(value) for key, value in record.items()})

        df_hitter_map.to_sql('hitter_mapping', conn, if_exists='replace', index=False)
        pd.read_sql('SELECT * FROM hitter_mapping', conn)

        print("Hitter Mapping Records Added")

    # populates a SQL table for pitcher mapping from mapping.py using PitcherMapping()
    def insert_pitcher_mapping(self):

        conn = self.db_engine.connect()
        call = PitcherMapping()
        table = self.meta.tables['pitcher_mapping']

        record = call.pitchermapping
        df_pitcher_map = pd.DataFrame({key: pd.Series(value) for key, value in record.items()})

        df_pitcher_map.to_sql('pitcher_mapping', conn, if_exists='replace', index=False)
        pd.read_sql('SELECT * FROM pitcher_mapping', conn)

        print("Pitcher Mapping Records Added")
