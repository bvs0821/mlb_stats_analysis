from datetime import datetime as dt
import datetime as date
import os, re, csv
from os import walk
import statsapi as mlb
import pandas as pd
import sys
import json
from operator import itemgetter
from collections import defaultdict
import pybaseball as pybb
from pybaseball import playerid_reverse_lookup
#import _pickle as pickle


# creates a dictionary to map hitters between MLB-Stats API, Fangraphs, Baseball Reference
# uses MLB-Stats API person ID as the primary key for SQL tables later created
def get_hitter_mapping(hitterIDs):

    hitter_ln = list()
    hitter_fn = list()
    hitter_key_mlbam = list()
    hitter_key_retro = list()
    hitter_key_bbref = list()
    hitter_key_fangraphs = list()
    hitter_mlb_played_first = list()

    for ID in hitterIDs:
        holder = [ID]
        name = playerid_reverse_lookup(holder, key_type='mlbam')
        if name.empty:
            pass
        else:
            hitter_ln.append(name['name_last'].values[0])
            hitter_fn.append(name['name_first'].values[0])
            hitter_key_mlbam.append(name['key_mlbam'].values[0])
            hitter_key_retro.append(name['key_retro'].values[0])
            hitter_key_bbref.append(name['key_bbref'].values[0])
            hitter_key_fangraphs.append(name['key_fangraphs'].values[0])
            hitter_mlb_played_first.append(name['mlb_played_first'].values[0])

    hitter_mapping = {}
    hitter_mapping['personID'] = hitter_key_mlbam[0:len(hitterIDs) - 1]
    hitter_mapping['lastName'] = hitter_ln[0:len(hitterIDs) - 1]
    hitter_mapping['firstName'] = hitter_fn[0:len(hitterIDs) - 1]
    hitter_mapping['key_mlbam'] = hitter_key_mlbam[0:len(hitterIDs) - 1]
    hitter_mapping['key_retro'] = hitter_key_retro[0:len(hitterIDs) - 1]
    hitter_mapping['key_bbref'] = hitter_key_bbref[0:len(hitterIDs) - 1]
    hitter_mapping['key_fangraphs'] = hitter_key_fangraphs[0:len(hitterIDs) - 1]
    hitter_mapping['mlb_played_first'] = hitter_mlb_played_first[0:len(hitterIDs) - 1]

    # creates a pickled file of hitter mapping dictionary
    # with open('hitter_mapping.pkl', 'wb') as f:
    #   pickle.dump(hitter_mapping, f)

    return hitter_mapping

# creates a dictionary to map pitcher between MLB-Stats API, Fangraphs, Baseball Reference
# uses MLB-Stats API person ID as the primary key for SQL tables later created
def get_pitcher_mapping(pitcherIDs):

    pitcher_ln = list()
    pitcher_fn = list()
    pitcher_key_mlbam = list()
    pitcher_key_retro = list()
    pitcher_key_bbref = list()
    pitcher_key_fangraphs = list()
    pitcher_mlb_played_first = list()

    for ID in pitcherIDs:
        holder = [ID]
        name = playerid_reverse_lookup(holder, key_type='mlbam')
        if name.empty:
            pass
        else:
            pitcher_ln.append(name['name_last'].values[0])
            pitcher_fn.append(name['name_first'].values[0])
            pitcher_key_mlbam.append(name['key_mlbam'].values[0])
            pitcher_key_retro.append(name['key_retro'].values[0])
            pitcher_key_bbref.append(name['key_bbref'].values[0])
            pitcher_key_fangraphs.append(name['key_fangraphs'].values[0])
            pitcher_mlb_played_first.append(name['mlb_played_first'].values[0])

    pitcher_mapping = {}
    pitcher_mapping['personID'] = pitcher_key_mlbam[0:len(pitcherIDs) - 1]
    pitcher_mapping['lastName'] = pitcher_ln[0:len(pitcherIDs) - 1]
    pitcher_mapping['firstName'] = pitcher_fn[0:len(pitcherIDs) - 1]
    pitcher_mapping['key_mlbam'] = pitcher_key_mlbam[0:len(pitcherIDs) - 1]
    pitcher_mapping['key_retro'] = pitcher_key_retro[0:len(pitcherIDs) - 1]
    pitcher_mapping['key_bbref'] = pitcher_key_bbref[0:len(pitcherIDs) - 1]
    pitcher_mapping['key_fangraphs'] = pitcher_key_fangraphs[0:len(pitcherIDs) - 1]
    pitcher_mapping['mlb_played_first'] = pitcher_mlb_played_first[0:len(pitcherIDs) - 1]

    # creates a pickled file of pitcher mapping dictionary
    # with open('pitcher_mapping.pkl', 'wb') as f:
    #    pickle.dump(pitcher_mapping, f)

    return pitcher_mapping

# class to instantiate hitter mapping
class HitterMapping():

    #pickled_calls = []
    #pickled_calls = [x.strip('.pkl') for x in pickled_calls]
    def __init__(self):

        hitterIDs = open("hitterID.txt").read().split()
        hitterIDs = list(map(int, hitterIDs))

        self.hittermapping = get_hitter_mapping(hitterIDs)


    def __repr__(self):
        return f"<Hitter Mapping Complete>"

# class to instantiate pitcher mapping
class PitcherMapping():

    # pickled_calls = []
    # pickled_calls = [x.strip('.pkl') for x in pickled_calls]
    def __init__(self):

        pitcherIDs = open("pitcherID.txt").read().split()
        pitcherIDs = list(map(int, pitcherIDs))

        self.pitchermapping = get_pitcher_mapping(pitcherIDs)

    def __repr__(self):
        return f"<Pitcher Mapping Complete>"
