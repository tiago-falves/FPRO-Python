def summary_ranges(astring):
    
    astring=astring.split(",")
    s=""
    i=0
    while i<len(astring):
        inicial=astring[i]
        for j in range(i,len(astring)-1):
            if int(astring[j+1])==int(astring[j])+1:
                i+=1
                continue
            else:
                break
        if inicial ==astring[i]:
            
            s+=inicial+","
            i+=1
        else:
            s+=inicial+"->"+astring[i]+","
            i+=1
    return s[:len(s)-1]

    