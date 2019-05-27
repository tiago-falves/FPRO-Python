def grep(pattern,files_list,flags=""):
    s=""
    flags=flags.split()
    for file in files_list:
        with open(file,"r") as my_file:
            texto=my_file.read()
            lista_linhas=my_file.readlines()
            
            if "-l" in flags:
                    s+=file
            if "-c" in flags:
                if texto.find(pattern)!=-1:
                    s+=file+":"+str(texto.count(pattern))
                    
            for linei in range(len(lista_linhas)):
                if flags == []:
                    if lista_linhas[linei].find(pattern)!=-1:
                        s+=file+":"+str(linei+1)+":"+lista_linhas[linei]
                if "-x" in flags:
                    if pattern==lista_linhas[linei]:
                        s+=file+":"+str(linei+1)+":"+lista_linhas[linei]+"\n"
                if "-i" in flags:
                    if lista_linhas[linei].lower().find(pattern.lower())!=-1:
                        s+=file+":"+str(linei+1)+":"+lista_linhas[linei]+"\n"
                if "-v" in flags:
                    if lista_linhas[linei].find(pattern.lower())==-1:
                        s+=file+":"+str(linei+1)+":"+lista_linhas[linei]+"\n"
                
            s+="\n"
                
                
    return s

print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i'))