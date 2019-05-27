def cut(filename,delimiter,field):
    with open(filename,"r") as myfile:
        s=""
        for line in myfile.readlines():
            line=line.split(delimiter)
            if type(field).__name__=="list":
                for i in field:
                    s+=line[i-1]+delimiter
                s=s[:len(s)-1]
                
            else:
                s+=line[field-1]
            s+="\n"
        return s

            
            
    