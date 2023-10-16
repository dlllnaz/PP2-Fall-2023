movies = [{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"},
{"name": "Hitman",
"imdb": 6.3,
"category": "Action"},
{"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"},
{"name": "The Help",
"imdb": 8.0,
"category": "Drama"},
{"name": "The Choice",
"imdb": 6.2,
"category": "Romance"},
{"name": "Colonia",
"imdb": 7.4,
"category": "Romance"},
{"name": "Love",
"imdb": 6.0,
"category": "Romance"},
{"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"},
{"name": "AlphaJet",
"imdb": 3.2,
"category": "War"},
{"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"},
{"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"},
{"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"},
{"name": "Detective",
"imdb": 7.0,
"category": "Suspense"},
{"name": "Exam",
"imdb": 4.2,
"category": "Thriller"},
{"name": "We Two",
"imdb": 7.2,
"category": "Romance"}]

#task1
def is_imdb_above_5_5(movie):
    return movie["imdb"] > 5.5
movie = {    "name": "The Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"}
print(is_imdb_above_5_5(movie))  

#task2
def movies_above_5_5(movies):
    idmb = float(input())
    return [movie for movie in movies if movie["imdb"] > idmb]
above_5_5_movies = movies_above_5_5(movies)
print("Movies with IMDB score above 5.5:")
for movie in above_5_5_movies:
    print(f"{movie['name']} - IMDB Score: {movie['imdb']}")

#task3
def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
category_name = str(input())
romance_movies = get_movies_by_category(movies, category_name)
print(f"Movies in the {category_name} category:")
for movie in romance_movies:
    print(f"{movie['name']} - IMDB Score: {movie['imdb']}")

#task4
def calculate_average_imdb(movies):
    if not movies:
        return 0.0
    total_imdb = sum(movie["imdb"] for movie in movies)
    return total_imdb / len(movies)
average_imdb_all = calculate_average_imdb(movies)
print(f"Average IMDB score for all movies: {average_imdb_all}")

#task5
def average_imdb_by_category(movies, category):
    total_imdb = 0.0
    count = 0
    for movie in movies:
        if movie["category"] == category:
            total_imdb += movie["imdb"]
            count += 1
    return total_imdb / count if count > 0 else 0.0
category = str(input())
average_imdb = average_imdb_by_category(movies, category)
print(f"Average IMDB score for {category} movies: {average_imdb}")

