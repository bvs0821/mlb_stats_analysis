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
# import _pickle as pickle

# creates a list of number of days to be analyzed, input by user
def date_ranges():
    num_days = list(map(int, input("Enter the amount(s) of days you are analyzing: ").split()))
    return num_days

# recursively flattens dictionary of dictionaries
def flatten_dicts(dictionary):
    # base case
    if dict not in [type(x) for x in dictionary.values()]:
        return dictionary
    else:
        for key, value in dictionary.items():
            if type(value) == dict:
                temp_dict = dictionary.pop(key)
                for k, v in temp_dict.items():
                    dictionary[f"{key}_{k}"] = v
                return flatten_dicts(dictionary)


# creates a dictionary of hitter stat dataframes from MLB-Stats API from number of days assigned
def get_hitter_stats(hitterIDs, num_days):
    if num_days[0] == 0:
        hitter_stats = {}
    else:
        print(num_days)
        hitter_stats = {}
        hitter_details = {}

    all_df_hitters = {}

    for days in num_days:
        i = 0
        end_date = date.date.today()
        start_date = end_date - date.timedelta(days=days - 1)
        end_date = dt.strftime(end_date, "%Y-%m-%d")
        start_date = dt.strftime(start_date, "%Y-%m-%d")
        print(f"Starting date is: {start_date}")
        print(f"Ending date is: {end_date}")

        tag_string_hitting = "stats(group=[hitting],type=[byDateRange],startDate={},endDate={},season=2022)".format(
            start_date, end_date)

        for ID in hitterIDs:
            print(ID)
            hitterstats = {}
            hitterdetails = {}
            try:
                try:
                    hitterstats = \
                        mlb.get("people", {"personIds": ID, "hydrate": tag_string_hitting})['people'][0]['stats'][
                            0]['splits'][0]['stat']
                    names = mlb.lookup_player(ID)
                    attributes = mlb.player_stat_data(ID, group="[hitting,pitching,fielding]", type="season")

                except ConnectionError:
                    hitterstats = \
                        mlb.get("people", {"personIds": ID, "hydrate": tag_string_hitting})['people'][0]['stats'][
                            0]['splits'][0]['stat']
                    names = mlb.lookup_player(ID)
                    attributes = mlb.player_stat_data(ID, group="[hitting,pitching,fielding]", type="season")

                except TimeoutError:
                    hitterstats = \
                        mlb.get("people", {"personIds": ID, "hydrate": tag_string_hitting})['people'][0]['stats'][
                            0]['splits'][0]['stat']
                    names = mlb.lookup_player(ID)
                    attributes = mlb.player_stat_data(ID, group="[hitting,pitching,fielding]", type="season")

                except KeyError:
                    pass

                hitter_stats[ID] = hitterstats

                hitterdetails['lastName'] = names[0]['lastName']
                hitterdetails['firstName'] = names[0]['firstName']
                hitterdetails['personID'] = ID
                hitterdetails['teamID'] = names[0]['currentTeam']['id']
                hitterdetails['teamName'] = attributes['current_team']
                hitterdetails['position'] = names[0]['primaryPosition']['abbreviation']
                hitterdetails['batSide'] = attributes['bat_side']
                hitterdetails['throwHand'] = attributes['pitch_hand']

                hitter_details[ID] = hitterdetails
                hitter_details[ID].update(hitter_stats[ID])

            except IndexError:
                pass

        df_hitters = pd.DataFrame.from_dict(hitter_details)
        all_df_hitters[days] = df_hitters.transpose()

    # creates a pickled file of mlb stat api hitting dictionary
    # with open('hitter_mlbstats.pkl', 'wb') as f:
    #     pickle.dump(hitter_details, f)

    # hitter_details = flatten_dicts(hitter_details)

    return all_df_hitters
    # return hitter_details

# creates a dictionary of pitcher stat dataframes from MLB-Stats API from number of days assigned
def get_pitcher_stats(pitcherIDs, num_days):
    if num_days[0] == 0:
        pitcher_stats = {}
    else:
        print(num_days)
        pitcher_stats = {}
        pitcher_details = {}

    all_df_pitchers = {}

    for days in num_days:
        i = 0
        end_date = date.date.today()
        start_date = end_date - date.timedelta(days=days - 1)
        end_date = dt.strftime(end_date, "%Y-%m-%d")
        start_date = dt.strftime(start_date, "%Y-%m-%d")
        print(f"Starting date is: {start_date}")
        print(f"Ending date is: {end_date}")

        tag_string_pitching = "stats(group=[pitching],type=[byDateRange],startDate={},endDate={},season=2022)".format(
            start_date, end_date)

        for ID in pitcherIDs:
            print(ID)
            pitcherstats = {}
            pitcherdetails = {}

            try:
                names = mlb.lookup_player(ID)
                attributes = mlb.player_stat_data(ID, group="[hitting,pitching,fielding]", type="season")

                try:
                    pitcherstats = \
                        mlb.get("people", {"personIds": ID, "hydrate": tag_string_pitching})['people'][0]['stats'][
                            0]['splits'][0]['stat']

                except ConnectionError:
                    pitcherstats = \
                        mlb.get("people", {"personIds": ID, "hydrate": tag_string_pitching})['people'][0]['stats'][
                            0]['splits'][0]['stat']

                except TimeoutError:
                    pitcherstats = \
                        mlb.get("people", {"personIds": ID, "hydrate": tag_string_pitching})['people'][0]['stats'][
                            0]['splits'][0]['stat']

                except KeyError:
                    pass

                pitcher_stats[ID] = pitcherstats

                pitcherdetails['lastName'] = names[0]['lastName']
                pitcherdetails['firstName'] = names[0]['firstName']
                pitcherdetails['personID'] = ID
                pitcherdetails['teamID'] = names[0]['currentTeam']['id']
                pitcherdetails['teamName'] = attributes['current_team']
                pitcherdetails['batSide'] = attributes['bat_side']
                pitcherdetails['throwHand'] = attributes['pitch_hand']

                pitcher_details[ID] = pitcherdetails

                pitcher_details[ID].update(pitcher_stats[ID])

            except IndexError:
                pass

        df_pitchers = pd.DataFrame.from_dict(pitcher_details)
        all_df_pitchers[days] = df_pitchers.transpose()

    # creates a pickled file of pitcher mlb api stats dictionary
    # with open('pitcher_mlbstats.pkl', 'wb') as f:
    #    pickle.dump(pitcher_details, f)

    return all_df_pitchers
    # return pitcher_details

# class to instantiate MLB-Stats API hitter statistics
class MLB_HitterCall():

    # pickled_calls = []
    # pickled_calls = [x.strip('.pkl') for x in pickled_calls]
    def __init__(self):
        hitterID = open("hitterID.txt").read().split()
        hitterID = list(map(int, hitterID))
        num_days = date_ranges()

        self.hitters = get_hitter_stats(hitterID, num_days)
        self.number_of_days = num_days

    # def __dict__(self):
    #    return self.hitters

    def __repr__(self):
        return f"<MLB_API_call: Complete>"

# class to instantiate MLB-Stats API pitcher statistics
class MLB_PitcherCall():

    # pickled_calls = []
    # pickled_calls = [x.strip('.pkl') for x in pickled_calls]
    def __init__(self):
        pitcherID = open("pitcherID.txt").read().split()
        pitcherID = list(map(int, pitcherID))
        num_days = date_ranges()

        self.pitchers = get_pitcher_stats(pitcherID, num_days)
        self.number_of_days = num_days

    # def __dict__(self):
    #    return self.pitchers

    def __repr__(self):
        return f"<MLB_API_call: Complete>"



