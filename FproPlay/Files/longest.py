def longest(filename):
    with open(filename) as myfile:
        texto=myfile.read()
        texto=texto.split()
        maxi=max(map(lambda x:len(x),texto))
        
        return list(filter(lambda x: len(x)==maxi,texto))[0]
