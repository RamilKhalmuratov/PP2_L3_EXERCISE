def is_imdb_score_above_threshold(movie):
    return movie['imdb'] > 5.5

movie_example = {
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
}

result = is_imdb_score_above_threshold(movie_example)
print(result)  