#------------------------------------------------
# Lab 7 - Question 2 - Matteo Dagostino
#------------------------------------------------

import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

players = {}
teams = []
team_dict = {}

for i in range(0, int(input("Enter the amount of players to add: "))):
    name = input(str(i+1) + ") Enter a player: ")
    team = input("  ---> Enter their team: ")
    players[name] = team
    teams.append(team)


for i in range(0, len(teams)):
    test = []
    for key,value in players.items():
        if value == teams[i]:
            test.append(key)

    team_dict[teams[i]] = test

print("----------------------------------------------------------")
print(players)
print()
print('\n'.join(f'{key}: {value}' for key, value in team_dict.items()))
print()
