import json

__author__ = 'Maxim'


filename = 'data.json'


# Reads data from file. Returns database
def get_database():
    file = open(filename, 'r')
    return json.load(file)


# Writes data to file. Updates database
def push_database(database):
    file = open(filename, 'w')
    json.dump(database, file)
