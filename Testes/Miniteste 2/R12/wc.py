def wc(filename):
    linhas=0
    ch=0
    palavras=0
    with open(filename,"r") as my_document:
        for line in my_document:
            linhas+=1
            palavras+=len(line.split())
            ch+=len(line)
    return (linhas,palavras,ch)
