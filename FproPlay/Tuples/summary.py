def summary(text):
    text=text.split()
    k=0
    for i in text:
        if "e" in i or "E" in i:
            k+=1
    return(len(text),k)
