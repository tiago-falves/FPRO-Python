def interleave(alist1, alist2):
    lista=[]
    def extra(alist1,alist2,lista):
        if len(alist1)< len(alist2):
            
            for i in range(len(alist1)):
                if type(alist1[i]).__name__=="list":
                    return extra(alist1[i],alist2[i],lista)
                else:
                    lista.append(alist1[i])
                    lista.append(alist2[i])
        else:
            for i in range(len(alist2)):
                if type(alist1[i]).__name__=="list":
                    return extra(alist1[i],alist2[i],lista)
                else:
                    lista.append(alist1[i])
                    lista.append(alist2[i])
        return lista
    return extra(alist1,alist2,lista)

        
            

         
    
    