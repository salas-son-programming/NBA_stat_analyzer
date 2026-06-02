import numpy
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("NBA_GAMES.csv")

team_names = {
    1610612737: "Atlanta Hawks",
    1610612751: "Brooklyn Nets",
    1610612738: "Boston Celtics",
    1610612766: "Charlotte Hornets",
    1610612741: "Chicago Bulls",
    1610612739: "Cleveland Cavaliers",
    1610612742: "Dallas Mavericks",
    1610612743: "Denver Nuggets",
    1610612765: "Detroit Pistons",
    1610612744: "Golden State Warriors",
    1610612745: "Houston Rockets",
    1610612754: "Indiana Pacers",
    1610612746: "Los Angeles Clippers",
    1610612747: "Los Angeles Lakers",
    1610612763: "Memphis Grizzlies",
    1610612748: "Miami Heat",
    1610612749: "Milwaukee Bucks",
    1610612750: "Minnesota Timberwolves",
    1610612740: "New Orleans Pelicans",
    1610612752: "New York Knicks",
    1610612760: "Oklahoma City Thunder",
    1610612753: "Orlando Magic",
    1610612755: "Philadelphia 76ers",
    1610612756: "Phoenix Suns",
    1610612757: "Portland Trail Blazers",
    1610612758: "Sacramento Kings",
    1610612759: "San Antonio Spurs",
    1610612761: "Toronto Raptors",
    1610612762: "Utah Jazz",
    1610612764: "Washington Wizards"
}

# Replace IDs with team names
df["Team_ID"] = df["Team_ID"].map(team_names)

# Highest Scoring Team with average points and total number of points
team_avr_points = df.groupby("Team_ID")['PTS'].mean()
print(f"The team with the highest average points is {team_avr_points.idxmax()} with the average of {team_avr_points.max()}\n")

#PLOTTING

# plt.barh(team_avr_points.index, team_avr_points.values)
# plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)
# plt.title("Team Points Distribution",
#           fontweight="bold",
#           fontsize=20,)
# plt.xlabel("Teams average Points", fontweight="bold")
# plt.ylabel("Teams", fontweight="bold")
# plt.grid(axis="y",linewidth=1,linestyle="dotted")
# plt.grid(axis="x",linewidth=1,linestyle="dotted")

# Highest Scoring Team with total number
score_points = df.groupby("Team_ID")['PTS'].sum()

print(f"The team that has scored the most points is {score_points.idxmax()} with {score_points.max()} points.\n")

#PLOTTING

# plt.barh(score_points.index, score_points.values)
# plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)
# plt.title("Score Points Distribution",
#           fontweight="bold",
#           fontsize=20,)
# plt.xlabel("Teams Points", fontweight="bold")
# plt.ylabel("Teams", fontweight="bold")
# plt.grid(axis="y",linewidth=1,linestyle="dotted")
# plt.grid(axis="x",linewidth=1,linestyle="dotted")

# Best Rebounding Team with Average Rebounds
rebounds = df.groupby("Team_ID")['REB'].mean()
print(f"The {rebounds.idxmax()} is the best rebounding team with the average of {rebounds.max()} per game\n")

# #PLOTTING
#
# plt.barh(rebounds.index, rebounds.values)
# plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)
# plt.title("Rebounding Team Points",
#           fontweight="bold",
#           fontsize=20,)
# plt.xlabel("Average rebounds", fontweight="bold")
# plt.ylabel("Teams", fontweight="bold")
# plt.grid(axis="y",linewidth=1,linestyle="dotted")
# plt.grid(axis="x",linewidth=1,linestyle="dotted")

# Best Assisting Team with Average Assists
assists = df.groupby("Team_ID")['AST'].mean()
print(f"The {assists.idxmax()} is the best assisting team with the average of {assists.max()} per game\n")
#PLOTTING

# plt.barh(assists.index, assists.values)
# plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)
# plt.title("Assists Distribution",
#           fontweight="bold",
#           fontsize=20,)
# plt.xlabel("Assists", fontweight="bold")
# plt.ylabel("Teams", fontweight="bold")
# plt.grid(axis="y",linewidth=1,linestyle="dotted")
# plt.grid(axis="x",linewidth=1,linestyle="dotted")

# Best Winning Percentage with Win percentage team
winning = df.groupby("Team_ID")['W'].max()

print(f"The {winning.idxmax()} is the team with the most winning games with {winning.max()} wins\n")

#PLOTTING

# plt.barh(winning.index, winning.values)
# plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)
# plt.title("Wins Distribution",
#           fontweight="bold",
#           fontsize=20,)
# plt.xlabel("Wins", fontweight="bold")
# plt.ylabel("Teams", fontweight="bold")
# plt.grid(axis="y",linewidth=1,linestyle="dotted")
# plt.grid(axis="x",linewidth=1,linestyle="dotted")

#Most Points In A Single Game with the number of point and the opponents
games = df.groupby("Team_ID")['PTS'].max()
print(f"The team that has scored the most points in a single game is {games.idxmax()} with {games.max()} points.\n")

#PLOTTING

# most_points_team = df[df["Team_ID"]==games.idxmax()]
# print(most_points_team)
# print(games.idxmax())
# plt.plot(most_points_team["GAME_DATE"], most_points_team["PTS"], marker=".", linewidth=1)
# plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.2)
# plt.title("Pacers Points per Game",
#           fontweight="bold",
#           fontsize=20,)
# plt.xlabel("Dates", fontweight="bold")
# plt.ylabel("Points", fontweight="bold")
# plt.grid(axis="y",linewidth=1,linestyle="dotted")
# plt.grid(axis="x",linewidth=1,linestyle="dotted")
# plt.xticks(rotation="vertical", fontsize=6)

plt.show()
