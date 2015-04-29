from work_with_file import *
from list import *
from find import *
from edit import *

__author__ = 'Maxim'


def menu():
    database = get_database()

    work = True

    while work:
        choise = input('\nEnter number:\n'
                       '1. List all\n'
                       '2. Add new\n'
                       '3. Delete film\n'
                       '4. List film by name mask\n'
                       '5. Find by name film\n'
                       '6. Find film by name producer\n'
                       '7. Find film by rating\n'
                       '8. Exit\n')

        if choise == '1':
            list_all(database)
        elif choise == '2':
            name = input("\nEnter movie name\n")
            director = input("\nEnter director name\n")
            try:
                year = int(input("\nEnter movie release year\n"))
            except ValueError:
                print('Year must be integer')
                continue
            try:
                rating = float(input("\nEnter movie rating\n"))
            except ValueError:
                print('Rating must be float')
                continue
            if name and director:
                add(database, name, director, year, rating)
                print('Added\n')
            else:
                print('Next time enter all fields\n')
        elif choise == '3':
            name = input("\nEnter movie name\n")
            was = False
            if find_by_name(database, 'name', name):
                print('Deleted\n')
            else:
                print('No with this name\n')
            delete(database, name)
        elif choise == '4':
            mask = input("\nEnter name mask\n")
            movies = list_film_by_mask(database, mask)
            for movie in movies:
                print(movie)
            if not movies:
                print('No with this mask\n')
        elif choise == '5':
            name = input("\nEnter movie name\n")
            movies = find_by_name(database, 'name', name)
            for movie in movies:
                print(movie)
            if not movies:
                print('No with this name\n')
        elif choise == '6':
            director = input("\nEnter producers` name\n")
            movies = find_by_name(database, 'director', director)
            for movie in movies:
                print(movie)
            if not movies:
                print('No with this name\n')
        elif choise == '7':
            try:
                rating = float(input("\nEnter movie rating\n"))
            except ValueError:
                print('Rating must be float')
                continue
            movies = find_by_name(database, 'rating', rating)
            for movie in movies:
                print(movie)
            if not movies:
                print('No with this name\n')
        elif choise == '8' or choise == 'exit':
            break
    push_database(database)


menu()
