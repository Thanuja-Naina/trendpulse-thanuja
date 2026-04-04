import pandas as pd
import json

data = "C:\\Users\\Dell\\Desktop\\AI_and_ML\\Vscode_git_session\\data\\trends_20260404.json"
df = pd.read_json(data)
print(f"Loaded {len(df)} stories from data/trends_20260404.json")


df = df.drop_duplicates(subset=['pot_id'])
print(f"After removing duplicates: {len(df)}")

df = df.dropna(subset=['pot_id','title', 'score'])

print(f"After removing nulls: {len(df)}")


df = df[df['score']>=5].reset_index()

print(f"After removing low scores: {len(df)} ")


df['title'] = df['title'].str.strip()


df.to_csv('trends_clean.csv', index=False)
print(f"Saved {len(df)} rows to data/trends_clean.csv")

print(f"Stories per category: \n{df['category'].value_counts()}" )