def solver(a, b, c):
    d=b**2-4*a*c
    if a==0 or d<0:
        return []
    elif d >= 0:
        if (-b+d**(1/2))/(2*a) == (-b-d**(1/2))/(2*a):
            result=[(-b+d**(1/2))/(2*a)]
        else:
            result= [(-b-d**(1/2))/(2*a),(-b+d**(1/2))/(2*a)]
    return sorted(result)
def pascal(n):
    import math
    s=""
    for i in range (n):
        for j in range(i+1):
            a=(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)))
            s = s + str(a) + " "           
        s=s.strip()
        s+="\n"
    return s
def collatz(n):
    a=str(n)
    while n!=1:
        if n==1:
            a+=str(n)
        elif n%2==0:
            n=n//2
            a+=","+str(n)
        else:
            n=n*3+1
            a+=","+str(n)
    return a
def minion(astring):
    for i in range(len(astring)):
        if astring[i] in "AEIOU":
            print(astring[i]+",")
            for j in range(len(astring)):
                print(astring[j])
 
        

def palindrome_index(s):
    k=0
    for i in range(len(s)):
        a=s[0:i]+s[i+1:]
        if a==a[-1::-1]:
            index=i
            k=1
            break
    if s==s[-1::-1] or k==0:
        return -1
    else:
        return index
def summary_ranges(astring):
    astring=astring.split(",")
    i=0
    s=""
    while i+1< len(astring)-1:
        a=i   
        s+=str(astring[i])
        while astring[i+1] == str(int(astring[i])+1):            
            i+=1
        if a==i:
            s+=","
            i+=1
            continue
        else:
            s+="->"
        s+=str(astring[i])+","
        i+=1    
  
    print(s)

def add_item(tup, idx, item):
    if idx==0:
        ntup=(item,)
        for i in range(1,len(tup)):
            ntup+=(tup[i],)
    elif idx==len(tup)-1:
        ntup=()
        for i in range(len(tup)-1):
            ntup+=(tup[i],)
        ntup+=(item,)      
    else:
        ntup=()
        for i in range(idx):
            ntup+=(tup[i],)
        ntup+=(item,)
        for i in range(idx,len(tup)):
            ntup+=(tup[i],)
    return ntup
            
def remove_leading(ip):
    a=ip.split(".")
    s=""    
    for i in range(len(a)):  #para tirar os 0 a  esquerda transformar em int!
        j=0
        if len(a[i])==1:
            s+=a[i]
        else:            
            while a[i][j]=="0":
                j+=1
            s+=a[i][j:] 

        s+="."
    s=s[0:len(s)-1]
    print(s)
    return s

def rangoli(N):
    s=""
    k=2    
    abc="abcdefghijklmnopqrstuwxyz"
    for i in range(1,N):
        n=N
        s=""
        traços=2*N-k
        k+=2
        s=traços*"-"
        for j in range((2*i-1)//2+1):
            s+=abc[n-1]+"-"
            n-=1
        
        for j in range((2*i-1)//2):
            s+=abc[n+1]+"-"
            n+=1
        s=s[:len(s)-1]
        s+="-"*traços
    k=0
    
    for i in range(N-1,0,-1):
        n=N
        k+=2
        traços=0
        traços+=k
        s=traços*"-"

        for j in range((2*i-1)//2+1):
            s+=abc[n-1]+"-"
            n-=1        
        for j in range((2*i-1)//2):
            s+=abc[n+1]+"-"
            n+=1
        s=s[:len(s)-1]
        s+=traços*"-"
    return s
def unpack_rev(atuple):
    a=list(atuple)
    s=""
    for i in a:
        s=" "+str(i)+s
    s=s.strip()
    return 
def count_until(tup):
    b=-1
    for i in range(len(tup)):
        c=type(tup[i]).__name__
        if c=="tuple":
            b=i
            break
    if b==-1:
        return -1
    else:        
        return b
def count_elems(tup):
    """gosto"""
    a=list(tup)
    b=()
    for i in a:
        if type(i).__name__=="str" or type(i).__name__=="tuple" or type(i).__name__=="list":
            b+=(len(i),)
        else:
            b+=(1,)
    return b
def summary(text):
    a=text.split()
    k=0
    b=(len(a),)
    for i in a:
        if "e" in i or "E" in i:
            k+=1
    b+=(k,)
    return b
            
def remove_duplos(frase):
    b=[]
    for i in range(len(frase)):
        if frase[i] in b:
            continue
        else:
            b.append(frase[i])
    return str(b)
l=[1,2,[3,1,[2,4,5]]]
def max_nested(l):
    maximo=None
    for i in l:
        if type(i).__name__=="list":
            maximo=max(maximo,max_nested(i))
        else:
            if maximo==None or i>maximo :
                maximo=i
    return maximo                  
            
                
def permutations(l):
    import itertools
    return itertools.permutations(l)



