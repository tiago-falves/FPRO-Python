def anagrams(alist):

    final=[]
    n=[]
    for i in range(len(alist)):
        if alist[i] in n:
            continue
        else:
            l=[]
            l.append(alist[i])
            for j in range(i+1,len(alist)):
                k=0      
                alistx=list(map(lambda x: x.upper(),alist.copy()))
                
#                if len(alist[i])==len(alist[j]):#  
                for ch in alist[i]:
                    if alistx[j].find(ch)!=-1 or alistx[j].find(ch.upper())!=-1:
                        k+=1
                if k==len(alist[i]):
                    l.append(alist[j])
                    n.append(alist[j])
    #                   alist.remove(alist[j])
        l.sort()
        final.append(l)
    return sorted(final,key=lambda x: x[0].lower())
#print(anagrams(['Edward Gorey', 'Ogdred Weary', 'Regera Dowdy', 'E G Deadworry']))
#def anagrams(alist):
#
#    final=[]
#    n=[]
#    for i in range(len(alist)):
#        if alist[i] in n:
#            continue
#        else:
#            l=[]
#            l.append(alist[i])
#            for j in range(i+1,len(alist)):
#                k=0      
#                
##                if len(alist[i])==len(alist[j]):#  
#                for ch in alist[i]:
#                    if alist[j].find(ch)!=-1 or alist[j].find(ch.upper())!=-1:
#                        k+=1
#                if k==len(alist[i]):
#                    l.append(alist[j])
#                    n.append(alist[j])
#    #                   alist.remove(alist[j])
#        l.sort()
#        final.append(l)
#    return sorted(final,key=lambda x: x[0].lower())
#print(anagrams(['funeral', 'restful', 'fluster', 'apple', 'real fun']))