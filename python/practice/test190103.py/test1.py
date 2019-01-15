def shorten(name):
    names = name.split()
    for i in range(1, len(names)-1):
        names[i] = name[i][0].upper()+ '.'
    return ' '.join(names)

shorten('Alice betty catherine David')