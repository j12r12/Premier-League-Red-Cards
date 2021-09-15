import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

df = pd.read_csv("../input/english-premier-league-data-for-10-seasons/epldat10seasons/epl-allseasons-matchstats.csv")

# Create column containing total reds per game, rather than split by home/away
df["TotalReds"] = df["HomeRedCards"] + df["AwayRedCards"]

# Group numbers of red cards by referee
referees_totals = df.groupby("Referee")["TotalReds"].agg(["count", "sum", "mean"]).rename(columns={"count":"Matches",
                                                                                                   "sum":"Red Cards", "mean":"Career - Red Cards Per Game"})

# Remove referees with fewer than 20 games
refs_over_20 = referees_totals[referees_totals["Matches"]>=20].sort_values(by="Career - Red Cards Per Game", ascending=False)

# Create distplot graph
plt.style.use("seaborn-poster")
fig, ax = plt.subplots(figsize=[12,8])
sns.distplot(refs_over_20["Career - Red Cards Per Game"], bins=10)
plt.savefig("Career Distplot.png", bbox_inches = "tight")

# Calculate z-value and p-value for Phil Dowd
z = (0.2076 - (refs_over_20["Career - Red Cards Per Game"].mean())) / refs_over_20["Career - Red Cards Per Game"].std()
p = scipy.stats.norm.sf(abs(z))

# Create 2014/15 season dataframe and limit filter to referees with 15 games or more
s1415 = df[df["Season"]=="2014/15"]
s1415_refs = s1415.groupby("Referee")["TotalReds"].agg(["count", "sum", "mean"]).rename(columns={"count":"Matches",                                                                                              "sum":"Red Cards", "mean":"Red Cards Per Game"})
s1415_refs = pd.merge(s1415_refs, referees_totals["Career - Red Cards Per Game"], on="Referee", how="left")
s1415_refs["Career vs Season"] = s1415_refs["Red Cards Per Game"] - s1415_refs["Career - Red Cards Per Game"]
s1415_refs_over15 = s1415_refs[s1415_refs["Matches"]>=15]
referees_totals_over15 = referees_totals[referees_totals["Matches"]>=15]

# Create graph to show differences between career and 2014/15
plt.style.use("seaborn-poster")
plt.figure(figsize=[12,8])
plt.title("Difference in Red Cards/Game - 2014/15 vs Career")
plt.ylabel("Difference")
plt.bar(s1415_refs_over15.index, s1415_refs_over15["Career vs Season"])
plt.xticks(rotation=90)
plt.grid(alpha=0.2)
plt.savefig("Difference.png", bbox_inches = "tight")

# Create histogram graph showing differences between career and 2014/15
fig, ax = plt.subplots(figsize=[12,8])
plt.style.use("seaborn-poster")
plt.hist(s1415_refs_over15["Red Cards Per Game"], label="2014/15", bins=10, alpha=0.3)
plt.hist(referees_totals_over15["Career - Red Cards Per Game"], label="Career", bins=10, alpha=0.3)
plt.vlines(s1415_refs_over15["Red Cards Per Game"].mean(), ymin=0, ymax=10, color="r", linestyle="--")
plt.vlines(referees_totals_over15["Career - Red Cards Per Game"].mean(), ymin=0, ymax=10, color="g", linestyle="--")
ax.set_ylim([0,5.2])
plt.text(0.095, 2.4, f"Career Mean\n{referees_totals_over15['Career - Red Cards Per Game'].mean():.3f}")
plt.text(0.196, 2.4, f"Season Mean\n{s1415_refs_over15['Red Cards Per Game'].mean():.3f}")
plt.legend()
plt.xlabel("Red Cards Per Game")
plt.ylabel("Frequency")
plt.title("Red Cards Per Game - 2014/15 vs Career")
plt.savefig("Hists.png")

# Calculate z-value
z = (0.189 - 0.133) / referees_totals_over15["Career - Red Cards Per Game"].std()

print("Complete.")