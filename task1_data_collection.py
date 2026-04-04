import requests
import json
import time
import os
from datetime import datetime

BASE_URL = "https://hacker-news.firebaseio.com/v0"
headers = {"User-Agent": "TrendPulse/1.0"}

#grouping the categories
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

collected = []
category_counts = {cat: 0 for cat in CATEGORIES}

#Fetching the top stories
try:
    url = f"{BASE_URL}/topstories.json"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    story_ids = response.json()[:1000]
except Exception as e:
    print("Error fetching IDs:", e)
    story_ids = []

print(f"Top story list : {story_ids}")

for story_id in story_ids:
    try:
        url = f"{BASE_URL}/item/{story_id}.json"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        story = response.json()
    except Exception as e:
        print(f"Error fetching story {story_id} : ", e)
        continue

    #skip if the story is empty or it has no title in it
    if not story or "title" not in story:
        continue

    title = story['title'].lower()

    #Finding the category of the story
    category = None
    for cat, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in title:
                category = cat
                break
            if category:
                break
    #skip if there is no category
    if not category:
        continue

    #skip if the category count is already 25 or more
    if category_counts[category] >= 25:
        continue

    data = {
        "pot_id" : story.get("id"),
        "title" : story.get("title"),
        "category": category,
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by"),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    }

    collected.append(data)

    category_counts[category] += 1

    if category_counts[category] == 25:
        print(f"Category {category} completed, waiting 2 seconds")
        time.sleep(2)

    if min(category_counts.values()) >= 25:
        break

#save to the file

if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(collected, f, indent=4)

print(f"Collected {len(collected)} stories. Saved to {filename}")