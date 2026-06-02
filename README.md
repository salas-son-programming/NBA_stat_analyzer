# NBA Stats Analyzer 🏀

This project is one of my first data analysis projects using Python, Pandas, and Matplotlib.

The goal was to analyze NBA team statistics and answer questions such as:

- Which team scores the most points?
- Which team has the highest average points per game?
- Which team rebounds the best?
- Which team gets the most assists?
- Which team has the most wins?
- What is the highest scoring game in the dataset?

I built this project to practice working with real-world data and improve my Python and data analysis skills.

---

## What I Used

- Python
- Pandas
- Matplotlib

---

## About the Dataset

The dataset contains NBA game statistics for every team throughout the season.

Some of the information included:

- Team ID
- Game ID
- Game Date
- Points scored
- Rebounds
- Assists
- Wins

One challenge I faced was that the dataset stored teams as numerical IDs instead of team names.

To make the analysis easier to understand, I created a dictionary that converts team IDs into actual NBA team names.

For example:


1610612754 -> Indiana Pacers\
1610612738 -> Boston Celtics\
1610612747 -> Los Angeles Lakers


---

## What the Program Does

### Highest Average Scoring Team

The program calculates the average number of points scored per game by each team and identifies the highest one.

Example output:

```text
The team with the highest average points is Indiana Pacers with an average of 118.7 points per game.
```

---

### Team With The Most Total Points

The program adds up all points scored throughout the season and finds the team with the highest total.

Example output:

```text
The team that has scored the most points is Oklahoma City Thunder with 16714 points.
```

---

### Best Rebounding Team

The program calculates average rebounds per game for every team.

Example output:

```text
The New York Knicks is the best rebounding team with an average of 48.3 rebounds per game.
```

---

### Best Assisting Team

The program calculates average assists per game.

Example output:

```text
The Indiana Pacers is the best assisting team with an average of 29.5 assists per game.
```

---

### Team With The Most Wins

The program finds the team with the highest number of wins recorded in the dataset.

---

### Highest Scoring Game

The program identifies the highest point total scored by a team in a single game.

---

## Data Cleaning

While working on the project, I discovered that some games appeared multiple times in the dataset.

At first, this caused unrealistic results. For example, one team appeared to score more than 700 points in a game, which obviously isn't possible.

After investigating, I found that the same game was being stored multiple times. This taught me an important lesson about checking data quality before doing any analysis.

---

## Visualizations

I also experimented with Matplotlib visualizations to compare team performance.

Some of the charts include:

- Team average points
- Total points scored
- Average rebounds
- Average assists
- Win distribution

---

## What I Learned

This project helped me practice:

- Reading CSV files with Pandas
- Grouping and aggregating data
- Finding trends in sports data
- Creating visualizations with Matplotlib
- Cleaning messy datasets
- Debugging data analysis problems
- Using Git and GitHub for version control

---

## Future Improvements

Some ideas I would like to add later:

- Interactive dashboard
- Team vs Team comparison tool
- Player statistics analysis
- Machine learning predictions
- Web application version

---

## Author

Yaniss Bantse

Computer Engineering Student

This project was created as part of my journey learning Python, Data Science, and Artificial Intelligence.
