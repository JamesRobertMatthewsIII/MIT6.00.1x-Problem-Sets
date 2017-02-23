def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    d3 = {}
    d4 = {}
    for key, value in d1.items():
        if key in d2.keys():
            d3[key] = f(d1[key], d2[key])
        else:
            d4[key] = value

    for key2, value2 in d2.items():
        if key2 not in d1.keys():
            d4[key2] = value2

    return d3, d4

def f(a, b):
    return a > b

print(dict_interdiff({1:30, 2:20, 3:30}, {1:40, 2:50, 3:60}))







