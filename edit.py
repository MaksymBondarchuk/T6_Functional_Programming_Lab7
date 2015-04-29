__author__ = 'Maxim'


# Adds movie to database. Data inputted from terminal
def add(database, name, director, year, rating):
    database.append({'name': name, 'director': director,
                     'year': year, 'rating': rating})


# Deletes movie with name == name from database
def delete(database, name):
    for movie in database:
        if movie['name'] == name:
            database.remove(movie)
