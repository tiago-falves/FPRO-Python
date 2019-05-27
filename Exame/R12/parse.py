def parse(filename):
    tupl=()
    s=""
    with open(filename,"r") as myfile:
        for line in myfile.readlines():
            line=line.strip()
            if line=="(" :
                s+=line
            else:
                s+=line+","

#                
                
                
    return "("+s+")"

            