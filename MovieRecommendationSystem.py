# Item Based Recommendation System
movie_db = {
    "action" : ["hulk","thor","ironman","kgf","robot","pushpa","avengers","batman",
                "superman","captain america"],
    "comedy" : ["dhamaal", "hera pheri", "thor", "golmaal"],
    "horror" : ["nun","ring","oculus","conjuring","golmaal"],
    "sci-fi" : ["interstellar","robot","ironman","avengers","time machine"]
}

user = {"hulk","thor","batman","robot","golmaal","pushpa"}

# Jaccard Distance
scores = {}

for movies in movie_db:
    a = set(movie_db[movies])
    b = user
    s = len(a.intersection(b)) / len(a.union(b))
    scores[movies] = s

print(scores)

max_value = max(scores.values())
for item in scores:
    if scores[item] == max_value:
        category = item
        break

recommended_movies = set(movie_db[category]) - user
print(recommended_movies)