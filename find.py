__author__ = 'Maxim'


# Finds movies in which field is equal to name
def find_by_name(database, field, name):
    ret_list = []
    for movie in database:
        if movie[field] == name:
            ret_list.append(movie)
    return ret_list
