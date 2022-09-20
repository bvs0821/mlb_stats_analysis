# MLB Stats Analysis

MLB Stats Analysis is a project intended to give insight on the performance of MLB hitters and pitchers using a wide range of statistics from the MLB-Stat API, Baseball Reference, and FanGraphs. The program uses Python v3.9.

In its current form, the program pulls statistics from MLB-Stat API for pitchers and hitters with date ranges input by the user. These date ranges are intended to be flexible but uniformity in the ranges would eliminate the need to factor in variable date ranges when performing analysis. 

Results are stored in a SQL database named mlb_stats.db. For each date range, a SQL table is made (using SQLAlchemy and a SQLite DBMS) for the hitter and pitcher statistics. In addition, two additional tables are generated to map player statistics across the various databases that the statistics are pulled. The mapping database tables will later be used to perform analysis across the different date ranges and different databases.

## Usage

The players analyzed are determined by the player IDs for hitters and pitcher using hitterID.txt and pitterID.txt. These .txt files are populated using findplayerID.py with the user inputting the number of players analyzed. However, demonstration hitterID.txt and pitcherID.txt files are included in the repository if the user would like to skip this step.

```python
python3.9 findplayerID.py

How many players are you analyzing?
> *insert number of players* 
```
Three additional .txt files are included containing all active player IDs (master_pitcherID.txt, master_hitterID.txt, and overall reference master_playerID.txt). These can be copied (or a portion copied) over to hitterID.txt and pitcherID.txt as to not have to run findplayerID.txt.

The program initiated by running the compile_databases.py file. The user is then prompted to keep or delete all tables in mlb_stats.db. It is recommended that user selects Y.

```python
python3.9 compile_databases.py

Would you like to delete all tables? [Y/N] 
> *insert Y or N*
```

Following the decision to keep or delete the database tables, the user is prompted to input the number of dates to be analyzed for hitting statistics, which will be implemented as the date ranges. The user can input up to 5 date ranges with each creating a SQL table with the associated statistical data from the MLB-Stats API. An example input for date ranges of 2, 4, 6, 8, and 10 days is as follows:

```python
Enter the amount(s) of days you are analyzing:
2 4 6 8 10
```

The user is prompted to do the same for the pitching statistics, although the date ranges do not need to match.

## What's Next?
The next step of the project is to add in additional statistical databases which have statistics not available in the MLB-Stat API. Once all databases are added, various analysis techniques will be performed to better understand which statistical metric produces the best estimation of future performance. In addition, the aforementioned assessment over various date ranges will allow for a better determination of how long a player performs at a certain level before improving or regressing.

## Contact
For inquiries about the project, please email brandon.v.schiller@gmail.com