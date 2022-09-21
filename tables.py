from sqlalchemy.orm import sessionmaker
from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy import Table, Column, Integer, String, DateTime, Date, Boolean, Float
from playerdatabase import StatDatabase

# script used to create tables for SQLALchemy Object Relational Mapping
db = StatDatabase()

# Note on tables.py: in the future, script is intended to be updated to dynamically change __tablename__ and create a
# table with that name. This will allow for any date ranges to be analyzed.

# class to instantiate a table for hitting stats from MLB-Stats API for first date range
class MLBHittingStats_Int1(db.Base):
    __tablename__ = "mlb_hitting_stats_int1"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['hitter_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    groundIntoTriplePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    plateAppearances = Column(Integer)
    totalBases = Column(Integer)
    rbi = Column(Integer)
    leftOnBase = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)
    babip = Column(Float)
    groundOutsToAirouts = Column(Float)
    catchersInterference = Column(Integer)
    atBatsPerHomeRun = Column(Float)

    def __repr__(self):
        return "<Hitting Stats Date Range 1: Table Created>"

# class to instantiate a table for hitting stats from MLB-Stats API for second date range
class MLBHittingStats_Int2(db.Base):
    __tablename__ = "mlb_hitting_stats_int2"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['hitter_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    groundIntoTriplePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    plateAppearances = Column(Integer)
    totalBases = Column(Integer)
    rbi = Column(Integer)
    leftOnBase = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)
    babip = Column(Float)
    groundOutsToAirouts = Column(Float)
    catchersInterference = Column(Integer)
    atBatsPerHomeRun = Column(Float)

    def __repr__(self):
        return "<Hitting Stats Date Range 2: Table Created>"

# class to instantiate a table for hitting stats from MLB-Stats API for third date range
class MLBHittingStats_Int3(db.Base):
    __tablename__ = "mlb_hitting_stats_int3"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['hitter_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    groundIntoTriplePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    plateAppearances = Column(Integer)
    totalBases = Column(Integer)
    rbi = Column(Integer)
    leftOnBase = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)
    babip = Column(Float)
    groundOutsToAirouts = Column(Float)
    catchersInterference = Column(Integer)
    atBatsPerHomeRun = Column(Float)

    def __repr__(self):
        return "<Hitting Stats Date Range 3: Table Created>"

# class to instantiate a table for hitting stats from MLB-Stats API for third date range
class MLBHittingStats_Int4(db.Base):
    __tablename__ = "mlb_hitting_stats_int4"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['hitter_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    groundIntoTriplePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    plateAppearances = Column(Integer)
    totalBases = Column(Integer)
    rbi = Column(Integer)
    leftOnBase = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)
    babip = Column(Float)
    groundOutsToAirouts = Column(Float)
    catchersInterference = Column(Integer)
    atBatsPerHomeRun = Column(Float)

    def __repr__(self):
        return "<Hitting Stats Date Range 4: Table Created>"

# class to instantiate a table for hitting stats from MLB-Stats API for third date range
class MLBHittingStats_Int5(db.Base):
    __tablename__ = "mlb_hitting_stats_int5"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['hitter_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    groundIntoTriplePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    plateAppearances = Column(Integer)
    totalBases = Column(Integer)
    rbi = Column(Integer)
    leftOnBase = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)
    babip = Column(Float)
    groundOutsToAirouts = Column(Float)
    catchersInterference = Column(Integer)
    atBatsPerHomeRun = Column(Float)

    def __repr__(self):
        return "<Hitting Stats Date Range 5: Table Created>"

# class to instantiate a table for pitching stats from MLB-Stats API for date range 1
class MLBPitchingStats_Int1(db.Base):
    __tablename__ = "mlb_pitching_stats_int1"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['pitcher_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    gamesStarted = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    era = Column(Float)
    inningsPitched = Column(Float)
    wins = Column(Integer)
    losses = Column(Integer)
    saves = Column(Integer)
    saveOpportunities = Column(Integer)
    holds = Column(Integer)
    blownSaves = Column(Integer)
    earnedRuns = Column(Integer)
    whip = Column(Float)
    battersFaced = Column(Integer)
    outs = Column(Integer)
    gamesPitched = Column(Integer)
    completeGames = Column(Integer)
    shutouts = Column(Integer)
    strikes = Column(Integer)
    strikePercentage = Column(Float)
    hitBatsmen = Column(Integer)
    balks = Column(Integer)
    wildPitches = Column(Integer)
    pickoffs = Column(Integer)
    totalBases = Column(Integer)
    groundOutsToAirouts = Column(Float)
    winPercentage = Column(Float)
    pitchesPerInning = Column(Float)
    gamesFinished = Column(Integer)
    strikeoutWalkRatio = Column(Float)
    strikeoutsPer9Inn = Column(Float)
    walksPer9Inn = Column(Float)
    hitsPer9Inn = Column(Float)
    runsScoredPer9 = Column(Float)
    homeRunsPer9 = Column(Float)
    inheritedRunners = Column(Integer)
    inheritedRunnersScored = Column(Integer)
    catchersInterference = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)

    def __repr__(self):
        return "<Pitching Stats Date Range 1: Table Created>"

