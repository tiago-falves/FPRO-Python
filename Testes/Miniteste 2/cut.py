def cut(filename, delimiter, field):
    
    with open(filename,"r") as my_document:
        s=""
        k=0
        if type(field).__name__=="int":
            field=[field]
            k=1
        
        
        for line in my_document:
            line=line.split(delimiter)
            for n in field:
                
                
                if len(field)==1:
                   
                    s+=line[n-1]
                else:
                    
                    s+=line[n-1]+delimiter
            if k==0:
                
                s=s[0:len(s)-1]
            
            s+="\n"
        s=s[0:len(s)-1]
        return s
            
print(cut("data.csv", ",", [2,4]))            
    