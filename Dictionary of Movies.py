# Analyze a set of movies from a dictionary

# Dictionary of movies
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

# print(isinstance(movies, (dict)))
# print(movies[0])
# print(movies.index("imdb"))

class movie_analyser:

    def __init__(self, movie_dict):
        self.movie_dict = movie_dict

    def rating_confirmation(self, rating, name):
        if rating > 5.5:
            print("Following film's rating, " + name + ", is above a 5.5 rating on imdb\n")
        # else:
        #     print("Movie rating is less than 5.5")

    def movie_sublist(self, rating, name):
        if rating > 5.5:
            return name

    def movie_category(self, check, category_specific):
        if check == category_specific:
            return True

    def average_score(self, movies_list):
        size = len(movies_list)
        total = 0
        for movie in movies_list:
            total += movie['imdb']
            # print(total)

        # return total/size
        return ("{:.2f}".format(total/size))

movie_list = movie_analyser(movies)
sublist_rating = []
sublist_category = []

print("Your average score is:")
print(movie_list.average_score(movies))
print("")

'Loop through list and access each imdb score and movie name appropriately'
for movie in movies:
    imdb_score = movie['imdb']
    movie_name = movie['name']

    '''Confirm if rating is above 5.5'''
    movie_list.rating_confirmation(imdb_score, movie_name)
    '''Return movie names with rating above 5.5'''
    for_sublist = movie_list.movie_sublist(imdb_score, movie_name)
    '''Add movie name to list'''
    if for_sublist != None:
        sublist_rating.append(for_sublist)

print("The list of films with an imdb rating above 5.5 is:")
print(sublist_rating)
print("")

category = input("Please type in the category you want to find movies for: ")
for movie in movies:
    '''Create variable instances'''
    movie_category = movie['category']
    movie_name = movie['name']

    '''Check is inputed category matches with instance of category'''
    # print(movie_category)
    check = movie_list.movie_category(category, movie_category)
    '''If true append to sublist of movies with same category'''
    if check == True:
        sublist_category.append(movie_name)

print("The list of films under your selected category is:")
print(sublist_category)