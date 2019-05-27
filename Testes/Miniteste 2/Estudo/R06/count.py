def count(word,phrase):
    phrase=phrase.split()
    k=0
    for i in phrase:
        if i.upper()==word.upper():
            k+=1
    return k
