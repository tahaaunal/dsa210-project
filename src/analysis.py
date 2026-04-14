# DSA 210 - League of Legends Meta Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# 1. LOAD DATA
# -------------------------

summoner = pd.read_csv("SummonerMatchTbl.csv")
match = pd.read_csv("MatchTbl.csv")
team = pd.read_csv("TeamMatchTbl.csv")
champ = pd.read_csv("ChampionTbl.csv")
rank = pd.read_csv("RankTbl.csv")

print("Data loaded successfully")

# -------------------------
# 2. MERGE DATA
# -------------------------

merged_match = match.merge(team, left_on="MatchId", right_on="MatchFk")

player_df = summoner.merge(
    merged_match,
    left_on="MatchFk",
    right_on="MatchId"
)

player_df = player_df.merge(
    champ,
    left_on="ChampionFk",
    right_on="ChampionId"
)

player_df = player_df.merge(
    rank,
    left_on="RankFk",
    right_on="RankId",
    how="left"
)

print("Merging completed")

# -------------------------
# 3. FEATURE ENGINEERING
# -------------------------

player_df["Win"] = player_df["BlueWin"]
player_df["IsBlue"] = player_df["BlueWin"] == 1
player_df["IsRed"] = player_df["RedWin"] == 1

print("Feature engineering done")

# -------------------------
# 4. BASIC INFO
# -------------------------

print("\nDataset shape:", player_df.shape)
print("\nColumns:")
print(player_df.columns)

# -------------------------
# 5. SAVE SAMPLE
# -------------------------

player_df.head(100).to_csv("sample_output.csv", index=False)

print("Sample output saved")
