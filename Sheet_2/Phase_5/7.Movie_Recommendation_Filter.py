import json

movie_data = json.loads(input("Enter Movie Data: "))

filtered_movies = [
    name
    for name, movie in movie_data.items()
    if movie['rating'] > 8.5 and 'Sci-Fi' in movie['genres']
]

print(filtered_movies)