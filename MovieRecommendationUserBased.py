# Item Based Recommendation System
movie_db = {
    "action" : ["hulk","thor","ironman","kgf","robot","pushpa","avengers","batman",
                "superman","captain america"],
    "comedy" : ["dhamaal", "hera pheri", "thor", "golmaal"],
    "horror" : ["nun","ring","oculus","conjuring","golmaal"],
    "sci-fi" : ["interstellar","robot","ironman","avengers","time machine"]
}

user_1 = {"hulk","thor","batman","robot","superman", "hera pheri"}
user_2 = {"batman","robot","golmaal","pushpa","avengers","time machine"}

# 1. find common movies of both users
# 2. now find score of common movies with respect to movie_db
# 3. Extract the category with most score
# 3. now we will recommend movies of user_1 to user_2 based on
#     - find out those movies which user_1 has seen of that category which we have
#     - extracted in step 3 and recommend movies to user_2 which user_1 has seen but not user_2

