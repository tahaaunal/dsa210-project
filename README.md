# DSA 210 Project - League of Legends Meta Analysis

## 📌 Project Overview

This project analyzes the impact of meta champions on match outcomes in League of Legends across different skill levels (ranks).

The goal is to understand whether playing meta champions provides a measurable advantage, and whether this advantage changes across different ranks.

---

## 🎯 Research Question

Do meta champions significantly increase win rates, and does this effect vary across different ranks?

---

## 📊 Dataset

The dataset consists of multiple relational tables:

- MatchTbl.csv
- TeamMatchTbl.csv
- SummonerMatchTbl.csv
- ChampionTbl.csv
- RankTbl.csv

These tables were merged into a unified player-level dataset using relational keys.

⚠️ Note:  
Due to file size limitations, the dataset is not included in this repository.  
The data was obtained from an external source (Kaggle) and used locally.

---

## ⚙️ Methodology

This project follows a structured data science pipeline:

1. Data Preparation  
- Loaded and merged multiple CSV tables  
- Filtered ranked matches  
- Created a unified dataset  

2. Feature Engineering  
- Created win/loss indicator  
- Identified player side (blue/red)  
- Defined meta champions based on win rate threshold  
- Mapped champion and rank information  

3. Exploratory Data Analysis  
- Win rate by champion  
- Win rate by rank  
- Meta vs non-meta comparison  

4. Visualization  
- Top and bottom champions by win rate  
- Rank-based comparisons  
- Win rate vs games played  

---

## 🧪 Hypothesis Testing

Two hypotheses were tested:

### Hypothesis 1: Meta Advantage

H0: There is no difference in win rates between meta and non-meta champions.  
H1: Meta champions have higher win rates than non-meta champions.  

### Hypothesis 2: Rank-Based Difference

H0: There is no difference in meta champion win rates between high-elo and low-elo players.  
H1: Meta champion win rates differ between high-elo and low-elo players.  

A two-sample t-test was performed.

**Result:**  
The p-value was greater than 0.05, meaning that the null hypothesis could not be rejected.

This suggests that while meta champions tend to perform better, the difference across ranks was not statistically significant.

---

## 🤖 Machine Learning

A machine learning approach was applied to predict match outcomes (win/loss).

### Models Used:
- Logistic Regression  
- Random Forest  

### Features:
- Meta status  
- Player rank  
- Champion  
- Team side  
- Game duration  

### Results:

- Logistic Regression → ~51.4% accuracy  
- Random Forest → ~50.6% accuracy  

Both models performed only slightly better than random guessing (50%).

### Interpretation:

This indicates that match outcomes are difficult to predict using only the available features.

Although meta champions show higher win rates in earlier analysis, machine learning results suggest that meta alone is not a strong predictor of match outcomes.

This highlights the complexity of League of Legends matches, where additional factors such as team coordination and player skill play a significant role.

---

## 📈 Key Findings

- Meta champions generally show higher win rates  
- The advantage is consistent but not strongly rank-dependent  
- Small sample sizes can produce misleading results  
- Match outcomes are difficult to predict using limited features  

---

## ⚠️ Limitations

- Meta definition is simplified and not patch-specific  
- Dataset may contain sampling bias  
- External factors (team composition, player skill variance) are not included  

---

## 🤖 AI Usage

AI tools (ChatGPT) were used for:

- Debugging Python code  
- Improving visualization ideas  
- Structuring the analysis pipeline  

All outputs were reviewed and implemented manually.

---

## 👤 Author

Taha Unal