# class to instantiate a table for pitching stats from MLB-Stats API for date range 2
class MLBPitchingStats_Int2(db.Base):
    __tablename__ = "mlb_pitching_stats_int2"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['pitcher_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    gamesStarted = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    era = Column(Float)
    inningsPitched = Column(Float)
    wins = Column(Integer)
    losses = Column(Integer)
    saves = Column(Integer)
    saveOpportunities = Column(Integer)
    holds = Column(Integer)
    blownSaves = Column(Integer)
    earnedRuns = Column(Integer)
    whip = Column(Float)
    battersFaced = Column(Integer)
    outs = Column(Integer)
    gamesPitched = Column(Integer)
    completeGames = Column(Integer)
    shutouts = Column(Integer)
    strikes = Column(Integer)
    strikePercentage = Column(Float)
    hitBatsmen = Column(Integer)
    balks = Column(Integer)
    wildPitches = Column(Integer)
    pickoffs = Column(Integer)
    totalBases = Column(Integer)
    groundOutsToAirouts = Column(Float)
    winPercentage = Column(Float)
    pitchesPerInning = Column(Float)
    gamesFinished = Column(Integer)
    strikeoutWalkRatio = Column(Float)
    strikeoutsPer9Inn = Column(Float)
    walksPer9Inn = Column(Float)
    hitsPer9Inn = Column(Float)
    runsScoredPer9 = Column(Float)
    homeRunsPer9 = Column(Float)
    inheritedRunners = Column(Integer)
    inheritedRunnersScored = Column(Integer)
    catchersInterference = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)

    def __repr__(self):
        return "<Pitching Stats Date Range 2: Table Created>"

# class to instantiate a table for pitching stats from MLB-Stats API for date range 3
class MLBPitchingStats_Int3(db.Base):
    __tablename__ = "mlb_pitching_stats_int3"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['pitcher_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    gamesStarted = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    era = Column(Float)
    inningsPitched = Column(Float)
    wins = Column(Integer)
    losses = Column(Integer)
    saves = Column(Integer)
    saveOpportunities = Column(Integer)
    holds = Column(Integer)
    blownSaves = Column(Integer)
    earnedRuns = Column(Integer)
    whip = Column(Float)
    battersFaced = Column(Integer)
    outs = Column(Integer)
    gamesPitched = Column(Integer)
    completeGames = Column(Integer)
    shutouts = Column(Integer)
    strikes = Column(Integer)
    strikePercentage = Column(Float)
    hitBatsmen = Column(Integer)
    balks = Column(Integer)
    wildPitches = Column(Integer)
    pickoffs = Column(Integer)
    totalBases = Column(Integer)
    groundOutsToAirouts = Column(Float)
    winPercentage = Column(Float)
    pitchesPerInning = Column(Float)
    gamesFinished = Column(Integer)
    strikeoutWalkRatio = Column(Float)
    strikeoutsPer9Inn = Column(Float)
    walksPer9Inn = Column(Float)
    hitsPer9Inn = Column(Float)
    runsScoredPer9 = Column(Float)
    homeRunsPer9 = Column(Float)
    inheritedRunners = Column(Integer)
    inheritedRunnersScored = Column(Integer)
    catchersInterference = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)

    def __repr__(self):
        return "<Pitching Stats Date Range 3: Table Created>"

# class to instantiate a table for pitching stats from MLB-Stats API for date range 4
class MLBPitchingStats_Int4(db.Base):
    __tablename__ = "mlb_pitching_stats_int4"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['pitcher_mapping.personID']
        ),
        {'extend_existing': True}
    )
    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    gamesStarted = Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    era = Column(Float)
    inningsPitched = Column(Float)
    wins = Column(Integer)
    losses = Column(Integer)
    saves = Column(Integer)
    saveOpportunities = Column(Integer)
    holds = Column(Integer)
    blownSaves = Column(Integer)
    earnedRuns = Column(Integer)
    whip = Column(Float)
    battersFaced = Column(Integer)
    outs = Column(Integer)
    gamesPitched = Column(Integer)
    completeGames = Column(Integer)
    shutouts = Column(Integer)
    strikes = Column(Integer)
    strikePercentage = Column(Float)
    hitBatsmen = Column(Integer)
    balks = Column(Integer)
    wildPitches = Column(Integer)
    pickoffs = Column(Integer)
    totalBases = Column(Integer)
    groundOutsToAirouts = Column(Float)
    winPercentage = Column(Float)
    pitchesPerInning = Column(Float)
    gamesFinished = Column(Integer)
    strikeoutWalkRatio = Column(Float)
    strikeoutsPer9Inn = Column(Float)
    walksPer9Inn = Column(Float)
    hitsPer9Inn = Column(Float)
    runsScoredPer9 = Column(Float)
    homeRunsPer9 = Column(Float)
    inheritedRunners = Column(Integer)
    inheritedRunnersScored = Column(Integer)
    catchersInterference = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)

    def __repr__(self):
        return "<Pitching Stats Date Range 4: Table Created>"

