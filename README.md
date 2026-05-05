# DSA 210 Project - League of Legends Meta Analysis

## 📌 Project Overview
This project analyzes the impact of **meta champions** on match outcomes in League of Legends across different skill levels (ranks).

The goal is to understand whether playing meta champions provides a measurable advantage, especially in higher tiers.

---

## 🎯 Research Question
Do meta champions significantly increase win rates, and does this effect change across different ranks?

---

## 📊 Dataset
The dataset consists of multiple relational tables:

- MatchTbl.csv
- TeamMatchTbl.csv
- SummonerMatchTbl.csv
- ChampionTbl.csv
- RankTbl.csv

---

## ⚙️ Methodology

### 1. Data Preparation
- Loaded multiple CSV tables
- Merged relational data (matches, teams, players)
- Cleaned and filtered ranked matches

### 2. Feature Engineering
- Created win/loss indicators
- Identified player side (blue/red)
- Mapped champions and ranks

### 3. Exploratory Data Analysis
- Win rate by champion
- Win rate by rank
- Meta vs non-meta comparison

### 4. Visualization
- Top and bottom champions by win rate
- Rank-based win rate comparison
- Win rate vs games played (reliability-aware)

### 5. Hypothesis Testing
- Performed statistical testing (t-test)
- Compared meta vs non-meta performance

---

## 📈 Key Findings
- Meta champions generally show higher win rates
- The advantage is more consistent in higher ranks
- Small sample sizes can create misleading win rates

---

## 📁 Project Structure



## Hypothesis Testing

Two hypotheses were tested in this project:

### Hypothesis 1: Meta Advantage

H0: There is no difference in win rates between meta and non-meta champions.  
H1: Meta champions have higher win rates than non-meta champions.

### Hypothesis 2: Rank-Based Difference

H0: There is no difference in meta champion win rates between high-elo and low-elo players.  
H1: Meta champion win rates differ between high-elo and low-elo players.

A two-sample t-test was performed to evaluate these hypotheses.

Results:
The p-value was greater than 0.05, meaning that the null hypothesis could not be rejected.

This suggests that although meta champions tend to perform better, the difference between ranks was not statistically significant in this dataset.



## 🤖 AI Usage

AI tools (ChatGPT) were used for:
- debugging code
- improving visualizations
- structuring analysis

All final decisions and implementation were performed by the author.

---



## 👤 Author
Taha Unal



