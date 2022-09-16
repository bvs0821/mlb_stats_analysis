import statsapi as mlb
from datetime import datetime as dt
import datetime as date

num_player = int(input("How many players are you analyzing?\n>"))
num_player = num_player
all_player_ID = []
hitter_ID = []
pitcher_ID = []

for i in range(0, int(num_player)):
    try:
        player = mlb.lookup_player('')
        player_ID = int(player[i]['id'])
        all_player_ID.append(player_ID)
    except TimeoutError:
        player = mlb.lookup_player('')
        player_ID = int(player[i]['id'])
        all_player_ID.append(player_ID)
    except IndexError:
        pass

for ID in all_player_ID:

    position_code = mlb.lookup_player(ID)[0]['primaryPosition']['code']
    if position_code == '1':
        try:
            pitcher_ID.append(ID)
        except NameError:
            pass

    elif position_code != '1':
        try:
            hitter_ID.append(ID)
        except NameError:
            pass

print(all_player_ID)
print('')
print('Hitter IDs:')
print(hitter_ID)
print('')
print("Pitcher IDs")
print(pitcher_ID)

with open('pitcherID.txt', 'w') as file:
    file.write('\n'.join(str(pitcher_ID) for pitcher_ID in pitcher_ID))

with open('hitterID.txt', 'w') as file:
    file.write('\n'.join(str(hitter_ID) for hitter_ID in hitter_ID))

with open('playerID.txt', 'w') as file:
    file.write('\n'.join(str(all_player_ID) for all_player_ID in all_player_ID))
