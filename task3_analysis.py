#1 — Load and Explore

import pandas as pd
import numpy as np

df = pd.read_csv("trends_clean.csv")

print(f"Loaded data : {df.shape}")

print(f"First 5 rows: \n{df.head()}")

print(f"Average score: {round(df['score'].mean(),3)}")

print(f"Average comments: {round(df['num_comments'].mean(),3)}")

#2 — Basic Analysis with NumPy

np_score = np.array(df['score'])
np_comments = np.array(df['num_comments'])

print(f"Mean score   : {round(np.mean(np_score),3)}")
print(f"Median score : {np.median(np_score)}")
print(f"Std deviation: {np.std(np_score)}")
print(f"Max score    : {np.max(np_score)}")
print(f"Min score    : {np.min(np_score)}")

count_max = df['category'].value_counts().max()
cat_max = df['category'].value_counts().idxmax()

print(f"Most stories in: {cat_max} ({count_max} stories)")

most_com = df['num_comments'].max()
com_title = df.iloc[df['num_comments'].idxmax()]

print(f"Most commented story: \"{com_title['title']}\"  — {most_com} comments")

#3 — Add New Column

df['engagement'] = df['num_comments'] / (df['score']+1)
df['is_popular'] = df['score']>df['score'].mean()

#4 — Save the Result
df.to_csv('trends_analysed.csv', index=False)
print(f"Saved to data/trends_analysed.csv")