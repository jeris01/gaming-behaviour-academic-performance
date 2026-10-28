"""
Gaming Behaviour and Academic Performance Analysis
Beginner-friendly project for B.Tech AI & Data Science.

IMPORTANT: The included dataset is synthetic (simulated) demonstration data.
It does not represent real students and cannot establish cause and effect.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = Path("gaming_academic_synthetic_data.csv")
OUTPUT_DIR = Path("visualizations")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("First five rows:")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nData types and non-null counts:")
df.info()
print("\nMissing values before cleaning:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Clean: convert numeric columns and fill missing values with column medians.
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
df = df.drop_duplicates()

# Basic checks for impossible values
df["daily_gaming_hours"] = df["daily_gaming_hours"].clip(0, 24)
df["daily_study_hours"] = df["daily_study_hours"].clip(0, 24)
df["sleep_hours"] = df["sleep_hours"].clip(0, 24)
df["attendance_percent"] = df["attendance_percent"].clip(0, 100)
df["academic_score_percent"] = df["academic_score_percent"].clip(0, 100)

print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nSummary statistics:")
print(df.describe().round(2))

# Group students by daily gaming hours for a simple comparison.
bins = [-0.01, 1, 3, 5, 24]
labels = ["0–1 hour", ">1–3 hours", ">3–5 hours", ">5 hours"]
df["gaming_group"] = pd.cut(df["daily_gaming_hours"], bins=bins, labels=labels)
group_summary = df.groupby("gaming_group", observed=False).agg(
    students=("student_id", "count"),
    mean_score=("academic_score_percent", "mean"),
    mean_study_hours=("daily_study_hours", "mean"),
    mean_sleep_hours=("sleep_hours", "mean")
).round(2)
print("\nSummary by gaming group:")
print(group_summary)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="daily_gaming_hours", y="academic_score_percent", alpha=0.7)
sns.regplot(data=df, x="daily_gaming_hours", y="academic_score_percent",
            scatter=False, color="red")
plt.title("Daily Gaming Hours vs Academic Score")
plt.xlabel("Gaming hours per day")
plt.ylabel("Academic score (%)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "gaming_vs_score.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="gaming_group", y="academic_score_percent",
            errorbar=None)
plt.title("Average Academic Score by Gaming Group")
plt.xlabel("Daily gaming group")
plt.ylabel("Average academic score (%)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "scores_by_gaming_group.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="daily_study_hours", y="academic_score_percent",
                hue="gaming_group", alpha=0.75)
plt.title("Study Hours vs Academic Score")
plt.xlabel("Study hours per day")
plt.ylabel("Academic score (%)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "study_vs_score.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 6))
corr_cols = ["daily_gaming_hours", "daily_study_hours", "sleep_hours",
             "attendance_percent", "stress_level_1_to_10", "academic_score_percent"]
sns.heatmap(df[corr_cols].corr(numeric_only=True), annot=True, cmap="coolwarm",
            vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=150)
plt.show()

correlations = df[corr_cols].corr(numeric_only=True)["academic_score_percent"].drop("academic_score_percent")
print("\nCorrelation with academic score (descriptive only):")
print(correlations.sort_values(ascending=False).round(3))

print("\nConclusion guide:")
print("- Describe patterns visible in your output, not assumptions.")
print("- Correlation does not prove gaming causes grades to change.")
print("- This demonstration dataset is synthetic; repeat with approved real data for real conclusions.")
