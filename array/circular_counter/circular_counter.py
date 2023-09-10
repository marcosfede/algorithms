a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def circ_counter(int_list, skip):
    skip = skip - 1  # list starts with 0 index
    idx = 0
    while len(int_list) > 0: # while the list is not empty
        idx = (skip + idx) % len(int_list) # hashing to keep changing the index to every 3rd
        print(int_list.pop(idx)) #prints the elemennt that has been removed of int_list, e.i.: idx


circ_counter(a, 3)
