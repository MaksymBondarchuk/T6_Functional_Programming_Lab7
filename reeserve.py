__author__ = 'Maxim'


# Prints all movies
def list_all(database):
    for i in database:
        print(i)


# Prints all movies with mask in name
def list_film_by_mask(database, mask):
    # Delete adjacent '*'
    idx = 0
    new_mask = ''
    was_star = False
    while idx < len(mask):
        if mask[idx] == '*':
            if not was_star:
                new_mask += mask[idx]
        else:
            new_mask += mask[idx]
        if mask[idx] == '*':
            was_star = True
        else:
            was_star = False
        idx += 1
    mask = new_mask
    # If last symbol is '*'
    if mask[len(mask) - 1] == '*':
        mask = mask[:-1]

    ret_list = []
    for movie in database:
        i = 0
        j = 0
        while i < len(movie['name']):
            if mask[j] != '*':
                if movie['name'][i] == mask[j]:
                    i += 1
                    j += 1
                    if len(mask) <= j:
                        break
                else:
                    i += 1
                    j = 0
            else:
                if mask[j + 1] == movie['name'][i]:
                    j += 2
                    if len(mask) <= j:
                        break
                i += 1
        if len(mask) <= j:
            ret_list.append(movie)
    return ret_list
