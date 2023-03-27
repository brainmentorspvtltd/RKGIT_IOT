# User Based Recommendation System
movie_db = {
    "action" : ["hulk","thor","ironman","kgf","robot","pushpa","avengers","batman",
                "superman","captain america"],
    "comedy" : ["dhamaal", "hera pheri", "thor", "golmaal"],
    "horror" : ["nun","ring","oculus","conjuring","golmaal"],
    "sci-fi" : ["interstellar","robot","ironman","avengers","time machine"]
}

user_1 = {"hulk","thor","batman","kgf","robot","golmaal","pushpa"}
user_2 = {"hulk","thor","golmaal","kgf","pushpa","avengers","interstellar"}

commonMovies = user_1.intersection(user_2)
# Jaccard Distance
scores = {}
for items in movie_db:
    movies = movie_db[items]
    movies = set(movies)
    numer = commonMovies.intersection(movies)
    denom = commonMovies.union(movies)
    score = len(numer) / len(denom)
    scores[items] = round(score,2)

print(scores)
category = max(scores, key=scores.get)

rec_movies = user_1.intersection(set(movie_db[category])) - user_2
print(rec_movies)








