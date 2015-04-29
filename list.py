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

    ret_list = []
    for movie in database:
        i = 0
        j = 0
        rollback_i = 0
        rollback_j = 0
        need_rollback = False
        while i < len(movie['name']):
            if mask[j] == '*':
                if j < len(mask) - 1 and movie['name'][i] == mask[j + 1]:
                    rollback_i = i
                    rollback_j = j
                    need_rollback = True
                    j += 1
                    continue
                else:
                    i += 1
            elif movie['name'][i] == mask[j]:
                j += 1
                i += 1
            else:
                if need_rollback:
                    i = rollback_i + 1
                    j = rollback_j
                    need_rollback = False
                    continue
                break
            if len(mask) <= j:
                if len(mask) - 1 <= j and len(movie['name']) <= i:
                    break
                else:
                    i = rollback_i + 1
                    j = rollback_j
                    need_rollback = False
                    continue
        if len(mask) - 1 <= j and len(movie['name']) <= i:
            ret_list.append(movie)
    return ret_list
