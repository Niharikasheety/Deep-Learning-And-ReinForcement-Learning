import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cs_students_performance.csv")

# Clean & convert
df['weekly_study_hours'] = pd.to_numeric(df['weekly_study_hours'], errors='coerce')
df['final_score'] = pd.to_numeric(df['final_score'], errors='coerce')

# 1. Average score by programming language
lang_scores = df.groupby('programming_language')['final_score'].mean().sort_values(ascending=False)
lang_scores.plot(kind='bar', color='skyblue')
plt.title('Average Final Score by Programming Language')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("score_by_language.png")
plt.close()

# 2. Study time vs Final score
plt.scatter(df['weekly_study_hours'], df['final_score'], color='purple', alpha=0.6)
plt.title('Weekly Study Hours vs Final Score')
plt.xlabel('Weekly Study Hours')
plt.ylabel('Final Score')
plt.grid(True)
plt.tight_layout()
plt.savefig("time_spent_vs_score.png")
plt.close()

# 3. Completion rate by CS background
completion = df.groupby('cs_background')['completed'].value_counts(normalize=True).unstack().fillna(0)
completion.plot(kind='bar', stacked=True, color=['salmon', 'mediumseagreen'])
plt.title('Completion Rate by CS Background')
plt.ylabel('Percentage')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("completion_rate_by_background.png")
plt.close()

print("All visualizations saved successfully.")