# class to instantiate a table for pitching stats from MLB-Stats API for date range 5
class MLBPitchingStats_Int5(db.Base):
    __tablename__ = "mlb_pitching_stats_int5"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['personID'],
            refcolumns=['pitcher_mapping.personID']
        ),
        {'extend_existing': True}
    )

    numberOfDays = Column(Integer)
    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    position = Column(String(2))
    batSide = Column(String(5))
    throwHand = Column(String(5))
    teamID = Column(Integer)
    teamName = Column(String(30))
    gamesPlayed = Column(Integer)
    gamesStarted= Column(Integer)
    groundOuts = Column(Integer)
    airOuts = Column(Integer)
    runs = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    homeRuns = Column(Integer)
    strikeOuts = Column(Integer)
    baseOnBalls = Column(Integer)
    intentionalWalks = Column(Integer)
    hits = Column(Integer)
    hitByPitch = Column(Integer)
    avg = Column(Float)
    atBats = Column(Integer)
    obp = Column(Float)
    slg = Column(Float)
    ops = Column(Float)
    caughtStealing = Column(Integer)
    stolenBases = Column(Integer)
    stolenBasePercentage = Column(Float)
    groundIntoDoublePlay = Column(Integer)
    numberOfPitches = Column(Integer)
    era = Column(Float)
    inningsPitched = Column(Float)
    wins = Column(Integer)
    losses = Column(Integer)
    saves = Column(Integer)
    saveOpportunities = Column(Integer)
    holds = Column(Integer)
    blownSaves = Column(Integer)
    earnedRuns = Column(Integer)
    whip = Column(Float)
    battersFaced = Column(Integer)
    outs = Column(Integer)
    gamesPitched = Column(Integer)
    completeGames = Column(Integer)
    shutouts = Column(Integer)
    strikes = Column(Integer)
    strikePercentage = Column(Float)
    hitBatsmen = Column(Integer)
    balks = Column(Integer)
    wildPitches = Column(Integer)
    pickoffs = Column(Integer)
    totalBases = Column(Integer)
    groundOutsToAirouts = Column(Float)
    winPercentage = Column(Float)
    pitchesPerInning = Column(Float)
    gamesFinished = Column(Integer)
    strikeoutWalkRatio = Column(Float)
    strikeoutsPer9Inn = Column(Float)
    walksPer9Inn = Column(Float)
    hitsPer9Inn = Column(Float)
    runsScoredPer9 = Column(Float)
    homeRunsPer9 = Column(Float)
    inheritedRunners = Column(Integer)
    inheritedRunnersScored = Column(Integer)
    catchersInterference = Column(Integer)
    sacBunts = Column(Integer)
    sacFlies = Column(Integer)

    def __repr__(self):
        return "<Pitching Stats Date Range 5: Table Created>"

# class to instantiate a table for hitter mapping
class HitterMapping(db.Base):
    __tablename__ = "hitter_mapping"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['hitter_mapping.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_hitting_stats_int1.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_hitting_stats_int2.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_hitting_stats_int3.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_hitting_stats_int4.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_hitting_stats_int5.personID']
        ),
        {'extend_existing': True}
    )

    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    key_mlbam = Column(Integer)
    key_retro = Column(Integer)
    key_bbref = Column(Integer)
    key_fangraphs = Column(Integer)
    mlb_played_first = Column(Integer)

    def __repr__(self):
        return "<Hitting Mapping: Table Created>"

# class to instantiate a table for pitcher mapping
class PitcherMapping(db.Base):
    __tablename__ = "pitcher_mapping"
    __table_args__ = (
        PrimaryKeyConstraint('personID'),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['pitcher_mapping.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_pitching_stats_int1.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_pitching_stats_int2.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_pitching_stats_int3.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_pitching_stats_int4.personID']
        ),
        ForeignKeyConstraint(
            columns=['key_mlbam'],
            refcolumns=['mlb_pitching_stats_int5.personID']
        ),

        {'extend_existing': True}
    )

    personID = Column(Integer)
    lastName = Column(String(20))
    firstName = Column(String(20))
    key_mlbam = Column(Integer)
    key_retro = Column(Integer)
    key_bbref = Column(Integer)
    key_fangraphs = Column(Integer)
    mlb_played_first = Column(Integer)

    def __repr__(self):
        return "<Pitching Mapping: Table Created>"

if __name__ != '__main__':
    db.Base.metadata.create_all()
