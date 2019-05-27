#def wc(filename):
#    with open(filename,"r") as myfile:
#        
#        content=myfile.read()
#        words=content.split()
#        return (len(myfile.readlines()),len(words),len(content))
#print(wc("shakespeare.txt"))
def wc(filename):
    linha=0
    words=0
    caracteres=0
    with open(filename,"r") as myfile:
        for line in myfile:
            linha+=1
            words+=len(line.split())
            caracteres+=len(line)
        return(linha,words,caracteres)
print(wc("shakespeare.txt"))