def discard_middle(s):
    if len(s)<=3:
        return ""
    else:
        return s[0]+s[1]+s[len(s)-2]+s[len(s)-1]
def longest(s):
    s=s.split()
    maxi=len(s[0])
    for i in s:
        if len(i)>maxi:
            maxi=len(i)
    return maxi
def remove_leading(ip):
    s=""
    ip=ip.split(".")
    for i in ip:
        s+=str(int(i))+"."
    return s[0:len(s)-1]
def summary_ranges(astring):
    
    s=""
    b=-1
    astring1=astring[0]
    astring=astring.split(",")
    for i in astring:
        if i not in astring1:
            astring1+=","+ i
    astring=astring1
    astring=astring.split(",")
    for i in range(len(astring)-1):
        if i>int(b):
            k=0
            a=astring[i]
            for j in range(i,len(astring)-1):
                
                if int(astring[j+1])==int(astring[j])+1:
                    b=j+1
                    k+=1
                else:
                    break
            if k!=0:            
                s+=a+"->"+astring[b]+","
            else:
                s+=a+","
    return s[0:len(s)-1]
#def minion(astring):
#    d={}
#    k=0
#    for i in range(len(astring)):
#        if astring[i] in "AEIOU":
#            for k in range(len(astring)-i):
#                for j in range(i+1,len(astring)-k):
#                    a=astring[i]+astring[j:j+k+1]
#                    if astring[i]+astring[j:j+k+1] not in d:
#                        d[astring[i]+astring[j:j+k+1]]=1
#                    else:
#                        d[astring[i]+astring[j:j+k+1]]+=1
#    print(d)
#                    



























            
        
