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
