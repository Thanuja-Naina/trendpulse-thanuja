import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv("trends_analysed.csv")

folder_name = 'outputs/'

# Check if the folder already exists
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")

df_top_stories = df.sort_values(by='score', ascending=False).head(10)
df_top_stories['title'] = df['title'].apply(lambda x: x if len(x) <= 50 else x[:50] + '...')

plt.barh(df_top_stories['title'], df_top_stories['score'])
plt.xlabel('Score')
plt.ylabel('Title')
plt.title('Top 10 Stories by Score')

output_folder = 'outputs/'
filename = 'chart1_top_stories.png'
output_path = os.path.join(output_folder, filename)

plt.savefig(output_path)

print(f"Figure saved to: {output_path}")

plt.show()

categories = df['category'].value_counts().index
values = df['category'].value_counts().values

colors = ['skyblue', 'lightcoral', 'lightgreen', 'orange', 'mediumpurple']

plt.bar(categories, values, color=colors)
plt.xlabel('Categories')
plt.ylabel('Number of Stories')
plt.title('Stories per Category')
plt.xticks(rotation=45)

output_folder = 'outputs/'
filename = 'chart2_categories.png'
output_path = os.path.join(output_folder, filename)

plt.savefig(output_path)
print(f"Figure saved to: {output_path}")
plt.show()

#4 — Chart 3: Score vs Comments

colors = ['green', 'red']

# Plot popular stories in green
plt.scatter(df[df['is_popular'] == True]['score'],
            df[df['is_popular'] == True]['num_comments'],
            color=colors[0], label='Popular')

# Plot not popular stories in red
plt.scatter(df[df['is_popular'] == False]['score'],
            df[df['is_popular'] == False]['num_comments'],
            color=colors[1], label='Not Popular')

plt.xlabel('Score')
plt.ylabel('Number of Comments')
plt.title('Score vs Comments')
plt.legend() # This will now use the labels from the scatter calls

output_folder = 'outputs/'
filename = 'chart3_score_vs_comments.png'
output_path = os.path.join(output_folder, filename)

plt.savefig(output_path)
print(f"Figure saved to: {output_path}")
plt.grid(True)
plt.show()

#Dash board creation 

fig, axes = plt.subplots(1,3,  figsize = ((20,6)))
plt.suptitle('TrendPulse Dashboard', fontsize=18)

axes[0].barh(df_top_stories['title'], df_top_stories['score'])
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Title')
axes[0].set_title('Top 10 Stories by Score')


categories = df['category'].value_counts().index
values = df['category'].value_counts().values

category_colors = ['skyblue', 'lightcoral', 'lightgreen', 'orange', 'mediumpurple']
axes[1].bar(categories, values, color=category_colors)
axes[1].set_xlabel('Categories')
axes[1].set_ylabel('Number of Stories')
axes[1].set_title('Stories per Category')
axes[1].set_xticks(categories)
axes[1].tick_params(axis='x', rotation=45)

popularity_colors = ['green', 'red']
axes[2].scatter(df[df['is_popular'] == True]['score'], df[df['is_popular']==True]['num_comments'], color=popularity_colors[0], label='Popular')
axes[2].scatter(df[df['is_popular'] == False]['score'], df[df['is_popular']==False]['num_comments'], color=popularity_colors[1], label='Not Popular')
axes[2].set_xlabel('Score')
axes[2].set_ylabel('Number of Comments')
axes[2].set_title('Score vs Comments')
axes[2].legend()


output_folder = 'outputs/'
filename = 'dashboard.png'
output_path = os.path.join(output_folder, filename)

plt.savefig(output_path)

print(f"Dashboard saved to: {output_path}")

plt.show()